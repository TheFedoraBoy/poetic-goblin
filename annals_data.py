"""
The Annals of Elysal — 4,000 Years of History
Compiled by Kratikar Klae, Letterboy of Hejem University, Catcher's Rim
"""

ANNALS_INTRO = """At the end of the Age of Solitude, a young Hiyalmite sat down on a grassy hill overlooking Catcher's Rim and began to chronicle the history of Elysal. He was a student, a letterboy at Hejem University with a dream of creating some sort of encyclopedia of all that had happened in the four thousand years since the inception of civilization. His work took thousands of interviews all around the world, expeditions to long lost libraries and castles of old, and the better part of his life, but it culminated in one of the seminal works of his time: The Annals.

His name was Kratikar Klae.

Klae was not a historian by training. He was a clerk's apprentice who read too much and asked too many questions, which in Hiyalm is considered a character flaw and in the rest of the world is considered a profession. He began his work at the age of nineteen with a knapsack, a journal, and passage on a trade vessel bound for Fondore. He returned forty-three years later with six hundred tomes of interviews, sketches, transcribed scrolls, and enough stories to fill a library. Then he filled one. The Annals are now housed in the Library of Spires at Klae's famed alma mater, where they exist over hundreds of tomes and scrolls, and continue to grow with contributions from scholars, adventurers, and ordinary citizens who believe their piece of the world deserves remembering.

The Annals cover eight ages, eighty centuries, and thousands of stories of noble heroes, tragic villains, despotic kings and their peasant usurpers, wise monks and treacherous rogues, and everything in between. From the first civilization of the Ghenyarians in Waydren, to the steam and iron of the Age of Solitude, the Annals provide an account of a world that has been at war with itself since the moment it learned how to hold a weapon, and at peace with itself in the rare and precious moments it chose to put one down.

Is your story in here? Perhaps buried under some sheets of parchment and cobwebs, waiting for a young scholar to blow off the dust and be enthralled by your tale. Klae certainly hoped so. He was fond of saying that history was not the study of the dead but of the living, because every person walking the streets of Boulavar or fishing off the docks of Catcher's Rim was the end product of eight thousand years of decisions, mistakes, love affairs, murders, and lucky breaks. The Annals do not judge. They simply remember, so that we don't have to do it alone."""

AGES = [
    {
        "number": 1,
        "name": "Whispered Beginnings",
        "year_start": 1,
        "year_end": 500,
        "description": """The beginnings of civilization were mere whispers in a primal storm of earth and animals. The first evidence of organized life came amongst the tribes of Ghenyar, stone age humans living in the coastal hills of what has become modern day Waydren. A great warrior clad in bearskins united a loose alliance of clans through diplomacy, marriage, and the occasional act of violence that accompanies both. His name was Hipolyptica, and he founded a city in his name: Hipola, now known as Hypolta, the oldest city in existence.

From this single settlement on a rocky peninsula, humanity spread like spilled wine across a tablecloth. Tribes became towns. Towns became kingdoms. Kingdoms made contact with one another and immediately began arguing about borders. The Ghenyarians built the first roads, the first written language, the first courts of law. They also built the first armies, which tells you something about priorities.

But the First Age was not only the story of men. Across the Erezetta Ocean, lizardfolk were crawling out of volcanic jungles and learning to walk upright. In the savannahs of Tzun, lions were becoming something more than lions. On the frozen continent of Acumfrial, a race of small and stubborn people were building a wall against horrors that defied description. And in the Pasav desert, a man named Illiman was born in a town that nobody remembers, and he would go on to change the moral framework of the world.

The First Age is the age of firsts. First cities, first wars, first religions, first betrayals. Everything that came after was, in one way or another, a consequence of decisions made by people who had no idea what they were starting.""",
        "centuries": [
            {"number": 1, "name": "First Century",
             "description": "The Age of First Men. The Ghenyarian tribes unite under Hipolyptica and found the city of Hipola, later Hypolta, on the coast of Waydren. The earliest recorded wars are fought between rival island clans. The Gecka barbarians descend from the north and are driven back after years of brutal conflict, banished to the Cindour islands. Across the world, the Icraza begin their slow evolution in the jungles of Metzerul.",
             "stories": [
                {"title": "The Founding of Hipola",
                 "content": """There is no surviving portrait of Hipolyptica. No bust, no statue, no cave painting that historians can point to and say with any certainty, that is the man who started it all. What survives are fragments. A clay tablet recovered from the foundations of the old city describes him as seven feet tall and clad in bearskins. A oral tradition passed down through Waydrani fishing villages says he had a voice that could be heard across a valley. A Gechann military treatise from the Fourth Age, of all things, credits him with the invention of the shield wall, though this is almost certainly propaganda meant to claim Ghenyarian tactics as Geckish heritage.

What we know for certain is this: sometime in the first decades of recorded history, a man of considerable physical and political ability gathered a loose confederation of coastal tribes on the Waydrani peninsula and convinced them, through some combination of diplomacy and the threat of being hit with a very large stick, to stop killing each other and start building something. The something was Hipola.

Hipola was not much to look at in those early years. A collection of stone huts on a rocky promontory overlooking the strait, surrounded by a ditch that optimistic historians call a wall. But it had three things that no other settlement in the world could claim: a system of barter based on standardized shell currency, a standing garrison of warriors who trained instead of farmed, and a council of elders who met every new moon to settle disputes that would have otherwise been settled with clubs.

Hipolyptica ruled for what the oral traditions describe as a long time, which could mean anything from thirty to sixty years. He united the Caemu and Tynm, rival tribes from the outer islands, after defeating their combined force of three hundred warriors in what later historians would call the Battle of the Dawn Shore. The Ghenyarian defenders numbered only a hundred and twenty, but they fought from prepared positions behind the rock formations and killed a hundred and thirty-four of the attackers while losing twenty-three of their own. The victory was decisive enough that Hipolyptica could afford to be magnanimous. He absorbed both tribes into Ghenyar rather than enslaving them, a decision that his descendants would alternate between celebrating and regretting for the next several thousand years.

By the time of his death, Hipola had currency, a merchant class, a standing army, and a handful of early scholars who were developing a written language based on symbols and star signs. Hipolyptica was buried on the promontory overlooking the city, though the exact location of his grave has been lost. Klae notes, with characteristic understatement, that this is appropriate. The man built the foundation. He did not need to be remembered for it to hold."""},

                {"title": "The Geckan Invasion",
                 "content": """In the eighth year of the Klae calendar, while the Ghenyarians were busy inventing civilization, civilization came looking for them. It arrived in the form of the Gecka: wild, pale-skinned men with unruly shocks of red hair who poured down from the northern plains like a river that had forgotten where its banks were.

The Gecka were not stupid. That is a common misconception born from Ghenyarian prejudice and several thousand years of the Waydrani calling them barbarians at dinner parties. The Gecka were, in fact, resourceful and organized enough to mount a sustained military campaign across unfamiliar territory against a fortified enemy. What they lacked was writing, permanent architecture, and the basic courtesy of sending a diplomatic envoy before showing up with axes.

The Geckan-Ghenyar War lasted three years and claimed seven thousand lives, which by the standards of the age was apocalyptic. The Ghenyarians fought defensively, using their knowledge of the terrain and their fortified positions to bleed the invaders at every river crossing and mountain pass. The Gecka fought with the particular ferocity of a people who have nothing to go back to, which as it turns out, they didn't. Drought and tribal conflict had driven them south. They weren't invading so much as relocating, with extreme prejudice.

The war ended at the decisive Battle of Suntrae, where the Ghenyarian general Lycrh (great-grandson of Hipolyptica by most reckonings) caught the Geckan host in a river ford and destroyed it. The Geckan commander Kledarus was executed in front of the remnants of his army, and the surviving Gecka were banished to the Cindour Islands, a miserable chain of rocks off the northern coast that nobody wanted.

This was, by every reasonable measure, a mistake. Not the banishment itself, which was sensible enough, but the assumption that a defeated enemy will stay defeated if you put them on an island and forget about them. The Gecka did not forget. They sat on their rocks for over a century, nursing their wounds and their grudges in roughly equal measure. And when they finally came back, they came back as the Gechann, and they came back to stay.

A Waydrani proverb that Klae was fond of quoting: 'The stone you throw into the sea will wash back to your shore.' The Ghenyarians threw the Gecka into the sea. The sea, as it does, brought them back."""}
            ]},

            {"number": 2, "name": "Second Century",
             "description": "The Prophet's Road. In a small Pasav desert town, a man named Illiman is born and begins preaching a doctrine of asceticism and forgiveness that reshapes the moral landscape of Fondore. Meanwhile, the Ghenyarians expand past the Cindour islands and make disastrous contact with the Debrears in the Thaugren forest, suffering one of the worst military defeats in early history.",
             "stories": [
                {"title": "Illiman of the Pasav",
                 "content": """In the forty-sixth year of the Klae calendar, a child was born in a town in the Pasav desert so small that it does not appear on any surviving map. The town was under Cynthian control at the time, as was most of the desert, and the child's parents were unremarkable people whose names are not recorded anywhere. This is fitting. Illiman never spoke of his parents, his childhood, or where he came from. He spoke only of where everyone was going, and what they ought to do about it.

The doctrine he preached was not complicated. Be kind. Forgive those who wrong you, not because they deserve it but because carrying hatred is heavier than carrying stone. Look inward before you look outward. Treat the stranger and the neighbor with the same basic decency. Do not steal, do not murder, do not lie unless the lie prevents a greater cruelty, and even then think twice.

This was, by the standards of the age, revolutionary. The prevailing religious customs in Fondore involved ancestor worship, animal sacrifice, and in certain Cynthian districts, paying a temple priest to curse your enemies. Illiman walked into this landscape and said, more or less, 'Stop it. All of you. You're embarrassing yourselves.'

He traveled for decades. He visited the bustling markets of Hipola, where merchants tried to sell him silk and he tried to sell them restraint. He crossed the Leimbordur, where Northern tribesmen who had never seen a desert man before listened to him speak and found, to their confusion, that they agreed with most of it. He walked the Cynthian coast and debated philosophers who had more degrees than him and less wisdom.

Many wanted him dead. The Cynthian religious establishment in particular found his teachings offensive, as they tended to cut into the temple revenue. Ruler Luole of Cynthia was petitioned repeatedly to execute Illiman for heresy. Luole declined, reportedly saying that killing a man for telling people to be nice seemed like it would prove his point.

Illiman died on a road. Not dramatically, not as a martyr, not at the hands of his enemies. A highwayman killed him for whatever was in his traveling sack, which by all accounts was nothing of value. His followers found his body the next morning. They buried him where he fell and continued walking.

The religion that bears his name, Ceresy, would go on to dominate Fondore for millennia. Temples would be built. Wars would be fought. Kings would invoke his name to justify acts he would have wept over. But the core of what he taught has survived every corruption and misuse, which is perhaps the strongest argument for its truth. Be kind. Forgive. Look inward. It is simple. It has never been easy."""},

                {"title": "The Massacre at Thaugren",
                 "content": """Payt Vyr was an explorer, which in the First Age was a polite word for a man willing to walk into unknown territory with a sword and a sense of entitlement. He was Ghenyarian, from the city-state of Hipola, and in the eighty-ninth year of the Klae calendar he led an expedition of fifty men past the Cindour islands and into the dense forests of what is now central Fondore. His mission, as recorded in the expedition charter, was 'to catalogue new lands for the glory of Ghenyar and the enrichment of her people.' In practice, this meant finding someone to trade with or, failing that, someone to take things from.

What Payt Vyr found were the Debrears.

The Debrears were not a people who enjoyed being found. They had lived in the Thaugren forest for as long as anyone could remember, and they had developed a military culture specifically designed to ensure that nobody bothered them. They were woodsmen, guerrilla fighters, and they did not appreciate fifty armed foreigners walking through their territory cataloguing things.

Three of Payt's explorers were killed before anyone realized they were under attack. The Debrears struck from the tree line, vanished, struck again from a different direction, vanished again. Payt ordered a retreat to a defensible clearing, but the Thaugren didn't have clearings. Every gap in the canopy was a kill zone. Every fallen log was an ambush site.

General Groyar of Ghenyar, upon hearing of the killings, dispatched four hundred soldiers to drive away the Debrear tribe. Groyar expected a punitive expedition. What he got was a catastrophe. The Debrear commander, a man remembered only as Ufhu the Slayer, used the forest itself as a weapon. Ghenyarian soldiers trained for open-field formation combat found themselves fighting shadows between trees they couldn't see past. Supply lines were cut. Scouts disappeared. Men who wandered ten feet from their unit to relieve themselves were found dead hours later, arranged in positions that were clearly meant to be insulting.

Of the four hundred soldiers sent into the Thaugren, twenty-six came out.

One of them was an infantryman named Jaylae Liys, who wrote a scroll about his experience that became the first widely distributed book in Elysal, translated into Cynthian and Mezan. It is a harrowing document. Jaylae describes the sound of Debrear war drums at night, the way the forest seemed to close in around the column as they marched deeper, the moment when his commanding officer sat down in the middle of a path and refused to move and had to be carried.

Ghenyar mourned and made the only sensible decision available: they left the Debrears alone. The Thaugren remained uncharted on Ghenyarian maps for another century, marked only with the notation that Klae found on a surviving copy: 'Do not go here.'"""}
            ]},

            {"number": 3, "name": "Third Century",
             "description": "Beasts and Builders. Across the Erezetta, the lizardfolk called Icraza emerge from the volcanic jungles of Metzerul and found the city of Imbraxione under the warlord Corytzenss. In Tzun, something extraordinary happens to the lions of the savannah — they begin to walk upright. The Pridekin enter history with sharpened claws and no concept of mercy.",
             "stories": [
                {"title": "The Dragon of Boudazi",
                 "content": """The Icraza were not always the Icraza. Before they were a civilization, before they had cities or language or kings, they were simply lizards that had started doing things lizards were not supposed to do. They grew longer spines. Their limbs stretched and thinned. They stood upright. And then, around the twelfth year of the Klae calendar, they started talking to each other, which in retrospect was the most dangerous development of all.

By the hundred and eleventh year, a lizardfolk called Corytzenss settled his large family on a coastal plain near the volcano Boudazi and founded a village he called Ictuczul, meaning Corner of the Mountain. It was twelve huts and a well. Within a decade, word had spread and lizardfolk arrived from across Metzerul, drawn by the novel concept of not sleeping in a cave alone. Corytzenss renamed his village Imbraxione, meaning My Warrior Home, declared himself king, and began conquering the surrounding tribes with the enthusiasm of a man who had just invented the concept of owning things.

By the hundred and thirty-fourth year, Lirza was the largest kingdom in the world by landmass. And then Boudazi erupted.

What happened next is mythology, but it is mythology that the Lirzans themselves believe, and Klae recorded it as he found it. From the lava and fire that rained down on Imbraxione, a winged creature burst forth. Not an Icraza but something older, something the lizardfolk called Darteco. Dragon. The creature was enormous, intelligent, and apparently interested in negotiating. It offered Corytzenss a deal: the dragon would save the city from the lava in exchange for Corytzenss's daughter.

Corytzenss agreed. This is the part of the story that Klae found most revealing. Not the dragon, not the eruption, but the fact that the first recorded diplomatic agreement in Lirzan history was a father trading his daughter for real estate. Corytzenss's daughter married the dragon and bore a child that was neither fully lizard nor fully dragon but something between. The first dragonborn.

The dragonborn heir, Zugaraz, could breathe fire and endure temperatures that would kill any normal Icraza. He finished his grandfather's conquest of the Metzerul jungles and then turned north to invade the Wintermen. The Lirzans had found their ruling class, and it was half a myth. The dragon itself flew off to wherever dragons go, which no one has ever satisfactorily explained. But its blood ran through the veins of every Lirzan monarch that followed, and anyone who questioned this lineage tended to find out very quickly whether or not the fire-breathing was also hereditary."""},

                {"title": "When the Lions Stood",
                 "content": """No one can explain the Pridekin. This is not for lack of trying. Scholars from every discipline and every nation have spent centuries debating what happened in the savannahs of Tzun around the hundred and fourth year of the Klae calendar, and the best answer anyone has produced is: something.

The lions of the Tzun savannah began to change. Their hind legs lengthened. Their forepaws developed something resembling thumbs. They started walking upright, and then they started making sounds that were not roars or growls but words, organized into a language of grunts and pitched vocalizations that linguists have spent entire careers trying to transcribe.

The Pridekin themselves, when asked about their origin, tend to shrug. The concept of racial mythology does not interest them. They are here. They were not here before. The in-between is considered unimportant.

What is important is what they did once they arrived. The Pridekin developed a complex social structure organized around prides, invented an array of weapons including the Gaarklaw — a double-bladed bone knife strapped to the wrist like an extension of their natural claws — and became the most efficient hunters on the continent. They hunted wild horses. They hunted the zebra-like creatures called Junta. And then, inevitably, they hunted the Tzunadaine.

The Tzunadaine were the human inhabitants of Middle Tzun, and they had established their first tribe around the eighty-third year. They were, by all accounts, terrified of the Pridekin, and with good reason. The Pridekin brain, as later Cynthian scientists would discover, lacked the capacity for empathetic thought. They were not cruel in the way that humans are cruel, which requires imagination. They were simply indifferent. Hunting a Tzunadaine for food was no different to them than hunting a horse. It was meat.

This arrangement persisted until the Tzunadaine king Tuuip declared war on the Pridelands in the two hundred and thirty-fourth year. The war was short and decisive in the humans' favor, because the Pridekin, for all their individual prowess, were hunters, not soldiers. They did not understand formations or sieges or the concept of strategic retreat.

A peace was signed. Head Pridestalker Aauuran Rageblade agreed to stop hunting humans for sport. The Pridekin turned to spear fishing and farming instead, and a Pridekin named Rija Whitefoot invented the crossbow, using a vine, a wooden cross, and small stone gears. The design would go on to revolutionize warfare across all of Elysal.

Klae noted the irony: a species that could not feel empathy invented a weapon that would kill more people at a greater distance with less personal involvement than any tool before it. Perhaps empathy was never the point. Perhaps efficiency was."""}
            ]},

            {"number": 4, "name": "Fourth Century",
             "description": "The Fracturing. After centuries of prosperity, the great Ghenyarian state collapses under its own weight and splinters into eleven city-states, each convinced it is the rightful heir to Hipolyptica's legacy. Across the Erezetta, the Kingdom of Vera consolidates power under King Sokotros and subjugates the Karaf people of the Rokori Mountains, beginning one of the longest and most brutal slave systems in Elysal's history.",
             "stories": [
                {"title": "Eleven Sons of Hipola",
                 "content": """The fall of Ghenyar was not dramatic. There was no great battle, no foreign invasion, no single catastrophic event that historians can point to and say: there. That is where it ended. Instead, it was a slow, grinding dissolution driven by the most mundane of forces: tax disputes, succession crises, provincial governors who decided they'd rather be kings, and the fundamental difficulty of governing a territory that had grown too large for its administrative systems.

By the hundred and forty-third year of the Klae calendar, the nation that Hipolyptica had forged was eleven separate city-states, each controlling its own territory, each maintaining its own militia, and each claiming to be the true continuation of the Ghenyarian legacy. Hypolta, the oldest. Suntrae, the wealthiest. Jayvlun, the most democratic. Gisup Geronus, the most cultured. And so on. Eleven cities, eleven governments, eleven opinions on who owed taxes to whom.

The remarkable thing is that the fracturing was largely peaceful. There were skirmishes, certainly, and border disputes that occasionally escalated into small wars lasting a season or two. But the Ghenyarian city-states shared too much — language, religion, trade networks, intermarried noble families — to truly want to destroy each other. They settled into a pattern of bickering that would define Geckish politics for centuries: aggressive enough to be interesting, restrained enough to keep the markets open.

The Gecka, still sitting on their island exile in the Cindour chain, watched all of this with great interest. In the hundred and thirty-seventh year, a diplomat from the city-state of Saul traveled to Cindour and negotiated the Gecka's return to the mainland. This was considered a generous act of reconciliation at the time. It was, in hindsight, the most consequential mistake in Fondorian history. The Gecka came back literate, organized, and very, very patient.

The desert people of the Pasav also took advantage of the fracturing. They united under one banner and formed the nation of Mural Cere, declaring the city of Vaserine — birthplace of the prophet Illiman — as their holy capital. The High Cere Yahtek proclaimed himself Emperor of all Fondore, a title that no one outside the Pasav took seriously but that would cause an extraordinary amount of trouble in the centuries to come.

Klae described the Fracturing as 'the moment humanity learned that building a nation is easy compared to keeping one.' Every state that rose in the ages that followed would eventually confront the same truth. They would all handle it differently. None of them would handle it well."""},

                {"title": "The Karaf in Chains",
                 "content": """The Kingdom of Vera was founded in the thirty-fourth year of the Klae calendar by a tribal leader named Sokotros who looked at an island and decided it was his. He was not the first man to have this thought, but he was the first to act on it with sufficient violence to make it stick.

Vera was a large island off the western coast of Fondore, lush and fertile and home to two peoples: the Verans, who were human, and the Karaf, who were not quite. The Karaf inhabited the Rokori Mountains at the island's southern tip. They were a subrace of humans called Quenbo — grey-skinned, sharp-featured, pointy-eared, and by most accounts strikingly beautiful. They were also fierce fighters with famously short tempers, and they had a cultural practice of consuming the bodies of fallen enemies that made negotiations difficult.

Sokotros decided the Karaf needed subjugating, and in the forty-second year he got his war. The fighting in the Rokori Mountains was brutal. Karaf warriors used the mountain terrain to devastating effect, and the stories of enemy corpses being eaten spread through the Veran ranks with predictable consequences for morale. But numbers and organization won in the end, as they usually do.

The Karaf were made slaves.

It is important to pause here and note what that means, because the word slave gets used so often in historical texts that it begins to lose its weight. The Karaf were stripped of their names, their language, their family structures, and their right to exist as anything other than property. They were sent to work on tropical farms and fisheries across the island. They were bred like livestock. Their children were born into chains and died in chains and their children's children knew no other life.

The Verans did not consider this cruel. They considered it natural. The Karaf looked different, acted different, ate different. They were clearly lesser, and lesser beings existed to serve greater ones. This logic, which requires no evidence and tolerates no contradiction, would sustain the Veran slave system for centuries.

Klae, who was not a man given to editorial comment, allowed himself one line in his account of the Karaf subjugation. He wrote: 'The chains were bronze, because iron had not yet been discovered. The cruelty, however, required no technological advancement.'"""}
            ]},

            {"number": 5, "name": "Fifth Century",
             "description": "Walls Against the Dark. On the remote continent of Acumfrial, the Hiyalmites build the Styrmwall to protect themselves from the eldritch horrors of the Styrm. Across the world, the Verans attempt transoceanic exploration, and their greatest ship becomes the vehicle for the most daring slave escape in history.",
             "stories": [
                {"title": "The Styrmwall",
                 "content": """The Hiyalmites are a difficult people to write about. Not because they are secretive, though they are. Not because they are small, though they are that too. The difficulty is that Hiyalmite history does not follow the same narrative patterns as the rest of Elysal. There are no great conquests, no sweeping empires, no legendary warriors whose names echo through the ages. There is instead a small, stubborn people who spent centuries trying very hard not to die.

The Styrm is the reason. Klae visited Acumfrial in the fourteenth year of his research and described the Styrm as 'a wound in the sky that never heals.' It is a perpetual magical storm that hangs over portions of the Asafin sea and the eastern reaches of Acumfrial, and from it come creatures that defy easy description. Styrm beasts, the Hiyalmites call them, and they range from the merely dangerous to the incomprehensibly horrific. Klae declined to describe the specimens he was shown preserved in Hiyalmite museums. He noted only that he did not sleep well for several weeks afterward.

The Hiyalmites settled in the Mountains of Qaiute around the two hundred and thirty-first year, and by the two hundred and forty-fifth they had declared the nation of Hiyalm and begun construction on the Styrmwall: a massive stone barrier encircling the mountain settlements, designed to keep the Styrm beasts out. The wall took years to complete. When it was finished, the High Hrogern Temp Doon shut the gate for good, and an entire generation of Hiyalmites grew up without ever seeing the world outside.

The Hrogern was chosen by an unusual method. A tamed Styrm beast called Grue, described as a massive bird-like creature with talons and a sharp beak, was presented with the most viable candidates for leadership every ten cycles. Grue killed all of them except one, and that one became the Hrogern. Temp Doon, notably, was considered a coward by his people. Many were confused by Grue's choice. No one questioned it.

The Styrmwall held. The Hiyalmites farmed their mountains, developed their own culture in isolation, and tried very hard to forget that there was an outside. This worked until the Styrmwalkers arrived — Hiyalmites who had been locked outside when the gate closed, whose descendants now came to reclaim their heritage. That story ends in blood, as most stories about locked doors eventually do.

But the wall itself stands to this day. It is not beautiful. It was not built to be beautiful. It was built by a small people who looked at the darkness outside their windows and decided, with a stubbornness that borders on the irrational, that the darkness would not get in."""},

                {"title": "The Kola Tai",
                 "content": """The Verans were ambitious people. They had conquered their island, enslaved the Karaf, and built a kingdom that was, by the standards of the age, genuinely impressive. But islands have a way of making ambitious people look outward, and King Meos, who ruled in the early three hundreds, looked outward with the intensity of a man who has run out of things to conquer at home.

In the three hundred and thirteenth year, Meos sent four ships in four directions with orders to find whatever was out there. None returned. This would have discouraged a reasonable man, but Meos was a king, and kings are not selected for their reasonableness. He ordered the construction of a super ship, the largest vessel ever built, capable of carrying hundreds of men across the open ocean. It was called the Kola Tai, and its construction was powered by Karaf slave labor.

What happened next is one of the great stories of the First Age, and Klae collected multiple versions of it from Karaf oral tradition, Veran records, and third-party accounts from Wompartian traders who heard it secondhand.

A young Karaf slave named Karco devised a plan. While the Karaf slaves built the Kola Tai, they built something else into it: a secret compartment, hidden behind a false bulkhead in the lower decks. The plan was passed from slave to slave in whispers, across plantations and fisheries, through a network of communication that the Verans never knew existed. Slowly, carefully, over the course of months, fifty Karaf boys and fifty Karaf girls were smuggled across the island to the shipyards at Loka and hidden in the compartment.

When the Kola Tai launched, the Karaf crew members waited until the ship was at sea. Then they mutinied. The fighting was short. Karaf who had spent their entire lives in chains fought with a fury that the Veran sailors were wholly unprepared for. Control of the ship changed hands.

The Karaf did not keep the ship. They sailed to Karto, an island south of the Veran coast that the Verans had never bothered to claim, and deposited the hundred children there with instructions that were simple and absolute: survive, multiply, and never let anyone put chains on you again.

Then they sailed the Kola Tai back out to open water and scuttled it, with both the remaining Karaf crew and the captured Veran sailors aboard. The ship and everyone on it went to the bottom.

Klae recorded this without commentary. The facts, he seemed to believe, spoke loudly enough on their own. A hundred children on an empty island, watching the horizon where their parents had just drowned themselves rather than risk anyone following them. The Karaf nation, such as it was, had been born. Its founding act was an act of sacrifice so complete that the people who made it did not survive to see what they had built.

Meos, upon learning of the ship's loss, abandoned his overseas ambitions. He never learned the truth. No Veran would for centuries."""}
            ]},

            {"number": 6, "name": "Sixth Century",
             "description": "Songs and Swords. Cynthia experiences its first cultural flowering, with the invention of the first musical instrument and major advances in art and philosophy. Meanwhile, tensions between the Pridekin and the Tzunadaine of Middle Tzun reach a breaking point over the arrival of the Gezedaine — giants from the eastern lowlands — forcing ancient enemies into an uneasy alliance.",
             "stories": [
                {"title": "The Kouth and the Concert at Oradova",
                 "content": """In the hundred and twenty-sixth year of the Klae calendar, a Cynthian woman named Tasa Devuo stretched a series of dried animal sinews across a carved piece of driftwood and plucked them. The sound that came out was, by all accounts, terrible. It was thin and tinny and the sinews snapped after approximately four notes. But it was the first time in the history of Elysal that a person had deliberately created a musical sound using a purpose-built instrument, and that is the kind of thing that changes a world.

Tasa spent the next several years refining her design. She replaced the sinews with twisted gut strings. She hollowed out the wooden body to create resonance. She added a curved neck to allow different notes to be produced by pressing the strings at different points. The result was the Kouth, a large lyre-like instrument that could produce a range of tones that, when played in sequence, sounded like something between a harp and a woman weeping. It was beautiful.

Cynthia, which had always valued art and beauty more than the martial cultures of Fondore, embraced the Kouth with an enthusiasm that bordered on religious fervor. Within a decade, every Cynthian household that could afford one had a Kouth hanging on the wall, and those that couldn't had children carving imitations out of whatever wood was available.

The concert at Oradova, held sometime around the hundred and thirtieth year, is considered the first public musical performance in history. Tasa herself played for an audience of several hundred Cynthians in the amphitheater overlooking the sea. The program, insofar as it could be called one, consisted of Tasa playing improvisations on themes she had composed, accompanied by a small chorus of singers who harmonized with the instrument.

There is a fragment of a letter from an attendee that Klae recovered from a private collection in Tobries. It reads: 'I do not know what she did to us. I know only that when it was over, the man next to me was crying, and I was too, and neither of us was ashamed.'

Music would go on to become a defining characteristic of Cynthian culture and, through Cynthian influence, of all Fondorian civilization. Armies would march to drums. Lovers would court with songs. Monks would chant the verses of Illiman to melodies that could make atheists reconsider. And all of it traced back to a woman with a piece of driftwood and the audacity to think that the world could sound better than it did."""},

                {"title": "The Giants Come",
                 "content": """The Gezedaine arrived in Tzun the way most catastrophes arrive: without warning and from an unexpected direction.

They came from the Palkur Islands off the eastern coast, and nobody has ever satisfactorily explained how they got across the shark-infested waters of the Avadacaster strait. The prevailing theory involves large slabs of a lightweight sandstone called Itun, essentially floating across on rafts of rock, which is either ingenious or insane depending on your perspective. The Gezedaine grew to twelve feet tall, with the largest reaching fifteen. Their technology consisted of loincloths and clubs made from tree branches or, in some cases, entire trees. Their language was a series of grunts and hand gestures. They were, by most measures, not intelligent.

But one Gezedaine could kill ten men, and they traveled in groups.

When they rampaged into Tzunadaine territory, King Oonjibr found himself facing an enemy that his soldiers simply could not put down. Bronze swords bounced off Gezedaine skin. Spears that would fell a horse merely annoyed them. In desperation, Oonjibr went to the one neighbor he had hoped never to need: Head Pridestalker Uraahnan of the Pridekin.

Uraahnan gave the Tzunadaine dozens of crossbows, the weapon his people had invented. He refused to send any Pridekin to help. The Pridekin did not fight other people's wars. This was a principle. It was also, as Klae noted, convenient.

The crossbows worked. Bolts fired from Rija Whitefoot's design could punch through Gezedaine hide at ranges that kept the shooter alive. The giants were driven back, seven hundred Tzunadaine dead and forty-three giants slaughtered.

But the giants returned a generation later, this time carrying weapons traded from the Ghenyarian city-states: modified maces called Styplia and five sets of smithed armor. The crossbows that had worked before bounced off bronze plate. King Huuopek II lost forty-three soldiers without killing a single giant and was forced to go crawling back to the Pridekin.

This time, Head Pridestalker Hugrhaar Waterwake refused to help — until the Gezedaine crossed the border into the Pridelands. Then he sent four hundred of his best hunters, led by a warrior named Ghaarm Shadowleap. The Pridekin tracked five armored giants to their camp and attacked at night, but three more appeared and killed five hunters before the rest could scatter.

Ghaarm did not scatter. He fought alone, leaping from shadow to shadow, slashing with his Gaarklaw, retreating, striking again. He wore the three giants down over the course of hours, bleeding them one cut at a time, until he could close in for the kill. Three giants. One Pridekin. The histories of Tzun do not agree on much, but they agree on Ghaarm Shadowleap. He was the first warrior from any race whose name was known across an entire continent, and he earned it alone in the dark against enemies three times his size."""}
            ]},

            {"number": 7, "name": "Seventh Century",
             "description": "Five Crowns, One Throne. In the frozen North of Fondore, five tribes descended from the mythical Sons of Rabax have been warring for centuries. Through betrayal, alliance, and a final cataclysmic battle, a warrior named Kunit unites the North under a single banner and founds the Kingdom of Raxone, creating a military power that will shape continental politics for millennia.",
             "stories": [
                {"title": "The Sons of Rabax",
                 "content": """The Northern tribes had been killing each other for as long as anyone could remember, which in the North was not particularly long because they had not yet developed a written language and oral traditions tended to be drowned out by the sound of axes hitting shields.

There were five tribes, each ruled by a dynasty that claimed descent from Rabax, a Northern god whose defining characteristics were strength, stubbornness, and a prodigious number of sons. The Houses of Uratt, Cantra, Susset, Trakaw, and Paurex controlled territories stretching across hundreds of miles of taiga and frozen coastline. They had complex road systems, wagons, and a level of technological sophistication that the Southern peoples would have found surprising, had they ever bothered to check.

The trouble started, as it usually does, with an ambitious man and a map. Tiix of the House of Uratt looked at his territory, looked at his neighbors' territories, and did some arithmetic that ended with him owning all of it. He convened a secret meeting with the Houses of Cantra, Susset, and Trakaw. The proposal: divide Paurex among them. Paurex was the weakest of the five, and nobody liked them much. The others agreed.

Paurex was invaded, conquered, and divided in the sixty-seventh year of the Klae calendar. The operation was clean and efficient, which should have alarmed the other houses, because it demonstrated that Tiix was capable of planning and executing a military campaign without the usual Northern approach of getting drunk and charging.

The alarm came too late. Trakaw was the next to fall, absorbed by Uratt in a campaign so swift that Cantra and Susset barely had time to sign an alliance treaty before Tiix's armies were at their borders. What followed was a war that lasted nearly three centuries, a slow, grinding conflict of ambushes, sieges, betrayals, and truces that lasted exactly as long as both sides needed to reload.

The North bled. And bled. And bled. Generation after generation of young men marched south or east or west to fight cousins they had never met over territory their grandfathers had stolen from someone else. The economy collapsed. The roads fell into disrepair. The only industry that flourished was the manufacture of weapons.

Klae found this period particularly difficult to research, because the Northern tribes did not start writing things down until the very end of it, and the oral accounts he collected were so contradictory that reconstructing a coherent narrative was, in his words, 'like trying to assemble a vase from the shards of six different vases, all of which were thrown at someone's head.'"""},

                {"title": "The Battle of Bosta",
                 "content": """Three hundred and forty-four years after the Klae calendar began, a man named Kunit stood on a hill overlooking the burning city of Bosta, the capital of the House of Cantra, and watched the last organized resistance to Uratt dominance die in the streets below him.

Kunit was a direct descendant of Tiix, the man who had started the Northern wars nearly three centuries earlier. He had the same ambition, the same tactical mind, and one crucial advantage that Tiix had lacked: he was the last one standing. The Houses of Trakaw and Paurex were long gone. Susset had been absorbed two generations prior. Cantra was falling as he watched. There was no one left to fight.

The Battle of Bosta was not a great battle in the military sense. Cantra's forces were exhausted, outnumbered, and fighting for a cause that most of them had stopped believing in years ago. Kunit's army overwhelmed the city's defenses in less than a day. The real significance was what happened afterward.

Kunit killed his cousin Ewaix of Cantra personally, on the walls of the city, in full view of both armies. This was not cruelty. It was calculation. The Northern tribes respected strength, and Kunit needed them to see that the old order was dead and that he was the one who had killed it.

Then he did something unexpected. He abolished the houses. All of them. Including his own. The Houses of Uratt, Cantra, Susset, Trakaw, and Paurex had defined Northern identity for centuries, and Kunit erased them in a single decree. There would be no more tribal loyalty. There would be only Raxone, named for Rabax, the god they all shared.

Kunit crowned himself king and moved the capital to a new city he called Raxona, built on neutral ground that had belonged to none of the old houses. The message was clear: the past was over. Whatever came next would be built on new foundations.

The Raxonians, as they now called themselves, were stunned. Then they were furious. Then, gradually, they were relieved. Three centuries of war had exhausted them so thoroughly that the prospect of a unified kingdom under a single strong ruler was not tyranny but mercy. The swords came down. The plows went in. Kunit's kingdom held.

Within twelve years, Cynthian explorers would arrive on the Raxonian coast, and the Twin Skies Treaty would be signed, and Raxone would enter a golden age of unprecedented prosperity. But that is a story for the next century. The story of this century is simpler and older: a people who had been at war with themselves for three hundred years finally, painfully, stopped."""}
            ]},

            {"number": 8, "name": "Eighth Century",
             "description": "The Veran Tide. Under the ruthless Sokotros IV, the Kingdom of Vera launches a campaign of conquest that spans half the known world, creating the first true empire. Meanwhile, the prophet Illiman's teachings reach every corner of Elysal, fundamentally reshaping morality and culture. In the North, the newly unified Raxone enters its Golden Age.",
             "stories": [
                {"title": "Sakatari's March",
                 "content": """Sokotros IV of Vera was not the kind of king who sat on a throne and issued orders. He was the kind of king who sat on a horse, pointed at the horizon, and said: that too.

By the three hundred and fiftieth year, Vera was at its peak. The island kingdom had a professional navy, a seasoned army, and an economy built on the labor of Karaf slaves who had no say in the matter. Sokotros IV inherited all of this and decided it wasn't enough. He wanted the world. Or at least, the parts of the world he could reach by boat.

His instrument was a man named Sakatari. Sakatari was part Quenbo — he had Karaf blood from a grandfather's affair with a slave, which in Vera's rigid social hierarchy should have been a handicap but in practice made him harder, meaner, and more willing to do things that pure-blooded Verans found distasteful. He was the perfect colonial general: effective, brutal, and deniable.

The conquests began with the Kyzyl Peninsula, where the Wintermen were caught off guard by a seaborne invasion and enslaved within a season. Sakatari renamed the peninsula Sova Vera and handed the Wintermen over to Karaf slave masters, creating a hierarchy of cruelty that would have impressed a bureaucrat. Former slaves now owned slaves. The Wintermen, designated Rusikis, occupied the bottom of a social order that was only a few generations old and already hideously complex.

From the peninsula, Sakatari pushed north into the Balmur lands and then into Gardinsvo, cutting deals with the Lirzans and rolling forty thousand troops across the Northern Wastes. Every Winterman found was enslaved. Over a million Rusikis were taken. Three hundred thousand were shipped back to Vera.

Then Sokotros turned to the Womparti islands. Five thousand Veran soldiers landed in the Northern Rim and immediately discovered that conquering jungle islands was not the same as conquering frozen plains. The Wompartians under Chief Pepee fought with a resourcefulness that cost the Verans dearly. The Battle of Ugaloo remains the bloodiest engagement by deaths-per-minute in the entire First Age: 1,217 dead in four hours on a single small island.

The Veran Conquests ended in the three hundred and seventy-third year with the invasion of Lirza itself, the Verans' former allies. Sakatari broke the alliance with the same ease he broke everything else, and the Lirzan army was crushed at Uxitule. By the time Sokotros IV died in the three hundred and seventy-sixth year, Vera controlled territory across the entire Erezetta, from the Northern Wastes to the Rim.

Sakatari lived until the three hundred and eighty-ninth year. He owned two hundred Karaf and a hundred Rusikis at the time of his death. Klae recorded this number without comment, which for Klae was the harshest condemnation he knew how to give."""},

                {"title": "The Golden Age of Illiman",
                 "content": """By the late third century, Ceresy had become more than a religion. It had become the air that Fondore breathed.

Every major nation on the continent had adopted some form of Illiman's teachings, though the interpretations varied enough to give the prophet himself a headache had he been alive to hear them. The Raxonians practiced a form of Ceresy that involved a great deal of communal singing and outdoor worship, which suited their climate and temperament. The Gecks, characteristically, had organized Ceresy into an institutional hierarchy with tax benefits. The Leimish had turned it into an art form, with illuminated manuscripts and cathedral architecture. The Cynthians, being Cynthian, had written seventeen scholarly treatises debating whether Illiman's message was literal or metaphorical before most of them had actually read it.

The High Cere Uhktet in Mural Cere, who claimed religious authority over all Cereysts, declared this period the Golden Age of Illiman. He had some justification. Ceresy had spread beyond Fondore: the Submassa carried it to the ocean kingdom of Ulceron, and from Ulceron it reached Hiyalm, where the gnomes were cautiously receptive. It crossed the Avadacaster strait to Tzun, where it provoked a civil war between traditionalists and converts. The traditionalists won, but Ceresy survived underground, practiced in secret for generations.

But the Golden Age was also the age of the first religious wars. In the four hundred and sixty-second year, a man in the city-state of Gisup Geronus accused his neighbor of worshipping a different god than Illiman's. A group of traditionalists dragged the neighbor into the street and killed him. The violence spread. Traditionalists and New Cereysts, as the reformers called themselves, fought openly across the countryside, then across the continent.

Raxone suppressed its religious dissent through the invention of the Cereyst Inquisition, a bureau dedicated to identifying and destroying deviation from accepted doctrine. This was effective. It was also, as Illiman himself would have pointed out, completely contrary to everything he had ever taught. The man who preached forgiveness and introspection had, two centuries after his death, inspired an organization whose primary tool was the interrogation chamber.

The wars burned for decades and ended only when King Rhianal of Cynthia declared the Heresy Act, allowing both forms of Ceresy to be practiced without punishment. It was a pragmatic solution to a spiritual problem, and it worked everywhere except Ulceron, where the wars continued well into the Second Age.

Klae's assessment of the Golden Age was typically measured. He wrote: 'Illiman gave humanity a mirror. Some used it to see themselves clearly. Most used it to check whether their hat was on straight.'"""}
            ]},

            {"number": 9, "name": "Ninth Century",
             "description": "Snow and Fire. The newly crowned Kingdom of Raxone, still basking in its Golden Age, makes the fateful decision to wage war against the Wintermen. The resulting conflict ends the golden age and begins a rivalry that will last millennia. Meanwhile, the Mermassa of Ulceron make their first bewildering contact with the surface world.",
             "stories": [
                {"title": "The First Winter War",
                 "content": """In the four hundred and nineteenth year of the Klae calendar, Raxonian explorers reached the Turwhet islands and encountered the Wintermen for the first time. The Wintermen were huge, pale, and spoke a language that sounded like someone gargling gravel. They were also, as the explorers quickly discovered, cannibals.

Chief Yoq of the Wintermen ordered the explorers killed and eaten, not necessarily in that order. This was, by Winterman standards, a perfectly reasonable response to strangers showing up uninvited. By Raxonian standards, it was an act of war.

King Jontire Uratt, the ruling monarch of the still-young kingdom, made a decision that historians have been arguing about ever since. He mobilized twenty thousand soldiers under General Pondike Uratt and sent them to the Turwhet islands to punish the Wintermen and claim the territory for Raxone. This was, by any rational calculation, unnecessary. The Turwhet islands were frozen rocks with no strategic value, and the Wintermen posed no threat to Raxone's borders. But Jontire was a young king with a young kingdom, and young kingdoms have a tendency to prove themselves through violence.

The First Winter War lasted a year and was a nightmare. The Wintermen fought on their home terrain with a ferocity that the Raxonians had never encountered. The first battle, at a place called Shevlar, was a decisive Raxonian defeat. The Wintermen simply charged through the Raxonian lines, and soldiers trained to fight other humans found themselves facing opponents who were a foot taller and did not seem to notice when they were hit.

Pondike adapted. He ordered the capture and training of Pittenn, large goat-like creatures with thick fur and sharp teeth, native to the northern tundra. Hundreds were fitted with bronze armor and saddles and given a new name: Oburpittenn, War Beasts. This was the first recorded use of animals in organized warfare.

At the Battle of Icespicks, two hundred Oburpittenn charged the Winterman lines. The result was slaughter. Nine hundred Wintermen died, cut down by Raxonian riders wielding icepicks from atop their armored mounts. The Wintermen, who had never seen anything like it, called the day the Icepick Massacre.

The war ended at the Battle of Hatahune, where over ten thousand men from both sides died. Raxone won, technically. They claimed the islands. But when Pondike brought his surviving soldiers home, he found not parades but riots. Nearly fourteen thousand Raxonians had died for a cluster of frozen rocks, and the population was furious. King Jontire was assassinated. His replacement, Langrun, cut the army in half and instituted a policy called Plow Over Sword, a desperate attempt to restart the Golden Age.

It didn't work. The Golden Age was over. Raxone had traded its innocence for the Turwhet islands, and the exchange was not favorable. The Wintermen, meanwhile, retreated deeper into the wastes and began planning their revenge. They would take centuries to deliver it, but the Wintermen were patient in the way that ice is patient. They did not forget."""},

                {"title": "The Depths of Ulceron",
                 "content": """King Tessarion III of Ulceron had a problem that no other king in history had ever faced: he had discovered humans, and he could not figure out how to talk to one without drowning it.

The Mermassa had always known there was something above the water. They could see light filtering down from an incomprehensible ceiling. Occasionally things fell in — branches, leaves, the odd dead animal. But the Mermassa were an underwater civilization with underwater concerns, primarily the business of fighting each other, which they did with tremendous enthusiasm using tamed sharks, dolphins, and in some cases three-headed whales called Kessian.

Tessarion's curiosity was triggered by boats. He had been in the lowland waters near the Schvaine islands, crushing a rebellion, when he noticed objects on the surface. Wooden objects, moving under their own power, producing sounds. He sank one to investigate its inhabitants and found creatures that looked like Mermassa but had no fins, no tails, and possessed a strange organ in their chests that could only process air. They drowned before he could learn anything useful.

This did not deter Tessarion. It made him obsessed. He abducted humans from ships whenever he could, dragging them below the surface and attempting to communicate during the brief window between their submersion and their death. This was not productive.

Finally, Tessarion commissioned the construction of the Marinas Cove: an excavated rock chamber with an air pocket in the center, connected to the surface by a tube of seastone and seaweed nearly a mile long. He abducted another human, a fisherman from Suntrae named Kaed, and brought him to the Cove at maximum speed. After extensive medical treatment from Ulceronian doctors who had to hold their breath each time they entered the air pocket, Kaed survived.

The two became friends, improbably. Tessarion gave Kaed gills through an organ transplant that should not have worked but did. Kaed married Tessarion's daughter Pristin, beginning the line of half-human, half-Mermassa beings called Submassa. It was, by any measure, one of the strangest love stories in Elysali history.

It did not end well. While Tessarion was focused on his human project, the rebels he had been suppressing grew stronger and overthrew the kingdom. Tessarion was executed. But the Submassa survived, a bridge between two worlds that had never known the other existed. They would carry Ceresy into the oceans and eventually make contact with the surface civilizations that their ancestor Kaed had been snatched from.

Klae found this story particularly moving. He wrote: 'The distance between the surface and the sea floor is perhaps a mile. The distance between understanding and ignorance is the same. Both can be crossed, but only if someone is willing to drown a little in the attempt.'"""}
            ]},

            {"number": 10, "name": "Tenth Century",
             "description": "The Cereyian Wars. The final century of the First Age is defined by religious conflict as the spread of Ceresy triggers doctrinal disputes across Fondore. Traditionalists and reformers tear at the fabric of every nation, and only a last-minute act of political pragmatism prevents the age from ending in total holy war. The age closes not with a bang but with an exhausted silence.",
             "stories": [
                {"title": "The Heresy at Gisup Geronus",
                 "content": """The man who started the Cereyian Wars did not intend to start anything. He was a potter in the city-state of Gisup Geronus, and his name has not survived, which is perhaps for the best. He accused his neighbor of worshipping a different god. That was all. A potter, a neighbor, and an accusation.

The neighbor was killed by a mob of traditionalists who had been looking for an excuse. The excuse was doctrine. The New Cereysts, as they called themselves, had begun interpreting Illiman's teachings in ways that the old guard found unacceptable. The specifics of the doctrinal dispute have been lost, which tells you something about how important they actually were. What mattered was that people on both sides believed they were right, and people who believe they are right about religion are capable of extraordinary violence.

The fighting spread from Gisup Geronus to the surrounding city-states within weeks. It crossed into Mural Cere within a month. It reached Cynthia by autumn. Within a year, every major nation in Fondore was dealing with religious violence of some kind, ranging from street brawls to organized military campaigns.

The Raxonians, still reeling from the Winter War, handled the problem with characteristic directness. King Langrun created the Cereyst Inquisition, a bureaucratic apparatus designed to identify religious deviants and destroy them. The Inquisition was staffed by men who had been soldiers and now had too much free time. They were efficient. They were thorough. They were also, by any reasonable reading of Illiman's actual teachings, committing the exact sins that Illiman had spent his life preaching against, a contradiction that apparently occurred to no one involved.

The Gecks handled it differently. The city-states, always more interested in commerce than theology, attempted to simply outlaw the dispute. This worked about as well as outlawing weather. The Leimish handled it with characteristic indecision, issuing proclamations that were so carefully worded as to say nothing at all.

The wars lasted for decades. They ended not through any spiritual revelation or military victory but through the Heresy Act, issued by King Rhianal of Cynthia in the four hundred and ninety-eighth year. The Act was simple: both forms of Ceresy could be practiced without punishment. Practice what you want, worship how you want, and for the love of whatever god you're arguing about, stop killing each other.

It was not a satisfying conclusion. There was no grand reconciliation, no moment of collective enlightenment. Just exhaustion. The nations of Fondore had spent the better part of a century fighting over the correct way to interpret a man who had told them to be kind to each other, and they were tired.

Klae wrote: 'The Cereyian Wars proved that humanity is capable of missing the point on a continental scale.'"""},

                {"title": "The Last Day of the First Age",
                 "content": """The First Age ended quietly. There was no ceremony. No declaration. The last day of the five hundredth year passed like any other day, and the world continued to spin on its axis without any particular awareness that an era was over and another was about to begin.

In Hipola, which was now called Hypolta, fishermen mended their nets on the docks of the oldest city in the world. A couple of them were arguing about the price of squid. Neither had any idea that they were living in a city that had been founded by a man in bearskins five centuries earlier, or that the argument they were having was essentially the same argument that every fisherman in every port in the world was having at that exact moment, because squid prices are universal and eternal.

In Raxona, the new capital of the new kingdom, builders were laying the foundation stones of Ditran Palace. The quarrymen were on strike because they hadn't been paid. King Langrun's finance minister was trying to explain that the treasury was empty because of the Winter War, and the quarrymen were explaining, with considerable force, that they didn't care.

In Imbraxione, the Lirzan capital and the largest city in the world, a dragonborn prince was being born in the royal chambers. He was the great-great-great-grandson of Zugaraz, and he could already breathe small puffs of smoke by the time he was three hours old. His nurse found this alarming. His mother found it hilarious.

In the Pasav desert, a Cereyst monk was walking the road where Illiman had been killed by a highwayman centuries before. The road was still dusty. The monk was still walking. He did not know where he was going, which Illiman probably would have said was exactly the point.

And on the remote island of Lipse, off the coast of Acumfrial, a Hiyalmite fishing family was building a house. It was a small house, on a small island, at the edge of the known world. No one who lived there had any idea that centuries later, a young man named Kratikar Klae would sit on a hill overlooking this same spot and begin writing the book you are now reading.

The First Age was over. Humanity had learned to build cities, forge bronze, worship gods, wage wars, make music, and enslave each other. They had not yet learned to do any of these things well, or wisely, or without causing extraordinary suffering to the people standing next to them. But they had started. And starting, as Klae was fond of saying, is the hardest part. Everything after that is just consequences."""}
            ]}
        ]
    },
]

# Ages 2-8: structure in place, stories to be written
for age_data in [
    (2, "The Miracles of Illiman", 501, 1000,
     "The Second Age was a bustle of activity from across Fondore, with petty kingdoms of men sprouting up across the continent. The Gecka barbarians dominated the south but their learned Ghenyarian slaves schemed and planned in secret for a day of reckoning. To the North across the great mountain range known as the Leimbordur, woodland tribes were banding together under a new banner, The House of Clairdwell. The West had fervent grassland dwellers forming mead halls and horse farms centered around modern day Epervinay. But by far, the most significant legacy of this age was the institutional spread of Ceresy: no longer a wandering prophet's teaching but an organized religion with temples, hierarchies, and political ambitions that rivaled any kingdom's.",
     ["The Reckoning of Ghenyar", "The Rise of the Clairdwells", "The Debrear Kingdom", "The Punitive Wars", "The Second Age War", "Mark of Tzun", "The Shoalene Wars", "The Winter Division", "The Knights of Lambridge", "The Elysal Compact"]),
    (3, "The Era of Sail", 1001, 1500,
     "The winds were blowing West and the men of Fondore could not withstand the call. All across the continent, seaside nations were becoming maritime with the first operable deepwater ships being constructed by the great Leimish engineer Raist Celle on the coast of the Ardent. Nations were truly forming now and Fondore was being carved up into the seven kingdoms of men. Mercantile ships left the ports of Clarity, Rin Nohara, Erogan, Hypolta, and Suntrae, led by patriotic adventurers, curious explorers, and greedy thieves alike. Within time, these seekers of fortune would discover that the lands beyond the Erezetta were not so uninhabited as originally believed, either to great delight or brutal horror.",
     ["The First Ships", "Colonial Landings", "Rundelian Ceresy", "Novus Gecharium", "The First Holy War", "The Arden Federations", "The Barren Wars", "Capera Cuza", "Rise of the Luschnypp", "The Shrinking Map"]),
    (4, "An Empire of Men", 1501, 2000,
     "The story belongs not to the man who died, but to the man who wrote about it. This ancient Cynthian proverb originated in the Fourth Age during the Pervin Wars. The fourth age saw the rise of the first continental empire: the Gechann. Through constant warmongering, advances in military tactics and logistics, and the creation of the first professional army, Geckish domination throughout the realm of men was unstoppable. But empires, as Klae observed, carry the seeds of their own destruction, and the Gechann sowed more seeds than most.",
     ["Rise of Imperial Gecha", "The Pervin Wars", "Fall of Vera", "Rise of the Karagon", "The Icrazan Genocide", "Palasor City", "The Second Holy War", "Kingdom of the North Divided", "The Schvainese Rebellion", "The Long Shadow"]),
    (5, "The Rise of the North", 2001, 2500,
     "The Fifth Age belongs to Raxone. After centuries of playing second fiddle to Gechann ambition and Cynthian diplomacy, the Kingdom of the North rose to become the dominant military power on Fondore. Raxonian mercenaries had always been present in foreign wars, but now Raxone fought its own, and won. The balance of power shifted northward, and the nations of Fondore scrambled to adjust to a world where the men who drank too much and laughed too loud were suddenly the ones making the rules.",
     ["The Raxonian Ascendancy", "War of Snow", "Lipse Founded", "The Border Tensions", "Concert of Nations", "The Great Plague", "Pervin Awakening", "The Merchant Princes", "Northern Reforms", "A Fragile Peace"]),
    (6, "A Leap of Faith", 2501, 3000,
     "The Sixth Age was an age of ideas. Philosophy, science, and political theory erupted across Fondore with an intensity that made the old institutions nervous and the young populations excited. The printing press equivalent arrived in Clarity and within a generation, pamphlets were more dangerous than swords. Ceresy faced its most serious internal crisis since the Cereyian Wars, and the nations of Fondore began to grapple with questions that had no easy answers: What is a citizen? What does a king owe his people? And what happens when the people decide the answer is: everything?",
     ["The Printing Revolution", "The Reformations", "The Terminal War", "The Philosophers of Oradova", "The Pervin Republic", "Fall of the Clairdwells", "The Geckish Civil War", "The Luschnypp Ascendant", "The Treaty of Clarity", "New Faiths"]),
    (7, "A Sacred Hegemony", 3001, 3500,
     "The Seventh Age saw the great powers of Fondore settle into a precarious balance that historians would later call the Sacred Hegemony — not because it was holy, but because disturbing it was considered sacrilege by the diplomats who maintained it. Gecha, Raxone, and Hyacinth formed the three pillars of continental order, each checking the others while smaller nations navigated the spaces between them. It was an age of standing armies, professional diplomats, absolute monarchs, and the slow realization that the old ways of doing things were running out of time.",
     ["The Three Pillars", "Absolutism in Gecha", "The Cynthian Renaissance", "Raxone Colonizes Perut", "The Karagon Crisis", "Court Intrigue in Clarity", "The Assassin's Age", "The Pervin Question", "The Naval Arms Race", "Cracks in the Hegemony"]),
    (8, "The Age of Solitude", 3501, 4000,
     "The Eighth Age earned its melancholy name not from isolation but from the growing sense, felt across all of Elysal, that the world was changing faster than anyone could follow. Steam power arrived. Factories rose in Boulavar and Raxona. Railways began to connect cities that had taken weeks to travel between. The old feudal order crumbled under the weight of new money, new ideas, and new weapons that could kill at distances the knights of Lambridge would have found obscene. It was an age of revolutions, both industrial and political, and by the time it ended, the world that Hipolyptica had built from a collection of stone huts was unrecognizable.",
     ["The Steam Revolution", "The Factory Cities", "The Great Upheaval", "Railways and Rifles", "The Democratic Movements", "Twilight of Kings", "The Workers' Revolt", "The Colonial Reckoning", "The Annals Begin", "The Unwritten Chapter"]),
]:
    num, name, ys, ye, desc, century_names = age_data
    centuries = []
    for ci, cname in enumerate(century_names, 1):
        cent = {
            "number": ci,
            "name": f"{['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth','Ninth','Tenth'][ci-1]} Century",
            "description": f"The {cname}. This century shaped the course of the {name} through events both grand and intimate. Scholars continue to debate its significance to this day.",
            "stories": [
                {"title": f"Chronicles of the {cname}",
                 "content": f"[This chapter of the Annals awaits a chronicler. The events of the {cname} during the {name} are known in fragments — recovered scrolls, oral traditions, and the occasional archaeological discovery. Kratikar Klae left this entry open, trusting that a worthy scholar would one day fill these pages with the truth of what happened.]\n\nWhat is known: this was a period of significant change within the {name}. The forces that defined the age were particularly acute during this century.\n\nAdventurers, scholars, and witnesses: the Annals welcome your contributions."},
                {"title": f"Voices from the {cname}",
                 "content": f"[Collected testimonies from the {cname} — fragments gathered by Kratikar Klae during his decades of research.]\n\n'We thought we understood the world. We were wrong.' — Anonymous scholar, early {cname}\n\nThese pages remain open for new voices. The Annals are a living document, and the {cname} of the {name} deserves to be told in full."},
            ]
        }
        centuries.append(cent)
    AGES.append({
        "number": num,
        "name": name,
        "year_start": ys,
        "year_end": ye,
        "description": desc,
        "centuries": centuries,
    })

# Sort ages by number
AGES.sort(key=lambda a: a["number"])