---
title: 'Reanimating Corpora: SIMSSA and DREaM'
layout: post
permalink: /blog/:title/
author: ehopkins
categories:
  - DH
  - Digital Humanities
  - DREaM
  - VIS
upload: ""
---

Last Thursday, SIMSSA participated in the Works in Progress series for [McGill Digital Humanities](http://digihum.mcgill.ca/), alongside the [DREaM Project](http://earlymodernconversions.com/introducing-dream/). In "Reanimating Corpora: The Single Interface for Music Score Searching and Analysis (SIMSSA) and Distant Reading Early Modernity (DREaM)", researchers from DREaM and SIMSSA shared some of their latest developments and talked about challenges in common when making decisions about how to organize large corpora, whether written texts or musical scores.

SIMSSA started things off, with an [overview of SIMSSA]({{ site.url }}/assets/files/fujinaga15DHWiP1.pdf) presented by Ichiro Fujinaga, our PI and Content Axis leader. He discussed the process of Optical Music Recognition, and what goes into developing the viewing and searching capacities for the interface we're working towards.

Next up, Alexander Morgan gave a presentation on ["Integral Analysis in VIS."]({{ site.url }}/assets/files/AlexMIntegralAnalysisDHNov2015.pdf) He talked about clustering composers' work by comparing the similarity of the intervallic content of their works, demonstrating this technique with a comparison of duets by Josquin, Lassus, and Morley. Below is the heat map view of the duets' similarities to each other.

![]({{ site.url }}/assets/img/heatmapfull.png)

The last SIMSSA presentation, from Reiner Krämer, was on ["Markov Models and Renaissance Music: Re-examining Four-Voice Motets by Josquin."]({{ site.url }}/assets/files/ReinerMarkovModelsDHNov2015.pdf)  Reiner first gave some examples from literature analysis of statistical modelling of texts: Markov's analysis of consonant and vowel relationships in Pushkin's Eugene Onegin, and Donald Knuth's mapping of relationships between characters in _Les Misérables_ in a State Transition Network (STN). Below is the map depicting interactions between characters in Victor Hugo's novel:

![]({{ site.url }}/assets/img/lesmismap.png)

He then talked about how Markov chains and STNs can be used to model any kind of relationship, including those between pitch, rhythm, and other factors that make up music. Reiner showed us the State Transition Matrices, and then networks, that he built based on motets composed by (or at least attributed to) Josquin, mapping the probability of different melodic intervals. Below is the State Transition Matrix, colour-coded to show probability.

![]({{ site.url }}/assets/img/josquinstm.png)

The second half of the event featured Stéfan Sinclair and Matt Milner giving us an update on the [DREaM Project](http://earlymodernconversions.com/introducing-dream/) (Distant Reading Early Modernity). This project is focussed on working with written texts, but there are many parallel concerns in terms of Optical Character Recognition and organizing large corpora.

Stéfan Sinclair talked about the [Early Modern Conversions](http://earlymodernconversions.com/) project, as well as working with [EEBO (Early English Books Online)](http://eebo.chadwyck.com/home) . Specifically, he discussed the challenge of searching texts from an era before English spelling was standardized, and the process of spelling normalization. [VARD 2](http://ucrel.lancs.ac.uk/vard/about/) is software designed to help deal with spelling variations. It uses a dictionary to compare spellings and allows words to be tagged with other spellings so that they can be searched for with alternate spellings more readily.

![]({{ site.url }}/assets/img/vard.png)

The question of how to capture the process of improvement came up as well -- when corrections are made, how do we share the new versions? How do we keep track of when and how edits were made? The DREaM Project (check out their demo video [here](http://earlymodernconversions.com/digital-humanities/demo-video-for-the-dream-project/)) is built on a web-based text analysis suite to allow search results to be downloaded and used in [Voyant](http://voyant-tools.org/), a web-based reading and analysis environment for digital texts.

[![]({{ site.url }}/assets/img/voyant-see.png)](http://voyant-tools.org/)

Next, Matt Milner spoke from his perspective as a historian about the need to critique our metadata: who decides what is correct? Are we keeping track of corrections as we make them? How trustworthy are assertions about authorship, for example? He also talked about trying to parse information in the publishing details of a text to derive the address. In order to build an appropriate [regex](https://en.wikipedia.org/wiki/Regular_expression) for searching a text, decisions must be made about the nature of the object you're searching for. In this process, there are interesting implications in terms of how we define what an "address" is throughout history.

After, there was a chance to discuss some further questions and common threads between SIMSSA and DREaM. In particular, OCR/OMR progress, procedures for tracking edits to materials as their digitized forms are improved, and better collaborations with libraries and librarians. We also discussed the potential for future collaborations between various [Digital Humanitie](http://digihum.mcgill.ca/)s projects at McGill... in the meantime, you should check out [some of the other DH projects at McGill](http://digihum.mcgill.ca/) and some great [Digital Humanities tools](http://digihum.mcgill.ca/resources/tools/).
