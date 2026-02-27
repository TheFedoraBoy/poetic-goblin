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
    {
        "number": 2,
        "name": "The Miracles of Illiman",
        "year_start": 501,
        "year_end": 1000,
        "description": """The Second Age was a bustle of activity from across Fondore, with petty kingdoms of men sprouting up across the continent. The Gecka barbarians, no longer barbarians but still called that by everyone who wasn't one, dominated the southern city-states and grew fat on trade and ambition. To the north across the great mountain range known as the Leimbordur, woodland tribes were banding together under a new banner: the House of Clairdwell. The west had fervent grassland dwellers forming mead halls and horse farms in lands that would become Epervinay. And in the great forests of Thaum, the Debrears were doing something nobody expected — they were building a civilization.

But the age takes its name from none of these. It takes its name from the institutional spread of Ceresy, from the moment Illiman's wandering teachings became a structured religion with temples and hierarchies and political ambitions that rivaled any kingdom's. Ceresy did not merely survive the Cereyian Wars of the First Age; it emerged stronger, more organized, and more politically useful. Kings discovered that a religion which taught people to forgive their rulers was a very convenient religion to support.

The Second Age is the age of first kingdoms. Not tribes, not city-states, not loose alliances of chiefs who agreed to stop hitting each other for a season. Proper kingdoms, with borders and laws and standing armies and all the bureaucratic apparatus necessary to tax a population that would rather not be taxed. Fondore was being carved into shapes that would endure for millennia, and the carving was done primarily with swords.""",
        "centuries": [
            {"number": 1, "name": "First Century",
             "description": "The Forging of Deberania. The wild Debrear tribes of the Thaugren forest unite under the warrior-king Bugutahff and declare themselves a nation. The great walled city of Foebrier rises on the central plains, and the Debrears transform from forest raiders into a feudal kingdom with astonishing speed. Not everyone in their claimed territory agrees with the new arrangement.",
             "stories": [
                {"title": "The Thaumfuher's Decree",
                 "content": """The Debrears had spent the better part of the First Age being left alone, which was exactly how they liked it. They lived in the Thaugren forest, they raided anyone foolish enough to walk through it, and they maintained a reputation for savagery that kept more civilized neighbors at a comfortable distance. The massacre of Ghenyarian soldiers under General Groyar was still taught in Geckish military academies as a cautionary tale about the dangers of underestimating forest people.

But the world was closing in. The Kingdom of Raxone pressed from the north, its borders creeping southward with each passing decade. The Geckish city-states pushed from the south, their traders and settlers nibbling at Debrear territory like mice at a grain store. The warrior-leader Laur Bugutahff looked at a map, looked at the arrows pointing inward from every direction, and made a calculation that his ancestors would have found blasphemous: the Debrears needed to stop being Debrears and start being a country.

In the thirteenth year of the Second Age, he declared the Thaumatarchy — a council of the high warrior chiefs and their families, with the Bugutahff clan at the apex. The scattered tribal lands of Thaum became the kingdom of Deberania, and Bugutahff gave himself a title that roughly translated to King of Everything: Thaumfuher.

The transformation was remarkable. Within a generation, the Debrears went from forest raiders to feudal lords. They adopted farming, irrigation, written law, siege warfare, and — most reluctantly — table manners. Bugutahff ordered the construction of Foebrier, the Great Walled City, on a sprawling plain inland from the east coast. The walls went up first: twenty feet of stone on all sides. Then came the markets, the taverns, the barracks, and at the center of it all, Thaumarch Keep, a fortress so imposing that visiting diplomats from Gisup Geronus described it as 'a very large fist made of rock.'

By the twenty-sixth year, Foebrier had sixty thousand residents, making it the second largest city in Fondore after Oradova. The Debrears, who a generation earlier had been eating their meals with their hands around campfires, now had a standing army, a tax system, and a court where disputes were settled by judges instead of axes. Bugutahff even commissioned a national history, though the scribes found the early chapters difficult to write since most of the source material consisted of battle scars and grudges.

Klae described Deberania's rise as 'the fastest civilizational sprint in recorded history, achieved by a people who ran not because they wanted to but because they heard footsteps behind them.'"""},

                {"title": "The Lemish Problem",
                 "content": """Not everyone within Deberania's claimed borders was happy about being claimed. The Lemish had never been Debrears, not really. They were a branch of the same ethnic tree, technically, but a branch that had grown in such a different direction that calling them cousins was generous. While the Debrears had been perfecting the art of ambush and forest warfare, the Lemish had been perfecting the art of everything else. Music, painting, poetry, architecture, the radical innovation of using forks instead of fingers. They had built the city of Clarity sometime in the late First Age and had been living there in genteel contentment ever since, practicing Ceresy with particular devotion and developing a language so beautiful that other nations learned it just to write love letters.

The Thaumfuher regarded the Lemish with a mixture of contempt and necessity. They were soft, they were pretentious, and their soldiers looked like they had been dressed by their mothers. But they controlled the eastern coast, which meant trade with Ulceron and the sea routes, which meant money. And Bugutahff, for all his forest instincts, understood money.

Diplomatic relations opened between Foebrier and Clarity. The Debrear diplomat Pito Risselbrohn argued for Lamland — as the Lemish had begun calling their territory, a name the Debrears found irritatingly independent — to join Greater Deberania. The Lemish diplomat Emantine Crueqet argued for full sovereignty. The negotiations went nowhere, which was predictable, because one side was offering partnership and the other side was offering subjugation and calling it partnership.

The leader of Lamland was a knight named Sir Clairdwell. He was, by most accounts, a decent man with decent intentions and an indecent lack of military resources. When the talks collapsed and Deberania declared war, Clairdwell did the only sensible thing available to him: he called for help. A messenger was sent to Cynthia, the great power across the strait, begging for soldiers.

Three thousand Cynthian troops arrived at Clarity by boat. For a brief, shining moment, the Lemish believed they were saved. They were wrong, but the belief itself was important, because it would be the last time the Lemish trusted anyone to save them without conditions. The betrayal that followed would shape their national character for millennia: polite, cultured, and always, always, prepared to be abandoned."""}
            ]},

            {"number": 2, "name": "Second Century",
             "description": "The Siege of Clarity. Cynthia withdraws its promised military support and the Debrears descend upon the Leimlands. The three-month siege of Clarity becomes one of the defining tragedies of the age, and the young soldier Emantine Asaundier escapes to the Isles of Schvaine with a handful of survivors, carrying with him a hatred that will become a kingdom.",
             "stories": [
                {"title": "The Great Siege of Clarity",
                 "content": """The Cynthians left on a Tuesday.

That detail is not recorded in any official history. It comes from a fragment of a private letter recovered by Klae from the estate of a Leimish wool merchant, and it reads: 'The Cynthian ships departed on the second day of the week, which was a Tuesday, and I remember this because my wife had baked a cake for the officers and the cake was still warm when we saw the sails turning south.' The merchant's name is lost. The detail about the cake survived.

King Sans IV of Cynthia had sent three thousand soldiers to defend Clarity against the Debrears. He was seventeen years old, freshly crowned, and had made the decision with the conviction of a young man who believes in sovereignty and has never been to war. Within weeks, the Thaumfuher made it clear that Cynthian involvement in what he considered an internal affair would be treated as an act of war against Deberania. Sans IV consulted his advisors, who consulted their fear, and the soldiers were recalled.

Thaumgenerulf Igorion marched his army through the Leimlands like a man walking through his own garden. The countryside was defenseless. Thousands of Lemish farmers fled toward Clarity, and Igorion's soldiers processed them as they went — some taken as prisoners, some murdered, some left alone for no discernible reason other than the whims of individual officers. The randomness was, in some ways, worse than systematic cruelty. There was no logic to appeal to.

When the Debrear host arrived at Clarity's walls, the city was swollen with refugees and short on everything except despair. Captain Qercy De' Tourmont commanded the defense with a valor that the Leimish have never forgotten. The siege lasted three months. The Debrears built siege towers. The Leimish burned them. The Debrears dug tunnels. The Leimish flooded them. For ninety days, a city of musicians and poets and fork-users held off an army of professional warriors, and the fact that they eventually lost does not diminish what they did.

The most famous moment came on the sixty-third night. Seventy Leimish cavalrymen under Brigadier Sergeant Qercy De' Levaun charged through the gates at midnight into the sleeping Debrear camp, slaughtering dozens before being overwhelmed. It was suicide, and everyone involved knew it was suicide, and they did it anyway. The Leimish have a word for this: Vendabaine. It means, roughly, 'the beautiful death.'

Among the cavalrymen who survived was a young soldier named Emantine Asaundier. He escaped Clarity by boat, fleeing to the Isles of Schvaine with a handful of other survivors. He carried nothing except his sword, his name, and a promise that he would come back.

Clarity fell. The Debrears marched in, tore down the Clairdwell banners, and began the process of turning the most beautiful city in Fondore into a provincial capital. It would take them years to realize that you cannot occupy a city without occupying its culture, and the culture of Clarity was not the kind that submitted to being occupied."""},

                {"title": "The Exile of Asaundier",
                 "content": """The Isles of Schvaine were cold, wet, and inhabited primarily by fishermen who wanted to be left alone. They were not the kind of place where kingdoms were born. This made them perfect for Emantine Asaundier's purposes, because nobody was looking.

Asaundier was young, probably in his early twenties, though Leimish records of the period are unreliable because the Debrears burned most of them. What is known is that he arrived on Schvaine with fewer than forty men, no money, no supplies, and an absolute conviction that he was going to take back his country. The fishermen thought he was insane. They helped him anyway, because Leimish culture has a deep and abiding respect for people who commit to things that are clearly impossible.

He spent years on the islands. He drilled his men in the rocky coves, practicing formations on beaches and sword work in the rain. He sent agents back to the mainland to recruit sympathizers, building a network of Leimish loyalists who passed messages through merchant routes and buried dead drops. He studied the Debrear military — their tactics, their weaknesses, the rotation of their garrisons. And he forged a code of conduct for his growing band of warriors that drew on three sources: the Leimish tradition of chivalry, the Cereyst principles of mercy and honor, and a practical understanding that men who fight for a cause need rules to distinguish them from men who fight for plunder.

He called his order the Knights of Lambridge.

The name was deliberate. Not the Knights of Clarity, the fallen capital. Not the Knights of Schvaine, their current home. The Knights of Lambridge — a name that claimed the entire Leimish territory, past and future, as their responsibility. It was an act of audacity that bordered on delusion, and it worked precisely because of that. Men who had lost everything needed something enormous to believe in, and Asaundier gave them a country-sized belief.

Klae tracked the growth of the order through scattered records and oral traditions. From forty men on a wet island to several hundred within a decade. From fishing boats to proper warships donated by Cynthian merchants who felt guilty about their king's betrayal. From a ragged band of exiles to a disciplined military force that the Debrear governors on the mainland began to hear rumors about and chose, fatally, to dismiss.

Asaundier's retaking of the Leimlands is a story for a later century. But the founding of the Knights of Lambridge — on a cold island, with nothing but swords and stubbornness — is the foundation that everything after was built on. Klae wrote of Asaundier: 'He was not the greatest swordsman, nor the greatest tactician, nor the greatest leader of men. He was simply the man who refused to accept that the story was over.'"""}
            ]},

            {"number": 3, "name": "Third Century",
             "description": "The Liberation of Lambridge. Emantine Asaundier and the Knights of Lambridge return to the mainland, igniting a war of liberation against Debrear occupation. The fighting is long and brutal, but the Leimish reclaim their homeland and establish the Kingdom of Lambridge under the Clairdwell dynasty, protected by the Leimbordur mountains that will become Fondore's most important geographic feature.",
             "stories": [
                {"title": "The Return of the Knights",
                 "content": """Asaundier came back with the tide.

There is some debate among historians about the exact year, because the Leimish calendar had fallen into disuse during the Debrear occupation and nobody could agree on what day it was. But the oral traditions all agree on the weather: it was raining. It was always raining on the day that mattered most in Leimish history, which either speaks to the climate of the Leimlands or to the Leimish preference for dramatic narrative.

The Knights of Lambridge crossed the strait from Schvaine in a fleet of forty ships — warships, merchant vessels, fishing boats, anything that could float and carry armed men. They landed at dawn on the eastern coast and immediately attacked the Debrear garrison at Loquive, a port town that the occupiers had turned into a naval depot. The garrison was overwhelmed in hours. Asaundier's men had been training for this moment for years, and the Debrear soldiers, who had grown accustomed to policing farmers rather than fighting warriors, were unprepared for the ferocity of the assault.

The landing at Loquive was the match, but the fire had been laid long before. Asaundier's network of Leimish sympathizers activated simultaneously across the Leimlands. Debrear tax collectors were murdered in their offices. Supply wagons were burned on the roads. Bridges were destroyed, messengers intercepted, garrison commanders who had married local women found their doors locked from the inside. It was not a conventional military campaign. It was a coordinated act of national fury.

The Debrears responded as all occupying forces respond when the occupied population stops cooperating: with escalating brutality. Villages suspected of harboring rebels were burned. Public executions were held in town squares. The Thaumfuher dispatched reinforcements from Foebrier with orders to crush the rebellion entirely.

The war lasted years. The Leimlands are not good terrain for a conventional army — dense forests, rolling hills, rivers that flood unpredictably, and a local population that knew every path and shortcut. The Knights fought like the Debrears' own ancestors had once fought in the Thaugren: from the trees, in the shadows, striking and vanishing. The irony was not lost on anyone.

The decisive engagement came at the Battle of the Leimbordur, fought in the mountain passes that separated the Leimlands from the southern plains. Asaundier's forces, now swelled by thousands of Leimish volunteers, held the passes against a Debrear army twice their size. The mountains did what mountains do: they equalized numbers. The Debrears could not bring their full strength to bear in the narrow defiles, and the Leimish defended each ridge and ravine with the desperation of people who knew that the mountains were the only thing between them and re-conquest.

The Debrears broke. Not all at once, but gradually, the way an army breaks when it realizes that the land itself is fighting against it. The Thaumfuher, facing unrest in his own territories and a war that was costing more than it was worth, withdrew his forces south of the Leimbordur. The mountains became a border. They remain one to this day."""},

                {"title": "The First Clairdwell King",
                 "content": """With the Debrears driven out, the question became: who rules?

Asaundier had the army, the loyalty of the people, and every practical justification for crowning himself king. He declined. This was either an act of extraordinary humility or extraordinary political calculation, and knowing the Leimish, it was probably both.

Instead, Asaundier tracked down the surviving members of the old Clairdwell family, the pre-Debrear nobility who had been scattered across Fondore during the occupation. He found them living as merchants in Geckish cities, as servants in Raxonian households, as monks in Cereyst temples. He gathered them together and presented them with a crown.

The first Clairdwell king of Lambridge — the records disagree on his given name, though Emmantine is most common — was crowned in a ceremony held in the ruins of Clarity's great cathedral. The cathedral had been damaged during the siege and the occupation, and it would take decades to fully restore. Asaundier chose the location deliberately. The message was clear: we are rebuilding on what was broken.

The Kingdom of Lambridge was declared sovereign, with its capital at Clarity and its borders defined by the Leimbordur to the south and the Erezetta Ocean to the west. The Knights of Lambridge became the kingdom's military order, sworn to protect the Clairdwell dynasty and the Leimish people. The code of honor that Asaundier had written on Schvaine became the code of the kingdom: chivalry, mercy, service.

The Debrears, for their part, retreated to their heartland around Foebrier and settled into a long sulk. They had lost the Leimlands, the coast, and a significant portion of their national pride. The rivalry between Deberania and Lambridge would simmer for centuries, occasionally erupting into border skirmishes and more frequently into acts of cultural snobbery that both sides found more insulting than actual warfare.

But the Clairdwell dynasty held. It would go on to become one of the longest-reigning bloodlines in Fondore, producing kings who ranged from the brilliant to the catastrophic but who all, without exception, claimed descent from a soldier on a rainy beach who refused to accept that his country was gone.

Klae found this deeply moving. He wrote: 'The Clairdwells did not earn their throne through conquest or divine right. They earned it because one man gave it to them, and that man had earned the right to give it by fighting for everyone else first.'"""}
            ]},

            {"number": 4, "name": "Fourth Century",
             "description": "A United Gecha. The Geckish city-states, long content with their loose confederation, are forced into unity by the ambitions of Varius Vazonus of Saul. The Punitive Wars reshape the political landscape of southern Fondore and produce the first elected Supremus Leader, the beginning of a uniquely Geckish form of government that blends democracy with autocracy.",
             "stories": [
                {"title": "The Poisoner of Saul",
                 "content": """Varius Vazonus wanted Suntrae, and Bor Atlas was in the way.

Suntrae was the jewel of the Geckish city-states: an island fortress that controlled the richest trade routes in southern Fondore, with harbors deep enough for the largest merchant ships and warehouses full of goods from Ulceron, Hiyalm, and the distant Rim. Saul, Varius's own city-state, was respectable — a center of science and philosophy — but it lacked Suntrae's commercial power, and Varius was the kind of man who kept a ledger of his own deficiencies.

In the forty-fifth year of the Second Age, talks opened between Saul and Suntrae about a joint union. Bor Atlas, the Minister of Suntrae, was not opposed to cooperation. The problem, as always with Gecks, was who would be in charge. Both men were intelligent, ambitious, and constitutionally incapable of being second to anyone.

Bor Atlas fell ill in the forty-sixth year. The illness was sudden, mysterious, and fatal. Suspicions of poisoning circulated through every tavern and court in the city-states, but no proof surfaced, because Varius was either innocent or very good at not being caught. With Bor dead, Varius was declared leader of both states and immediately renamed the combined entity Ichin Saul.

The other city-states watched this with the kind of alarm that only Gecks can produce: furious, calculating, and expressed primarily through strongly worded letters. Gisup Geronus, Jayvlun, and Skylaer formed a coalition led by three men — Avictus Lectom, Taegen Shaen, and Kaed Aromus — who called themselves the Trinium: the first formal triumvirate in Geckish politics. They demanded Varius release Suntrae. Varius, who had not poisoned a man and absorbed a city-state just to give it back, refused.

The Punitive Wars lasted from the forty-ninth to the fifty-sixth year and were fought with the particular viciousness that family feuds produce. These were not foreigners fighting each other. They were Gecks fighting Gecks, people who shared a language, a religion, trade networks, and frequently blood relations. Over fifty thousand soldiers saw active service. Cynthia secretly funneled aid to the coalition. Famous commanders on both sides earned reputations that would follow them into much larger wars: Bor Otticus held a position for the Saul forces with forty men against hundreds, a feat that his descendants would spend centuries embellishing until the forty men became four and the hundreds became thousands.

Klae noted that the Punitive Wars were the moment the Gecks stopped being a collection of city-states and started becoming a nation, even though it would take another generation before anyone used that word."""},

                {"title": "Lae Unaebrum Gecharium Dyuem",
                 "content": """The Battle of Vericou ended the Punitive Wars, and it ended them ugly.

Bor Raed, Varius Vazonus's best commander, marched six thousand veteran soldiers through the night to the coalition encampment near the town of Vericou. The coalition forces, eight thousand strong under Supremus Commandant Polta Blya, had been marching for thirty miles the previous day and were exhausted. Blya had direct orders to continue to the fort at Aemore, but he decided to let his men rest for the night. This decision killed him.

Bor Raed's men hit the camp in the dark. The fighting was confused, desperate, and one-sided. Five thousand coalition soldiers were captured. Polta Blya was publicly executed. Without their rear guard, the coalition's core city-states were exposed, and the surrender came within weeks.

The peace terms were Varius's masterpiece. Rather than annexing the defeated states — which would have produced another war within a decade — he proposed something new. Each city-state would retain its sovereignty, but all would answer to a single elected leader chosen every ten years. This leader, called the Supremus, would control international affairs and collect taxes. The capital would be whichever city-state the Supremus came from.

It was democracy with a knife behind it, and Varius made sure everyone understood both parts. He declared himself the first Supremus Leader, and Ichin Saul became the capital. The city-states prospered under his rule. Trade expanded. The military was professionalized, with standardized ranks and equipment. The pike and the use of cavalry became accepted doctrine. Geckish merchants, always aggressive, became ubiquitous — loan sharks and wine traders in every major city on Fondore.

When Varius stepped down in the sixty-sixth year and Taegen Shaen — his former enemy — was elected to succeed him, the system proved it could survive a transfer of power. This was the real achievement: not the winning but the letting go.

Varius Vazonus died in the seventy-first year, alone in his villa on Suntrae, the island he had murdered for. His last words were recorded by a servant: 'Lae Unaebrum Gecharium Dyuem.' A United Gecha At Last.

Klae, who spent considerable effort verifying this quote, concluded that it was probably authentic, because it was exactly the kind of thing a dying Geck would say — self-congratulatory, historically aware, and in a dead language that nobody else in the room could understand."""}
            ]},

            {"number": 5, "name": "Fifth Century",
             "description": "The Pervin Powder Keg. Underneath the surface of Cynthian civilization, the Pervins — the original inhabitants of the southwestern peninsula — live as serfs and second-class citizens in their own ancestral lands. Tensions that have been building since the formation of Cynthia finally find their flashpoint in the murder of a young Pervin soldier.",
             "stories": [
                {"title": "The Flogging of Caid Liedech",
                 "content": """There are moments in history where a single act of cruelty becomes the hinge on which everything turns. The flogging of Private Caid Liedech was such a moment, though no one involved understood it at the time. Not the Cynthian colonel who ordered it. Not the soldiers who carried it out. And not Caid himself, who died on the eighty-ninth year of the Second Age, face down in the mud of a military encampment, his back opened to the bone.

Caid Liedech was Pervin. This was the beginning and end of his crime. The charges were treason, but treason in the northeastern provinces of Cynthia was whatever the local commander said it was, and Cynthian commanders in Pervin territory had a habit of saying it often. The Pervins — descendants of one of the three original tribes that had formed Cynthia centuries earlier — had been relegated to serfdom while the Cynthian and Hyach tribes occupied the upper classes. They farmed Cynthian land, served in Cynthian armies, and paid Cynthian taxes, and in return they received the privilege of being called Cynthian citizens, which was a bit like being called a member of a family that locked you in the basement.

Caid's father was Sans Liedech, a farmer from Ryad's Landing who was also one of the most influential communal leaders in the Pervin northeast. Caid had been the pride of the community — a young man who had enlisted in the Cynthian military, proof that a Pervin could succeed within the system. His death was proof of the opposite.

The news reached Ryad's Landing and the city exploded. Sans Liedech himself dragged the Cynthian governor out of his house and hung him from a lantern post. This was not a riot. It was the beginning of a war that the Cynthians would spend the next decade losing and the next millennium regretting.

Klae collected seventeen different accounts of the flogging. They disagree on the time of day, the weather, and the exact charges. They agree on one detail: the colonel who ordered it, Helter Bakiter, was not Cynthian. He was Raxonian, serving in a Cynthian regiment. This would matter enormously in the weeks that followed, because Raxone would use his death as a pretext to insert itself into a conflict that had nothing to do with it, which is what great powers do when they smell opportunity in someone else's suffering."""},

                {"title": "Sans the Avenger",
                 "content": """Sans Liedech did not look like a revolutionary. He was a farmer with calloused hands and a face that had spent too many years squinting into the sun. He did not give rousing speeches. He did not write manifestos. When he spoke, he spoke quietly, in the Pervin way, and people leaned in to listen.

After hanging the governor, Sans organized the men of Ryad's Landing into a militia and marched them to find Colonel Bakiter's regiment. Four thousand Pervins, armed with farming tools, hunting weapons, and a handful of proper military arms stolen from the garrison. They found Bakiter's force of two hundred regulars in the spring of the ninetieth year and massacred them. Bakiter himself was tortured, humiliated, and beheaded, all of which was chronicled by a scribe named Haiten Creid, who would go on to become the Pervin revolution's official historian and, in Klae's assessment, its most shameless propagandist.

Queen Liasal of Cynthia dismissed the rebellion with a phrase that Klae found in three separate sources: 'The farmers will return to their farms in less than a month.' She was wrong by approximately a decade.

Sans took the city of Angelozi. He fortified Ryad's Landing. He rallied every Pervin town and village to his cause, and his fighting force swelled to ten thousand. A Geckish mercenary captain named Kevus Embrum trained them through the summer, turning farmers into soldiers with the brutal efficiency for which Geckish military contractors were famous.

The Cynthians sent an army. Sans beat it. They sent a bigger army. He beat that too, at the Battle of Broken Shields, where six hundred Cynthian soldiers died trying to retake Ryad's Landing. The queen called for Raxonian help, and three thousand Raxonian regulars arrived under Wildrow Bakiter — the dead colonel's brother, which tells you everything about the war's ability to generate vendetta.

Sans knew he couldn't fight two great powers alone. He turned to the Gecks, who had been waiting for exactly this opportunity. The current Supremus, Tobias Moranibul, was sympathetic to the Pervin cause and furious about Cynthia's interference in the Punitive Wars. The Gecks joined the war.

In the ninety-second year, the Pervins declared independence. The ancient tribal name was revived: Epervinay. Sans Liedech, a farmer who had never held political office, became the acting minister of a country that was, at that moment, mostly a collection of burning towns and angry people.

He did not live to see peace. But he lived long enough to see his people free, which was more than most revolutionaries get. The Pervins remember him simply as Sans the Avenger, and in Epervinay, there is no higher title."""}
            ]},

            {"number": 6, "name": "Sixth Century",
             "description": "The Second Age War. What began as a Pervin rebellion becomes a continental conflict. Gecha, Epervinay, and Vera align against Cynthia, Raxone, and Mural Cere in a war that reshapes the map of Fondore and establishes Epervinay as a sovereign nation for the first time in centuries. The Battle of Yoen becomes the decisive engagement.",
             "stories": [
                {"title": "The Largest Army the World Had Ever Seen",
                 "content": """By the ninety-third year of the Second Age, the Pervin rebellion had become something much larger and much uglier. It had become the Second Age War, a continental conflict that dragged in every major power in Fondore and several that had no business being involved.

On one side: the Pervins, fighting for their homeland. The Geckish city-states, fighting because they hated Cynthia. And the Kingdom of Vera, fighting because Sokotros XI had been promised Cynthian islands in exchange for his fleet, and Veran kings never turned down free territory.

On the other: Cynthia, fighting to keep its empire. Raxone, fighting because a Raxonian colonel had been killed and national honor demanded blood. And Mural Cere, fighting because Cynthia asked and Mural Cere needed Cynthian trade routes to survive.

Sans Liedech commanded the rebel alliance with the help of his Geckish advisor Kevus Embrum, and when all forces were rallied, the combined army numbered nearly one hundred and fifteen thousand soldiers. It was the largest organized military force the world had ever seen, and assembling it required a diplomatic skill that Sans had not possessed a decade earlier and had learned entirely through necessity.

The war was fought across the width of Fondore. The Verans island-hopped through western Cynthia, seizing coastal fortifications and cutting trade routes. The Gecks pushed north through Mural Cere, fighting the Cereyst militias who defended the desert with the fanaticism of men who believed their homeland was holy ground. The Pervins drove south and east into the Cynthian heartland, burning manors and freeing serfs.

The Cynthian-Raxonian alliance fought back with discipline and resources, but they were fighting on too many fronts. Raxone's soldiers were professionals, but they were far from home and fighting in terrain they didn't understand. Cynthia's army was large, but it was filled with conscripts who had been dragged from their farms and had no particular desire to die for a queen who had dismissed the entire conflict as a farming dispute.

The war stalemated for years. Supply lines stretched. Treasuries emptied. Young men who had enlisted with patriotic fervor found themselves sitting in trenches watching their friends die of dysentery and wondering what, exactly, they were fighting for. Klae collected soldiers' letters from every side of the conflict, and the most common theme was not hatred of the enemy but exhaustion with the war itself."""},

                {"title": "The Battle of Yoen",
                 "content": """The Battle of Yoen was not the largest battle of the Second Age War. It was not the longest. It was not even the bloodiest. But it was the one that mattered, because it was the battle that broke Cynthia's will to continue.

Sans Liedech and his Pervin forces had been maneuvering for months, trying to force a decisive engagement with the Cynthian main army. General Tehan Tan, Cynthia's most capable commander, had been avoiding exactly this, preferring to fight a war of attrition that favored Cynthia's larger population and deeper treasury. But political pressure from Queen Liasal demanded results, and Tan was ordered to crush the rebellion before the next harvest season.

Tan marched seven thousand men to the town of Yoen, a crossroads settlement in the Pervin hills. Sans was waiting for him with twelve thousand, positioned on the high ground above the town. The terrain favored the defenders absolutely, which is why Sans had chosen it, and which is why Tan should have refused to attack. He did not refuse, because refusing would have meant returning to the queen empty-handed, and Cynthian generals who disappointed the queen tended to find themselves reassigned to very distant islands.

The battle lasted two days. Tan's soldiers charged uphill into prepared positions, were repulsed, regrouped, and charged again. The Pervins held every line. By the second evening, Tan's army had been reduced by half and the survivors were retreating in disorder. Tan himself was captured. Sans treated him with the courtesy that Pervin culture demanded — fed him, housed him, and sent him back to the queen with a message that Klae recorded: 'Tell her the farmers are not going back to their farms.'

The armistice was signed within months. The terms gave the Pervins all their old territory plus Eastern Ansal and the Paronis Hills. Gecha gained northern Mural Cere. Vera took three Cynthian islands. Cynthia lost territory, prestige, and the illusion that the Pervins were a temporary problem.

Epervinay was free. It would not stay free forever — the nation's geographic position between larger and more aggressive neighbors virtually guaranteed future invasions — but the independence won at Yoen was real, and it was won by a farmer's son who had watched his boy die in the mud and decided that no one else's boy would die for the same reason.

The Second Age War was over. The map of Fondore had been redrawn. And in Ryad's Landing, the lantern post where Sans had hung the Cynthian governor still stood, and would stand for centuries, maintained by the city as a monument to the day the Pervins stopped asking for permission."""}
            ]},

            {"number": 7, "name": "Seventh Century",
             "description": "The Mark of Tzun. While Fondore recovers from the Second Age War, the continent of Tzun explodes into violence. King Bomahj of the Tzunadaine receives a vision from the god Jaga and launches a war of unification against the Pridekin and the Gezedaine. The resulting conquest is one of the most brutal campaigns of the age.",
             "stories": [
                {"title": "The Vision of Bomahj",
                 "content": """King Bomahj of the Tzunadaine was not, by most accounts, a visionary man. He was a competent ruler of a middling kingdom on a continent that the rest of the world had largely forgotten about, and he had spent most of his reign dealing with the kind of problems that middling kings deal with: rebellions, tax shortfalls, a son who got himself assassinated, and a holy man who ate a poisonous snake in protest and died, which was somehow Bomahj's fault.

Then Jaga spoke to him.

Jaga was one of the gods of Ezgo, the traditional Tzunadaine religion that had survived the underground spread of Ceresy. Bomahj claimed that Jaga appeared to him in a vision and showed him a united Tzun: Tzunadaine, Pridekin, and Gezedaine under one banner, the banner of Middle Tzun. Whether this vision was genuine divine revelation, a convenient hallucination, or a calculated political fiction is impossible to determine and ultimately irrelevant. What matters is what Bomahj did with it.

He called in his generals. He raised a massive army. He annulled every existing treaty with the Pridelands and the Gezedaine territories. And then, under cover of night, he declared war on both.

The campaign that followed was a masterwork of military planning applied to horrific ends. Bomahj's armies had superior technology — bronze weapons, organized formations, siege equipment — and they rolled across the Pridelands with devastating speed. General Jakoujhi led the first army into the Pridekin heartland of Yaarga Atpur and immediately began the systematic destruction of Pridekin society. Females and cubs were enslaved. Males were slaughtered. Head Pridestalker Nir Shallowbreath was captured, scalped atop Mount Rii, and displayed as a trophy.

The Gezedaine fared no better. Despite their enormous physical advantage, the giants had never developed the organizational capacity to resist a coordinated military assault. They fought individually, as they always had, and were picked apart by Tzunadaine formations that had been specifically designed to exploit that weakness.

The brutality was noted across the Asafin. A Ghenyarian diplomat named Rentha Dymokolo from the city-state of Vealus witnessed the atrocities firsthand and barely escaped back to Fondore to report them. His account prompted Minister Aranyth Lapheli of Vealus to embargo Middle Tzun, a decision that Bomahj interpreted as an act of war and responded to by invading Vealus.

Klae wrote of Bomahj: 'He was a man who heard what he wanted to hear, and what he wanted to hear was that everything belonged to him.'"""},

                {"title": "The Scalping of Shallowbreath",
                 "content": """Head Pridestalker Nir Shallowbreath was one hundred and twelve years old when they captured him, which for a Pridekin is the prime of middle age. He had been the leader of his people for decades, a position earned not through inheritance or election but through the simple and violent mechanism of being the best hunter alive. No Pridekin had challenged his status in forty years, because no Pridekin thought they would survive the attempt.

Bomahj's soldiers captured him at the Fall of Yaarga Atpur. The Pridekin capital — if a collection of communal dens and hunting grounds could be called a capital — was overrun in a single day. The Pridekin were magnificent individual fighters but had never developed the concept of organized defense, because their society was built around the hunt, and the hunt does not involve holding territory. They were ambush predators in an open-field battle, and the result was predictable.

Nir Shallowbreath fought until he couldn't. The accounts say he killed seventeen Tzunadaine soldiers before they brought him down, though Pridekin oral traditions put the number considerably higher and Tzunadaine records put it lower. He was brought before Jakoujhi in chains. The general, operating under Bomahj's explicit orders to make examples of Pridekin leadership, had Shallowbreath dragged to the summit of Mount Rii and scalped alive.

The scalping was not simply torture. It was a calculated act of cultural desecration. Pridekin manes — the thick fur around their heads and necks — were considered sacred, the physical manifestation of a hunter's pride and honor. Removing it was, in Pridekin terms, the destruction of the soul. Shallowbreath died on the mountain. His mane was sent to Bomahj as a trophy and reportedly hung in the royal palace for the rest of the king's reign.

The Pridekin did not recover from the Mark of Tzun for centuries. Their population was decimated, their social structures destroyed, their hunting grounds occupied. Some fled to the deep savannahs where the Tzunadaine couldn't follow. Others were enslaved. A few, the very toughest, disappeared into the wilderness and became legends — lone Pridekin who haunted the edges of Tzunadaine settlements, hunting the hunters.

Klae interviewed descendants of Mark of Tzun survivors during his research in Tzun and found a consistent refrain: 'We do not forget. We are not built to forget.' The Pridekin brain, which lacks the capacity for empathetic thought, also lacks the capacity for forgiveness. What was done to them is stored without the softening lens of time, and every Pridekin alive carries it the same way their ancestors did: raw, exact, and waiting."""}
            ]},

            {"number": 8, "name": "Eighth Century",
             "description": "Raxone Ascendant. The Kingdom of Raxone, having recovered from the Winter Wars and the chaos of the Second Age War, enters a period of expansion and cultural development. Raxonian explorers push deeper into the Northern Wastes, Raxonian mercenaries serve in every army on Fondore, and the Princes of Rax begin the internal power struggles that will define Northern politics for centuries.",
             "stories": [
                {"title": "The Princes of Rax",
                 "content": """Raxone's monarchy had a problem that no other kingdom in Fondore shared: it was too big and too cold for a single king to control.

The kingdom stretched from the Leimbordur in the south to the frozen wastes in the north, hundreds of miles of taiga, forest, tundra, and the occasional settlement that had been built more out of stubbornness than strategic planning. A king in Raxona could issue a decree in the morning and it would reach the frontier in, optimistically, several weeks, by which time the frontier would have already solved the problem itself, usually with axes.

The solution, developed over the course of the middle Second Age, was the Princes of Rax: regional governors drawn from the old noble families who ruled their territories with near-total autonomy. The king in Raxona handled foreign affairs, collected a percentage of taxes that everyone agreed to and nobody fully paid, and maintained the Grand Raxonian Army. The princes handled everything else. They built roads, administered justice, raised local militias, and — inevitably, predictably, constantly — fought each other.

The princely feuds of Raxone became legendary throughout Fondore. They were fought over territory, over trade routes, over insults real and imagined, over a particularly good hunting dog that one prince claimed had been stolen by another. They were fought with professional soldiers, hired mercenaries, personal retinues, and in at least one documented case, a prince's mother-in-law, who besieged a rival's castle with her household staff and a profound sense of grievance.

The king tolerated this, partly because suppressing the princes would have required a military campaign against his own nobility and partly because the feuds served a useful purpose: they kept the princes too busy fighting each other to challenge the throne. It was a system built on controlled chaos, and it worked exactly as well as that sounds.

Raxonian mercenaries, products of this perpetually martial culture, became the most sought-after soldiers-for-hire in Fondore. A Raxonian sword-for-rent could be found in virtually every army on the continent, and the peculiar situation of Raxonians fighting Raxonians in someone else's war became so common that it barely merited comment. The taverns of Raxone — ubiquitous, rowdy, and considered the kingdom's most important cultural institution — were full of veterans who had served on opposite sides of the same battle and now drank together without apparent irony.

Klae, who spent three years researching in Raxone and developed a deep fondness for the people, wrote: 'The Raxonians have solved the fundamental problem of civilization, which is what to do with violent men. They let them fight each other, then they let them drink together, then they let them fight again. It is not elegant, but it has kept the kingdom intact for longer than most empires.'"""},

                {"title": "The Tavern at Esterhai",
                 "content": """This story has no great battle, no political upheaval, no world-changing event. It is a story about a tavern, and Klae included it because he believed that history is not only made on battlefields but in the places where ordinary people live.

The Tavern at Esterhai sat on a crossroads between the princely territories of eastern and western Raxone, in a town that existed primarily because travelers needed somewhere to sleep between one place that mattered and another place that mattered. The tavern was called the Frosted Shield, though the sign had been repainted so many times that the shield looked more like a lopsided egg. It was owned by a woman named Hilsa Maraxa, who had inherited it from her father, who had won it in a card game from a man who had built it with money stolen from a prince's tax collector.

Hilsa served ale, stew, and a type of fermented berry wine that the locals called Kript and that visitors called undrinkable. She also served as an informal court of arbitration for the surrounding district. Farmers with border disputes, merchants with contract disagreements, husbands and wives with grievances that had been accumulating for decades — they all came to Hilsa's tavern, and Hilsa settled their problems with a combination of common sense, forceful personality, and the implicit threat that anyone who caused trouble in her establishment would be removed by her two enormous sons.

The tavern also served as a hiring hall for mercenaries. Princes sent agents to Esterhai to recruit soldiers, and the tavern's back room was where contracts were signed, payments exchanged, and oaths sworn over cups of Kript. The mercenary culture of Raxone was, in this sense, deeply personal. A man did not join an army. He sat in a tavern, shook hands with someone who looked trustworthy, and hoped for the best.

Klae spent a week at the Frosted Shield during his research and recorded conversations with seventeen different patrons. A retired mercenary who had fought in six different wars for five different princes and couldn't remember which side he'd been on in most of them. A farmer who had walked forty miles to ask Hilsa whether he should sell his pigs or his goats. A young woman who was leaving for Raxona to become a singer and had stopped for one last bowl of stew before her old life ended and her new one began.

None of these people would appear in any other history. But Klae believed, and wrote, that the tavern at Esterhai was as important to understanding Raxone as any battle or treaty, because it was where the kingdom actually happened. Not in the palaces of the princes or the halls of the king, but in a room that smelled like stew and Kript, where a woman with strong opinions kept the peace better than any army."""}
            ]},

            {"number": 9, "name": "Ninth Century",
             "description": "Faiths and Frontiers. Ceresy, now the dominant religion across Fondore, begins to fracture along national lines. The Raxonians develop their own interpretation — Rundelian Ceresy — which emphasizes communal worship and rejects the centralized authority of the High Cere in Mural Cere. Meanwhile, on the frontiers of the known world, explorers begin to wonder what lies beyond the horizon.",
             "stories": [
                {"title": "The Rundelian Heresy",
                 "content": """The trouble with a universal religion is that it cannot stay universal for long. Ceresy had been adopted by every major nation in Fondore, but each nation had adopted it in its own image, and the images were starting to look very different from each other.

The Geckish practiced a highly organized, institutional Ceresy with hierarchies, tax exemptions, and a bureaucratic apparatus that would have impressed a government minister. The Leimish practiced a beautiful, artistic Ceresy of illuminated manuscripts and soaring cathedrals and monks who spent decades on a single page of calligraphy. The Pervins practiced a quiet, personal Ceresy of farmhouse prayers and community meals. And the Raxonians practiced a Ceresy that involved large groups of people singing very loudly in the snow.

This last version became known as Rundelian Ceresy, named after the monk Rundel who codified its principles in the early centuries of the age. Rundel's central argument was simple: Illiman had been a wanderer, not a bureaucrat. He had never built a temple, never established a hierarchy, never appointed a High Cere to speak on his behalf. The elaborate religious infrastructure that had grown up around Ceresy — the temples, the priests, the collection plates — was, in Rundel's view, a betrayal of Illiman's original message of simplicity and direct communion with the divine.

The High Cere in Mural Cere disagreed, vehemently. The Cereyst hierarchy had spent centuries building its power and was not inclined to accept criticism from a Northern monk who thought the correct form of worship involved standing in a field and yelling. The theological dispute was genuine, but the political dimensions were enormous: if every nation could interpret Ceresy however it pleased, the centralized religious authority that Mural Cere had been accumulating for centuries would evaporate.

The dispute did not immediately produce war, but it produced something that would eventually be worse: permanent division. The nations of Fondore aligned themselves along doctrinal lines that just happened to correspond perfectly to their political alliances. Raxone, Lambridge, and Epervinay leaned Rundelian. Gecha and Cynthia remained Orthodox. Mural Cere, naturally, insisted that only its version was correct and everyone else was going to whatever the Cereyst equivalent of hell was.

Klae, who was not a religious man and found doctrinal disputes tedious, nonetheless recognized their importance. He wrote: 'Men will die for an idea more readily than they will die for a piece of land, because a piece of land can be divided but an idea cannot. The Rundelian split proved that Ceresy was strong enough to survive being believed in two different ways. Whether Fondore was strong enough to survive the same thing remained to be seen.'"""},

                {"title": "The Edge of the Map",
                 "content": """Sometime in the late Second Age — the exact date is disputed — a Geckish cartographer named Penelue Alyva Jayvlunnus was commissioned to produce the most complete map of the known world ever drawn. The result, which Klae examined in the archives of Jayvlun, was a masterpiece of draftsmanship: Fondore in precise detail, the Avadacaster strait, the northern coast of Tzun, the Schvaine islands, fragments of the Silcrian ocean with Ulceron marked by a series of speculative dotted lines.

The map's most interesting feature was its edges. To the west, where the Erezetta ocean stretched to an unknown horizon, Penelue had written in her careful script: 'Here be what we do not know.' To the east, past the Asafin sea: 'Here be what we have not reached.' To the south, past Tzun: 'Here be what we fear.' And to the north, past Raxone: 'Here be what doesn't want to be found.'

Penelue's map was not meant as an invitation. It was meant as a record of the limits of Geckish knowledge, and she was a careful enough scholar to mark those limits honestly. But maps have a way of provoking the very expeditions they were meant to make unnecessary. Looking at Penelue's edges, with their tantalizing confessions of ignorance, every ambitious captain and restless prince in Fondore saw the same thing: a blank space that could be filled with their name.

Small expeditions had been launched before, of course. Fishing boats blown off course had reported distant shorelines. Traders following the coast had pushed further than their predecessors. Raxonian hunters in the Northern Wastes had encountered settlements of Wintermen and returned with stories of giants and ice goblins that their countrymen believed about as much as they believed the wolf creature stories.

But the Second Age lacked the shipbuilding technology for true deep-ocean navigation. The vessels that existed could hug coastlines and island-hop across narrow straits, but the open ocean — weeks of sailing with no land in sight — was beyond them. Penelue's blank edges would remain blank for another age.

When the ships finally came, they would change everything. The people living beyond the edges of Penelue's map — the Lirzans, the Karagonians, the Wintermen of Perut, the Hiyalmites behind their Styrmwall — had no idea they were about to be found. Some would welcome the contact. Most would not. And the map itself, with its honest admissions of ignorance, would be replaced by maps that were confident and comprehensive and wrong about almost everything that mattered.

Klae kept a copy of Penelue's map in his study at Hejem University. He said it was his favorite historical document, because it was the only map he had ever seen that told the truth."""}
            ]},

            {"number": 10, "name": "Tenth Century",
             "description": "The Closing of the Second Age. Fondore settles into an uneasy peace. Seven distinct kingdoms of men have crystallized on the continent: Gechann, Lambridge, Epervinay, Hyacinth (still under old Cynthian rule), Mural Cere, Waydren, and Raxone. The Debrears simmer in their heartland. The stage is set for the age of exploration.",
             "stories": [
                {"title": "Seven Kingdoms",
                 "content": """By the end of the Second Age, Fondore had settled into a configuration that would have been recognizable to anyone who looked at a map a thousand years later. The seven kingdoms of men — the phrase itself was coined by a Cynthian poet whose name has been lost — occupied their territories with the stubbornness of tenants who had nowhere else to go.

The Gechann dominated the southeastern plains: proud, mercantile, aggressive, organized into city-states under an elected Supremus who was theoretically a democrat and practically a dictator. Their plains were unforgiving but their cities were wealthy, linked by roads and trade routes that made the Geckish economy the strongest in Fondore. Boulavar was rising as the dominant city, though Suntrae still controlled the richest harbors.

Lambridge sat behind its mountains, protected by the Leimbordur and by the memory of what happened when the Debrears came through it. The Clairdwells ruled from Clarity, the most beautiful city in the world, and the Knights of Lambridge kept the passes guarded. The Leimish were artists, musicians, diplomats — and they were terrified, because they knew that mountains only stop armies that don't want to cross them badly enough.

Epervinay held its hard-won territory in the southwestern hills, perpetually squeezed between Cynthia to the west and Gecha to the east. The Pervins farmed, trained, and waited. They were very good at waiting.

Cynthia still controlled the western peninsula and its archipelago, but the loss of the Pervin territories had weakened the kingdom. The court at Oradova maintained its reputation for culture and philosophy, but the military that had once dominated Fondore was stretched thin and tired.

Mural Cere was holy and poor, its desert towns sustained by pilgrim traffic and the political leverage of being Illiman's birthplace. Waydren was tiny, ancient, and had been conquered so many times that its people had developed survival into an art form. And Raxone sprawled across the entire north, enormous and chaotic and held together by the Princes of Rax and the shared conviction that drinking was more important than governance.

This was Fondore at the end of the Second Age. Seven kingdoms, seven cultures, seven armies, and one religion that they all interpreted differently. The continent was a powder keg, and it knew it. But the fuse, when it came, would not be lit on Fondore. It would be lit on the ocean, by a ship sailing west toward a horizon that nobody had crossed, carrying men who had no idea what they were about to find.

The Second Age ended as the First had: with the world on the brink of something enormous, and nobody looking in the right direction."""},

                {"title": "A Letter Never Sent",
                 "content": """Klae found this letter in a private collection in Clarity. It was written by an unnamed Leimish soldier, sometime in the final years of the Second Age, and it was never sent. The intended recipient is unknown.

The letter reads:

'I have been thinking about what you said, about whether any of it mattered. The siege, the war, the years we spent in the cold. Whether Sans was right. Whether the Clairdwells deserve the crown. Whether Ceresy is true or just a story we tell ourselves because the alternative is worse.

I don't have answers. I'm a soldier. Soldiers are the last people who should be asked whether wars are worth it, because we have too much invested in the answer being yes.

But I will tell you what I know. I know that Clarity still stands. I know that the Leimbordur still holds. I know that my daughter was born free, in a free city, in a kingdom that was bought with blood I helped to pay. Whether that makes it worth it depends on who you ask, I suppose. Ask my daughter and she will say yes. Ask the men I buried and they cannot answer, which is the whole problem with asking the dead to justify the living.

The world is bigger than we think. Traders come through Clarity now with stories of lands past the horizon, of creatures and peoples we have never imagined. I think the next age will be different from this one. I think the ships will sail, and the edges of the map will fill in, and we will discover that we are not alone in this world and never were.

I hope we are kinder to whoever we find than we have been to each other. I doubt it. But I hope.'

Klae published this letter without commentary. He felt, and Klae was usually right about such things, that the soldier had said everything that needed to be said."""}
            ]}
        ]
    },
    {
        "number": 3,
        "name": "The Era of Sail",
        "year_start": 1001,
        "year_end": 1500,
        "description": """The winds were blowing west and the men of Fondore could not withstand the call. All across the continent, seaside nations were becoming maritime with the first operable deepwater ships being constructed by the great Leimish engineer Raist Celle on the coast of the Ardent. Nations were truly forming now and Fondore was being carved into what would become the seven kingdoms of men, but for now were still confederations of houses and clans jostling for position.

Mercantile ships left the ports of Clarity, Rin Nohara, Erogan, Hypolta, and Suntrae. They were led by patriotic adventurers, curious explorers, and greedy thieves alike, all looking for a piece of the unknown to carve out for themselves. A Leimish ship under command of Emmantine Jlain made port on the misty isles of Erezetta. Pervin vessels found themselves washed onto the dark rocky beaches of Metzerul. Within time, these seekers of fortune would discover that their marked lands were not so uninhabited as originally believed, either to great delight or brutal horror. Karagonians, Lirzans, Pkoyte, mysterious newcomers with pointed ears who called themselves Cynthian — all manner of peoples came to meet the explorers in either diplomacy or battle.

But when one ship was staved off or burned, her sailors run off or slain, ten more would appear upon the horizon. The era of sail was in full swing and the genie had exited the bottle. The world, which had seemed so large when Penelue drew her map, was about to get very small very quickly.""",
        "centuries": [
            {"number": 1, "name": "First Century",
             "description": "The First Ships. The Leimish engineer Raist Celle constructs the first true deepwater vessel on the Ardent coast, capable of surviving the open ocean. Within a decade, every maritime nation in Fondore is building ships. The edges of Penelue's map begin to fill in.",
             "stories": [
                {"title": "Raist Celle's Folly",
                 "content": """Everyone told Raist Celle he was going to drown.

The Leimish engineer had been obsessed with shipbuilding since childhood, which in Lambridge was considered an eccentric hobby, like collecting beetles or talking to horses. The Leimish were a land people. Their ships, such as they were, hugged the coastline and fell apart in bad weather. The ocean was something you looked at from the cliffs of Rin Nohara, not something you sailed across.

Celle disagreed. He had studied the coastal vessels used by fishermen and traders, identified their weaknesses — flat bottoms that rolled in swells, single masts that couldn't catch a crosswind, hulls built from green wood that warped in salt water — and spent fifteen years developing solutions to each. His workshop on the Ardent coast became a monument to obsession: scale models of hulls, drawings of sail configurations, calculations of displacement and ballast that nobody else in the kingdom could follow.

The first deepwater ship launched from the Ardent in the early years of the Third Age. It had a keeled hull for stability, multiple masts with adjustable rigging, sealed decking, and a cargo hold large enough to carry supplies for weeks at sea. The Leimish court sent a delegation to watch the launch, expecting a spectacle of failure. The ship sailed out past the breakwater, past the coastal shelf, and into the open ocean. It stayed there for three weeks, then returned.

Raist Celle had not discovered the open ocean. He had made it survivable.

Within a decade, every maritime nation in Fondore had either purchased, stolen, or reverse-engineered Celle's designs. The Geckish, characteristically, improved the hull construction. The Arden shipwrights on the Erezetta coast — already the most experienced sailors in the Leimlands — refined the rigging. The Waydrani, whose fishermen had been risking their lives on the Avadacaster strait for generations, adapted the design for speed.

The ocean, which had been a barrier, became a highway. And highways, as Klae observed, do not care what travels on them. The same ships that carried explorers and diplomats would soon carry soldiers and slavers. Raist Celle built his ship to expand human knowledge. The world used it to expand human greed. He reportedly found this development unsurprising but disappointing, which is the most Leimish reaction imaginable."""},

                {"title": "The First Horizon",
                 "content": """The first true ocean voyage from Fondore was not a grand expedition. It was an accident.

A Leimish merchant vessel under the command of Emmantine Jlain was sailing from Rin Nohara to the Schvaine islands when a storm blew it far off course into the open Erezetta. For three days, Jlain's crew fought to keep the ship afloat in waters that no Fondorian had ever sailed. When the storm cleared, they had no idea where they were. The coastline was gone. In every direction, there was only water.

Jlain, who kept a log that Klae later recovered from the Clairdwell Archives, recorded his first impression of the open ocean: 'It is very large, and we are very small, and I have made a terrible mistake.' He ordered the ship to sail west, reasoning that any direction was better than no direction, and after four more days they sighted land.

The land was one of the outer Erezetta islands — a volcanic speck that did not appear on any map, inhabited by seabirds and a species of crab that Jlain described as 'hostile.' They did not stay long. But Jlain marked the island's position by the stars, replenished their water supply from a freshwater spring, and sailed back to Fondore with proof that there was something out there.

The Erezetta islands, as they came to be called, were not the goal. They were stepping stones. Each expedition went a little further, charting another island, another reef, another deepwater channel. Pervin fishing boats, tougher than they looked, pushed south into the Avadacaster and reported volcanic landmasses in the distance. Geckish merchant vessels probed the northern coast, trading with the Raxonians and hearing their stories of Wintermen and ice goblins in the far north.

The world was opening up. The blank edges of Penelue's map were being filled in, one voyage at a time, by men who were either very brave or very lost. Most were both. The distinction between exploration and desperation is thinner than historians like to admit.

Klae recorded a saying that was common among sailors of the early Third Age: 'The horizon is a liar. It promises you the edge of the world, and when you get there, it moves.' The saying was meant as a warning. It was taken as an invitation."""}
            ]},

            {"number": 2, "name": "Second Century",
             "description": "The Strangers from the Sea. Tall, sharp-featured people with pointed ears arrive on the shores of the Cynthian peninsula in ships of unfamiliar design. They call themselves Cynthians and claim to come from a land not recorded in any history. Their arrival transforms the western peninsula and begins one of the most enduring mysteries of Elysal.",
             "stories": [
                {"title": "The Arrival of the Pointed Ears",
                 "content": """They came from the west, which was the direction that nobody was looking.

While Fondorian explorers were pushing outward in every direction, charting islands and filling maps, a fleet of ships appeared on the western coast of the peninsula that would come to bear their name. The ships were unlike anything in Fondore: sleek, elegant, with hulls shaped from a pale wood that no local carpenter could identify and sails that caught wind at angles that should not have worked.

The people who stepped ashore were tall, sharp-featured, and possessed of ears that came to a noticeable point. They were beautiful in a way that made the local Pervin inhabitants uncomfortable, the kind of beauty that felt like it was making a point. They spoke a language that bore no relation to any Fondorian tongue, though they learned Common Speak with unnerving speed, as if language itself was simply a tool they could pick up and put down at will.

They called themselves Cynthians, which caused immediate confusion, because Cynthia already existed as a nation in central Fondore — the old human civilization that had occupied the Pasav region since the First Age. The newcomers seemed unconcerned by this. They claimed their name predated any human use of it, which was a bold assertion from people who had just shown up.

Where they came from is unknown. Their own histories, which they shared sparingly, referenced a homeland across the sea that they had left for reasons they declined to specify. Klae, who interrogated every available source during his research, could not determine their origin. He wrote, with visible frustration: 'They know where they came from. They choose not to say. I have learned to recognize the difference between a people who have forgotten their past and a people who are keeping it secret. The Cynthians are keeping it secret.'

The Pervins of the western peninsula — hardworking hill people who had been farming the land since the Second Age — reacted to the newcomers with the wariness that Pervins bring to everything: watching, waiting, saying little. The Cynthians, for their part, did not invade. They settled. They built. They traded. They intermingled with the local population. And within a few generations, they had transformed the peninsula from a collection of Pervin farming communities into something else entirely.

The old Cynthian nation in central Fondore protested the use of the name but could do nothing about it. The newcomers were too numerous, too established, and too indifferent to complaints. The peninsula became Hyacinth. The newcomers became the ruling class. And the Pervins, who had been there first, discovered what it felt like to be a guest in their own home."""},

                {"title": "Oradova Reborn",
                 "content": """The city of Oradova had existed before the Cynthians arrived. It was a Pervin settlement, modest and functional, built on a natural harbor on the peninsula's western coast. It had stone houses, a marketplace, a temple to Illiman, and the kind of quiet, weathered dignity that characterizes places where people have been living for a long time without anyone asking them to be impressive.

The Cynthians looked at Oradova and decided it was not enough.

Within decades of their arrival, the city was unrecognizable. The Cynthians had a gift for architecture that bordered on the supernatural — arches that seemed to defy gravity, towers that caught the light at precise angles, public squares designed so that the acoustics of a conversation on one side could be heard perfectly on the other. They built a harbor that could accommodate their elegant ships and Fondorian merchant vessels alike. They built libraries, academies, concert halls.

They also built homes for the Pervins. This detail is often omitted from Cynthian historical accounts, but Klae found it in Pervin oral traditions: the newcomers did not simply take the city. They expanded it, and they included the original inhabitants in the expansion. Pervin neighborhoods were not demolished. They were incorporated, surrounded by Cynthian architecture that was grander but that left the original structures intact, like a jeweler setting a rough stone in an elaborate frame.

This was both generous and patronizing, and the Pervins recognized it as such. They were not displaced. They were diminished. Their city was still there, but it was no longer theirs. It belonged to the Cynthians now, and the Pervins were residents in someone else's masterpiece.

The relationship between the Cynthians and the Pervins of Hyacinth would become one of the defining tensions of Fondorian history. The Cynthians were not humans — not entirely. Their pointed ears, their preternatural grace, their unsettling intelligence suggested something else, something that scholars would debate for millennia. Part elf, some said. Descendants of the fey, others claimed. The Cynthians themselves said nothing, which only made the speculation worse.

What was clear was that they considered themselves superior to the Pervins, and they expressed this superiority not through violence but through condescension. The Pervins were welcomed in Cynthian society the way a child is welcomed at an adult dinner: tolerated, patronized, and expected to be grateful for the invitation.

Klae spent considerable time in Oradova and found the city breathtaking. He also found it sad, in the particular way that a beautiful thing built on an ugly foundation is sad. He wrote: 'Oradova is a monument to what the Cynthians could create. It is also a monument to what they could not see: that the people they built it on top of had built something there first.'"""}
            ]},

            {"number": 3, "name": "Third Century",
             "description": "The Kingdom of Hyacinth. The Cynthian newcomers consolidate their hold on the western peninsula and formally establish the Kingdom of Hyacinth. The Pervins within Hyacinth's borders are absorbed as a lower class. Meanwhile, the Kingdom of Lambridge grows in strength behind the Leimbordur, and the Arden coast becomes a hub of maritime innovation.",
             "stories": [
                {"title": "King Lomei's Crown",
                 "content": """The establishment of the Kingdom of Hyacinth was, depending on whom you asked, either the natural elevation of a superior civilization or the formal subjugation of a free people. Both descriptions are accurate. They describe the same event from different sides of the same wall.

King Lomei was the first to take the title, uniting the various Cynthian settlements on the peninsula under a single crown. He was, by all accounts, brilliant — a diplomat, a patron of the arts, a military strategist who had studied the wars of Fondore and learned from every one of them. He built Hyacinth into a paradise, if you were Cynthian. If you were Pervin, he built it into a cage.

The Pervins within Hyacinth's borders were not enslaved. This is an important distinction, and a meaningful one, and also a convenient one for the Cynthians who made it. The Pervins could own property, in theory. They could practice Ceresy, within limits. They could hold certain occupations, mostly the ones that the Cynthians found beneath them. What they could not do was govern, command, judge, or in any way exercise authority over a Cynthian. They were citizens of a kingdom that was not for them.

The Pervin folk traditions — their music, their stories, their ways of marking births and deaths and the turning of seasons — were not outlawed. They were simply ignored, which is worse, because an outlaw is at least acknowledged as a threat. The Cynthians had their own culture, ancient and refined and beautiful, and it filled every public space until the Pervin traditions retreated into farmhouses and back rooms, practiced in whispers.

Lomei knew what he was doing. He was too intelligent not to. But he believed, with the total conviction of a man who has never been wrong, that Cynthian civilization was better, and that the Pervins would eventually recognize this and be grateful. He was wrong about the gratitude. He was not entirely wrong about the civilization. Hyacinth under Lomei produced philosophy, music, architecture, and scientific thought that enriched all of Fondore. The cost was paid by people who were never asked if they wanted to pay it.

Klae, who conducted interviews in both Cynthian palaces and Pervin farmhouses during his research in Hyacinth, found the same story told in two completely different ways. In the palaces, Lomei was a visionary. In the farmhouses, he was a thief. Both were right. History does not require consistency."""},

                {"title": "The Ardent Shipwrights",
                 "content": """While kingdoms rose and fell and argued about who owned which piece of dirt, the people of the Ardent coast were building boats.

The Ardent was a stretch of the Leimish coastline facing the Erezetta Ocean, technically part of Lambridge but in practice a world unto itself. The people there were Leimish in language and culture but independent in temperament, more interested in what was across the water than in who sat on the throne behind them. They had been seafarers since the First Age, and when Raist Celle's deepwater designs arrived, they adopted them with the enthusiasm of people who had been waiting their entire lives for someone to solve the hull problem.

The Ardent shipwrights did more than copy. They innovated. They developed the lateen sail, which could catch wind from multiple angles and allowed ships to tack against headwinds that would have stopped earlier vessels. They experimented with hull coatings that resisted barnacles and bore-worms. They designed cargo holds that could keep grain dry and water fresh for weeks at sea. And they built an infrastructure of drydocks, chandleries, and navigation schools that made the Ardent the shipbuilding capital of Fondore.

The city of Rin Nohara, at the heart of the Ardent coast, became a boomtown. Merchants, sailors, mapmakers, rope-makers, sailmakers, and the various parasites that attach themselves to prosperity all converged on the city. The harbor was crowded with vessels from every nation in Fondore, and the dockside taverns were the most multilingual places in the world.

Out of this chaos, a political entity emerged. The Arden Trade Federations — a loose alliance of merchant houses, shipping companies, and port authorities — declared themselves an autonomous territory within Lambridge. They were not seeking independence, exactly. They were seeking the freedom to do business without a king telling them whom they could trade with. The Clairdwell dynasty, which needed the Arden's ships and the Arden's taxes, agreed to the arrangement with the resigned air of a parent who has lost an argument to a teenager.

The Arden Trade Federations would become one of the most influential political entities in Fondore, not because they had an army but because they had ships. In an age of sail, the people who controlled the ships controlled the world. The Ardenese understood this before anyone else, and they profited accordingly.

Klae called the Ardent shipwrights 'the midwives of the new age.' They did not build the world that was coming. They built the vehicles that carried everyone to it."""}
            ]},

            {"number": 4, "name": "Fourth Century",
             "description": "Beyond the Horizon. Fondorian ships cross the Erezetta Ocean and make contact with the island continent of Karagon, discovering a civilization built on the ruins of genocide. Meanwhile, Pervin and Leimish explorers probe the dark beaches of Metzerul and encounter the Lirzans for the first time.",
             "stories": [
                {"title": "The Discovery of Karagon",
                 "content": """The first Fondorian ship to reach Karagon was a Geckish merchant vessel captained by a man named Lyco Pervyc Suntraenus, though history remembers him simply as Lyco the Lucky. He was not, in fact, lucky. He was lost. A navigational error had sent his ship hundreds of miles off its intended course, and by the time his navigator admitted the mistake, they were in waters that no Fondorian chart had ever mapped.

They sighted Karagon at dawn. The island continent rose from the ocean like a dream, green and mountainous, with smoke from cooking fires visible along the coast. Lyco, who had been expecting to find empty ocean or, at best, a cluster of rocky islands, found himself staring at a harbor, a city, and a people who were already staring back.

The Karagonians met him on the beach. They were tiefling-featured — grey-skinned with sharp features and small horns, striking enough that Lyco's crew initially refused to disembark. The Karaf, as they called themselves, seemed unsurprised by the arrival of foreigners. They were wary, but not hostile. They traded. They talked, through gestures at first and then through the halting common vocabulary that develops between people who want to understand each other.

What Lyco did not learn until much later, through interpreters and years of subsequent contact, was the history behind the civilization he had found. The Karaf were the descendants of slaves — the same Karaf who had been enslaved by the Verans in the First Age, who had escaped on the Kola Tai, and who had been deposited on the island of Karto as children with instructions to survive. They had done more than survive. They had multiplied. They had built. And when the Verans eventually found them and tried to re-enslave them, the Karaf had risen up and destroyed the Veran civilization entirely. Every Veran on Karagon was dead. The Karaf had built their new nation on the bones of their former masters.

Lyco found this deeply unsettling, which was the correct response. The Karagonians had built something remarkable — a functioning society with laws, trade, and even attempts at democratic governance — but it was built on an act of total annihilation that the Karaf discussed with a matter-of-factness that chilled the Geckish sailors to their bones.

Klae, who visited Karagon during his research, described the national character as 'a people who had looked into the darkest part of the human soul and decided to build a country anyway.' The Karaf were free. They were also haunted by what freedom had cost them, and every institution they built was designed, consciously or unconsciously, to ensure that nobody — not the Karaf, not anyone — would ever be enslaved again."""},

                {"title": "Dark Beaches",
                 "content": """The first Fondorian contact with Metzerul was not a discovery. It was a shipwreck.

A Pervin fishing vessel, blown off course in a storm while navigating the northern Erezetta, was dashed against the rocky western coast of a landmass that was not on any chart. The crew — seven men and one woman who served as the ship's navigator — survived by clinging to wreckage and washing ashore on a beach of black volcanic sand. They were the first Fondorians to set foot on Metzerul.

What they found was a jungle so dense that the canopy blocked the sky. The air was thick with moisture and the sounds of creatures they could not identify. The beach was scattered with bones — animal bones, mostly, but some that looked disturbingly humanoid. And there were tracks in the sand, leading into the tree line, left by something that walked on two legs but was clearly not human.

The survivors made camp on the beach and waited for rescue that did not come. After three days, hunger forced them into the jungle. They followed a river inland, eating fruit they couldn't identify and hoping nothing was following them. On the second day in the jungle, they found a road. Not a path or a game trail but a road, paved with flat stones and wide enough for a cart.

The road led to a village, and the village was inhabited by lizardfolk.

The Lirzans — for that is what they were — reacted to the Fondorian survivors with curiosity rather than hostility. The local village was a modest outpost on the fringe of the vast Lirzan kingdom, and its inhabitants had never seen humans before. They examined the Fondorians with the same interest that a naturalist examines a new species of beetle, which was not entirely reassuring.

Communication was impossible at first. The Lirzan language, Sizzeracisenn, bore no relation to any human tongue, and the hissing consonants and glottal clicks were nearly impossible for human vocal cords to reproduce. But trade goods speak a universal language, and the Pervins had salvaged enough from their wreck to establish a rudimentary barter system.

Three of the seven survivors eventually made it back to Fondore, years later, on a Lirzan trading vessel that had begun to probe the Erezetta in the opposite direction. They brought with them stories of a continent larger than Fondore, inhabited by lizardfolk, dragonborn, dwarves, giants, and creatures that breathed fire. The stories were met with skepticism in the courts of Fondore and with enthusiasm in the taverns, which tells you everything about where truth goes to be believed.

Klae noted that the discovery of Metzerul was not really a discovery at all. The Lirzans had known about Fondore. The Wintermen of the northern wastes had been crossing the ice bridges for centuries. The only people who thought the world was unknown were the people who had never bothered to ask anyone else."""}
            ]},

            {"number": 5, "name": "Fifth Century",
             "description": "Holy Fire. The growing power of national churches threatens the unity of Ceresy. The High Cere in Mural Cere calls for a holy war to reassert religious authority over the wayward kingdoms. The First Holy War — Fondore's first true crusade — reshapes the political and spiritual landscape of the continent.",
             "stories": [
                {"title": "The Call of the High Cere",
                 "content": """The First Holy War was not about God. It was about power, dressed in vestments and carrying a censer.

By the middle centuries of the Third Age, the religious authority of Mural Cere had been eroding for decades. Rundelian Ceresy in the north, national churches in every kingdom that answered to their king before they answered to the High Cere, and a general sense among the laity that the desert monks had become more interested in collecting tithes than saving souls. The current High Cere — a politically astute man named Gloron Pav — decided that what Ceresy needed was a war. Not a doctrinal argument, not a theological council, not a strongly worded encyclical. A war. With swords.

The pretext was the Geckish occupation of northern Mural Cere, territory the Gechann had claimed during the Second Age War. The holy city of Ramal Cere, while not occupied, was uncomfortably close to Geckish military outposts, and the presence of Geckish tax collectors in historically Cereyst territory was, Gloron argued, an intolerable desecration.

The call went out to the kingdoms of Fondore: march south, free the holy lands, restore the authority of Mural Cere. The response was enthusiastic, which should have been the first warning sign. When kings and princes eagerly agree to fight for a religious cause, the cause is usually secondary to what they hope to gain from the fighting.

Lambridge sent knights — the descendants of Asaundier's order, resplendent in armor and conviction. Raxone sent mercenaries, because Raxone always sent mercenaries. Epervinay sent soldiers who were grateful for a war that pointed away from their own borders for once. Even Cynthia — the old Cynthia, not the newcomers on the peninsula — contributed troops, hoping to regain prestige lost in the Second Age War.

The Gechann, naturally, were the enemy. They had no intention of surrendering territory they had fought for, and the current Supremus, a hard man from Aemore named Gryzal Parthyc Boulvaranus, made it clear that any army marching south would be met with steel.

The First Holy War had begun. It was fought in the name of Illiman, a man who had spent his life preaching forgiveness. The irony, as Klae observed, was lost on everyone who had a sword in their hand."""},

                {"title": "The Siege of Ramal Cere",
                 "content": """The crusading army reached Ramal Cere after weeks of marching through the Pasav desert, which had a way of burning the romance out of holy war. Men who had left their homes in the green hills of Lambridge or the cool forests of Raxone found themselves in an oven of sand and rock that seemed to exist for the sole purpose of making human beings miserable. Water was rationed. Horses died. Knights in full plate armor cooked inside their shells like lobsters.

When they finally reached Ramal Cere, they found it defended not by the Gechann but by Mural Cereyns — desert fighters loyal to their own local chiefs rather than to the High Cere or anyone else. The politics of the Pasav were more complicated than the crusaders had been led to believe, and the local population's enthusiasm for being liberated was considerably less than advertised.

The siege lasted months. The crusaders camped outside the walls in the killing heat while the defenders waited inside with access to the city's wells and granaries. Dysentery killed more crusaders than the enemy did. Morale collapsed. The Leimish knights, who had brought their code of chivalry to the desert, discovered that chivalry does not function well when you are dehydrated, sunburned, and being shot at from walls you cannot climb.

The city fell, eventually, not through military brilliance but through a combination of starvation, treachery, and the kind of desperate final assault that happens when an army realizes it will die outside the walls if it doesn't die inside them. The sack of Ramal Cere was brutal. Crusaders who had marched for months in the name of Illiman's mercy showed none. The local population, Cereyst and otherwise, was subjected to three days of violence that Klae described in the barest possible terms, because more detail was unnecessary.

The High Cere declared victory. The holy lands were liberated. A crusader state was established in northern Mural Cere, garrisoned by soldiers from every crusading nation, theoretically governed by the Church but practically governed by whoever had the most men with swords.

The crusader state lasted less than a century. The Gechann retook the territory in a campaign so efficient that it barely qualified as a war. But the First Holy War's legacy was not territorial. It was psychological. It proved that Ceresy could be weaponized, that kings could use God as a justification for conquest, and that ordinary men would march across a desert and kill strangers if someone in a robe told them it was righteous.

Illiman, who had died on a road carrying nothing of value, would have recognized none of it as his."""}
            ]},

            {"number": 6, "name": "Sixth Century",
             "description": "Novus Gecharium. The Geckish city-states, emboldened by their defeat of the crusaders and enriched by trade, begin to expand beyond their traditional borders. The Supremus Leader declares a Novus Gecharium — a New Gecha — and the first stirrings of Geckish imperialism reshape the power dynamics of southern Fondore.",
             "stories": [
                {"title": "The Thirteen Families",
                 "content": """The Gechann had always been ambitious. They were Gecks; ambition was a cultural imperative, like mercantile cunning and an inability to admit they were wrong. But the ambition of the middle Third Age was different in kind from what had come before. It was organized.

The old elective monarchy of the Supremus Leader had evolved. The thirteen major city-states — each controlled by a dominant family — had formalized their relationship into something between a federation and a conspiracy. The Thirteen Families, as they were called, met annually to set trade policy, military strategy, and the price of olive oil, which in Gecha was considered equally important. The strongest family's patriarch was chosen as Supremus Leader, and his home city became the capital.

This system produced a peculiar form of government: competitive oligarchy. The families cooperated when it was profitable and competed when it was not, and the line between cooperation and competition shifted constantly. A Geckish merchant from Suntrae might be trading partners with a merchant from Aemore in the morning and sabotaging his shipping routes in the afternoon, and both would consider this normal business practice.

The declaration of Novus Gecharium — literally, the New Gecha — marked the moment when internal competition turned outward. The current Supremus, whose name has been preserved in seventeen different spellings none of which agree, announced that the Geckish city-states would no longer content themselves with their traditional territory. They would expand. They would build colonies. They would project Geckish power across Fondore and beyond.

The first targets were predictable: Waydren, which had been a Geckish dependency in all but name for centuries, was formally absorbed. Northern Mural Cere, retaken from the crusaders, was garrisoned permanently. Trade outposts were established on the Arden coast, in Tzun, and on several Erezetta islands.

The Novus Gecharium was not yet an empire. It was the blueprint for one. The actual empire — the Imperial Gechann that would dominate the Fourth Age — was still centuries away. But the foundations were being laid by merchants, soldiers, and bureaucrats who understood something that the other kingdoms of Fondore had not yet grasped: that power in the age of sail belonged not to the nation with the largest army but to the nation with the longest reach.

Klae described the Thirteen Families as 'the most efficient machine for generating wealth and misery that the world had yet produced.' He meant it as both criticism and grudging admiration."""},

                {"title": "The Waydrani Yoke",
                 "content": """Waydren had been conquered before. This was, in a sense, the defining characteristic of the nation: being conquered, enduring the conquest, and still being there when the conquerors left. The Waydrani were the oldest people in Fondore — direct descendants of the Ghenyarians, the first humans, the builders of Hipola — and they had been invaded, occupied, absorbed, and discarded by every major power on the continent at one point or another.

The Geckish absorption of Waydren during the Novus Gecharium was different from previous conquests because it did not feel like a conquest. There was no invasion, no siege, no dramatic military campaign. The Gechann simply tightened the economic and political screws that had been in place for decades until Waydren's nominal independence became a fiction that nobody bothered maintaining.

Geckish governors replaced Waydrani officials. Geckish tax codes replaced local law. Geckish was declared the language of commerce and government, pushing the ancient Ghenyarian tongue into homes and temples and the kind of underground preservation that oppressed cultures specialize in. The process was smooth, professional, and deeply humiliating.

What made the Waydrani case unique was the reaction: there was none. No rebellion, no resistance, no Sans Liedech figure rallying the population to throw off the yoke. The Waydrani had been through this too many times. They knew that resistance against Gecha — the most militarily powerful entity in southern Fondore — would result in casualties they could not afford in a population that was already small.

Instead, the Waydrani did what they had always done: they adapted. They learned Geckish. They entered Geckish institutions. They became advisors, administrators, translators, physicians, tutors to Geckish noble children. They made themselves indispensable, because a people who cannot fight for their survival must think for it instead.

The Geckish discovered, to their occasional discomfort, that the people they had conquered were smarter than they were. A Geckish proverb from this era captures the dynamic: 'A Waydrani will advise you to your face, profit from your back, and mourn at your funeral, and the only dishonest part is the mourning.' The Waydrani found this offensive. They also found it accurate, which was more offensive.

Klae, himself a member of a small and often-overlooked people, had obvious sympathy for the Waydrani. He wrote: 'They survived not by fighting but by being needed. It is a quieter form of resistance, and no less courageous, and it has the considerable advantage of leaving you alive at the end.'"""}
            ]},

            {"number": 7, "name": "Seventh Century",
             "description": "The Arden Ascendancy. The Arden Trade Federations reach the height of their influence, controlling the maritime trade routes that connect Fondore to the newly discovered continents. Rin Nohara becomes one of the wealthiest cities in the world. Meanwhile, the first permanent Fondorian settlements are established on Karagon and on the coasts of Metzerul.",
             "stories": [
                {"title": "Rin Nohara, City of Ships",
                 "content": """By the seventh century of the Third Age, Rin Nohara had become something that no city in Fondore had ever been: genuinely cosmopolitan.

Other cities were large. Boulavar had more people. Raxona covered more ground. Oradova was more beautiful. But Rin Nohara was the only city where a Geckish wine merchant could sit next to a Raxonian mercenary, a Pervin farmer, a Waydrani scholar, a Karaf trader from Karagon, and a Lirzan diplomat, and all six of them could conduct business in the same tavern without anyone reaching for a weapon. This was not because Rin Nohara was peaceful. It was because Rin Nohara was profitable, and profit has a way of making people tolerant of differences they would otherwise find intolerable.

The Arden Trade Federations had evolved from a loose alliance of shipwrights into the most powerful mercantile organization in Fondore. They controlled the trade routes to Karagon, to Metzerul, and to the Erezetta islands. They maintained a private navy that was larger than the official navies of most kingdoms. They had a seat at every diplomatic table, not because anyone had invited them but because the people who controlled the shipping controlled the conversation.

The federation was governed by a president elected from among the merchant houses — the closest thing to a functioning democracy in Fondore, if you defined democracy as government of the wealthy, by the wealthy, for the wealthy. The Clairdwell kings of Lambridge, who technically had sovereignty over the Ardent coast, had long since given up trying to control the federations and settled for collecting taxes that the Ardenese paid promptly and considered the cost of being left alone.

Rin Nohara itself was a marvel of commercial architecture. The harbor could accommodate two hundred ships. The warehouses were organized by commodity: silk in one district, grain in another, weapons in a third that was carefully separated from the tavern district to minimize the consequences of drunk sailors with access to inventory. The exchange floor, where trade contracts were negotiated and sealed, operated from dawn to midnight and conducted business in eleven languages.

Klae visited Rin Nohara and was overwhelmed. He wrote: 'It is the noisiest, busiest, most confusing city I have ever visited, and I have visited Imbraxione during a fire festival. Every corner of Elysal is represented in its streets. If the world has a center, it is here, in a harbor that smells of salt and money.'"""},

                {"title": "The Colony at Sheah Suraya",
                 "content": """The first permanent Fondorian settlement on Tzun was not established by soldiers or explorers. It was established by merchants, because in the Third Age, merchants went everywhere that soldiers were afraid to go, provided there was money to be made.

Sheah Suraya was built on the northern coast of Tzun, facing the Avadacaster strait, on a natural harbor that had been used by Tzunadaine fishermen for centuries. The fishermen were relocated — a euphemism that covered a range of outcomes from voluntary departure to forcible removal — and the Geckish and Ardenese merchants who had financed the colony moved in.

The purpose was trade. Tzun had resources that Fondore wanted: exotic hardwoods, spices, minerals, and the hides of animals that did not exist anywhere else in the world. The Fondorians had goods that Tzun wanted: metalwork, textiles, weapons, and Kript, the Raxonian berry wine that had somehow become popular in every corner of Elysal despite tasting, as Klae noted, 'like regret.'

Sheah Suraya grew quickly. It had none of the cultural refinement of Fondorian cities — it was a port town, built for function, with wooden buildings that could be replaced when they inevitably burned down and a population that turned over every few years as merchants completed their contracts and went home. But it served its purpose: it was the gateway between Fondore and Tzun, and everything that moved between the two continents moved through Sheah Suraya.

The Tzunadaine regarded the settlement with suspicion. The Pridekin ignored it entirely, as the Pridekin ignored most things that were not actively trying to eat them. The Gezedaine, who occasionally wandered near the settlement, caused periodic panics among the colonists, who had never seen a fifteen-foot humanoid and found the experience disagreeable.

The colony was a preview of what was coming. Fondore had discovered that there were lands beyond the ocean, and those lands had things that Fondore wanted. The acquisition of those things would be, in the coming ages, conducted through trade where possible and through force where convenient. The distinction between the two was never as clear as the merchants pretended, and the people on the receiving end of Fondorian expansion rarely had the luxury of pretending at all.

Klae found Sheah Suraya's founding ledger in a Geckish archive. The first entry listed the colony's assets: 'Two warehouses, one dock, forty-seven merchants, twelve guards, and one priest.' The last item was an afterthought. In the Third Age, God traveled in the cargo hold."""}
            ]},

            {"number": 8, "name": "Eighth Century",
             "description": "The Barren Wars. Territorial disputes between the expanding Fondorian powers erupt into a series of conflicts fought across disputed borderlands. The fighting is inconclusive but exhausting, and the wars earn their name from the desolation they leave in their wake.",
             "stories": [
                {"title": "The Wars Nobody Won",
                 "content": """The Barren Wars are the least celebrated conflicts in Fondorian history, and for good reason: nobody won them, nobody lost them, and the only measurable result was the creation of several hundred miles of devastated landscape that took generations to recover.

The fighting began, as most wars in Fondore do, over borders. The Novus Gecharium had pushed Geckish influence into territories that Lambridge, Epervinay, and Cynthia all considered their own. The crusader legacy in Mural Cere had left behind a patchwork of competing claims. Raxone was pushing south, not out of any particular ambition but because Raxonian princes needed something to fight about and the border was conveniently located.

The wars were fought in the spaces between kingdoms: the disputed borderlands, the unclaimed hill country, the river valleys that appeared on six different maps with six different names and six different owners. They were fought by professional soldiers, mercenary companies, local militias, and the occasional group of armed farmers who were simply tired of having armies march across their fields.

Nobody committed fully. The Gechann fought enough to maintain their territorial claims but not enough to provoke a coalition against them. Lambridge defended its southern border but did not counter-attack. Raxone raided, withdrew, raided again. Epervinay, as always, absorbed the punishment of being located between larger powers and survived through sheer durability.

The wars produced no decisive battles, no legendary commanders, no treaties worth remembering. They produced only the barren — vast stretches of land that had been fought over so many times that nothing grew there anymore. Fields that had been trampled by cavalry. Forests that had been cut down for siege works. Villages that had been burned, rebuilt, and burned again until the inhabitants gave up and left.

Klae devoted comparatively little space to the Barren Wars in the Annals, not because they were unimportant but because they were depressingly typical. He wrote: 'The Barren Wars proved nothing except that men will fight over land until there is nothing left worth fighting for, and then they will fight over the memory of what was there before.'"""},

                {"title": "A Pervin Field",
                 "content": """This is a small story. Klae collected hundreds of them — fragments of individual lives caught in the gears of history — and this one he placed in the Annals without explanation, trusting the reader to understand why it mattered.

A Pervin farmer named Tesh Ghorvan worked a plot of land in the hill country south of Havenaugh. The plot was small — enough for a family of five to live on, with some surplus to sell at the Havenaugh market in a good year. Tesh had inherited it from his father, who had inherited it from his father, who had cleared it from forest in the early Second Age. The Ghorvans were not important people. They grew wheat and raised goats and attended the Cereyst services at the village temple and otherwise asked nothing from the world except to be left alone.

The world declined.

Over the course of the Barren Wars, Tesh Ghorvan's field was crossed by seven different armies. Geckish regulars marched through in the spring, trampling the winter wheat. A Raxonian mercenary company camped on the southern half for three weeks in the summer, their horses eating the grass down to the dirt. A Leimish cavalry unit requisitioned the goats. A Cynthian foraging party took the grain stores.

Tesh replanted. The armies came back. He replanted again. They came back again. Over the course of a decade, the field was planted and destroyed eleven times. Tesh's wife died of a fever that the army surgeons might have treated if they had not already moved on. His eldest son joined the Pervin militia and was killed in a border skirmish that did not even have a name, because it was too small for anyone except the dead to notice.

By the end of the Barren Wars, Tesh Ghorvan was sixty years old and the field was bare. The topsoil had been compacted by boots and hooves until nothing would grow. He stood in the center of it and looked at the sky and did whatever a man does when everything he has built has been taken by people who will never know his name.

Klae found Tesh Ghorvan's story in a Pervin oral history collected by a monk in Havenaugh. He placed it in the Annals alongside the accounts of generals and kings and treaties, because he believed that the farmer's field was as true an account of the Barren Wars as any military history, and considerably more honest."""}
            ]},

            {"number": 9, "name": "Ninth Century",
             "description": "The Contested City. On the border between Lirzan and Wintermen territory in northern Metzerul, the city of Capera Cuza becomes one of the most fought-over pieces of real estate in the world. Claimed by both the Lirzans and the Wintermen, it exists in a state of permanent tension that makes it the most dangerous and most profitable city on the continent.",
             "stories": [
                {"title": "Two Names, One City",
                 "content": """Capera Cuza was a Lirzan name. Kaprva Kusa was the Wintermen's name for the same place. The city had two names because it had two owners, neither of whom recognized the other's claim, and both of whom were willing to kill to enforce their own.

The city sat on the border between Lirzan territory and the lands of the Wintermen in northern Metzerul, straddling a river that served as the theoretical boundary between the two powers. The Lirzan half had stone buildings, paved streets, and the organized efficiency that characterizes lizardfolk urban planning. The Wintermen's half had wooden structures, unpaved roads, and an atmosphere of cheerful menace. A bridge connected the two halves. It was the most heavily guarded bridge in the world.

Nobody controlled Capera Cuza. Not really. The Lirzans garrisoned their half with soldiers, and the Wintermen garrisoned theirs, and both sides maintained the polite fiction that the other half was merely a temporary occupation that would be resolved through diplomacy any day now. In practice, both sides had been saying this for centuries, and the diplomats had long since given up and gone home.

What filled the vacuum left by governance was commerce. Capera Cuza was where Lirzan goods — exotic jungle products, dragonborn metalwork, alchemical compounds — were exchanged for Wintermen goods — furs, ice-minerals, whale oil, and a fermented fish product that the Wintermen considered a delicacy and everyone else considered a weapon. The city's markets operated under an informal code: no questions about where anything came from, no questions about where it was going, and no weapons drawn until after the transaction was complete.

This code was enforced not by law but by mutual self-interest. A merchant who caused trouble in Capera Cuza found himself unable to do business in Capera Cuza, which was the same as finding himself unable to do business at all, because there was no other place in Metzerul where Lirzan and Wintermen goods changed hands.

Klae visited the city and found it exhilarating and terrifying in equal measure. He wrote: 'Capera Cuza is proof that commerce can exist without government, that trade can function without trust, and that two peoples who despise each other will cooperate if the profit margin is sufficient. It is not a lesson in hope. But it is a lesson in something.'"""},

                {"title": "The Birth of the Luschnypp",
                 "content": """Nobody knows exactly when the Luschnypp Syndicate was founded. This is by design. An organization dedicated to assassination, extortion, and the kind of crime that requires planning does not leave founding documents lying around for historians to find.

What is known is that the Syndicate emerged from the lawless border city of Capera Cuza sometime in the late Third Age, and that its founders were Pkoyte — dwarves from the mountain kingdom of Shoale, located in the highlands southwest of the Wintermen territories. The Pkoyte were a reclusive people who generally wanted nothing to do with the rest of the world, but a subset of them had discovered that the rest of the world would pay extremely well for the services that the Pkoyte were uniquely positioned to provide: precision, patience, and an absolute lack of squeamishness.

The Syndicate's early operations were local: assassination contracts in Capera Cuza, protection rackets targeting merchants who operated in the border zone, theft-to-order for noble patrons who wanted specific items and did not want to be connected to their acquisition. But the organization's ambitions, like the ambitions of any successful enterprise, grew with its profits.

By the end of the Third Age, the Luschnypp had agents in every major city in Metzerul. By the Fourth Age, they would have agents in Fondore. By the Sixth Age, they would be an international organization with the resources and reach of a small nation, capable of toppling governments and manipulating markets from their base in the only city in the world where no government could touch them.

Klae investigated the Syndicate during his research and was, by his own admission, terrified. He wrote: 'I was told, by a person whose identity I will not record, that the Luschnypp had considered killing me during my visit to Capera Cuza, decided I was not worth the effort, and then billed me for the consultation.' He never determined if this was true. He left the city the next morning.

The Luschnypp Syndicate is the shadow that every other institution in Elysal casts. Kings rule by daylight. The Syndicate rules by dark. And in Capera Cuza, where two nations pretend to share a city that neither controls, the dark has always been where the real business gets done."""}
            ]},

            {"number": 10, "name": "Tenth Century",
             "description": "The End of Discovery. The Era of Sail closes with the world largely mapped and the major civilizations in contact with one another. The age of exploration is giving way to the age of exploitation, and the ships that once carried curious explorers now carry soldiers, merchants, and the machinery of empire. The world is no longer unknown. It is merely unconquered.",
             "stories": [
                {"title": "The Shrinking Map",
                 "content": """By the end of the Third Age, Penelue's honest edges — 'Here be what we do not know' — had been almost entirely filled in. Cartographers in every nation produced maps that showed, with varying degrees of accuracy, the outlines of every major landmass in Elysal. Fondore in the east. Metzerul in the west. Tzun to the south. Karagon in the Erezetta. Acumfrial in the Asafin. The Rim Work to the south of Metzerul. Even Wyatak, the ice island in the far north, appeared as a vague blob on Raxonian charts.

The world, which had seemed infinite when Emmantine Jlain was blown off course into the open ocean, was finite after all. It had edges, and those edges had been reached. Every continent had been visited. Every major civilization had been contacted. Every ocean had been crossed, if not routinely then at least survivably.

This should have been a moment of triumph. In some ways it was. The exchange of goods, ideas, and technologies between Fondore and the wider world accelerated dramatically during the final centuries of the Third Age. Lirzan metalworking techniques improved Fondorian smithing. Karagonese democratic experiments influenced political theory in Gecha. Pridekin crossbow designs were adopted by every army in the world. Cynthian architecture, music, and philosophy enriched cultures that had never heard a Kouth until a Fondorian merchant brought one ashore.

But the shrinking map also meant something darker. The blank spaces where unknown peoples had lived in autonomy were now filled with names, borders, and claims. The Fondorian nations, having discovered that the world was full of resources and peoples who could be exploited, began the long, grinding process of doing exactly that. Colonies on Tzun expanded. Trade relationships with Karagon developed extractive elements. The Wintermen of Perut found Raxonian 'explorers' building permanent settlements in their territory.

The Era of Sail had opened the world. The question, as the Fourth Age approached, was what the world's openers planned to do with it.

Klae, who had the advantage of writing from the far end of history, knew the answer. He chose not to state it directly. Instead, he quoted a Hiyalmite proverb that he had learned during his years on Acumfrial: 'When the stranger arrives by boat, count his swords before you count his gifts.'"""},

                {"title": "A Sailor's Prayer",
                 "content": """Klae found this prayer written on a piece of sailcloth recovered from a shipwreck in the Erezetta. The ship was Ardenese, dating to the final century of the Third Age. The prayer was written in Leimish, in a hand that suggested education, and it was addressed to no one in particular, which is how the best prayers usually work.

'Illiman who walked the roads, walk with us upon the water. We are far from everything we know and close to everything we fear. The ocean does not care about us. We have learned this. The wind does not care. The stars do not care. We sail by the indifference of the world, and we have learned to navigate by it.

I have seen the coast of Metzerul, where lizards walk like men and the jungle goes on forever. I have seen Karagon, where a people freed from chains built a nation and did not know what to do with it. I have seen the Pridelands from the deck, and the Pridekin watching us from the shore, and I have never been so certain that I was being hunted and so uncertain by what.

The world is large. We said that before we left. Now we know it is true, and the knowing is heavier than the saying. There are things out here that we have no names for, peoples whose languages we cannot speak, places where the rules we live by do not apply. We have brought Ceresy with us in our hold, next to the grain and the weapons, and I do not know if that makes us missionaries or merchants or both.

Tomorrow we sail for home. The map is full now, or full enough. We know where everything is. We do not know what any of it means. Perhaps that is a question for people smarter than sailors. Perhaps it is a question that does not have an answer. Perhaps the answer is the sailing itself, the act of going, the willingness to leave the shore and trust that the horizon, which is a liar, will eventually show you something true.

Illiman who died on a road, carrying nothing, help us carry what we have found back to the people who sent us, and help them understand that the world is not ours. It was here before us. It will be here after. We are only passing through.'

Klae published this prayer as the final entry for the Third Age. He believed, correctly, that no historian could say it better."""}
            ]}
        ]
    },
    {
        "number": 4,
        "name": "An Empire of Men",
        "year_start": 1501,
        "year_end": 2000,
        "description": """The story belongs not to the man who died, but to the man who wrote about it. This ancient Cynthian proverb originated in the Fourth Age during the Pervin Wars, and it captures the essence of the age better than any historical analysis could. The Fourth Age was the age of the Gechann Empire, the first continental superpower, built through constant warmongering, advances in military tactics and logistics, and the creation of the first truly professional army. Geckish domination throughout the realm of men was, for a time, unstoppable.

But empires, as Klae observed, carry the seeds of their own destruction, and the Gechann sowed more seeds than most. The same military machine that conquered half of Fondore required constant feeding — in gold, in grain, in young men who marched south or west or east and did not come back. The conquered peoples who labored under Geckish governors did not forget who they were. The Pervins remembered. The Leimish remembered. The Verans, in what remained of their crumbling island kingdom, remembered most of all.

And beyond Fondore, in the jungles of Metzerul and the savannahs of Tzun, civilizations that the Gechann had dismissed as primitive were watching the empire's expansion with the particular attention of a prey animal observing a predator's habits. They were learning. They were adapting. And when the empire finally stumbled, they would be ready.

The Fourth Age is the age of empire. It is also, inevitably, the age of resistance. The two are inseparable, because every act of conquest produces an equal and opposite act of defiance, and the defiance, being cheaper and more sustainable, tends to win in the end.""",
        "centuries": [
            {"number": 1, "name": "First Century",
             "description": "The Rise of Imperial Gecha. The Geckish city-states, enriched by centuries of trade and emboldened by the Novus Gecharium, transform from a commercial federation into a military empire. The Supremus Leader takes the title of Imperator, and the Gechann begin the systematic conquest of their neighbors.",
             "stories": [
                {"title": "The Imperator's Speech",
                 "content": """The transformation of the Geckish city-states from a commercial federation into a military empire did not happen overnight. It happened over decades, in increments so gradual that most people did not notice until the process was complete, which is how the most dangerous transformations always work.

The Supremus Leader system established after the Punitive Wars had served Gecha well for centuries. It was flexible, competitive, and produced leaders who were, on average, competent, because incompetent leaders tended to be replaced at the next election by someone who was better at making money. But the system had a flaw: it was designed for a federation of city-states, not for an empire, and by the early Fourth Age, the Gechann had outgrown their institutions.

The catalyst was a man named Vorrikus Aelum Boulvaranus, the Supremus Leader from Boulavar who looked at the Novus Gecharium — the network of colonies, trade outposts, and military bases that the Gechann had built during the Third Age — and saw not a commercial enterprise but the skeleton of an empire. The flesh, he decided, would be military.

Vorrikus addressed the assembled representatives of the Thirteen Families in the grand senate hall at Boulavar and delivered a speech that Klae reconstructed from three separate sources, none of which agreed on the exact wording. The substance, however, was consistent: the Geckish city-states could no longer afford to be a federation of merchants. The world was too dangerous, the competition too fierce, the opportunities too vast. They needed a single voice, a single army, a single will. They needed an Imperator.

The vote was not unanimous. Jayvlun, the most democratic of the city-states, objected strenuously. Gisup Geronus abstained. But the majority — persuaded by Vorrikus's rhetoric, his military record, and the considerable economic pressure that Boulavar could bring to bear — voted yes. Vorrikus became the first Gechann Imperator, and the city-states became provinces of an empire.

The transition was, on paper, smooth. In practice, it was the beginning of the end of Geckish liberty. The elected Supremus became an appointed position. The Thirteen Families retained their wealth but lost their independence. The professional army that Vorrikus built was loyal not to the city-states but to the Imperator, and that distinction would matter enormously in the centuries that followed.

Klae wrote: 'The Gecks traded their freedom for power, which is the oldest bargain in civilization and the one that is always regretted first.'"""},

                {"title": "The Professional Army",
                 "content": """The Gechann had always been good at war. They had produced famous commanders, innovative tacticians, and soldiers whose discipline was the envy of Fondore. But they had never had a professional army in the modern sense: a standing military force that trained year-round, fought as a career, and owed its loyalty to the state rather than to a city-state, a prince, or a mercenary captain with a fat purse.

Vorrikus changed this. Drawing on lessons from the Punitive Wars, the Second Age War, the Barren Wars, and every conflict the Gechann had fought or observed, he created the Imperial Gechann Army: a force of thirty thousand professional soldiers organized into legions, equipped with standardized weapons and armor, trained to fight in coordinated formations, and paid a regular salary that made them dependent on the empire for their livelihood.

The legions were the backbone. Each consisted of five thousand infantry, organized into centuries of one hundred men under a centurion, with attached cavalry, engineers, and supply units. The infantry fought with the pilum — a heavy throwing javelin designed to bend on impact so it couldn't be thrown back — and the gladius, a short stabbing sword optimized for close-quarters combat in tight formations. The shield wall, refined over centuries of Geckish warfare, became the legion's signature tactic: an interlocking barrier of heavy wooden shields behind which the infantry advanced like a single armored organism.

The legions could march thirty miles in a day carrying their own supplies. They could build a fortified camp every evening and strike it every morning. They could construct bridges, siege works, and roads as part of their normal operations. They were, in Klae's words, 'an army that carried its civilization with it, and planted it wherever it stopped.'

The effect on Fondore was immediate. The kingdoms that had fought the Gechann to a standstill during the Barren Wars found themselves facing an enemy that was qualitatively different from anything they had encountered. The old tactics — guerrilla warfare, defensive fortifications, mercenary armies assembled for a season and disbanded afterward — did not work against an opponent that was always ready, always organized, and always advancing.

Within a generation, the Gechann had conquered Waydren formally, absorbed the border territories that had been contested during the Barren Wars, and established a military presence in northern Mural Cere that the desert monks could not dislodge. The empire was expanding, and it was expanding with a professional efficiency that made resistance feel not just futile but obsolete.

Klae noted, with his characteristic precision, that the Gechann army's greatest weapon was not the pilum or the gladius or the shield wall. It was the road. Every territory the legions conquered was connected to the empire by a paved road, and every road led back to Boulavar. The empire did not just conquer land. It connected it."""}
            ]},

            {"number": 2, "name": "Second Century",
             "description": "The Pervin Wars. The Gechann Empire turns its attention to Epervinay, the small but fierce nation that had won its independence in the Second Age War. The resulting conflict produces some of the most celebrated resistance fighters in Fondorian history, and demonstrates that professional armies can be beaten by people with nothing left to lose.",
             "stories": [
                {"title": "The Iron Fist in Epervinay",
                 "content": """Epervinay should not have mattered. It was a small nation of farmers and horse breeders wedged between Gecha, Hyacinth, and Lambridge, with a population that could barely field an army of ten thousand and an economy based primarily on wheat, goats, and the stubborn refusal to accept the obvious. By every rational calculation, the Gechann should have been able to absorb it as easily as they had absorbed Waydren.

The Gechann did not account for the Pervins.

The Pervin Wars began in the second century of the Fourth Age when the current Imperator — a hard, efficient man from Aemore whose name the Pervins refused to record in their histories, calling him only The Grey Fist — demanded that Epervinay accept a Geckish military garrison on its territory. The demand was phrased as a request for mutual security. Everyone knew what it actually was.

The Pervin minister, a woman named Rell Havenaugh, refused. The Grey Fist sent two legions. Rell Havenaugh mobilized the Pervin militia and called on the alliance treaties with Lambridge and Hyacinth. Lambridge sent three hundred knights. Hyacinth sent a strongly worded letter.

The first Geckish advance was a disaster for Epervinay. The legions crossed the border, defeated the Pervin militia in open battle — because militia cannot beat professional soldiers in open battle, which the Pervins should have known — and occupied the capital within a season. Rell Havenaugh fled to the hills. The Grey Fist declared Epervinay a Geckish protectorate and appointed a governor.

What followed was twenty years of the ugliest, most grinding, most exhausting guerrilla warfare that Fondore had ever seen. The Pervins refused to accept occupation. They had tried freedom, briefly, during the Second Age, and the taste of it had permanently ruined them for subjugation. Pervin farmers who had never held a sword picked up whatever was available — axes, pitchforks, sharpened stakes — and fought. They fought from the hills, from the forests, from the cellars of their own homes. They assassinated Geckish officers. They poisoned wells. They burned their own granaries rather than let the occupiers eat from them.

The Gechann responded with escalating brutality. Villages suspected of harboring resistance fighters were razed. Public executions became weekly events. The occupation army swelled from two legions to five, then to eight, tying down forty thousand professional soldiers in a territory that the empire had expected to pacify in a season.

Klae recorded a Geckish officer's letter home: 'We have conquered the land. We have not conquered the people. I am beginning to wonder if these are different things.'"""},

                {"title": "Rell of the Hills",
                 "content": """Rell Havenaugh became a legend despite her best efforts to the contrary. She was not a warrior. She was a politician — a minister's daughter from the provincial town of Havenaugh who had entered government because someone needed to do it and she was tired of waiting for a man to volunteer. She had never held a weapon. She had never commanded soldiers. She had never, in her own words, done anything more violent than argue with a tax collector.

The Geckish invasion changed this, as invasions tend to change everything. Rell fled the occupied capital with a handful of loyalists and established a resistance government in the hill country south of the Paronis. From there, she coordinated the guerrilla campaign that would torment the Gechann for two decades. She did not fight. She organized. She sent messages, gathered intelligence, arranged supply lines, and made the thousands of small, grinding decisions that keep a resistance alive when every rational calculation says it should surrender.

The Geckish called her the Hill Witch, a name she found amusing. The Pervins called her Rell of the Hills, which she found acceptable. She called herself 'the minister of a government that doesn't have a building,' which was accurate.

Her greatest contribution was not military but diplomatic. Rell understood that Epervinay could not defeat the Gechann alone. She needed allies, and allies required persuasion. She sent envoys to every kingdom in Fondore, not asking for armies — she knew better — but asking for economic pressure. Embargo Gecha. Refuse their trade. Make the occupation of Epervinay more expensive than it was worth.

The strategy worked, slowly. The Raxonians, who had been selling mercenaries to both sides, quietly raised their prices for Geckish contracts. The Ardenese, whose ships carried Geckish goods, began imposing surcharges. Even the Leimish, who generally avoided confrontation, restricted the sale of Ardent-built warships to the empire.

The Geckish treasury, which had expected a short campaign and was now funding a permanent occupation, began to strain. The Grey Fist's successor — the Imperator was elected every decade, though the elections were increasingly performative — made the calculation that every occupier eventually makes: this is costing more than it is worth.

The Gechann withdrew. Not completely — they maintained a military presence on the border that would endure for centuries — but they recognized Epervinay's sovereignty and removed their governor. Rell Havenaugh returned to the capital and governed for another decade.

She never wrote a memoir. She never commissioned a statue. When she died, she was buried in the family plot in Havenaugh, and the inscription on her stone was the same as every other Havenaugh buried there: name, dates, and the Pervin word for home.

Klae wrote: 'She saved her country by being too stubborn to admit it was lost. This is not a military strategy. It is a Pervin one.'"""}
            ]},

            {"number": 3, "name": "Third Century",
             "description": "The Fall of Vera. The ancient Kingdom of Vera, once the mightiest naval power in the world, collapses under the weight of its own slave economy and Geckish military pressure. The island kingdom that built the first transoceanic empire becomes a Geckish dependency, and the Karaf slaves who built Vera's wealth are freed — not by Veran conscience but by Geckish pragmatism.",
             "stories": [
                {"title": "The Last King of Vera",
                 "content": """The Kingdom of Vera had been dying for centuries. The diagnosis was simple: an economy built entirely on slave labor cannot adapt, because adaptation requires the kind of creative problem-solving that slave economies systematically destroy. The Verans had Karaf slaves for manual labor, Rusiki slaves for household work, and an aristocracy so accustomed to being served that many of its members could not dress themselves without assistance. This is not a recipe for national resilience.

The Gechann, who had been expanding their naval power throughout the Third Age, looked at Vera the way a doctor looks at a terminal patient: with clinical interest and a clear sense of inevitability. The island kingdom still had a fleet, but it was crewed increasingly by slaves who had no particular reason to fight for their masters. The army was small and poorly trained, because the aristocracy considered military service beneath them and the slaves were not trusted with weapons.

The last King of Vera — Sokotros XXIII, a number that tells you something about the dynasty's longevity and nothing about its quality — was a young man who had inherited a kingdom that was, by every measurable standard, bankrupt. The treasury was empty. The slave population, which outnumbered the free population three to one, was restive. The Geckish fleet was visible on the horizon on clear days.

Sokotros XXIII tried diplomacy. He offered trade concessions, military access, and a formal alliance. The Gechann accepted the concessions, noted the military access, and invaded anyway, because the Gechann had learned that the cheapest way to acquire something was to take it from someone who had already offered to give it away.

The invasion lasted three weeks. The Veran fleet, crewed by slaves who dropped their oars the moment the Geckish ships appeared, was captured without a significant engagement. The Veran army, such as it was, surrendered after a single battle outside the capital. Sokotros XXIII was deposed, exiled to a small estate on the Rokori peninsula, and spent the rest of his life writing poetry that nobody read.

The Gechann freed the Karaf slaves. This was not an act of moral conviction. It was an act of economic calculation. Free workers are more productive than slaves, require less policing, and do not periodically attempt to murder their employers. The Karaf, who had been in chains for millennia, were handed their freedom by the same empire that had just conquered their masters, which created a complicated emotional landscape that Klae found fascinating and the Karaf found exhausting.

Vera, the kingdom that had built the first transoceanic empire, ceased to exist. Its territory became a Geckish province. Its name survived only in geography and in the bitter memories of an aristocracy that had lost everything except its sense of entitlement."""},

                {"title": "Karaf Unchained",
                 "content": """The day the chains came off was not a celebration. It was a confusion.

The Karaf had been slaves for so long that freedom was not a concept most of them had personal experience with. Their great-grandparents had been slaves. Their great-great-grandparents had been slaves. The stories of the Kola Tai — the great escape during the First Age, when Karaf slaves had stolen a ship and founded a free colony on Karagon — were legends, not lived memory. For the Karaf on Vera, slavery was not an injustice. It was weather. It was the sky. It was the fundamental condition of existence.

The Geckish governor who announced the emancipation did so in a public square in the Veran capital, reading from a prepared text that had been drafted by bureaucrats in Boulavar. The language was dry, legalistic, and entirely inadequate to the moment. 'All persons held in bondage within the territories of the former Kingdom of Vera are hereby declared free citizens of the Gechann Empire, with all rights and responsibilities pertaining thereto.'

Rights and responsibilities. The Karaf standing in the square — grey-skinned, sharp-featured, bearing the physical marks of generations of forced labor — heard the words and did not know what to do with them. Some wept. Some stood in silence. Some walked away, because they had work to do and emancipation did not change the fact that the crops needed harvesting and the fishing boats needed mending.

The practical reality of emancipation was brutal. The Karaf were free, but they owned nothing. The land they had worked belonged to Veran aristocrats or, now, to the Geckish state. The skills they possessed were the skills of slaves: farming, fishing, construction, domestic service. The education system that might have prepared them for free citizenship had never existed, because educated slaves are dangerous slaves.

The Gechann provided, to their credit, a rudimentary transition program. Land grants were distributed — small parcels, mostly the worst land on the island, the rocky hillsides and marshy lowlands that nobody else wanted. Tools were provided. Cereyst missionaries established schools. It was not enough. It was never going to be enough. Centuries of bondage cannot be remedied by a decade of half-measures.

Some Karaf left Vera entirely. They sailed to Karagon, where the free Karaf nation had been building a civilization for millennia. The reunion was complicated: the Karagonese Karaf had developed a culture so different from the Veran Karaf that they were, in many ways, different peoples who happened to share a skin color and a history of suffering.

Klae spent months interviewing Karaf communities on both Vera and Karagon. He concluded: 'Freedom given is not the same as freedom taken. The Karaf of Karagon earned theirs with blood. The Karaf of Vera received theirs from the same kind of power that had stolen it in the first place. Both are free. Neither has forgotten.'"""}
            ]},

            {"number": 4, "name": "Fourth Century",
             "description": "The Rise of the Karagon. While the Gechann Empire expands across Fondore, the Karaf nation on Karagon emerges as an unlikely power. Built on the ruins of Veran colonialism and sustained by a fierce egalitarian culture, Karagon develops its own navy, its own trade routes, and its own ideas about how a nation should be governed.",
             "stories": [
                {"title": "The Republic of Karagon",
                 "content": """The Karaf had tried kings. It hadn't worked.

The early centuries of Karagonese independence had been governed by a rotating series of strongmen, warlords, and self-appointed monarchs who rose on the strength of their personality and fell when someone stronger came along. The cycle was predictable and exhausting, and by the middle centuries of the Third Age, the Karagonese had developed a cultural allergy to concentrated power that bordered on the pathological.

The solution they devised was radical: a republic. Not the elective monarchy of the Gechann, which produced dictators who called themselves elected officials. Not the constitutional monarchy of Lambridge, which produced kings who called themselves servants of the people. A genuine republic, where representatives were chosen by popular vote, served fixed terms, and could be removed by the same vote that installed them.

The system was messy. Elections were chaotic. Representatives spent as much time arguing with each other as governing, which the Karagonese considered a feature rather than a bug. The bureaucracy was slow, the military was underfunded, and foreign diplomats who were accustomed to dealing with a single authority figure found the Karagonese system baffling.

But it worked. Not perfectly, not elegantly, but it worked in the sense that power transferred peacefully, unpopular leaders were removed without bloodshed, and the government, despite its many inefficiencies, reflected the will of the people it governed more accurately than any other system in Elysal.

The Karagonese were particularly proud of one institution: the People's Court, where any citizen could bring a grievance against any official, up to and including the head of state. The court was staffed by randomly selected citizens who served for one year, ensuring that no judicial class could form. It was chaotic, unpredictable, and occasionally absurd — a fisherman once brought a complaint against the trade minister for the price of bait — but it kept the powerful honest, or at least nervous, which the Karagonese considered approximately the same thing.

Klae visited Karagon during his research and was deeply impressed. He wrote: 'The Karagonese have built the only government in Elysal that is designed to distrust itself. Every institution contains the mechanism for its own correction. Every leader serves knowing that the people who elevated them can bring them down. It is not efficient. It is not elegant. It may be the closest thing to justice that politics can produce.'"""},

                {"title": "The Karagonese Navy",
                 "content": """The Karagonese had a saying: the ocean freed us, and the ocean will keep us free. It was not a metaphor.

Karagon was an island. Its freedom depended entirely on the ability to prevent hostile fleets from reaching its shores, which meant that the Karagonese invested in their navy with the single-minded intensity of a people who understood that the alternative was extinction. Every child on Karagon learned to sail. Every coastal village maintained a fleet of fishing boats that could be converted to warships in an emergency. The shipyards at Kapolei, the capital, produced vessels that were fast, maneuverable, and designed for one purpose: making other people's ships sink.

The Karagonese ship design was distinctive. Where Fondorian vessels were built for cargo capacity and ocean endurance, Karagonese ships were built for speed and combat. They were lower, narrower, with hulls shaped to cut through waves rather than ride over them. Their signature weapon was the fire pot — a ceramic container filled with a mixture of pitch, sulfur, and other combustibles that could be catapulted onto an enemy deck, where it would shatter and ignite. The mixture was a closely guarded state secret, and Karagonese sailors were trained to destroy their own ships rather than allow the formula to be captured.

The navy's first major test came when a Geckish trading fleet, emboldened by the empire's conquest of Vera, attempted to establish a commercial outpost on Karagon's northern coast without permission. The Karagonese response was swift and unambiguous: the fleet was intercepted, the merchant ships were burned, and the Geckish captain was sent back to Boulavar on a raft with a message that Klae found in the Gechann imperial archives: 'Karagon is not Vera. We freed ourselves. Try us.'

The Gechann, who were stretched thin by their continental empire, decided that Karagon was not worth the effort. The island republic was left alone, which was all the Karagonese had ever wanted. They continued to trade with Fondore — Karaf merchants were welcome in every port — but they traded on their own terms, and any nation that attempted to impose terms on them discovered what the fire pots were for.

Klae noted that Karagon's independence was maintained not by diplomacy or alliances but by the simple, brutal logic of naval superiority. The Karagonese could not defeat the Gechann Empire in a war. But they could make any invasion so expensive that no Imperator would consider it worthwhile. This is the strategy of the small and the determined, and it has a perfect record against the large and the distracted."""}
            ]},

            {"number": 5, "name": "Fifth Century",
             "description": "The Icrazan Genocide. The Gechann Empire, seeking to secure its holdings in Metzerul, launches a campaign against the Lirzan Kingdom that escalates into one of the worst atrocities in Elysali history. The dragonborn ruling class is specifically targeted, and the events of this century leave scars that will never fully heal.",
             "stories": [
                {"title": "The Lirzan Question",
                 "content": """The Gechann called it the Lirzan Question, as if the existence of an entire civilization were a problem to be solved.

The Lirzan Kingdom in Metzerul had been a trading partner of Fondore since the Era of Sail. Lirzan goods — exotic metals, alchemical compounds, jungle hardwoods, and the distinctive fire-glazed ceramics that were fashionable in every Fondorian court — flowed through Capera Cuza and across the Erezetta. The Lirzans, for their part, imported Fondorian textiles, agricultural technology, and Kript, which they found revolting but which the Wintermen in their territories demanded.

The relationship worked because it was mutually profitable. It stopped working when the Gechann decided that mutual profit was insufficient and that total control was preferable.

The Fourth Age Imperator — a man named Gaius Thryvyc Saul, who had risen through the military ranks and viewed every problem as a logistics exercise — determined that the Gechann needed exclusive access to Lirzan resources. The Wintermen of Perut, the Raxonian merchants in Capera Cuza, the Ardenese trading companies — all of these competitors needed to be eliminated. And the Lirzans themselves, who had the inconvenient habit of setting their own prices and choosing their own partners, needed to be brought under control.

The initial approach was economic. Geckish trade representatives offered the Lirzan king exclusive contracts at favorable rates. The Lirzans declined, preferring to maintain their diverse trading relationships. The Gechann offered again, less favorably. The Lirzans declined again. The Gechann offered a third time, with an implied threat. The Lirzan king, a dragonborn named Zumarax III, reportedly breathed a small jet of fire in the direction of the Geckish ambassador and suggested he leave.

What followed was not a negotiation. It was a campaign of subjugation that began with trade blockades, escalated to naval engagements, and culminated in a full military invasion of coastal Metzerul. The Geckish legions, adapted for jungle warfare with lighter equipment and native guides, pushed into Lirzan territory with the methodical efficiency that defined every imperial campaign.

But the Lirzan campaign was different from Epervinay or Vera. The Lirzans were not humans. They were lizardfolk, with dragonborn at the apex of their society, and the Gechann treated them accordingly — not as a people to be conquered but as a species to be subdued.

Klae wrote: 'The Lirzan Question was never a question. It was an answer looking for a justification.'"""},

                {"title": "Fire and Scale",
                 "content": """The word genocide was not used in the Fourth Age. The concept did not yet have a name, because naming a thing requires acknowledging that it exists, and the Gechann were not in the business of acknowledging what they were doing.

The campaign against the Lirzans began as a conventional military operation and became something else. The Geckish legions conquered the coastal cities without great difficulty — the Lirzan military, organized for jungle warfare, was poorly suited to defending fixed positions. But the interior, where the great jungle cities like Imbraxione lay hidden beneath the canopy, proved unconquerable by conventional means. The legions could not march through terrain where every tree might contain an ambush, where the rivers were full of predators, and where the defenders could literally see in the dark.

The Imperator's solution was extermination. If the Lirzans could not be conquered, they would be destroyed — not all of them, because even Gaius Thryvyc recognized that someone needed to work the mines and farms, but enough of them to break any capacity for organized resistance. Specifically, the dragonborn.

The dragonborn were the ruling class of Lirzan society. They were the generals, the priests, the administrators. They were also, due to their dragon ancestry, the most dangerous combatants on the battlefield — capable of breathing fire, resistant to extreme temperatures, and possessed of a physical toughness that made them difficult to kill even when you caught them. The Gechann concluded, with the cold logic of empire, that removing the dragonborn would decapitate Lirzan society and render the remaining lizardfolk population docile and exploitable.

The campaign that followed targeted dragonborn specifically. Villages were raided and dragonborn identified by their distinctive features — the vestigial wing-bones, the darker scales, the smoke that curled from their nostrils. They were separated from the general population and killed. Not in battle, not in the chaos of combat, but systematically, in organized operations that had the bureaucratic efficiency of a tax collection.

The Lirzans resisted with everything they had. Dragonborn warriors fought to the last, and the legends of the Lirzan resistance are among the most harrowing in the Annals. But organization, numbers, and the industrial capacity of the Gechann Empire prevailed over individual heroism.

Klae recorded the Icrazan Genocide in the flattest, most clinical language he could manage. He did not editorialize. He did not moralize. He simply listed the numbers, the dates, the names of the dead where they could be recovered, and the names of the commanders who gave the orders. He believed that the facts, presented without adornment, were condemnation enough.

He was right."""}
            ]},

            {"number": 6, "name": "Sixth Century",
             "description": "Palasor City. At the height of its power, the Gechann Empire builds Palasor, a new capital designed to project imperial grandeur across the world. The city becomes a monument to Geckish ambition — and, eventually, a monument to the hubris that accompanies it.",
             "stories": [
                {"title": "The City That Swallowed the World",
                 "content": """Boulavar had been the capital of Gecha since the early days of the Novus Gecharium. It was a fine city — wealthy, well-defended, strategically located — but it was also a city that had grown organically, without plan, its streets a tangle of old neighborhoods and market districts that had been built by merchants, not architects. The Imperators who ruled from Boulavar's senate hall found it an unsatisfactory seat of power. It looked like what it was: a trading city that had stumbled into empire. They wanted something that looked like it was meant to rule.

Palasor was designed from the ground up as an imperial capital. The location was chosen for symbolism rather than strategy: a flat plain in central Gecha, equidistant from the major city-states, at the intersection of the empire's great military roads. The architect — a Waydrani genius named Thessik Moran, who had been recruited, or possibly coerced, from the university at Hypolta — was given unlimited resources and a simple brief: build a city that makes visitors feel small.

Thessik delivered. Palasor's central avenue was wide enough for three legions to march abreast. The Imperial Palace, called the Aurumthen, was a complex of marble and granite that covered more ground than some towns. The senate hall could seat a thousand. The public baths could accommodate ten thousand. The arena, where gladiatorial games and military demonstrations were held, was visible from five miles away.

The city was a statement, and the statement was: we are the most powerful civilization in the world, and we have built a city to prove it. Foreign ambassadors who visited Palasor returned home with descriptions that read like hallucinations. A Leimish diplomat's letter, recovered by Klae from the Clarity archives, reads: 'It is not a city. It is an argument made of stone.'

But Palasor had a problem that stone arguments always have: it was expensive. The construction alone consumed a significant portion of the imperial treasury. Maintaining it — the aqueducts, the roads, the public works, the garrison — required a constant flow of tax revenue from the provinces. And the provinces, several of which were occupied territories whose populations resented funding the construction of a monument to their own subjugation, were increasingly reluctant to pay.

Klae visited the ruins of Palasor during his research. By his time, the city had been abandoned for centuries, its marble cracked, its avenues overgrown, its arena home to nothing more threatening than nesting birds. He wrote: 'Palasor was built to last forever. It lasted as long as the money did, which is another way of saying it lasted as long as the empire did, which is another way of saying nothing lasts forever.'"""},

                {"title": "The Games at Palasor",
                 "content": """The arena at Palasor was the largest enclosed structure in Fondore, an oval of tiered stone seating that could hold forty thousand spectators and was rarely less than full. The games held there were the empire's most popular entertainment, and they were, depending on your perspective, either a celebration of martial culture or a systematic desensitization to violence dressed up as sport.

The games featured gladiatorial combat, military re-enactments, animal hunts, and public executions — the last of which were presented as entertainment rather than justice, which tells you something about how the empire viewed both. Gladiators were drawn from the prisoner population, from slaves, from condemned criminals, and from a surprising number of volunteers who chose the arena over poverty, which tells you something about the poverty.

The most popular events were the re-enactments: staged recreations of famous imperial victories, complete with thousands of combatants, elaborate scenery, and a script that ensured the Gechann always won. The Battle of the Thaugren, where the Gechann had crushed a Debrear border incursion, was a perennial favorite. So was the Fall of Vera, re-enacted with Veran prisoners playing themselves. The taste involved in making conquered peoples re-enact their own defeat for the entertainment of their conquerors was not questioned, because the Gechann did not consider it a question.

But the games served a political purpose that went beyond entertainment. They kept the population of Palasor — a city of bureaucrats, soldiers, merchants, and the various hangers-on that accumulate around power — occupied and distracted. A population watching gladiators is a population not questioning policy. The bread-and-games strategy is as old as civilization, and the Gechann executed it with their characteristic efficiency.

The games also served as a pressure valve for the empire's military culture. The Gechann glorified martial prowess, but the legions were fighting on distant frontiers, and the average citizen of Palasor would never see a real battle. The arena provided a substitute: controlled violence, presented as spectacle, allowing the population to participate vicariously in the martial virtues that the empire claimed as its identity.

Klae attended a re-enactment during his visit to the ruins, staged by a local historical society with considerably fewer resources than the original. He found it disturbing, not because of the violence — which was simulated — but because of the enthusiasm. 'The audience cheered,' he wrote, 'at the moment the Verans died. They have been cheering at this moment for centuries. I do not think they know what they are cheering for.'"""}
            ]},

            {"number": 7, "name": "Seventh Century",
             "description": "The Second Holy War. Emboldened by Geckish overextension, the High Cere calls a second crusade to retake the holy lands of Mural Cere. The war is larger, bloodier, and more cynical than the first, and it produces a generation of disillusioned soldiers who return home questioning everything they were told to believe.",
             "stories": [
                {"title": "The Call That Should Not Have Been Answered",
                 "content": """The Second Holy War was, in every measurable way, a mistake. The High Cere who called it — a man named Gloron Pav VII, deliberately named after his crusading predecessor to invoke the spirit of the First Holy War — was not a spiritual leader. He was a politician in robes who understood that Mural Cere's influence had been declining for centuries and that a war was the fastest way to reverse the trend.

The pretext was the same as the first time: Geckish occupation of historically Cereyst territory. The Gechann, stretched across half the world, had garrisoned northern Mural Cere with a single legion and a governor whose primary qualification was that nobody else wanted the job. The desert was hot, the population was hostile, and the posting was considered a punishment for officers who had disappointed their superiors.

Gloron Pav VII saw an opportunity. The empire was overextended. Its legions were committed in Metzerul, in Epervinay, in the border territories, in every corner of a domain that had grown faster than its ability to defend it. A well-timed crusade could recapture the holy lands while the Gechann were looking the other way.

The kingdoms of Fondore answered the call, again. Lambridge sent knights, again. Raxone sent mercenaries, again. Epervinay sent soldiers who were happy to fight anyone who wasn't fighting them for a change. And the crusading army marched south into the Pasav, again, through the same killing heat, toward the same fortified cities, against the same kind of enemy.

But the soldiers of the Second Holy War were different from their predecessors. They had read the histories of the first crusade. They knew about the sack of Ramal Cere. They knew that the crusader state had lasted barely a century before the Gechann retook it. And they marched anyway, because their kings told them to and their priests told them God wanted them to, and when kings and priests agree, the ordinary soldier's opinion is not consulted.

The war lasted years. It produced several significant battles, a handful of legendary commanders, and an enormous quantity of dead young men who had traveled hundreds of miles to die in a desert for a cause that their grandchildren would struggle to explain. The crusaders took territory, lost it, took it again, lost it again, in a cycle that achieved nothing except the enrichment of the weapons merchants and the impoverishment of everyone else.

Klae wrote: 'The Second Holy War was the First Holy War with the illusions removed. The first time, men marched for God. The second time, they marched because they had been told to march, and the difference between faith and obedience is the difference between a fire and its ashes.'"""},

                {"title": "The Veterans of Sand",
                 "content": """They came home changed. The soldiers who returned from the Second Holy War — those who returned at all — carried something with them that was more durable than their scars and more dangerous than their weapons. They carried doubt.

The crusaders had been told they were fighting for Illiman, for the holy lands, for the eternal salvation of their souls. What they had found in the Pasav was sand, heat, disease, and an enemy that fought with the same conviction and the same prayers to the same god. A Raxonian mercenary named Helter Jorunson, whose testimony Klae recorded in full, described the moment that broke him: hand-to-hand combat with a Mural Cereyn defender who was reciting Illiman's Prayer of Mercy while trying to kill him. 'He was praying the same prayer I was praying,' Jorunson said. 'And one of us was supposed to be wrong. I couldn't figure out which.'

The veterans returned to kingdoms that did not know what to do with them. They were too experienced to be farmers and too disillusioned to be soldiers. Many drank. Some turned to crime. A significant number joined the growing Rundelian movement, which rejected institutional Ceresy entirely and practiced a personal, unmediated relationship with the divine that did not require priests, temples, or wars fought in God's name.

The Rundelian movement had been growing since the Second Age, but the veterans of the Second Holy War gave it a critical mass of credibility. These were not philosophers or monks arguing about doctrine. They were men who had killed and nearly died in the name of a religion that they now believed had betrayed them. When they said the Church was corrupt, people listened, because the men saying it had the authority of experience.

The Gechann Empire, which had weathered the crusade with minimal territorial loss, observed the religious upheaval in its rivals with amusement. A Fondore divided by religious controversy was a Fondore too distracted to challenge Geckish hegemony. The Imperator reportedly said, upon hearing of the Rundelian schism: 'Let them argue about God. We will argue about borders. Our argument is more productive.'

He was wrong about that, as Imperators often are about things that do not involve legions. The religious transformation that the veterans brought home would reshape Fondorian society more profoundly than any military campaign, because it changed what people believed, and what people believe determines what they are willing to fight for and what they are willing to accept.

Klae, who was himself not religious, understood this. He wrote: 'The veterans came home and said: I have seen what is done in God's name, and I do not believe God wants it. This is a small sentence. It brought down cathedrals.'"""}
            ]},

            {"number": 8, "name": "Eighth Century",
             "description": "The Kingdom of the North Divided. The Raxonian monarchy, weakened by the princely feuds and the costs of the crusade, fractures into warring factions. The War of Snow — a civil war fought across the frozen North — produces one of the most devastating conflicts in Raxonian history and permanently alters the balance of power in northern Fondore.",
             "stories": [
                {"title": "The War of Snow",
                 "content": """The War of Snow did not begin with a declaration. It began with a door.

In the eighth century of the Fourth Age, King Brostav IV of Raxone was found dead in his bedchamber, the door locked from the inside, with no visible wounds and no explanation. The royal physician declared natural causes. The king's brother, Prince Varek, declared murder. The king's son, Prince Aldren, declared his father's brother a liar. And within a week, the kingdom was at war with itself.

The details of the succession crisis are tangled beyond recovery. Klae spent years trying to untangle them and eventually admitted defeat, writing: 'I have interviewed forty-seven Raxonians about the War of Snow and received fifty-three different explanations, because six of them changed their story between our first and second meetings.'

What is clear is this: the kingdom split roughly in half. The western provinces, controlled by the older princely families, backed Varek. The eastern provinces, controlled by newer families who had risen through the military, backed Aldren. The central territories, caught between the two, tried to stay neutral and were invaded by both sides for their trouble.

The War of Snow earned its name from the terrain and the season. The fighting began in winter, because Raxonians do not wait for favorable weather, and it was fought across hundreds of miles of frozen taiga, snowbound passes, and river crossings that were either frozen solid or frozen enough to look solid until a column of soldiers tried to cross and discovered otherwise.

The war lasted seven years. It produced no legendary battles, because battles in the Raxonian North tended to be confused, bloody affairs fought in poor visibility between men who could not feel their extremities. It produced, instead, a grinding attrition that consumed the kingdom's manpower, its treasury, and its capacity for self-governance. Towns changed hands repeatedly. Families were divided. Men who had drunk together at the Tavern at Esterhai found themselves on opposite sides of a shield wall.

The war ended when both sides ran out of men. Prince Varek was killed in a skirmish so minor that it does not appear in most histories. Prince Aldren took the throne and immediately faced a kingdom that was exhausted, depopulated, and broke. The Princes of Rax, who had fueled the war by backing different sides, emerged from the conflict with their power enhanced and the monarchy's power diminished. The king ruled in name. The princes ruled in fact.

Raxone would not recover for generations. And the Gechann, watching from the south, noted the North's weakness with the professional interest of an empire that had not yet run out of things to conquer."""},

                {"title": "The Frozen Truce",
                 "content": """After seven years of killing each other, the Raxonians needed to remember how to stop. This proved more difficult than the fighting.

The Frozen Truce — named for the river crossing where it was negotiated, and for the temperature, which was several degrees below what any Fondorian would consider habitable — was brokered not by diplomats but by tavern-keepers. This is not a metaphor. The tavern-keepers of Raxone, who occupied a social position somewhere between priest and magistrate, had watched their communities tear themselves apart and decided, collectively, that someone needed to intervene before there was nobody left to serve drinks to.

A woman named Inge Torvaldssen, who ran the largest inn in the border town of Voskraad, organized a meeting between representatives of both factions. She did this by the simple expedient of inviting both sides to her inn for a funeral — the funeral of a local farmer who had been killed by neither side but whose death she attributed to both, loudly, publicly, and with the kind of moral authority that only a woman who has been feeding your soldiers for seven years can claim.

The representatives came. They drank. They argued. They drank more. Inge Torvaldssen, who had been serving Kript to angry men for thirty years and was not impressed by either princes or generals, kept them in the same room until they reached an agreement. The agreement was simple: stop fighting. Divide the territory along the current battle lines. Let Aldren have the crown, because Varek was dead and crowns need heads. And for the love of everything sacred, rebuild the roads, because the trade routes were destroyed and nobody could get a shipment of anything anywhere.

The truce held, not because of its legal framework — which was minimal — but because of its practical foundation. The Raxonians were exhausted. The economy was shattered. The army, what was left of it, wanted to go home. And the tavern-keepers, who understood their countrymen better than any politician, had given both sides an exit that allowed them to stop fighting without admitting they had been wrong to start.

Klae found the Frozen Truce deeply characteristic of Raxone. He wrote: 'Other nations end their wars with treaties signed in palaces. The Raxonians ended theirs in a tavern, brokered by a woman who was tired of cleaning blood off her floorboards. I am not sure which approach is more civilized, but I know which one I prefer.'"""}
            ]},

            {"number": 9, "name": "Ninth Century",
             "description": "The Schvainese Rebellion. The Isles of Schvaine, long a Leimish territory and the birthplace of the Knights of Lambridge, erupt in revolt against the Clairdwell dynasty. The rebellion forces Lambridge to confront the contradiction at the heart of its national identity: a kingdom founded on liberation that has become, in its own small way, an oppressor.",
             "stories": [
                {"title": "The Sons of Schvaine",
                 "content": """The irony was exquisite, and the Schvainese were not shy about pointing it out.

The Isles of Schvaine had been the birthplace of the Knights of Lambridge — the rocky, wet islands where Emantine Asaundier had trained his exiled warriors before crossing back to the mainland to liberate the Leimlands from Debrear occupation. The Schvainese had sheltered the knights, fed them, given them boats and supplies and the quiet, steady support that makes exile survivable. They had done this freely, out of solidarity and shared Leimish identity.

In return, when the Clairdwell dynasty was established on the mainland, the Schvainese were made subjects. Not partners, not allies, not the honored founders of the liberation movement. Subjects. The islands were incorporated into Lambridge as a territory — technically equal under the law, practically subordinate in every way that mattered. Schvainese governors were appointed by the Clairdwell court. Schvainese taxes flowed to Clarity. Schvainese fishermen were conscripted into the Leimish navy.

For centuries, the Schvainese accepted this arrangement with the quiet resentment that characterizes people who know they are being taken for granted but cannot identify the precise moment when the taking began. The resentment accumulated like snow on a roof: imperceptibly, persistently, until the weight became unsupportable.

The rebellion began with a fishing tax. The Clairdwell court, straining under the costs of maintaining the Leimbordur garrisons and the Knights of Lambridge, imposed a new levy on Schvainese fishing catches. The tax was not large, but it was the final indignity for a population that had been providing fish, sailors, and soldiers to the kingdom for centuries without receiving proportional representation in return.

A fisherman named Colm Devane stood up in the Schvaine town assembly and said, in a speech that Klae reconstructed from six different oral accounts: 'We gave them an island to fight from, and they gave us a tax to pay. We sheltered their knights, and they sent us their governors. We are the cradle of Lambridge, and Lambridge has forgotten who rocked it.'

The assembly voted to withhold the tax. The Clairdwell court sent soldiers. The Schvainese met them on the docks, and the soldiers, who were Leimish and had Schvainese grandmothers, refused to fire.

The rebellion had begun, and it was the most dangerous kind: a rebellion that the oppressor's own people agreed with."""},

                {"title": "The Compromise of Tides",
                 "content": """The Schvainese Rebellion lasted two years and was resolved without a major battle, which is the most Leimish outcome imaginable.

The Clairdwell court was paralyzed. They could not crush the rebellion without crushing their own founding mythology, because every Leimish child grew up on stories of the Knights of Lambridge being sheltered on Schvaine, and sending an army to subjugate the islands would have been, symbolically, an act of national self-destruction. The knights themselves were divided: their code of honor demanded loyalty to the crown, but their origin story demanded gratitude to the Schvainese.

The Schvainese, for their part, did not want independence. They wanted recognition. They wanted representation in the Clairdwell court proportional to their contribution to the kingdom. They wanted their governors to be elected, not appointed. They wanted the fishing tax repealed, obviously. And they wanted an apology, which in Leimish culture carries more weight than a treaty, because a treaty can be broken but an apology, once given, becomes part of the historical record.

The resolution was called the Compromise of Tides, negotiated on a beach at low tide — literally between the worlds of land and sea, which the Schvainese insisted upon because they had a gift for symbolism that the mainland Leimish found simultaneously irritating and impressive.

The terms gave the Schvainese most of what they wanted. Elected governors. Proportional representation. The fishing tax was repealed and replaced with a voluntary contribution to the Leimish navy, which amounted to the same thing but was phrased differently, and phrasing matters to the Leimish. The Clairdwell king issued a formal statement acknowledging the debt that Lambridge owed to the Isles of Schvaine, which was not quite an apology but was close enough for the Schvainese to accept.

The Compromise of Tides was not a revolution. It was a correction — a small adjustment to a relationship that had been out of balance for centuries. Klae found it significant precisely because it was small. He wrote: 'The great revolutions get the histories. The small corrections get the results. The Schvainese did not overthrow their kingdom. They reminded it of its own principles, which is harder and more important.'"""}
            ]},

            {"number": 10, "name": "Tenth Century",
             "description": "The Long Shadow. The Gechann Empire reaches its maximum extent and begins to show the first signs of the decline that will define the next age. The conquered peoples are restless, the treasury is strained, the legions are spread thin across half the world. The Fourth Age ends not with a collapse but with a tremor — the first warning that the ground beneath the empire is not as solid as the marble of Palasor suggests.",
             "stories": [
                {"title": "The Cracks in the Marble",
                 "content": """At its height, the Gechann Empire controlled the entirety of the Geckish heartland, the Waydrani peninsula, northern Mural Cere, significant portions of coastal Metzerul, the former Kingdom of Vera, and a network of trade outposts, military bases, and colonial settlements that stretched from the frozen approaches of Raxone to the jungles of the Rim. On paper, it was the largest political entity in the history of Elysal.

Paper, as the empire was beginning to discover, is not the same as reality.

The cracks appeared first in the finances. The empire's economy was built on trade, tribute, and taxation, and all three were declining. Trade was disrupted by Karagonese competition and Raxonian piracy. Tribute from conquered territories was increasingly difficult to collect, because the populations of those territories had discovered that withholding payment was a form of resistance that did not require weapons. And taxation of the Geckish heartland itself was approaching the limit of what the population would tolerate, because even Gecks — who were culturally disposed to accept high taxes as the price of civilization — had a breaking point.

The legions were stretched thin. The professional army that had conquered half of Fondore now had to garrison it, and garrisoning is more expensive than conquering because it never ends. Every province required soldiers. Every border required patrols. Every colonial outpost required a detachment. The total military commitment had grown to over a hundred thousand men, and the empire's population, while large, was not inexhaustible.

The most dangerous crack was in the provinces themselves. The Waydrani, who had endured Geckish rule with characteristic quiet resistance, were producing a generation of intellectuals who wrote treatises on sovereignty and self-determination that circulated through the empire's own postal system. The Lirzan survivors in Metzerul had regrouped in the deep jungle and were launching raids against Geckish settlements. The Pervins of Epervinay, technically independent but hemmed in by Geckish military power, were building an army that would, in the next age, become the instrument of the empire's humiliation.

Klae, who had the advantage of writing from the far side of the empire's collapse, saw the pattern clearly. He wrote: 'The empire did not fall because it was attacked. It fell because it grew until it could no longer sustain its own weight, and the weight was not stone or marble but the accumulated resentment of every person who had been told that their subjugation was a form of civilization.'"""},

                {"title": "A Letter from the Frontier",
                 "content": """Klae found this letter in a Geckish military archive, filed under 'Miscellaneous Correspondence, Lirzan Frontier.' It was written by a Geckish centurion stationed in the jungle outpost of Vexillum, on the edge of Lirzan territory, sometime in the final decades of the Fourth Age. The intended recipient was the centurion's wife in Palasor.

'Talia,

I write this by lamplight because the jungle does not permit the luxury of daylight. The canopy above us is so thick that noon looks like dusk, and dusk looks like the inside of a tomb. I have been here for three years. My century is down to sixty-two men from the original hundred. The rest are dead, deserted, or invalided home with fevers that the physicians cannot name.

We are not fighting a war. A war has objectives, and we have none. We hold this outpost because we were ordered to hold it, and we were ordered to hold it because it appears on a map in Palasor, and the men who look at maps in Palasor have never been to a jungle and do not understand that a dot on parchment is not the same as a defensible position in a forest that is trying to eat you.

The Lirzans raid us every few weeks. They come at night, because they can see in the dark and we cannot. They kill one or two of our men, take what supplies they can carry, and vanish back into the trees. We cannot pursue them. We have tried. The jungle closes behind them like water behind a stone.

I do not hate the Lirzans. I understand this is an unusual statement for a man in my position. But I have been here long enough to understand what we did to them, and I have concluded that if someone had done to Gecha what we did to Lirza, I would be raiding their outposts too. This is not a popular opinion. I do not share it with my men.

I am told the empire is strong. I am told the Imperator has plans. I am told that our sacrifice serves a greater purpose. I believe the first two. I doubt the third. But I will hold this post because I was ordered to, and I am a Geck, and Gecks do what they are told until they are told something different.

Tell the children I am well. I am not, but tell them anyway.

Your husband, from the edge of everything.'

Klae published this letter as the final entry for the Fourth Age. He believed, and was probably correct, that the centurion on the frontier understood the empire's condition better than the Imperator in Palasor."""}
            ]}
        ]
    },
]

# Ages 5-8: structure in place, stories to be written
for age_data in [
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