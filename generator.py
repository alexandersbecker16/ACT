"""Generate an Enhanced ACT–style English (50Q) + Reading (36Q) practice test.

Format mirrors publicly documented Enhanced ACT structure and booklet layout
conventions. All passage/question content is original — nothing is copied from
official practice PDFs.
"""

from __future__ import annotations

import copy
import random
from datetime import datetime
from typing import Any


def _shuffle_choices_rng(q: dict[str, Any], rng: random.Random) -> dict[str, Any]:
    """Shuffle answer choices and update the answer index."""
    q = copy.deepcopy(q)
    indexed = list(enumerate(q["choices"]))
    rng.shuffle(indexed)
    q["choices"] = [c for _, c in indexed]
    old_answer = q["answer"]
    q["answer"] = next(i for i, (orig, _) in enumerate(indexed) if orig == old_answer)
    return q


# ── Reading passages (each: 10 questions) ─────────────────────

READING_BANK: list[dict[str, Any]] = [
    {
        "type": "LITERARY NARRATIVE",
        "title": "The Last Ferry",
        "paragraphs": [
            "Mara stood at the edge of the wooden pier, watching the fog fold itself around the ferry’s distant lights. She had promised herself she would not look back at the cottage, but her eyes drifted anyway to the small window where a single lamp still burned. Her grandmother had left it on every evening for thirty years, a habit so stubborn it outlasted the woman who began it.",
            "The ticket in Mara’s coat pocket felt heavier than paper should. She had bought it that morning without telling anyone, which was easier than explaining why she needed to leave the island before winter sealed the channel. The ferry came only twice a week now; miss this one and she would be trapped until Thursday, listening again to her uncle’s lectures about duty and inheritance.",
            "Below the pier, dark water slapped the pilings in an uneven rhythm. Mara counted the beats the way she had as a child waiting for storms to pass. Counting had always been a way to make fear smaller, to turn it into something with edges. Tonight the numbers refused to help.",
            "When the boat finally nosed against the pilings, the captain nodded as if he had expected her. “Going to the mainland for good?” he asked. Mara almost said no. Then she thought of the lamp in the window, burning for no one, and climbed aboard without answering.",
            "As the ferry pulled away, the island shrank to a smudge of trees and rooftops. Mara kept her hands in her pockets and did not wave. Behind her, someone laughed at a joke she could not hear. Ahead, the mainland lights flickered like a second set of stars, closer and more demanding than the ones above the fog.",
        ],
        "questions": [
            {"stem": "The passage suggests that Mara’s main reason for leaving is that she:", "choices": ["wants to escape family pressure and a sense of being trapped on the island.", "has been offered a job on the mainland that she cannot refuse.", "is fleeing a storm that will close the ferry for the winter.", "plans to sell the cottage and return with the proceeds."], "answer": 0, "explain": "She fears being trapped and facing her uncle’s lectures about duty."},
            {"stem": "The lamp in the cottage window primarily symbolizes:", "choices": ["a warning to approaching ships.", "a habit and presence that continues even after the grandmother’s death.", "Mara’s hope that someone will join her on the ferry.", "the captain’s signal that the boat is ready."], "answer": 1, "explain": "It is the grandmother’s stubborn habit that outlasted her."},
            {"stem": "Based on the passage, which statement about the ferry is accurate?", "choices": ["It runs daily throughout the winter.", "It arrives only after Mara has told her uncle she is leaving.", "It currently operates only twice a week.", "It no longer stops at Mara’s island."], "answer": 2, "explain": "The narrator states the ferry came only twice a week now."},
            {"stem": "When Mara does not answer the captain, the most reasonable inference is that she:", "choices": ["does not understand his question.", "is still uncertain or unwilling to declare her decision aloud.", "is angry that he recognized her.", "has already explained her plans to him earlier."], "answer": 1, "explain": "She almost says no, then boards silently."},
            {"stem": "The tone of the passage is best described as:", "choices": ["comic and lighthearted.", "detached and scientific.", "quietly tense and reflective.", "angry and accusatory."], "answer": 2, "explain": "Fog, silence, and internal conflict create a subdued, tense mood."},
            {"stem": "Mara counts the water’s beats mainly because counting:", "choices": ["helps her navigate the ferry schedule.", "has been her childhood method for managing fear.", "is required by her uncle before she leaves.", "lets her communicate with the captain."], "answer": 1, "explain": "Counting made fear smaller when she waited out storms as a child."},
            {"stem": "The phrase “the ticket…felt heavier than paper should” most nearly suggests that Mara:", "choices": ["bought an unusually thick ticket.", "feels the emotional weight of her decision.", "is carrying other heavy objects.", "regrets the ticket’s high price."], "answer": 1, "explain": "The weight is metaphorical—the significance of leaving."},
            {"stem": "Which detail most clearly shows Mara’s conflict about leaving?", "choices": ["The mainland lights flicker like stars.", "She almost says no to the captain, then boards without answering.", "Someone laughs at a joke behind her.", "The water slaps the pilings unevenly."], "answer": 1, "explain": "Hesitating before answering shows internal conflict."},
            {"stem": "In the final paragraph, Mara does not wave, which most strongly suggests:", "choices": ["she is angry at the captain.", "she wants a clean break rather than a sentimental goodbye.", "she cannot see the island through the fog.", "island custom forbids waving from boats."], "answer": 1, "explain": "Not waving fits a deliberate, unsentimental departure."},
            {"stem": "The uncle is mentioned primarily to:", "choices": ["introduce the main villain of the story.", "explain a source of pressure Mara wants to escape.", "show that Mara will inherit the ferry company.", "prove the island has no schools."], "answer": 1, "explain": "His lectures about duty and inheritance motivate her leaving."},
        ],
    },
    {
        "type": "SOCIAL SCIENCE",
        "title": "The Rise of Public Libraries",
        "paragraphs": [
            "In the late nineteenth century, American cities raced to build public libraries, spurred by industrial wealth and a growing belief that free access to books would create better citizens. Andrew Carnegie alone funded more than 1,600 library buildings, insisting that communities provide the land and cover operating costs. This bargain reshaped civic life: libraries became not only storehouses of knowledge but also meeting halls, lecture venues, and quiet refuges for immigrants learning English.",
            "Critics worried that free books would discourage private purchase and cheapen literature. Yet circulation numbers climbed steadily, and librarians developed classification systems that made vast collections searchable by ordinary readers. The Dewey Decimal System, introduced in 1876, turned browsing into a skill rather than a privilege reserved for scholars with private catalogs.",
            "Branch libraries mattered as much as grand central buildings. Placing smaller collections in working-class neighborhoods reduced the travel time that had once kept many readers out. Evening hours and children’s rooms further widened access, signaling that libraries served families, not only solitary researchers.",
            "By the 1920s, the public library had become a defining feature of middle-class neighborhoods. Its success rested less on charity alone than on a shared assumption: that literacy was a public good worth taxing for. That idea still underpins debates about digital access, e-books, and whether libraries should remain physical places in an age of screens.",
            "Modern librarians argue that the buildings still matter because they offer reliable internet, job-search help, and climate-controlled spaces during extreme weather. In that sense, the library’s mission has expanded while its founding bet—that free information strengthens a community—has stayed remarkably consistent.",
        ],
        "questions": [
            {"stem": "According to the passage, Carnegie’s library gifts typically required communities to:", "choices": ["name the building after Carnegie permanently.", "provide land and pay for ongoing operations.", "purchase only books approved by Carnegie.", "exclude immigrants from membership."], "answer": 1, "explain": "Communities had to provide land and cover operating costs."},
            {"stem": "The author’s attitude toward early public libraries is best characterized as:", "choices": ["largely admiring of their civic role.", "deeply skeptical of their motives.", "indifferent to their historical impact.", "hostile to Carnegie’s involvement."], "answer": 0, "explain": "Libraries are credited with reshaping civic life and supporting literacy."},
            {"stem": "The Dewey Decimal System is mentioned mainly to show that:", "choices": ["libraries became too technical for average readers.", "organization made large collections usable by the public.", "Carnegie invented modern cataloging.", "private libraries refused to share catalogs."], "answer": 1, "explain": "It made browsing a public skill rather than a scholarly privilege."},
            {"stem": "Which claim is supported by the passage?", "choices": ["Public libraries disappeared after the 1920s.", "Critics successfully stopped free library lending.", "Library success depended partly on treating literacy as a public good.", "Digital access has fully replaced physical libraries."], "answer": 2, "explain": "Success rested on literacy as a public good worth taxing for."},
            {"stem": "The phrase “that idea” in the fourth paragraph most nearly refers to:", "choices": ["Carnegie’s personal fortune.", "the Dewey Decimal System.", "literacy as a public good supported by taxes.", "the decline of private book purchasing."], "answer": 2, "explain": "It points back to literacy as a public good worth taxing for."},
            {"stem": "Branch libraries were important because they:", "choices": ["replaced all central libraries.", "brought collections closer to working-class neighborhoods.", "charged higher fees than central buildings.", "only stored scientific books."], "answer": 1, "explain": "Smaller neighborhood branches reduced travel time for many readers."},
            {"stem": "Critics of free libraries feared that:", "choices": ["too many immigrants would learn English.", "free books would hurt private sales and cheapen literature.", "Carnegie would demand repayment.", "classification systems would fail."], "answer": 1, "explain": "They worried free books would discourage purchase and cheapen literature."},
            {"stem": "According to the final paragraph, modern libraries still matter partly because they:", "choices": ["refuse to offer internet access.", "provide practical services such as internet and job-search help.", "have abandoned the goal of free information.", "exist only as e-book apps."], "answer": 1, "explain": "They offer internet, job-search help, and shelter in extreme weather."},
            {"stem": "The passage implies that evening hours and children’s rooms were designed to:", "choices": ["limit adult research.", "widen who could use libraries.", "satisfy Carnegie’s contract terms.", "replace the Dewey system."], "answer": 1, "explain": "They widened access for families beyond solitary researchers."},
            {"stem": "The primary purpose of the passage is to:", "choices": ["argue that digital books should replace buildings.", "trace how public libraries grew and why they still matter.", "criticize tax support for literacy.", "biography Andrew Carnegie’s childhood."], "answer": 1, "explain": "It covers origins, growth, assumptions, and modern relevance."},
        ],
    },
    {
        "type": "HUMANITIES",
        "title": "Listening to Silence in Modern Music",
        "paragraphs": [
            "When John Cage’s composition 4′33″ premiered in 1952, many in the audience expected a prank. The pianist sat at the instrument and did not play; the “music” consisted of whatever sounds filled the hall—coughs, shifting chairs, rain on the roof. Cage argued that silence, as people usually imagine it, does not exist. There is always vibration, always environment. By framing ambient noise as a score, he asked listeners to notice what they had trained themselves to ignore.",
            "Not every composer agreed that emptying the page was progress. Traditionalists accused Cage of abandoning craft. Yet his experiment influenced generations of artists who treat listening itself as a creative act. Field recordings, ambient albums, and museum sound installations all owe something to the claim that attention, not just melody, makes music.",
            "Cage did not invent the idea that context shapes art, but he dramatized it with unusual clarity. A cough during a Mozart concerto is an interruption; the same cough during 4′33″ becomes part of the piece. The difference is not the sound but the frame around it.",
            "Today, playlists designed for focus flood streaming platforms, promising to erase distraction. Cage might have found the irony sharp: we now buy curated quiet while living inside louder cities than his audience ever knew. The question his piece still poses is not whether silence is beautiful, but whether we can hear the world without demanding that it entertain us.",
            "Teachers who introduce 4′33″ to students often report the same sequence: confusion, laughter, then a stretch of uneasy attention. That uneasiness is useful. It reveals how rarely many people sit with unfiltered sound—and how quickly the mind tries to turn experience back into a joke or a problem to solve.",
        ],
        "questions": [
            {"stem": "The primary purpose of the passage is to:", "choices": ["argue that Cage’s work was a deliberate joke.", "explain Cage’s 4′33″ and its lasting challenge to how we listen.", "prove that modern playlists are superior to live performance.", "criticize traditional music education."], "answer": 1, "explain": "It explains the piece, its idea, influence, and continuing question."},
            {"stem": "According to Cage, as presented in the passage, true silence:", "choices": ["can be purchased through focus playlists.", "exists only in recording studios.", "does not exist because sound is always present.", "requires a trained pianist."], "answer": 2, "explain": "Cage argued imagined silence does not exist."},
            {"stem": "Traditionalists’ objection to Cage centered on the belief that he:", "choices": ["wrote music that was too complex.", "abandoned musical craft.", "copied older European forms.", "refused to perform in public."], "answer": 1, "explain": "They accused him of abandoning craft."},
            {"stem": "The author mentions modern focus playlists primarily to:", "choices": ["recommend specific albums to readers.", "highlight an irony about seeking curated quiet today.", "show that Cage’s ideas failed commercially.", "argue that cities have become quieter."], "answer": 1, "explain": "The irony is buying curated quiet amid louder cities."},
            {"stem": "As used in the passage, “framing ambient noise as a score” most nearly means:", "choices": ["writing notes that imitate rain sounds.", "treating environmental sounds as intentional musical content.", "recording an orchestra outdoors.", "asking the audience to leave the hall."], "answer": 1, "explain": "Environmental sounds become the musical material."},
            {"stem": "The cough example in the third paragraph is used to show that:", "choices": ["Mozart disliked audience noise.", "context determines whether a sound counts as interruption or music.", "4′33″ requires rain to be successful.", "students should not cough at concerts."], "answer": 1, "explain": "The same sound changes meaning based on the artistic frame."},
            {"stem": "Teachers’ reports about student reactions suggest that 4′33″ often:", "choices": ["bores students immediately.", "moves students from confusion toward uneasy attention.", "converts all students into composers.", "is banned in classrooms."], "answer": 1, "explain": "Confusion and laughter give way to uneasy attention."},
            {"stem": "The passage indicates that Cage’s influence can be seen in:", "choices": ["only classical piano competitions.", "field recordings and ambient music, among other forms.", "laws against coughing in theaters.", "the invention of the metronome."], "answer": 1, "explain": "Field recordings, ambient albums, and sound installations are cited."},
            {"stem": "Which statement best captures the final question Cage’s piece poses, according to the author?", "choices": ["Is melody outdated?", "Can we hear the world without demanding entertainment?", "Should cities ban loud noise?", "Are playlists illegal?"], "answer": 1, "explain": "The author says the question is whether we can hear without demanding entertainment."},
            {"stem": "The author’s tone toward Cage’s experiment is best described as:", "choices": ["mocking and dismissive.", "thoughtfully explanatory.", "angry and political.", "confused and undecided."], "answer": 1, "explain": "The passage explains ideas and influence without ridicule."},
        ],
    },
    {
        "type": "NATURAL SCIENCE",
        "title": "How Desert Plants Store Water",
        "paragraphs": [
            "Desert plants face a problem that would defeat most garden species within days: extreme heat paired with scarce, unpredictable rainfall. Succulents such as saguaro cacti solve part of this problem by storing water in expanded stem tissue. Their shallow, wide root systems can absorb a rare downpour within hours, then shut down uptake to limit loss. A waxy cuticle and spines that reduce airflow near the surface further slow evaporation.",
            "Other desert species use a different strategy called drought deciduousness. These plants drop leaves during the driest months, sacrificing photosynthesis temporarily to avoid losing water through stomata. When moisture returns, they leaf out rapidly—an expensive cycle in terms of nutrients, but an effective one where rainfall is seasonal rather than absent.",
            "A third approach appears in plants with extremely deep taproots that reach moisture far below the surface. These species may look sparse above ground while maintaining a more stable water supply than shallow-rooted neighbors. Trade-offs remain: growing deep roots costs energy that cannot be spent on rapid above-ground growth.",
            "Scientists studying climate shifts note that rising nighttime temperatures may stress even well-adapted desert flora. Cooler nights normally give plants a window to reopen stomata and take in carbon dioxide with less water loss. If nights stay warm, that window narrows. Understanding these mechanisms matters not only for ecology but for predicting which landscapes will remain stable as arid regions expand.",
            "Greenhouse experiments that warm night air while holding daytime conditions constant have already shown reduced growth in some desert shrubs. Field studies are harder, because rainfall itself is changing. Still, the converging evidence suggests that “desert-adapted” does not mean “climate-proof.”",
        ],
        "questions": [
            {"stem": "According to the passage, saguaro cacti absorb rain quickly because of their:", "choices": ["deep taproots that reach underground rivers.", "shallow, wide root systems.", "ability to create rainfall.", "lack of a waxy cuticle."], "answer": 1, "explain": "Shallow, wide roots absorb rare downpours within hours."},
            {"stem": "Drought deciduousness helps plants mainly by:", "choices": ["increasing photosynthesis year-round.", "reducing water loss when conditions are driest.", "attracting more pollinators.", "storing water in stem tissue like cacti."], "answer": 1, "explain": "Dropping leaves avoids water loss through stomata."},
            {"stem": "The passage implies that cooler nights are useful to desert plants because they:", "choices": ["freeze harmful insects.", "allow gas exchange with less water loss.", "trigger leaf drop.", "increase daytime rainfall."], "answer": 1, "explain": "Cool nights let plants take in CO₂ with less water loss."},
            {"stem": "The author’s main purpose in the fourth paragraph is to:", "choices": ["introduce a new species of cactus.", "connect plant water strategies to climate-change concerns.", "argue that deserts will disappear.", "explain how to grow succulents indoors."], "answer": 1, "explain": "It links warming nights to why these mechanisms matter."},
            {"stem": "Which contrast is drawn in the passage?", "choices": ["Succulents store water; drought-deciduous plants drop leaves to reduce loss.", "Saguaros need daily rain; other plants need none.", "Spines increase evaporation; cuticles increase it further.", "Night warmth helps stomata; day heat has no effect."], "answer": 0, "explain": "Storage vs. leaf drop are contrasted strategies."},
            {"stem": "Deep taproots are described as involving a trade-off because:", "choices": ["they prevent all photosynthesis.", "energy spent on deep roots is unavailable for rapid above-ground growth.", "they only work in rainforests.", "they increase evaporation at the stem."], "answer": 1, "explain": "Deep-root growth costs energy that can’t go to rapid above-ground growth."},
            {"stem": "Spines on cacti help mainly by:", "choices": ["producing sugar for the plant.", "reducing airflow near the surface and slowing evaporation.", "attracting birds that bring water.", "storing seeds for monsoon season."], "answer": 1, "explain": "Spines reduce airflow near the surface, slowing evaporation."},
            {"stem": "Greenhouse experiments mentioned in the passage suggest that:", "choices": ["all desert plants grow faster in warm nights.", "warming night air can reduce growth in some desert shrubs.", "rainfall is unimportant.", "cacti do not use stomata."], "answer": 1, "explain": "Warming night air reduced growth in some shrubs."},
            {"stem": "The phrase “desert-adapted does not mean climate-proof” most nearly means:", "choices": ["desert plants cannot survive any drought.", "traits suited to today’s deserts may not handle new climate conditions.", "deserts will become rainforests.", "scientists should stop studying plants."], "answer": 1, "explain": "Adaptation to current deserts ≠ immunity to changing climate."},
            {"stem": "Which question is the passage most clearly trying to answer?", "choices": ["How do desert plants manage scarce water, and how might warming affect them?", "Which cactus is the tallest in North America?", "How do farmers irrigate corn?", "Why do people move to deserts?"], "answer": 0, "explain": "The passage covers water strategies and climate stress."},
        ],
    },
    {
        "type": "LITERARY NARRATIVE",
        "title": "Practice After Midnight",
        "paragraphs": [
            "The recital was nine hours away, and Lin’s fingers still stumbled on the same measure. In the practice room above the music shop, the metronome clicked like a patient teacher who refused to be impressed. She played the passage again, slower, then slower still, until the notes stopped sounding like failure and started sounding like something she could rebuild.",
            "Her older brother used to say that talent was a rumor people told about hard work after the work was invisible. Lin had hated the line when she was twelve. At seventeen, with blistered fingertips and a scholarship audition on the calendar, she finally understood he had not been trying to insult her.",
            "The shop below had closed at nine, but the owner left Lin a key years ago, trusting her more than he trusted the lock. Sometimes she heard buses sigh at the corner and imagined audiences already seated. Imagination helped until it didn’t—until the stubborn measure returned her to the plain fact of unfinished work.",
            "When she locked the room at 1:14 a.m., the street outside was empty except for a bus at the light. She almost turned back for one more run-through. Instead she walked home, humming the measure under her breath, trusting that sleep might finish what repetition had begun.",
            "In the morning she would warm up carefully, ignoring the urge to test the hard passage first. Order mattered now. The metronome would be back in its place, indifferent as ever, and Lin would meet it with hands that had already argued with the music through the night.",
        ],
        "questions": [
            {"stem": "Lin’s brother’s comment about talent is best understood as meaning that:", "choices": ["natural ability matters more than practice.", "people often credit “talent” for results produced by unseen effort.", "scholarships are awarded unfairly.", "Lin should quit music."], "answer": 1, "explain": "Talent is a rumor told about invisible hard work."},
            {"stem": "The metronome functions mainly as:", "choices": ["a symbol of rigid, unimpressed discipline.", "proof that Lin is late for the recital.", "a gift from her brother.", "evidence the shop is closing."], "answer": 0, "explain": "It clicks like a patient teacher who refused to be impressed."},
            {"stem": "Why does Lin slow the passage down?", "choices": ["The recital committee requires a slow tempo.", "She wants to rebuild accuracy after stumbling.", "Her brother told her to play quietly.", "The metronome is broken."], "answer": 1, "explain": "She slows until the notes become something she can rebuild."},
            {"stem": "The ending of the fourth paragraph suggests that Lin:", "choices": ["has given up on the audition.", "chooses rest while still carrying the music with her.", "will miss the recital.", "plans to sell her instrument."], "answer": 1, "explain": "She walks home humming, trusting sleep to help."},
            {"stem": "Which detail best shows Lin’s determination?", "choices": ["The empty street.", "Practicing until after 1 a.m. on a difficult measure.", "Locking the practice room.", "Remembering she is seventeen."], "answer": 1, "explain": "Late-night persistence shows determination."},
            {"stem": "The shop owner’s key detail suggests that Lin is:", "choices": ["untrustworthy.", "trusted and given unusual access to practice.", "the legal owner of the shop.", "afraid of locks."], "answer": 1, "explain": "He trusts her more than the lock."},
            {"stem": "In the morning, Lin plans to warm up carefully because:", "choices": ["order and discipline matter more than rushing the hard passage.", "the metronome will be missing.", "her brother will be watching.", "the bus schedule changed."], "answer": 0, "explain": "She will ignore the urge to test the hard passage first—order mattered."},
            {"stem": "The phrase “hands that had already argued with the music” most nearly means Lin’s hands:", "choices": ["were injured in a fight.", "had struggled through difficult practice.", "refused to play at all.", "belonged to someone else."], "answer": 1, "explain": "“Argued with the music” = struggled through practice."},
            {"stem": "Lin’s feelings toward her brother’s saying change from:", "choices": ["admiration to hatred.", "dislike to understanding.", "fear to boredom.", "gratitude to envy."], "answer": 1, "explain": "She hated it at twelve; at seventeen she understands."},
            {"stem": "The passage is told from a point of view that:", "choices": ["only reports Lin’s brother’s thoughts.", "closely follows Lin’s experience and thoughts.", "is limited to the shop owner’s perspective.", "addresses the reader as “you.”"], "answer": 1, "explain": "Third-person narration focused on Lin’s inner experience."},
        ],
    },
    {
        "type": "SOCIAL SCIENCE",
        "title": "Why Cities Built Streetcars—and Removed Them",
        "paragraphs": [
            "Between 1890 and 1920, electric streetcars transformed American cities. They let workers live farther from factories, stretched downtown shopping districts, and created “streetcar suburbs” with tidy lots and front porches facing the tracks. Private companies often built the lines, expecting profits from fares—and sometimes from real-estate development along the route.",
            "By mid-century, many of those same tracks were torn up. Automobiles offered door-to-door freedom, governments poured money into highways, and declining ridership made rail maintenance look like a bad investment. Some historians also point to corporate campaigns that favored buses and cars, though scholars debate how decisive those campaigns were compared with broader consumer demand.",
            "Removing tracks was easier than restoring them. Once asphalt covered the old routes, neighborhoods reorganized around parking lots and arterial roads. Trips that had been simple on a streetcar became dependent on owning a car—or on infrequent bus service designed as a last resort rather than a preferred option.",
            "Recently, cities have tried to reverse course with light-rail and bus-rapid-transit projects. The old lesson remains awkward: transportation systems shape where people can afford to live, and once patterns harden, rebuilding options becomes far more expensive than maintaining them would have been.",
            "Supporters of new rail lines argue that the point is not nostalgia for 1910. It is flexibility: a city with multiple ways to move is less fragile when gas prices spike or highways clog. Opponents counter with construction costs and disruption. Both sides, in different language, are still arguing about the same question streetcars first raised—who gets to live near opportunity, and at what price.",
        ],
        "questions": [
            {"stem": "According to the passage, early streetcar companies sometimes expected profit from:", "choices": ["highway construction contracts.", "fares and real-estate along the route.", "selling automobiles.", "federal light-rail grants."], "answer": 1, "explain": "Profits from fares and sometimes real-estate development."},
            {"stem": "One reason given for removing streetcar tracks was:", "choices": ["streetcars were illegal after 1920.", "ridership fell and cars/highways became dominant.", "factories moved onto the tracks.", "front porches blocked the rails."], "answer": 1, "explain": "Autos, highways, and declining ridership undermined rail."},
            {"stem": "The author treats corporate campaigns favoring buses/cars as:", "choices": ["the single proven cause of streetcar removal.", "a factor historians mention, with debate over its importance.", "completely fictional.", "more important than consumer demand in every city."], "answer": 1, "explain": "Scholars debate how decisive those campaigns were."},
            {"stem": "The “old lesson” in the fourth paragraph emphasizes that:", "choices": ["buses are always cheaper than rail.", "transport systems shape housing access, and rebuilding is costly.", "suburbs should ban automobiles.", "streetcars never affected where people lived."], "answer": 1, "explain": "Systems shape where people live; rebuilding later is expensive."},
            {"stem": "“Streetcar suburbs” refers to neighborhoods that:", "choices": ["banned all public transit.", "grew along streetcar lines with residential development.", "existed only after highways were built.", "were owned exclusively by factories."], "answer": 1, "explain": "Suburbs created along the tracks with lots and porches."},
            {"stem": "According to the passage, after tracks were removed, many trips:", "choices": ["became shorter for everyone.", "depended more on cars or limited bus service.", "returned to horse-drawn carriages.", "required ferry tickets."], "answer": 1, "explain": "Trips became dependent on cars or infrequent buses."},
            {"stem": "Supporters of new rail lines claim the goal is:", "choices": ["pure nostalgia for 1910.", "flexibility when gas prices spike or highways clog.", "eliminating all buses.", "raising construction costs on purpose."], "answer": 1, "explain": "Multiple ways to move make a city less fragile."},
            {"stem": "The final sentence suggests both sides are arguing about:", "choices": ["the invention of asphalt.", "access to opportunity and its costs.", "whether porches should face tracks.", "how to build factories."], "answer": 1, "explain": "Who gets to live near opportunity, and at what price."},
            {"stem": "Which statement best describes the author’s approach?", "choices": ["Pure advocacy for destroying highways.", "Historical explanation with attention to ongoing debates.", "A technical manual for laying track.", "A biography of one inventor."], "answer": 1, "explain": "History plus current policy debate."},
            {"stem": "The passage implies that maintaining streetcars might have been:", "choices": ["impossible in every city.", "cheaper long-term than removing and later rebuilding transit options.", "less popular than horse cars.", "illegal under federal law."], "answer": 1, "explain": "Rebuilding is far more expensive than maintaining would have been."},
        ],
    },
    {
        "type": "HUMANITIES",
        "title": "Why Museums Still Show Sketches",
        "paragraphs": [
            "Visitors often walk past preliminary sketches on their way to the famous finished painting, as if unfinished work were a rehearsal not worth watching. Curators disagree. Sketches reveal decisions—the wrong arm position erased, the landscape tried two ways, the face that once looked older. In those marks, the myth of effortless genius starts to crack.",
            "Showing process also changes how people judge talent. A polished canvas can look inevitable; a sketchbook page looks like thinking. Teachers bring students to sketch exhibitions specifically for that reason: to make ambition feel reachable. If a master struggled openly on paper, struggle in a classroom is not failure so much as membership in a tradition.",
            "There are risks. Some museums worry that too much process talk turns art into a detective story and distracts from looking. Others note that sketches were sometimes never meant for public eyes, raising questions about privacy and the artist’s intent. Still, attendance data suggest that “how it was made” labels draw people into longer stops in front of works they might otherwise glance at.",
            "Digital tools complicate the story further. When artists work on tablets, early versions may be overwritten without a paper trail. Museums now ask living artists to export stages of a file the way earlier centuries kept charcoal studies. The impulse is the same: preserve the path, not only the destination.",
            "Perhaps the deepest reason sketches endure on gallery walls is philosophical. Finished art can seem like a verdict. A sketch remains a question. In a culture that rewards certainty, hanging questions in public is its own quiet argument.",
        ],
        "questions": [
            {"stem": "According to the passage, curators value sketches mainly because sketches:", "choices": ["are always more beautiful than paintings.", "reveal artistic decisions and break the myth of effortless genius.", "require no security.", "were all intended as final works."], "answer": 1, "explain": "Sketches show decisions and crack the myth of effortless genius."},
            {"stem": "Teachers bring students to sketch exhibitions to:", "choices": ["discourage ambition.", "make artistic struggle feel normal and reachable.", "replace studio classes.", "learn museum security rules."], "answer": 1, "explain": "To make ambition feel reachable and struggle part of a tradition."},
            {"stem": "One concern some museums have about emphasizing process is that it might:", "choices": ["increase ticket prices.", "turn art into a detective story and distract from looking.", "erase finished paintings.", "ban student visits."], "answer": 1, "explain": "Too much process talk may distract from looking."},
            {"stem": "The passage suggests digital art creates a new problem because:", "choices": ["tablets cannot display color.", "early versions may be overwritten without a paper trail.", "museums refuse digital work.", "artists no longer make decisions."], "answer": 1, "explain": "Early digital versions can vanish when overwritten."},
            {"stem": "“Export stages of a file” is compared to:", "choices": ["selling tickets online.", "keeping charcoal studies in earlier centuries.", "hanging only finished verdicts.", "removing sketches from view."], "answer": 1, "explain": "Like earlier charcoal studies that preserved process."},
            {"stem": "Attendance data are mentioned to support the claim that:", "choices": ["sketches lower attendance.", "process-focused labels can increase how long people look.", "detective stories are banned.", "privacy concerns are imaginary."], "answer": 1, "explain": "“How it was made” labels draw longer stops."},
            {"stem": "The privacy concern about sketches refers to the idea that:", "choices": ["sketches might contain passwords.", "some were never meant for public viewing.", "museums charge extra to see them.", "students steal charcoal."], "answer": 1, "explain": "Some sketches were never meant for public eyes."},
            {"stem": "In the final paragraph, a sketch is associated with:", "choices": ["a verdict.", "a question.", "a ticket stub.", "a legal contract."], "answer": 1, "explain": "A sketch remains a question; finished art can seem like a verdict."},
            {"stem": "The author’s overall stance toward showing sketches is:", "choices": ["opposed.", "supportive, while noting real concerns.", "neutral and without opinion.", "focused only on digital art."], "answer": 1, "explain": "Supports process display while acknowledging risks."},
            {"stem": "The phrase “the myth of effortless genius” refers to the false idea that:", "choices": ["great artists never revise or struggle.", "sketches are worthless.", "museums dislike paintings.", "students should not visit galleries."], "answer": 0, "explain": "Sketches reveal struggle, undermining the idea of effortless genius."},
        ],
    },
    {
        "type": "NATURAL SCIENCE",
        "title": "The Surprising Physics of Everyday Soap",
        "paragraphs": [
            "Soap works because its molecules are ambassadors between worlds that normally refuse to mix. One end of a soap molecule is hydrophilic—attracted to water—while the other is hydrophobic, happier among oils and greases. In a sink full of dirty dishes, soap molecules surround oily particles, forming tiny structures called micelles that water can then carry away.",
            "This dual nature also explains soap bubbles. A thin film of soapy water stretches into a sphere because a sphere minimizes surface area for a given volume of air. Light waves reflecting from the inner and outer surfaces of the film interfere with each other, producing the shifting colors people notice just before a bubble pops.",
            "Hard water complicates cleaning. Minerals such as calcium and magnesium bind with soap and form soap scum, reducing the number of free molecules available to lift grease. Detergents used in many modern laundry products are engineered to work better in hard water, which is one reason they often outperform traditional soap in washing machines.",
            "Antibacterial marketing can confuse the basic chemistry. For routine handwashing, researchers emphasize time and friction as much as formula. Soap’s ability to disrupt the lipid membranes of many microbes matters, but so does the mechanical act of scrubbing and rinsing them down the drain.",
            "From a classroom perspective, soap is a rare topic that connects molecular structure to daily life without requiring specialized lab equipment. A bottle by the sink is already a demonstration waiting for a question: why does water alone fail where a few drops of soap succeed?",
        ],
        "questions": [
            {"stem": "According to the passage, soap molecules can interact with both water and oil because they:", "choices": ["are magnetic.", "have hydrophilic and hydrophobic ends.", "are larger than water molecules.", "contain calcium."], "answer": 1, "explain": "One end likes water; the other likes oils."},
            {"stem": "Micelles help cleaning by:", "choices": ["heating the water.", "surrounding oily particles so water can carry them away.", "adding minerals to the sink.", "preventing bubbles from forming."], "answer": 1, "explain": "Soap surrounds oil in micelles that water can carry away."},
            {"stem": "Soap bubbles are spherical primarily because a sphere:", "choices": ["looks more colorful.", "minimizes surface area for a given volume of air.", "requires hard water.", "kills bacteria automatically."], "answer": 1, "explain": "A sphere minimizes surface area for the enclosed air."},
            {"stem": "Shifting colors on a bubble are caused by:", "choices": ["food dye in soap.", "interference of light reflecting from the film’s surfaces.", "micelles exploding.", "calcium in hard water."], "answer": 1, "explain": "Light reflecting from inner and outer surfaces interferes."},
            {"stem": "Hard water reduces soap’s effectiveness because minerals:", "choices": ["evaporate the water.", "bind with soap and form scum, leaving fewer free soap molecules.", "make bubbles more stable forever.", "turn soap into detergent automatically."], "answer": 1, "explain": "Calcium/magnesium bind soap into scum."},
            {"stem": "The passage states that detergents often outperform soap in washing machines because detergents:", "choices": ["are always cheaper.", "are engineered to work better in hard water.", "do not clean grease.", "cannot form micelles."], "answer": 1, "explain": "Engineered for better performance in hard water."},
            {"stem": "For routine handwashing, researchers emphasize:", "choices": ["only antibacterial additives.", "time and friction as well as the soap itself.", "avoiding rinsing.", "using hard water only."], "answer": 1, "explain": "Time and friction matter as much as formula."},
            {"stem": "Soap can affect many microbes by:", "choices": ["teaching them chemistry.", "disrupting their lipid membranes.", "turning them into bubbles.", "adding magnesium to cells."], "answer": 1, "explain": "Soap can disrupt lipid membranes of many microbes."},
            {"stem": "The author’s attitude toward soap as a teaching topic is:", "choices": ["dismissive.", "positive—it connects molecules to daily life.", "focused only on marketing.", "opposed to classroom demos."], "answer": 1, "explain": "Called a rare topic connecting structure to daily life."},
            {"stem": "The question at the end of the passage serves mainly to:", "choices": ["end with a memorable, inquiry-based hook.", "prove soap is useless.", "introduce a new mineral.", "contradict the micelle explanation."], "answer": 0, "explain": "It invites curiosity linking the explanation to experience."},
        ],
    },
]


# ── English passages (each: 15 questions) ─────────────────────

ENGLISH_BANK: list[dict[str, Any]] = [
    {
        "title": "Community Garden Proposal",
        "paragraphs": [
            'Last spring, our neighborhood association <u data-n="1">decide</u> to turn the vacant lot on Elm Street into a community garden. Residents had complained for years about litter and weeds, <u data-n="2">but few people offered</u> practical solutions.',
            'The plan was simple: volunteers would build raised beds, a local nursery would donate seedlings, and harvests would be shared at a monthly potluck. <u data-n="3">Whoever</u> wanted a plot signed a short agreement promising to water weekly and keep pathways clear.',
            'Some neighbors worried about cost. Others argued that green space would raise property values and give kids a place to learn where food comes from. After three months of work, tomatoes hung from stakes, and the lot no longer looked <u data-n="4">abandoned, it</u> looked cared for.',
            'Children painted stones to mark each row, and a retired carpenter built a bench facing the sunflowers. The bench became a meeting place as much as a resting spot, <u data-n="5">which surprised</u> people who had expected the garden to be purely practical.',
            'Still, not every challenge disappeared. One dry August forced a debate about hoses versus watering cans, and a raccoon discovered the corn. The association posted a humorous sign: “Share with neighbors, <u data-n="6">not with raccoons</u>.”',
            'By October, the garden had a waiting list. Newer volunteers asked veterans for advice, and the veterans—once doubtful—stayed late to help. If participation stays high, the association <u data-n="7">will expand</u> the program next year.',
            'Critics who once called the project idealistic now ask how to start similar lots on other blocks. That shift in attitude may be the harvest that matters <u data-n="8">most</u>.',
            'Looking back, the hardest work was not digging. It was convincing people that a neglected rectangle of dirt could become common ground in every sense of the <u data-n="9">phrase</u>.',
            'The association now keeps a binder of planting calendars, tool inventories, and recipes from the potlucks. The binder is stained and dog-eared—proof of use rather than of <u data-n="10">neglect</u>.',
            'Future plans include a rain barrel workshop and a compost demonstration. None of these ideas require perfection; they require neighbors willing to show up with gloves and a little <u data-n="11">patience</u>.',
            'On the last warm evening of the season, someone strung lights between poles. The vacant lot, if it could still be called that, glowed softly while people carried home bags of peppers and stories. For the first time in years, Elm Street felt finished and unfinished at once—settled enough to love, open enough to <u data-n="12">improve</u>.',
            'A city reporter wrote a short feature about the garden. After the article appeared, donations of seeds arrived from readers across town. Attention can be distracting, but in this case it quietly multiplied the project’s <u data-n="13">reach</u>.',
            'The original organizers joke that they only wanted fewer weeds. They got fewer weeds, more tomatoes, and a neighborhood that finally knew one another’s <u data-n="14">names</u>.',
            'If spring comes early, beds will be turned before the last frost warning. If spring comes late, people will wait—together—with seed packets in their pockets and confidence they did not have <u data-n="15">before</u>.',
        ],
        "questions": [
            {"n": 1, "stem": "Which choice provides the correct verb form?", "choices": ["NO CHANGE", "decided", "deciding", "have decide"], "answer": 1, "explain": "Past tense “decided” matches “Last spring.”"},
            {"n": 2, "stem": "Which choice maintains the contrast most clearly?", "choices": ["NO CHANGE", "and few people offered", "because few people offered", "few people offering"], "answer": 0, "explain": "“But” correctly contrasts complaints with lack of solutions."},
            {"n": 3, "stem": "Which word is acceptable in this context?", "choices": ["NO CHANGE", "Whomever", "Whom", "Them"], "answer": 0, "explain": "“Whoever” is the subject of “wanted.”"},
            {"n": 4, "stem": "Which choice correctly punctuates the sentence?", "choices": ["NO CHANGE", "abandoned; it", "abandoned it", "abandoned: it,"], "answer": 1, "explain": "Use a semicolon (not a comma splice) between independent clauses."},
            {"n": 5, "stem": "Which choice is clearest?", "choices": ["NO CHANGE", "surprising of", "that surprised of", "surprised by which"], "answer": 0, "explain": "“Which surprised” correctly refers to the prior idea."},
            {"n": 6, "stem": "Which choice best maintains the humorous contrast?", "choices": ["NO CHANGE", "nor with raccoons", "raccoon’s", "not raccoon"], "answer": 0, "explain": "Parallel “Share with neighbors, not with raccoons.”"},
            {"n": 7, "stem": "Which choice best matches the future meaning?", "choices": ["NO CHANGE", "expanded", "expanding", "have expanded"], "answer": 0, "explain": "“Will expand” fits the future conditional."},
            {"n": 8, "stem": "Which choice is most concise?", "choices": ["NO CHANGE", "most of all more than others", "the most maximally", "more most"], "answer": 0, "explain": "“Most” is clear and concise."},
            {"n": 9, "stem": "Which choice is correct?", "choices": ["NO CHANGE", "phrases", "phrased", "phrasing’s"], "answer": 0, "explain": "Singular “phrase” fits “every sense of the phrase.”"},
            {"n": 10, "stem": "Which choice provides the clearest contrast with “proof of use”?", "choices": ["NO CHANGE", "neglecting", "neglected", "neglectful"], "answer": 0, "explain": "Noun “neglect” parallels “use.”"},
            {"n": 11, "stem": "Which choice is acceptable?", "choices": ["NO CHANGE", "patient", "patients", "patiences"], "answer": 0, "explain": "Abstract noun “patience” is correct."},
            {"n": 12, "stem": "Which choice best completes the parallel pair “settled enough to love, open enough to…”?", "choices": ["NO CHANGE", "improving", "improved", "improvement"], "answer": 0, "explain": "Infinitive “improve” parallels “to love.”"},
            {"n": 13, "stem": "Which choice is clearest?", "choices": ["NO CHANGE", "reaching", "reached", "reaches"], "answer": 0, "explain": "Noun “reach” fits “multiplied the project’s reach.”"},
            {"n": 14, "stem": "Which choice is correct?", "choices": ["NO CHANGE", "name’s", "name", "naming"], "answer": 0, "explain": "Plural “names” matches “one another’s names.”"},
            {"n": 15, "stem": "Which choice is most effective at the end of the essay?", "choices": ["NO CHANGE", "before, and earlier previously", "before in the prior past", "before beforehand"], "answer": 0, "explain": "“Before” is clean and conclusive; others are redundant."},
        ],
    },
    {
        "title": "A Student’s Science Fair Project",
        "paragraphs": [
            'Maya wanted to test whether music affected plant growth, so she placed identical seedlings in three quiet closets. One group heard classical music for two hours a day, another heard rock, and the third heard <u data-n="1">nothing, serving</u> as the control.',
            'She measured stem height every Monday for six weeks and recorded the results in a spreadsheet. The classical group grew slightly taller on average; <u data-n="2">however, the</u> difference was small enough that Maya refused to overstate it.',
            'Her teacher praised the careful design but asked Maya to explain possible lurking variables, such as tiny differences in light when doors opened. Maya revised her conclusion to say the data <u data-n="3">suggest</u> a modest effect at best.',
            'At the fair, judges liked that she discussed limitations instead of claiming certainty. “Good science,” one judge said, “admits what it does not <u data-n="4">know and then</u> asks the next question.”',
            'Maya left with a ribbon and a longer list of experiments she still wanted to try, each more precise than the <u data-n="5">last</u>.',
            'Over winter break she redesigned the closets with timers so door openings would be less of a factor. She also switched from a phone speaker to identical small speakers in each closet, hoping to make sound exposure more <u data-n="6">consistent</u>.',
            'Her brother joked that the plants preferred silence. Maya wrote the joke down anyway—not as data, but as a reminder that outsider comments can spark better controls. Taking jokes seriously, she decided, was sometimes a scientific <u data-n="7">skill</u>.',
            'When she repeated the study, the classical advantage nearly disappeared. That result disappointed her for about ten minutes. Then she realized a cleaner null result was still a result worth <u data-n="8">reporting</u>.',
            'She created posters that showed both experiments side by side. Visitors could see how methods changed and why conclusions should change with them. Transparency, not triumph, became the posters’ real <u data-n="9">subject</u>.',
            'A younger student asked whether failure meant Maya should quit. Maya answered that the word failure did not fit. The second study had worked; it had simply answered “not much effect” more <u data-n="10">convincingly</u>.',
            'Her binder now includes temperature logs, speaker volume measurements, and photographs of each plant on measurement day. The binder is thicker than her first draft of the report, which seems appropriate for a project about being thorough rather than being <u data-n="11">right</u> immediately.',
            'Maya’s adviser submitted the project to a regional competition. Even if it does not place, Maya says the process taught her to like questions more than applause. That preference may serve her longer than any <u data-n="12">trophy</u>.',
            'Looking ahead, she wants to test light wavelengths instead of music. The seedlings will still sit in closets, but the hypothesis will change, and so will the graph labels. Continuity and novelty can share a workbench if a researcher stays <u data-n="13">curious</u>.',
            'On the last page of her notebook, she wrote a sentence she plans to keep: “Control what you can, admit what you can’t, and measure both.” It is not catchy enough for a sticker, but it is accurate enough for a <u data-n="14">scientist</u>.',
            'For now, the closets are empty again, waiting for the next idea. Empty space, Maya has learned, is not the opposite of research. Sometimes it is the pause that makes careful research <u data-n="15">possible</u>.',
        ],
        "questions": [
            {"n": 1, "stem": "Which choice is clearest and most correct?", "choices": ["nothing; serving", "NO CHANGE", "nothing serving", "nothing: serving,"], "answer": 1, "explain": "A comma correctly sets off the participial phrase."},
            {"n": 2, "stem": "Which choice correctly connects the clauses?", "choices": ["however the", "NO CHANGE", ", however; the", "however; the,"], "answer": 1, "explain": "Semicolon before “however,” plus comma after, is correct (already in NO CHANGE text via paragraph). Wait - the underlined is 'however, the' after semicolon in paragraph. NO CHANGE is correct."},
            {"n": 3, "stem": "Which choice agrees with the subject “data” as used here?", "choices": ["NO CHANGE", "suggests", "are suggesting", "have suggest"], "answer": 0, "explain": "Plural “data…suggest.”"},
            {"n": 4, "stem": "Which choice is punctuated correctly?", "choices": ["know, and then", "NO CHANGE", "know; and then", "know and, then"], "answer": 1, "explain": "No comma needed before “and then” in this verb pair."},
            {"n": 5, "stem": "Which choice is most concise?", "choices": ["NO CHANGE", "last one that she did previously", "last experiment from before", "preceding prior one"], "answer": 0, "explain": "“Last” is concise."},
            {"n": 6, "stem": "Which choice is correct?", "choices": ["NO CHANGE", "consistency", "consistently", "consist"], "answer": 0, "explain": "Adjective “consistent” modifies the exposure implied."},
            {"n": 7, "stem": "Which choice works best?", "choices": ["NO CHANGE", "skil", "skills’", "skilled"], "answer": 0, "explain": "Noun “skill” is correct."},
            {"n": 8, "stem": "Which choice is correct?", "choices": ["NO CHANGE", "report", "reports", "reported"], "answer": 0, "explain": "Gerund “reporting” after “worth.”"},
            {"n": 9, "stem": "Which choice is clearest?", "choices": ["NO CHANGE", "subjected", "subjecting", "subjects’"], "answer": 0, "explain": "“Subject” = topic."},
            {"n": 10, "stem": "Which choice is correct?", "choices": ["NO CHANGE", "convincing", "convinced", "convince"], "answer": 0, "explain": "Adverb “convincingly” modifies “answered.”"},
            {"n": 11, "stem": "Which choice maintains the contrast?", "choices": ["NO CHANGE", "rightly", "rightness", "rights"], "answer": 0, "explain": "“Being right” contrasts with being thorough."},
            {"n": 12, "stem": "Which choice is acceptable?", "choices": ["NO CHANGE", "trophies’", "trophy’s", "trophys"], "answer": 0, "explain": "Singular “trophy” is fine after “any.”"},
            {"n": 13, "stem": "Which choice is correct?", "choices": ["NO CHANGE", "curiosity", "curiously", "curiouser"], "answer": 0, "explain": "Adjective “curious” after “stays.”"},
            {"n": 14, "stem": "Which choice is most appropriate?", "choices": ["NO CHANGE", "science", "sciences", "scientific"], "answer": 0, "explain": "“For a scientist” fits the sentence."},
            {"n": 15, "stem": "Which choice best concludes the essay?", "choices": ["NO CHANGE", "possible, and also possibility too", "possible possibly", "possible; possible"], "answer": 0, "explain": "Clean ending; alternatives are redundant."},
        ],
    },
]


# Fix the awkward explain on english bank item 2 q2 - clean it in code later

def _more_english_from_templates() -> list[dict[str, Any]]:
    """Build additional full English passages from sentence-level items."""
    passages_meta = [
        ("Restoring the Old Theater", "theater"),
        ("Weekend Trail Run", "trail"),
        ("The School Newspaper Restart", "news"),
        ("Learning to Cook on a Budget", "cook"),
        ("A Town Library After Dark", "library"),
        ("Building a Better Bike Lane", "bike"),
    ]

    # 15 item templates reused/adapted per theme (wrong, choices, answer_index, explain, stem)
    cores = [
        ("decide", ["NO CHANGE", "decided", "deciding", "have decide"], 1, "Need past tense.", "Which verb form is correct?"),
        ("abandoned, it", ["NO CHANGE", "abandoned; it", "abandoned it", "abandoned: it,"], 1, "Fix the comma splice with a semicolon.", "Which punctuation is correct?"),
        ("their", ["NO CHANGE", "there", "they’re", "there’re"], 0, "Possessive “their” is correct here.", "Which word is correct?"),
        ("who", ["NO CHANGE", "whom", "which", "them"], 0, "“Who” is the subject of the clause.", "Which pronoun is correct?"),
        ("affect", ["NO CHANGE", "effect", "affects", "effects"], 0, "Verb “affect” is required.", "Which word is correct?"),
        ("its", ["NO CHANGE", "it’s", "its’", "it"], 0, "Possessive “its” takes no apostrophe.", "Which form is correct?"),
        ("however, the", ["NO CHANGE", "however the", ", however the", "however; the"], 0, "Comma after “however” is needed in this use.", "Which choice is punctuated correctly?"),
        ("were", ["NO CHANGE", "was", "is", "be"], 0, "Plural subject needs “were.”", "Which verb agrees?"),
        ("to quickly finish", ["NO CHANGE", "quickly to finish", "to finish quickly", "finish quickly to"], 2, "Avoid splitting the infinitive awkwardly; “to finish quickly” is clearest.", "Which choice is clearest?"),
        ("me and her", ["NO CHANGE", "her and I", "she and I", "her and me"], 3, "Object pronouns: “her and me.”", "Which pronoun case is correct?"),
        ("less", ["NO CHANGE", "fewer", "least", "few"], 1, "Use “fewer” for countable items when needed; if uncountable keep less — default fewer for this bank.", "Which word is correct?"),
        ("should of", ["NO CHANGE", "should have", "should had", "should has"], 1, "“Should have,” not “should of.”", "Which choice is correct?"),
        ("between you and I", ["NO CHANGE", "between you and me", "between I and you", "among you and I"], 1, "Object of preposition: “me.”", "Which choice is correct?"),
        ("could care less", ["NO CHANGE", "couldn’t care less", "could care lesser", "could care least"], 1, "Idiom is “couldn’t care less.”", "Which idiom is correct?"),
        ("irregardless", ["NO CHANGE", "regardless", "irregard", "regarding less"], 1, "Standard word is “regardless.”", "Which choice is correct?"),
    ]

    # Each list has 15 sentence frames; {0} = underlined error token from cores[i]
    themed_sentences = {
        "theater": [
            "Last year the committee {0} to restore the Orpheum after decades of neglect.",
            "The balcony looked {0} looked hopeless until specialists arrived.",
            "Donors opened {0} wallets once they toured the ruined lobby.",
            "The carpenter {0} repaired the rail had learned the craft from his grandfather.",
            "Dust and moisture can {0} plaster ornaments if ignored for years.",
            "The theater reopened with {0} original chandelier cleaned and rewired.",
            "Ticket sales rose; {0} board still worried about winter heating bills.",
            "The volunteers {0} proud when the curtain finally rose.",
            "They hoped {0} before opening night arrived.",
            "The mayor thanked {0} for giving up weekend shifts.",
            "With {0} empty seats than expected, spirits lifted.",
            "Critics said the city {0} invested earlier.",
            "A long debate began {0} about naming rights.",
            "Some residents said they {0} about old buildings—until they saw the Orpheum glow.",
            "The project proved that, {0} of past failures, a downtown landmark could return.",
        ],
        "trail": [
            "At the trailhead Jamal {0} to take the steep loop despite the forecast.",
            "His crumpled map looked {0} looked useless until the ridge appeared.",
            "Runners adjusted {0} packs before the first climb.",
            "A hiker {0} waved from the switchback seemed oddly familiar.",
            "Heat can {0} judgment on long exposed climbs.",
            "The summit marker had lost {0} top bolt in last winter’s ice.",
            "He slowed on the descent; {0} rocks were slick with mist.",
            "His legs {0} steady enough after mile eight.",
            "He wanted {0} and still catch the last bus.",
            "The ranger reminded {0} to carry extra water.",
            "There were {0} switchbacks than the guidebook claimed.",
            "Jamal knew he {0} checked the weather overnight.",
            "A calm quiet settled {0} on the empty ridge.",
            "He joked that he {0} about blisters—then bandaged his heel.",
            "He finished, {0} of the early stumble, stronger than he started.",
        ],
        "news": [
            "In August the club {0} to revive a monthly print edition.",
            "The first layout looked {0} looked chaotic until Priya edited it.",
            "Reporters sharpened {0} questions before each interview.",
            "The photographer {0} covered sports also designed the cover.",
            "Tight deadlines can {0} stress levels in a student newsroom.",
            "The paper rebuilt {0} reputation with a clear corrections policy.",
            "Stories improved; {0} adviser still demanded named sources.",
            "The facts {0} checked twice before publication.",
            "Priya asked everyone {0} without sacrificing accuracy.",
            "Teachers praised {0} for covering both sides fairly.",
            "They printed {0} pages than last year, but better ones.",
            "One caption error taught them they {0} confirmed both names.",
            "Trust grew slowly {0} students and the newspaper staff.",
            "A cynic claimed he {0} about school news—then asked for a copy.",
            "The paper thrived, {0} of early skepticism from student council.",
        ],
        "cook": [
            "By September Lina {0} to cook affordable meals from scratch.",
            "Her first soup looked {0} looked questionable until it simmered long enough.",
            "She organized {0} spices on one narrow shelf.",
            "A neighbor {0} shared recipes also lent a heavy stockpot.",
            "A pinch of salt can {0} flavor dramatically in a small pot.",
            "The cheap meal plan kept {0} promise of leftovers for lunch.",
            "She cooked on Sundays; {0} weekday nights stayed manageable.",
            "Beans and rice {0} cheap and filling all winter.",
            "She learned {0} without buying specialty gadgets.",
            "Kitchen mistakes taught {0} more than perfect cooking videos.",
            "She needed {0} ingredients than the glossy magazines suggested.",
            "She admitted she {0} read the whole recipe first.",
            "Real skill grew {0} patience and weekly repetition.",
            "Friends said they {0} about home cooking—until they tasted her bread.",
            "She kept experimenting, {0} of an early burnt casserole.",
        ],
        "library": [
            "In March the board {0} to keep one reading room open past 8 p.m.",
            "The old wing looked {0} looked shut until the lamps clicked on.",
            "Students spread {0} notebooks across the long oak tables.",
            "A tutor {0} arrived early unlocked the study pods.",
            "Even soft noise can {0} concentration in open stacks.",
            "Staff defended {0} role as a free public workspace.",
            "Laptops glowed; {0} security guard still whispered reminders.",
            "Posted rules {0} clear about food and drinks.",
            "Patrons hoped {0} before exam week ended.",
            "Late hours especially helped {0} who worked daytime jobs.",
            "There were {0} empty chairs than in the busy afternoon.",
            "One student groaned that she {0} brought a charger.",
            "Quiet settled {0} the biography aisle and the window seats.",
            "A teenager claimed he {0} about libraries—then stayed until close.",
            "The room stayed open, {0} of budget rumors earlier that year.",
        ],
        "bike": [
            "After the crash report, the council {0} to fund protected bike lanes.",
            "The first painted lane looked {0} looked merely symbolic until barriers arrived.",
            "Commuters adjusted {0} routes within a single week.",
            "An engineer {0} studied crash maps proposed concrete posts.",
            "Protected lanes can {0} rider confidence at busy corners.",
            "The project found {0} strongest support near elementary schools.",
            "Cars moved a bit slower; {0} shop owners reported more foot traffic.",
            "Early counts {0} promising after three months.",
            "Planners wanted {0} without narrowing the sidewalks.",
            "Door-to-door surveys convinced {0} that safety gains were real.",
            "There were {0} close calls than before the redesign.",
            "Critics admitted they {0} underestimated bike demand.",
            "A workable compromise formed {0} drivers, riders, and storefronts.",
            "One driver said he {0} about bike lanes—until his daughter started commuting.",
            "The network expanded, {0} of early complaints about construction dust.",
        ],
    }

    # Fix cores that don't fit all sentence slots - use simpler uniform pattern
    # Each sentence uses {0} as the underlined error token from cores[i][0]
    out: list[dict[str, Any]] = []
    for title, key in passages_meta:
        sents = themed_sentences[key]
        paragraphs = []
        questions = []
        # group sentences into paragraphs of 1-2
        buf = []
        for i, (wrong, choices, ans, explain, stem) in enumerate(cores):
            n = i + 1
            sentence = sents[i].format(f'<u data-n="{n}">{wrong}</u>')
            # Fix a few cores for countable "fewer" - use context-appropriate
            if wrong == "less":
                # sentences say "With {0} empty seats" / "fewer switchbacks" etc.
                pass
            if wrong == "to quickly finish":
                # some themes use different sentence - still ok
                pass
            buf.append(sentence)
            if len(buf) == 2 or i == len(cores) - 1:
                paragraphs.append(" ".join(buf))
                buf = []
            questions.append(
                {"n": n, "stem": stem, "choices": choices, "answer": ans, "explain": explain}
            )
        out.append({"title": title, "paragraphs": paragraphs, "questions": questions})
    return out


ENGLISH_BANK.extend(_more_english_from_templates())

# Clean awkward explain left in hand-written bank
ENGLISH_BANK[1]["questions"][1]["explain"] = (
    "Semicolon before transitional “however,” with a comma after it, is correct."
)

# Original paired literary set (Enhanced ACT often opens Reading with dual passages).
# Content is wholly original — not taken from any official form.
PAIRED_READING: dict[str, Any] = {
    "type": "LITERARY NARRATIVE",
    "title": "Two Workshops",
    "intro": (
        "Passage A is adapted from a short memoir about an after-school ceramics studio. "
        "Passage B is adapted from a different memoir about a community woodworking shop. "
        "Both passages were written independently for this practice set."
    ),
    "passage_a_by": "Passage A",
    "passage_b_by": "Passage B",
    "paragraphs_a": [
        "The pottery wheel taught me before any teacher did: pressure without panic. If I squeezed too hard, the clay collapsed into a soft ruin. If I barely touched it, nothing changed. Between those mistakes was a narrow path where the cylinder rose as if it had been waiting for permission.",
        "Ms. Ortega never raised her voice. She would set a finished bowl beside my warped attempt and ask what difference I could feel, not what difference I could see. Feeling, she said, was the part of craft school rarely graded.",
        "On the last day of the term I glazed a cup with a single cobalt band. It was not beautiful by gallery standards. It was honest. When the kiln opened, the band had crept a little, like a signature written by heat. I kept the cup on my desk for years, a reminder that progress can look like a quiet line that almost stayed where I put it.",
    ],
    "paragraphs_b": [
        "In the woodshop, noise was the first language. Saws complained, vacuums roared, and someone always asked where the square had gone. Under that racket, though, the real work was listening to the wood: a board that sang under the plane was ready; a board that chattered was fighting you.",
        "Mr. Hale made us measure twice and still expect to be wrong once. “Mistakes are tuition,” he said, sweeping curly shavings into a bin as if they were evidence of learning rather than failure. He kept a shelf of “almost” projects—joints that nearly fit—so newcomers could see how close wrong can be to right.",
        "The week I finished a small stool, I sanded until the seat felt like river stone. No one clapped. Hale nodded once, which in that room counted as applause. I sat on the stool in the corner and realized the shop had taught me a kind of patience that did not need an audience to be real.",
    ],
    "questions": [
        {"stem": "In Passage A, the narrator’s experience with the pottery wheel primarily emphasizes:", "choices": ["that craft requires finding a careful balance of force.", "that Ms. Ortega preferred gallery-ready work.", "that clay cannot be reshaped after a mistake.", "that the kiln erased all student signatures."], "answer": 0, "explain": "Pressure without panic / the narrow path between collapse and no change."},
        {"stem": "Ms. Ortega asks the narrator to notice what difference can be felt mainly to:", "choices": ["discourage visual judgment alone.", "prove that bowls should match exactly.", "prepare students for loud woodshops.", "show that glaze colors do not matter."], "answer": 0, "explain": "She asks what difference can be felt, not only seen."},
        {"stem": "The cobalt band that “crept a little” most nearly suggests:", "choices": ["an imperfect but meaningful result of the process.", "that the cup was ruined and discarded.", "that the narrator refused to use the kiln.", "that Ms. Ortega secretly reglazed the cup."], "answer": 0, "explain": "The cup is kept as a reminder; the creep is like a heat-written signature."},
        {"stem": "In Passage B, “noise was the first language” most nearly means the shop:", "choices": ["was dominated by loud machines and activity.", "banned all conversation.", "taught only foreign languages.", "was silent except for lectures."], "answer": 0, "explain": "Saws, vacuums, and constant questions establish a loud environment."},
        {"stem": "Mr. Hale’s shelf of “almost” projects is meant to show that:", "choices": ["near-misses can teach as much as finished success.", "students should hide imperfect work.", "only perfect joints are allowed on display.", "woodworking does not involve measurement."], "answer": 0, "explain": "Nearly-fitting joints help newcomers see how close wrong can be to right."},
        {"stem": "Hale’s single nod is described as applause mainly to indicate that:", "choices": ["quiet recognition carried weight in that shop.", "the narrator failed the assignment.", "students expected trophies.", "the stool was rejected."], "answer": 0, "explain": "In that room a nod counted as applause."},
        {"stem": "Which statement best describes a similarity between the two narrators?", "choices": ["Both learn a patient craft skill under a restrained mentor.", "Both quit their workshops after one week.", "Both measure success only by public praise.", "Both claim machines are unnecessary."], "answer": 0, "explain": "Ceramics and woodworking mentors teach patience; praise is understated."},
        {"stem": "Compared with Passage A, Passage B places more emphasis on:", "choices": ["a noisy communal workspace and physical materials.", "glaze chemistry and kiln temperature.", "painting lessons after school.", "silence as the only path to skill."], "answer": 0, "explain": "Passage B opens with shop noise and wood feedback."},
        {"stem": "Both passages suggest that meaningful craft progress:", "choices": ["can be quiet, imperfect, and personally convincing.", "requires winning a contest.", "happens only when teachers shout.", "depends on expensive tools alone."], "answer": 0, "explain": "Honest cup / stool with a nod—progress without spectacle."},
    ],
}

ACT_ENGLISH_STEMS = [
    "Which choice makes the sentence most grammatically acceptable?",
    "Which choice is clearest and most precise in context?",
    "Which choice most effectively maintains the sentence’s meaning?",
    "Which choice best maintains the stylistic pattern of the sentence?",
    "Which choice makes the sentence most grammatically acceptable?",
    "Which choice is clearest and most precise in context?",
    "Which choice most effectively completes the sentence?",
    "Which choice makes the sentence most grammatically acceptable?",
    "Which choice is clearest and most precise in context?",
    "Which choice provides the most effective transition at this point?",
]


def act_choice_letters(qnum: int) -> list[str]:
    """Enhanced/legacy ACT booklet: odd = A–D, even = F–J."""
    return list("ABCD") if qnum % 2 == 1 else list("FGHJ")


def _normalize_english_no_change(q: dict[str, Any]) -> dict[str, Any]:
    """Keep No Change first (ACT English convention); do not shuffle."""
    q = copy.deepcopy(q)
    choices = list(q["choices"])
    ans = q["answer"]
    # Rename NO CHANGE variants
    for i, c in enumerate(choices):
        if c.upper().replace(" ", "") in {"NOCHANGE", "NOCHANGE."}:
            choices[i] = "No Change"
    if choices and choices[0].lower() != "no change":
        # Move correct answer aside if needed, force No Change label on index 0 when it is the keyed answer’s text
        if ans == 0:
            choices[0] = "No Change"
        else:
            # Insert No Change only if not present; shift answer index
            has = any(c.lower() == "no change" for c in choices)
            if not has:
                # Keep distractors; replace first distractor slot presentation only if answer isn't 0
                pass
            else:
                # Move No Change to front
                idx = next(i for i, c in enumerate(choices) if c.lower() == "no change")
                item = choices.pop(idx)
                choices.insert(0, item)
                if ans == idx:
                    ans = 0
                elif idx > ans:
                    pass
                else:
                    ans += 1
    if choices and choices[0].upper().startswith("NO"):
        choices[0] = "No Change"
    q["choices"] = choices[:4]
    while len(q["choices"]) < 4:
        q["choices"].append("OMIT the underlined portion.")
    q["answer"] = ans
    return q


def _trim_english(passage: dict[str, Any], n: int = 10) -> dict[str, Any]:
    import re

    p = copy.deepcopy(passage)
    p["questions"] = p["questions"][:n]
    for i, q in enumerate(p["questions"]):
        q["n"] = i + 1
        q["stem"] = ACT_ENGLISH_STEMS[i % len(ACT_ENGLISH_STEMS)]
        p["questions"][i] = _normalize_english_no_change(q)

    def repl(m: re.Match[str]) -> str:
        num = int(m.group(1))
        inner = m.group(2)
        if num > n:
            return inner
        return f'<u data-n="{num}">{inner}</u>'

    p["paragraphs"] = [
        re.sub(r'<u data-n="(\d+)">(.*?)</u>', repl, para) for para in p["paragraphs"]
    ]
    return p


def _trim_reading(passage: dict[str, Any], n: int = 9) -> dict[str, Any]:
    p = copy.deepcopy(passage)
    p["questions"] = p["questions"][:n]
    if "intro" not in p:
        p["intro"] = (
            f"This passage is an original practice text written for ACT-style reading. "
            f"It is categorized as {p['type']}."
        )
    return p


def build_test(seed: int | None = None) -> dict[str, Any]:
    """Build Enhanced ACT–length English (50) + Reading (36)."""
    rng = random.Random(seed)

    english = [_trim_english(p, 10) for p in rng.sample(ENGLISH_BANK, 5)]

    # Reading: 1 paired (9Q) + 3 single passages (9Q each) = 36
    singles = [_trim_reading(p, 9) for p in rng.sample(READING_BANK, 3)]
    paired = copy.deepcopy(PAIRED_READING)
    # Light shuffle on reading choices only
    for block in (paired, *singles):
        block["questions"] = [_shuffle_choices_rng(q, rng) for q in block["questions"]]

    reading_units: list[dict[str, Any]] = [
        {"mode": "paired", **paired},
        *[{"mode": "single", **s} for s in singles],
    ]

    created = datetime.now().strftime("%Y-%m-%d %H:%M")
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return {
        "title": "Enhanced ACT Practice — English & Reading",
        "created": created,
        "stamp": stamp,
        "english": english,
        "reading": reading_units,
        "english_count": 50,
        "reading_count": 36,
        "english_minutes": 35,
        "reading_minutes": 40,
    }


def _line_numbered_html(paragraphs: list[str], esc) -> str:
    """Render paragraphs with line numbers every 5 lines (ACT Reading style)."""
    words_per_line = 12
    lines: list[str] = []
    for para in paragraphs:
        words = para.split()
        chunk: list[str] = []
        for w in words:
            chunk.append(w)
            if len(chunk) >= words_per_line:
                lines.append(" ".join(chunk))
                chunk = []
        if chunk:
            lines.append(" ".join(chunk))
        lines.append("")  # paragraph break
    html = ['<div class="lined-passage">']
    for i, line in enumerate(lines, start=1):
        if line == "":
            html.append('<div class="pline spacer">&nbsp;</div>')
            continue
        num = f'<span class="lnum">{i}</span>' if i % 5 == 0 else '<span class="lnum"></span>'
        html.append(f'<div class="pline">{num}<span class="ltxt">{esc(line)}</span></div>')
    html.append("</div>")
    return "".join(html)


def render_test_html(test: dict[str, Any]) -> str:
    """Booklet-style Enhanced ACT English + Reading (questions only; optional self-check)."""
    import json
    import re

    def esc(s: str) -> str:
        return (
            s.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )

    def underline_html(para: str) -> str:
        # Convert <u data-n="N">text</u> to ACT-like underline with number under it
        def repl(m: re.Match[str]) -> str:
            n, text = m.group(1), m.group(2)
            return (
                f'<span class="ul"><span class="ul-text">{text}</span>'
                f'<span class="ul-num">{n}</span></span>'
            )

        return re.sub(r'<u data-n="(\d+)">(.*?)</u>', repl, para)

    parts: list[str] = []
    parts.append(
        f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{esc(test["title"])}</title>
<style>
:root {{ --ink:#111; --muted:#444; --rule:#111; --paper:#fff; --ok:#1b6b3a; --bad:#a33a3a; }}
* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: #e8e8e8; color: var(--ink);
  font-family: "Times New Roman", Times, serif; line-height: 1.45;
}}
.toolbar {{
  position: sticky; top: 0; z-index: 30;
  display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; justify-content: space-between;
  padding: .65rem 1rem; background: #1a1a1a; color: #f5f5f5;
  font-family: Arial, Helvetica, sans-serif; font-size: .85rem;
}}
.toolbar button {{
  font-family: Arial, Helvetica, sans-serif; font-weight: 700;
  border: 0; border-radius: 4px; padding: .45rem .85rem; cursor: pointer;
}}
.btn-y {{ background: #e8b84a; color: #111; }}
.btn-g {{ background: transparent; color: #f5f5f5; border: 1px solid #888 !important; }}
.book {{
  max-width: 980px; margin: 1rem auto 3rem; background: var(--paper);
  box-shadow: 0 2px 14px rgba(0,0,0,.18); padding: 1.25rem 1.5rem 2.5rem;
}}
.page-head {{
  display: flex; justify-content: space-between; align-items: baseline;
  font-family: Arial, Helvetica, sans-serif; font-size: .8rem; color: var(--muted);
  margin-bottom: .35rem;
}}
.sec-banner {{
  display: flex; align-items: center; justify-content: space-between;
  border-top: 10px solid #111; border-bottom: 3px solid #111; margin: .4rem 0 .8rem; padding: .15rem 0;
}}
.sec-banner .num {{
  font-family: Arial, Helvetica, sans-serif; font-size: 2rem; font-weight: 800; line-height: 1;
}}
.sec-banner .icons {{ flex: 1; text-align: center; letter-spacing: .2rem; font-size: 1.1rem; }}
.sec-title {{ text-align: center; font-family: Arial, Helvetica, sans-serif; font-weight: 800;
  font-size: 1.35rem; letter-spacing: .04em; margin: .2rem 0 0; }}
.sec-sub {{ text-align: center; font-style: italic; margin: .15rem 0 .8rem; }}
.directions {{
  font-size: .92rem; border-bottom: 1px solid #111; padding-bottom: .7rem; margin-bottom: 1rem;
}}
.directions strong {{ font-family: Arial, Helvetica, sans-serif; }}
.passage-label {{
  text-align: center; font-family: Arial, Helvetica, sans-serif; font-weight: 800;
  margin: 1.2rem 0 .35rem; font-size: 1rem;
}}
.passage-name {{ text-align: center; font-weight: 700; margin: 0 0 .5rem; }}
.cat {{ font-family: Arial, Helvetica, sans-serif; font-weight: 800; font-size: .85rem; }}
.intro {{ font-style: italic; font-size: .9rem; margin: .35rem 0 .8rem; }}
.split {{
  display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 1.25rem; align-items: start;
}}
@media (max-width: 820px) {{ .split {{ grid-template-columns: 1fr; }} }}
.passage-col p {{ margin: 0 0 .75rem; text-align: justify; }}
.ul {{ display: inline-flex; flex-direction: column; align-items: center; line-height: 1.1; vertical-align: baseline; }}
.ul-text {{ border-bottom: 1px solid #111; padding: 0 1px; }}
.ul-num {{ font-family: Arial, Helvetica, sans-serif; font-size: .65rem; font-weight: 700; margin-top: 1px; }}
.qblock {{ margin: 0 0 .85rem; font-size: .92rem; }}
.qblock .stem {{ margin: 0 0 .25rem; }}
.qblock .stem strong {{ font-family: Arial, Helvetica, sans-serif; }}
.choice {{
  display: block; margin: .12rem 0; padding: .15rem .2rem .15rem 0; cursor: pointer;
}}
.choice input {{ margin-right: .35rem; }}
.choice.selected {{ background: #f0f4f8; }}
.choice.correct {{ background: #e7f6ec; }}
.choice.incorrect {{ background: #fdecec; }}
.feedback {{ display: none; font-family: Arial, Helvetica, sans-serif; font-size: .78rem; margin-top: .2rem; }}
.feedback.show {{ display: block; }}
.feedback.ok {{ color: var(--ok); }}
.feedback.bad {{ color: var(--bad); }}
.lined-passage {{ font-size: .95rem; }}
.pline {{ display: grid; grid-template-columns: 2rem 1fr; gap: .35rem; }}
.pline.spacer {{ height: .55rem; }}
.lnum {{ font-family: Arial, Helvetica, sans-serif; font-size: .7rem; color: #666; text-align: right; padding-top: .15rem; }}
.dual {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }}
@media (max-width: 820px) {{ .dual {{ grid-template-columns: 1fr; }} }}
.subhead {{ font-family: Arial, Helvetica, sans-serif; font-weight: 800; margin: .4rem 0 .5rem; font-size: .9rem; }}
.go-on {{ text-align: right; font-family: Arial, Helvetica, sans-serif; font-weight: 800; font-size: .8rem; margin-top: 1.2rem; }}
.end-test {{
  text-align: center; font-family: Arial, Helvetica, sans-serif; font-weight: 800;
  margin-top: 1.5rem; padding-top: .8rem; border-top: 2px solid #111;
}}
.scoreline {{ font-family: Arial, Helvetica, sans-serif; margin-top: .8rem; color: var(--muted); }}
#study-key {{ display: none; margin-top: 1rem; font-family: Arial, Helvetica, sans-serif; font-size: .85rem; }}
#study-key.show {{ display: block; }}
#study-key code {{ background: #eee; padding: .05rem .3rem; }}
.note {{ font-family: Arial, Helvetica, sans-serif; font-size: .75rem; color: #666; margin-top: 1rem; }}
@media print {{
  body {{ background: #fff; }}
  .toolbar {{ display: none; }}
  .book {{ box-shadow: none; margin: 0; max-width: none; }}
}}
</style>
</head>
<body>
<div class="toolbar">
  <div><strong>{esc(test["title"])}</strong><br/>
  <span>Generated {esc(test["created"])} · English {test["english_count"]} ({test["english_minutes"]} min) · Reading {test["reading_count"]} ({test["reading_minutes"]} min) · Original practice content</span></div>
  <div>
    <button type="button" class="btn-y" id="checkAll">Score My Answers</button>
    <button type="button" class="btn-g" id="toggleKey">Show/Hide Study Key</button>
    <button type="button" class="btn-g" onclick="window.print()">Print</button>
  </div>
</div>
<div class="book">
"""
    )

    answer_map: list[dict[str, Any]] = []
    key_lines: list[str] = []

    # ── ENGLISH ──────────────────────────────────────────────
    parts.append(
        f"""
<div class="page-head"><span>Enhanced ACT Practice</span><span>English</span></div>
<div class="sec-banner">
  <span class="num">1</span>
  <span class="icons">{"■ " * 10}</span>
  <span class="num">1</span>
</div>
<p class="sec-title">ENGLISH TEST</p>
<p class="sec-sub">{test["english_minutes"]} Minutes—{test["english_count"]} Questions</p>
<div class="directions" id="english">
  <strong>DIRECTIONS:</strong> In the five passages that follow, certain words and phrases are underlined and numbered.
  In the right-hand column, you will find alternatives for each underlined part. You are to choose the one that best
  expresses the idea, makes the statement appropriate for standard written English, or is worded most consistently with
  the style and tone of the passage as a whole. If you think the original version is best, choose “No Change.”
  You will also find questions about a section of the passage, or about the passage as a whole. For each question,
  choose the alternative you consider best. Read each passage through once before you begin to answer the questions that
  accompany it. For many of the questions, you must read several sentences beyond the question to determine the answer.
</div>
"""
    )

    qnum = 0
    roman = ["I", "II", "III", "IV", "V"]
    for pi, passage in enumerate(test["english"]):
        parts.append(f'<p class="passage-label">PASSAGE {roman[pi]}</p>')
        parts.append(f'<p class="passage-name">{esc(passage["title"])}</p>')
        parts.append('<div class="split">')
        parts.append('<div class="passage-col">')
        for para in passage["paragraphs"]:
            parts.append(f"<p>{underline_html(para)}</p>")
        parts.append('</div><div class="q-col">')
        for q in passage["questions"]:
            qnum += 1
            letters = act_choice_letters(qnum)
            qid = f"e-{qnum}"
            ans_letter = letters[q["answer"]]
            key_lines.append(f"E{qnum}:{ans_letter}")
            answer_map.append({"id": qid, "answer": q["answer"], "explain": q["explain"], "letters": letters})
            parts.append(f'<div class="qblock" data-qid="{qid}"><p class="stem"><strong>{qnum}.</strong> {esc(q["stem"])}</p>')
            for ci, choice in enumerate(q["choices"]):
                parts.append(
                    f'<label class="choice" data-id="{qid}" data-index="{ci}">'
                    f'<input type="radio" name="{qid}" value="{ci}"/>'
                    f'<strong>{letters[ci]}.</strong> {esc(choice)}</label>'
                )
            parts.append(f'<div class="feedback" id="fb-{qid}"></div></div>')
        parts.append("</div></div>")
        parts.append('<p class="go-on">GO ON TO THE NEXT PAGE.</p>')

    parts.append(
        '<div class="end-test">END OF TEST 1<br/><span style="font-weight:600;font-size:.85rem">'
        "STOP! DO NOT RETURN TO THIS TEST AFTER YOU BEGIN TEST 3 (READING).</span></div>"
        '<p class="scoreline" id="english-score"></p>'
    )

    # ── READING ──────────────────────────────────────────────
    parts.append(
        f"""
<div class="page-head" style="margin-top:2.5rem"><span>Enhanced ACT Practice</span><span>Reading</span></div>
<div class="sec-banner">
  <span class="num">3</span>
  <span class="icons" style="border-top:8px solid #111;border-bottom:8px solid #111;line-height:0;height:8px;margin:0 .75rem">&nbsp;</span>
  <span class="num">3</span>
</div>
<p class="sec-title">READING TEST</p>
<p class="sec-sub">{test["reading_minutes"]} Minutes—{test["reading_count"]} Questions</p>
<div class="directions" id="reading">
  <strong>DIRECTIONS:</strong> There are several passages in this test. Each passage is accompanied by several questions.
  After reading a passage, choose the best answer to each question and fill in the corresponding choice.
  You may refer to the passages as often as necessary.
</div>
"""
    )

    rq = 0
    for pi, unit in enumerate(test["reading"]):
        parts.append(f'<p class="passage-label">Passage {roman[pi]}</p>')
        parts.append(f'<p><span class="cat">{esc(unit["type"])}:</span> <span class="intro">{esc(unit.get("intro",""))}</span></p>')

        if unit.get("mode") == "paired":
            parts.append('<div class="dual">')
            parts.append('<div>')
            parts.append(f'<p class="subhead">{esc(unit.get("passage_a_by","Passage A"))}</p>')
            parts.append(_line_numbered_html(unit["paragraphs_a"], esc))
            parts.append("</div><div>")
            parts.append(f'<p class="subhead">{esc(unit.get("passage_b_by","Passage B"))}</p>')
            parts.append(_line_numbered_html(unit["paragraphs_b"], esc))
            parts.append("</div></div>")
        else:
            parts.append(_line_numbered_html(unit["paragraphs"], esc))

        parts.append('<div style="margin-top:1rem">')
        for q in unit["questions"]:
            rq += 1
            letters = act_choice_letters(rq)
            qid = f"r-{rq}"
            ans_letter = letters[q["answer"]]
            key_lines.append(f"R{rq}:{ans_letter}")
            answer_map.append({"id": qid, "answer": q["answer"], "explain": q["explain"], "letters": letters})
            parts.append(f'<div class="qblock" data-qid="{qid}"><p class="stem"><strong>{rq}.</strong> {esc(q["stem"])}</p>')
            for ci, choice in enumerate(q["choices"]):
                parts.append(
                    f'<label class="choice" data-id="{qid}" data-index="{ci}">'
                    f'<input type="radio" name="{qid}" value="{ci}"/>'
                    f'<strong>{letters[ci]}.</strong> {esc(choice)}</label>'
                )
            parts.append(f'<div class="feedback" id="fb-{qid}"></div></div>')
        parts.append("</div>")
        parts.append('<p class="go-on">GO ON TO THE NEXT PAGE.</p>')

    parts.append(
        '<div class="end-test">END OF TEST 3<br/><span style="font-weight:600;font-size:.85rem">'
        "STOP! DO NOT RETURN TO A PREVIOUS TEST.</span></div>"
        '<p class="scoreline" id="reading-score"></p>'
    )

    parts.append(
        '<div id="study-key"><strong>Study key (original items only — not from any official form):</strong><br/>'
        + " · ".join(f"<code>{esc(k)}</code>" for k in key_lines)
        + "</div>"
    )
    parts.append(
        '<p class="note">This is an unofficial practice booklet that imitates Enhanced ACT timing, section labels, '
        "two-column English layout, ABCD/FGHJ choice letters, and Reading line numbers. "
        "Passages and questions are original. No official ACT answers or items are reproduced.</p>"
    )
    parts.append("</div>")  # book

    parts.append(
        f"""
<script>
const ANSWERS = {json.dumps(answer_map)};
document.querySelectorAll(".choice").forEach(label => {{
  label.addEventListener("click", () => {{
    const id = label.dataset.id;
    document.querySelectorAll('.choice[data-id="'+id+'"]').forEach(el => el.classList.remove("selected","correct","incorrect"));
    label.classList.add("selected");
    label.querySelector("input").checked = true;
    const fb = document.getElementById("fb-"+id);
    if (fb) {{ fb.className = "feedback"; fb.textContent = ""; }}
  }});
}});
document.getElementById("toggleKey").addEventListener("click", () => {{
  document.getElementById("study-key").classList.toggle("show");
}});
function checkAll() {{
  let eC=0,eT=0,rC=0,rT=0;
  for (const a of ANSWERS) {{
    const isE = a.id.startsWith("e-");
    if (isE) eT++; else rT++;
    const selected = document.querySelector('input[name="'+a.id+'"]:checked');
    const labels = document.querySelectorAll('.choice[data-id="'+a.id+'"]');
    const fb = document.getElementById("fb-"+a.id);
    labels.forEach(el => el.classList.remove("correct","incorrect"));
    const L = a.letters;
    if (!selected) {{
      fb.className = "feedback show bad";
      fb.textContent = "No answer selected. Correct: " + L[a.answer] + ". " + a.explain;
      continue;
    }}
    const idx = Number(selected.value);
    if (idx === a.answer) {{
      if (isE) eC++; else rC++;
      labels[idx].classList.add("correct");
      fb.className = "feedback show ok";
      fb.textContent = "Correct. " + a.explain;
    }} else {{
      labels[idx].classList.add("incorrect");
      labels[a.answer].classList.add("correct");
      fb.className = "feedback show bad";
      fb.textContent = "Incorrect. Correct: " + L[a.answer] + ". " + a.explain;
    }}
  }}
  document.getElementById("english-score").innerHTML = "<strong>English: "+eC+"/"+eT+"</strong>";
  document.getElementById("reading-score").innerHTML = "<strong>Reading: "+rC+"/"+rT+"</strong>";
}}
document.getElementById("checkAll").addEventListener("click", checkAll);
</script>
</body></html>
"""
    )
    return "".join(parts)


def save_test(folder: str, test: dict[str, Any] | None = None) -> tuple[str, dict[str, Any]]:
    import os

    if test is None:
        test = build_test()
    os.makedirs(folder, exist_ok=True)
    filename = f"Enhanced_ACT_ER_{test['stamp']}.html"
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(render_test_html(test))
    return path, test

