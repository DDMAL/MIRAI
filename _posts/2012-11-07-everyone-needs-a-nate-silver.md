---
title: Everyone needs a Nate Silver
author: Catherine Motuz
layout: post
permalink: /blog/:title/
---

As Nate Silver wowed the world last week with his statistical prowess, proving triumphantly that for all the value we place on our gut instincts, they don't compare with mathematics when it comes to, say, predicting election results. Keeping this in mind, as the first strings of numbers pour out of VIS, our current task is learning how to interpret them. Following Ichiro Fujinaga's maxim "Never reinvent the wheel," the ELVIS team is happy to have among us Jamie Klassen, a BA student in mathematics and statistics, as well as Alex Morgan, a music theory graduate student with math proficiency, and Prof. Jon Wild, who did his bachelor degrees at McGill in both music and physics.

The numbers produced by VIS queries are called [n-grams](http://en.wikipedia.org/wiki/N-gram), with N representing the number of successive vertical intervals represented. The most basic n-gram in ELVIS is the 2-gram, made up of two successive intervals and represented by three numbers: 1-the first vertical interval, 2-the melodic interval of the lower voice, and 3-the second vertical interval (the melodic interval of the top voice can be deduced from the others). Thus, a parallel fifth on a rising second would be represented as follows: 5 +2 5. A 3-gram will add one more vertical interval, and by extension, another melodic one too. 5 +2 5 +2 5 indicates that both voices have again risen by a step to land on a fifth.

The point of converting 2-voice samples of music into number-units is that from a statistical viewpoint, we reckon that these structures represent a level similar to that of the unit of the word in linguistic theory. This means that we can put the developments of the relatively new field of linguistic analysis to use in understanding music. The idea is an old one—Pedro Cerone, 1613, writes  “Just as we need only 22 letters to make thousands of orations, we only need 22 intervals to make all music.”

This sequence of numbers is an extreme case: as a single parallel fifth is forbidden in renaissance counterpoint, and as the sample 3-gram involves two in a row, already we can say with a high degree of confidence that the piece is about as likely to belong to the Renaissance as the now English word "[LOL](http://www.urlesque.com/2010/09/17/bff-lmao-interweb-oxford-dictionary/)". Of course most n-grams we run across will not involve such drastic moves, but perhaps the linguistic equivalents of "you" and "thou", both of which have been used in the last 500 years but to highly varying degrees, and perhaps more pertinently, in combination with vastly different vocabularies.

While we can now see at a glance, thanks to the graph output programmed into VIS, what are some of the most and least popular n-grams in a given piece, the trends we can garner from these are of limited utility. On a statistical level, it may be more effective to plot n-grams onto distribution curves, to see for instance, if certain composers tend to repeat their structures more or less often than others or if some use a wider vocabulary in general. These elements would also affect the predictability of composers, which is expressed in statistics as "entropy".

As Alex explained on our forum, "The entropy of a given interval class in a given voice pair (let's say a fifth between tenor and bass) tells us how predictable the next interval will be." The lower the number, the more predictable the next interval would be. In certain kinds of organum, for instance, where fifths are always followed by other fifths, the entropy would be zero. In renaissance polyphony, many intervals can follow a fifth and the entropy of is higher. Jon Wild explained how the calculations are used in linguistics to show the predictability of a word following another:

"Example :

after word "a" the possible outcomes are "b" with 50%, "c" with 35%, "d" with 10% and "e" with 5%.
The entropy is (0.5 * log(0.5)) + (0.35 * log(0.35)) + (0.1 * log (0.1)) + (0.05) * log(0.05)) = -1.09...
Then multiply by -1 to get a positive value: 1.09..."

Once we have figured out the best way of calculating statistics, we need to find visual representations of our data which are intuitively understandable as well as containing exact data, so that those without a statistical background can parse them but those with will not find them too simplified. Fortunately, most graphs do just that. We are beginning to explore the possibilities, from simple charts to [Voronoi diagrams](http://en.wikipedia.org/wiki/Voronoi_diagram) and "word" clouds like the one I described earlier this year. Indeed, there is a lot of work ahead of us here, and it's among the most important yet—we look forward as much to making sense of our data as we did to watch the first n-grams come into being.
