---
title: 'Building the OMR Workflow: Workshop on SIMSSA XII'
layout: post
permalink: /blog/:title/
author: ehopkins
categories:
- IIIF
- OMR
- Pixel.js
- Neon.js
- machine learning
- workshops
- free software
- open source
- DIAMM
- Verovio
- Verovio Humdrum Viewer
- scoring up
- digital humanities
upload: ""
---

On August 7, 2017, we held the twelfth workshop on SIMSSA at the Schulich School of Music here in Montreal. Many of our SIMSSA Community members were in town for [DH2017](https://dh2017.adho.org/) so it was a great opportunity to share what everyone's been working on, including the progress from our [DDMAL summer development team](https://simssa.ca/blog/introducing-the-ddmal-summer-workers).

We started the morning with an introduction to the SIMSSA Project from Prof. Ichiro Fujinaga, who also introduced our keynote, SIMSSA Collaborator Craig Sapp. Craig gave a keynote introducing the [Verovio-Humdrum Viewer](http://verovio.humdrum.org/). This online viewer allows users to edit a kern or MEI file and see changes in the score in real time, as well as other features demonstrated in his slides [here](https://docs.google.com/presentation/d/1QR-XkMbJrqgmG5Hxyysf1SxObW7SR_WC0LO3Mh-L7Qs/edit#slide=id.p6). Below, the top voice of a Bach chorale is extracted for study in the viewer:

![]({{ site.baseurl }}/assets/img/bach-verovio.png)

Then, we had two more featured speakers. Andrew Hankinson, former SIMSSA postdoc and newly official SIMSSA Collaborator, now working for new SIMSSA Partner the [Bodleian Libraries](http://www.bodleian.ox.ac.uk/), gave a talk on _Building the New DIAMM: Linking and Sharing Data for Medieval Musicology_. Alex Morgan, former SIMSSA researcher and now a postdoc at the L’université libre de Bruxelles, gave us a presentation on _Cross-Platform Analysis: Combining Music Analysis Programs_. Check out his slides [here]({{ site.baseurl }}/assets/files/CrossPlatformAnalysis.pdf).

The next section of the workshop featured presentations from two of our postdocs and our summer DDMAL development team,
working on different parts of the Optical Music Recognition (OMR) workflow that is key to SIMSSA's ability to use digital images of scores for search and analysis.

First, SIMSSA Postdoc Gabriel Vigliensoni gave us an overview of the whole OMR process, outlining how the different components fit together. Next up, Jorge Calvo-Zaragoza (SIMSSA Postdoc, most recently from the [University of Alicante](https://www.ua.es/en/)) presented his most recent work in OMR and document analysis. He highlighted his pixelwise and image-to-image classification methods (see image below) and what that means for our processes. You can see his whole presentation [here]({{ site.baseurl }}/assets/files/jcalvo-simssa_xii-slides.pdf).

![]({{ site.baseurl }}/assets/img/jcalvo-simssa_xii-feature.png)

The next three presentations came from our pairs of developers working on different OMR applications this summer. First, Ké Zhang and Zeyad Saleh presented their work on [Pixel.js](https://github.com/DDMAL/Pixel.js). This web-based application can be used in the creation and correction of ground-truth images for training the OMR process. Check out their presentation [here]({{ site.baseurl }}/assets/files/Pixel_js_SimssaXII_Presentation.pdf).

Next, we heard from Sacha Perry-Fagant, presenting on behalf of her team including Alex Daigle. They worked on [Rodan](https://github.com/DDMAL/Rodan) and the [Interactive Classifier](https://github.com/DDMAL/Interactive-Classifier). This web-based application allows human users to insert themselves in the OMR process. The workflow outputs a set of classified glyphs, which can then be expanded or corrected by a human user and re-entered into the workflow to process more music, allowing us to train our classifier as we go. Below, you can see a screenshot -- the human-identified neumes are in green, and those the computer has classified are yellow. Check out their slides [here]({{ site.baseurl }}/assets/files/Interactive_classifier_presentation.pdf).

![]({{ site.baseurl }}/assets/img/IC-pic.png)

The next step in the OMR process is pitch-finding, after which an [MEI](http://music-encoding.org/) file is generated. However, there are usually still inaccuracies at this stage. [Neon.js](http://ddmal.github.io/Neon.js/) is designed to make the correction process fast and simple, with a visual interface that allows for corrections to the MEI file in real time. Designed for square notation, this latest version of Neon draws on early work from [Greg Burlet](https://github.com/gburlet) and [Alastair Porter](https://github.com/alastair), and will soon integrate with [Verovio](http://www.verovio.org/index.xhtml). You can view their slides [here]({{ site.baseurl }}/assets/files/Neon-SIMSSAXII.pdf).

Finally, the music search: David Garfinkle demonstrated his latest work on implementing music searching algorithms using music21. In [PatternFinder: Content-based music retrieval with music21]({{ site.baseurl }}/assets/files/PatternFinder.pdf), David introduced seven algorithms for different kinds of content-based music retrieval, and demonstrated how he's implemented them.

In the last section of the presentation, we heard about some more analysis-oriented projects. Yaolong Ju presented his work on using machine learning for harmonic analysis for Bach chorales in [Non-chord Tone Identification]({{ site.baseurl }}/assets/files/Non-chord-ToneID.pdf).

In [Using statistical extraction and machine learning in music research]({{ site.baseurl }}/assets/files/mckay17statistical.pdf), Cory McKay discussed the concept of "features" from a machine learning perspective, gave some updates on [jSymbolic2](http://jmir.sourceforge.net/index_jSymbolic.html), and presented a composer attribution study looking at Josquin, Ockeghem, and LaRue.

Cory also presented Claire Arthur's latest research on her behalf, as she was presenting at the [Society for Music Perception and Cognition Conference](http://smpc.ucsd.edu/) at the same time. Claire's paper, [Renaissance Counterport in Theory and Practise: a Case Study]({{ site.baseurl }}/assets/files/ClaireArthur_SIMSSAXII.pdf), focussed on examining the relationship between Renaissance harmonic treatises and Renaissance harmonic practise, looking specifically at the treatment of direct octaves and fifths.

Finally, Martha Thomae presented her [Automatic Scoring-Up Tool for Mensural Music]({{ site.baseurl }}/assets/files/MarthaThomae-ScoringUp.pdf), focussing on the work of her master's thesis. This tool can take a partbook in mensural notation, with each voice in a separate part of the page:

![]({{ site.baseurl }}/assets/img/partbook-blog.png)

And transform it into a score that's much easier to read, study, and perform from. Here it's shown rendered in [Verovio](http://www.verovio.org/index.xhtml):

![]({{ site.baseurl }}/assets/img/scored-up.png)

This task involves going beyond simply transcribing all the parts together on a modern staff -- unlike the common music notation developed later on, many of the rhythmic values in mensural music are context-dependent.

The workshop was a great way to round out a busy summer in the lab, and we're looking forward to seeing what the new school year has in store for SIMSSA!
