"""Local ACT Test Generator — run via run.bat."""

from __future__ import annotations

import json
import os
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from generator import build_test, render_test_html, save_test

ROOT = Path(__file__).resolve().parent
TESTS_DIR = ROOT / "tests"
PORT = 8766


INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>ACT Test Generator</title>
<style>
  :root {
    --ink: #1a2332;
    --paper: #f4f1ea;
    --accent: #1e5a8a;
    --gold: #e8b84a;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; min-height: 100vh;
    font-family: "Segoe UI", system-ui, sans-serif;
    background:
      radial-gradient(ellipse at 20% 0%, #dfeaf3 0%, transparent 50%),
      radial-gradient(ellipse at 80% 100%, #efe6d4 0%, transparent 45%),
      var(--paper);
    color: var(--ink);
    display: flex; align-items: center; justify-content: center;
    padding: 2rem 1rem;
  }
  .card {
    width: min(520px, 100%);
    background: #fff;
    border: 1px solid #d8d2c8;
    border-radius: 14px;
    padding: 2rem 1.75rem;
    box-shadow: 0 10px 40px rgba(26,35,50,.08);
  }
  h1 { font-family: Georgia, serif; font-size: 1.75rem; margin: 0 0 .5rem; }
  p { color: #5a6577; line-height: 1.5; margin: 0 0 1rem; }
  ul { color: #5a6577; margin: 0 0 1.5rem; padding-left: 1.2rem; line-height: 1.6; }
  button {
    width: 100%;
    border: none; border-radius: 8px;
    background: var(--gold); color: #111;
    font-size: 1.05rem; font-weight: 700;
    padding: .9rem 1rem; cursor: pointer;
  }
  button:disabled { opacity: .6; cursor: wait; }
  button:hover:not(:disabled) { filter: brightness(1.05); }
  .status {
    margin-top: 1rem; min-height: 3rem;
    font-size: .92rem; color: var(--accent);
  }
  .status.error { color: #a33a3a; }
  a { color: var(--accent); font-weight: 600; }
  .hint { font-size: .8rem; margin-top: 1.25rem; color: #888; }
</style>
</head>
<body>
  <div class="card">
    <h1>ACT Test Generator</h1>
    <p>Press the button to create an <strong>Enhanced ACT–style</strong> English + Reading practice test (original content) and save it in <code>tests</code>.</p>
    <ul>
      <li><strong>English:</strong> 5 passages · <strong>50</strong> questions · 35 minutes</li>
      <li><strong>Reading:</strong> paired + single passages · <strong>36</strong> questions · 40 minutes</li>
      <li>Booklet layout · ABCD / FGHJ · study key hidden until you open it</li>
    </ul>
    <button type="button" id="go">Generate Enhanced Practice Test</button>
    <div class="status" id="status"></div>
    <p class="hint">Keep the black terminal window open while you use this page. Double-click <code>run.bat</code> anytime to start again.</p>
  </div>
<script>
const status = document.getElementById("status");
const btn = document.getElementById("go");

btn.addEventListener("click", async () => {
  btn.disabled = true;
  status.className = "status";
  status.textContent = "Generating Enhanced ACT–style English + Reading test…";
  try {
    const res = await fetch("/api/generate", { method: "POST" });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "Generation failed");
    status.innerHTML = "Saved <strong>" + data.filename + "</strong><br/>"
      + '<a href="' + data.url + '" target="_blank">Open test in new tab</a>';
    window.open(data.url, "_blank");
  } catch (err) {
    status.className = "status error";
    status.textContent = String(err.message || err);
  } finally {
    btn.disabled = false;
  }
});
</script>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        sys.stdout.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))

    def _send(self, code: int, body: bytes, content_type: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path in ("/", "/index.html"):
            self._send(200, INDEX_HTML.encode("utf-8"), "text/html; charset=utf-8")
            return
        if path.startswith("/tests/"):
            name = path[len("/tests/") :]
            if ".." in name or "/" in name or "\\" in name:
                self._send(400, b"Bad request", "text/plain")
                return
            file_path = TESTS_DIR / name
            if file_path.is_file():
                data = file_path.read_bytes()
                self._send(200, data, "text/html; charset=utf-8")
                return
            self._send(404, b"Not found", "text/plain")
            return
        self._send(404, b"Not found", "text/plain")

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path != "/api/generate":
            self._send(404, b'{"error":"Not found"}', "application/json")
            return
        try:
            test = build_test()
            file_path, test = save_test(str(TESTS_DIR), test)
            filename = os.path.basename(file_path)
            payload = {
                "ok": True,
                "filename": filename,
                "path": file_path,
                "url": f"/tests/{filename}",
                "english_questions": test["english_count"],
                "reading_questions": test["reading_count"],
                "total": test["english_count"] + test["reading_count"],
            }
            body = json.dumps(payload).encode("utf-8")
            self._send(200, body, "application/json")
        except Exception as exc:  # noqa: BLE001
            body = json.dumps({"error": str(exc)}).encode("utf-8")
            self._send(500, body, "application/json")


def main() -> None:
    TESTS_DIR.mkdir(exist_ok=True)
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://127.0.0.1:{PORT}/"
    print("=" * 56)
    print("  ACT Test Generator is running")
    print(f"  Open: {url}")
    print(f"  Tests save to: {TESTS_DIR}")
    print("  Press Ctrl+C to stop")
    print("=" * 56)
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        server.server_close()


if __name__ == "__main__":
    main()
