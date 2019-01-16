---
title: "SIMSSA XVII: Infrastructure for Music Discovery"
layout: post
permalink: /blog/:title/
author: ehopkins
---

![]({{ site.baseurl }}/assets/img/group-shot-simssaxvii.png)

Earlier this month we had our seventeenth SIMSSA workshop, this time here at McGill in collaboration with [CIRMMT](https://www.cirmmt.org)). Sally Jo Cunningham gave a CIRMMT Distinguished Lecture earlier that week on [Engagement with Personal Music Collections](https://www.cirmmt.org/activities/distinguished-lectures/sally-jo-cunningham) which inspired our theme: Infrastructure for Music Discovery. We had 19 different speakers covering everything from OMR to library reference models to linked data to country music! Here is a roundup of all the presenter's slides and some pictures from the event.

To start the day, Ichiro Fujinaga gave us an overview of the project, including the most recent workshops and other activities. (Slides: [PDF]({{ site.baseurl }}/assets/files/fujinaga1-simssaxvii.pdf)). After that, I (Emily Hopkins) gave an introduction to the different components of the SIMSSA project, explaining how they all come together in context. (Slides: [Powerpoint]({{ site.baseurl }}/assets/files/hopkins1-simssaxvii.pptx) and [PDF]({{ site.baseurl }}/assets/files/hopkins1-simssaxvii.pdf))

Next, we had several updates from students working in the DDMAL labs on various parts of our OMR processes. Minh Anh Nguyen presented her work on the [Interactive Classifier](https://github.com/DDMAL/Interactive-Classifier). (Slides: [Powerpoint]({{ site.baseurl }}/assets/files/nguyen-simssaxvii.pptx) and [PDF]({{ site.baseurl }}/assets/files/nguyen-simssaxvii.pdf))

![]({{ site.baseurl }}/assets/img/nguyen-simssaxvii.png)


Then, Noah Baxter gave us a look at his recent progress on the pitch finding part of the process, including [diagonal neume slicing](https://github.com/DDMAL/diagonal-neume-slicing) and converting [JSON OMR files to MEI](https://github.com/DDMAL/JSOMR2MEI). (Slides: [PDF](({{ site.baseurl }}/assets/files/baxter-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/baxter-simssaxvii.png)

Next up is our ground truth image editor, [Pixel.js](https://github.com/DDMAL/Pixel.js) -- originally developed by Zeyad Saleh and Ké Zhang, most recently developed by Eric Liu. Our postdoc Gabriel Vigliensoni gave this presentation. (Slides: [PDF]({{ site.baseurl }}/assets/files/vigliensoni-simssaxvii.pdf))

After that, Tim De Reuse showed his most recent work developing a process for aligning musical texts with notation. (Slides: [Powerpoint]({{ site.baseurl }}/assets/files/de_reuse-simssaxvii.pptx) and [PDF]({{ site.baseurl }}/assets/files/de_reuse-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/de_reuse-simssaxvii.png)

Zoé McLennan and Juliette Regimbal presented their latest work on [Neon](https://github.com/DDMAL/Neon2), a web-based neume editor that uses [Verovio](http://www.verovio.org/index.xhtml) to render the music. (Slides: [PDF]({{ site.baseurl }}/assets/files/mclennan-regimbal-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/mclennan-simssaxvii.png)
![]({{ site.baseurl }}/assets/img/regimbal-simssaxvii.png)

Alex Daigle then gave us an overview of [Rodan](https://github.com/DDMAL/Rodan), which is our web-based workflow manager for the OMR process. (Slides: [Powerpoint]({{ site.baseurl }}/assets/files/daigle-simssaxvii.pptx) and [PDF]({{ site.baseurl }}/assets/files/daigle-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/daigle-simssaxvii.png)


Néstor Nápoles showed off his recent work on the [Cantus Editor](https://github.com/DDMAL/CantusEditor), working for [Cantus Ultimus](https://cantus.simssa.ca/). He also showed off the [Cantus Index](cantusindex.org) site, which brings many different chant collections (including the [Cantus Database](http://cantus.uwaterloo.ca/)) together. (Slides: [PDF]({{ site.baseurl }}/assets/files/napoles-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/napoles-simssaxvii.png)

[IIIF](https://iiif.io/) is already an important part of SIMSSA's infrastructure, and we've also been working with the British Library on developing the [IIIF AV player](https://github.com/DDMAL/IIIF-AV-player) for the new IIIF audio/visual support. Andrew Kam demonstrated his work on the player. (Slides: [Powerpoint]({{ site.baseurl }}/assets/files/kam-simssaxvii.pptx) and [PDF]({{ site.baseurl }}/assets/files/kam-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/kam-simssaxvii.png)


Martha Thomae is doing her dissertation on applying our OMR processes as well as her [Scoring-Up tool](https://github.com/ELVIS-Project/scoring-up) to musical manuscripts from her home country of Guatemala. She gave us an overview of the process involved, including working with different organizations in Guatemala and learning how to photograph scores for preservation. (Slides: [Powerpoint]({{ site.baseurl }}/assets/files/thomae-simssaxvii.pptx) and [PDF]({{ site.baseurl }}/assets/files/thomae-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/thomae-simssaxvii.png)

Matan Gover developed a musical query language as part of a class with Ichiro last year, and demonstrated it for us today. Instead of using text to query music, why not use actual music? Seen here is Craig Sapp's [Verovio Humdrum Viewer](http://verovio.humdrum.org/) in action. (Slides: [Keynote]({{ site.baseurl }}/assets/files/gover-simssaxvii.key) and [PDF]({{ site.baseurl }}/assets/files/gover-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/gover-simssaxvii.png)


David Garfinkle talked about his work on [PatternFinder](https://github.com/ELVIS-Project/PatternFinder), our melodic search technology. In addition to handling one-voice (monophonic) melodic search, David's implementation can also find melodies distributed across multiple voices (polyphony). (Slides: [Powerpoint]({{ site.baseurl }}/assets/files/garfinkle-simssaxvii.pptx) and [PDF]({{ site.baseurl }}/assets/files/garfinkle-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/garfinkle-simssaxvii.png)

[Eamonn Bell](https://music.columbia.edu/bios/eamonn-bell) is a PhD student at Columbia and came to the workshop as a visiting guest. He shared his work gamifying crowdsourced machine learning ground truth development (Slides: [PDF]({{ site.baseurl }}/assets/files/bell-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/bell-simssaxvii.png)

Julie Cumming presented her work with Cory McKay, using [jSymbolic](http://jmir.sourceforge.net/jSymbolic.html) to explore questions and assumptions about the origins of the madrigal. This included ways in which jSymbolic both confirmed and challenged Julie's predictions, and leads us to a lot of interesting new things to explore. (Slides: [Powerpoint]({{ site.baseurl }}/assets/files/cumming-mckay-simssaxvii.pptx) and [PDF]({{ site.baseurl }}/assets/files/cumming-mckay-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/cumming-simssaxvii.png)

Audrey Laplante gave a presentation on the social barriers researchers face to doing digital scholarship. What sorts of rewards or consequences await those who are doing things differently? Computer use is sometimes still seen as a shortcut, or as shallower engagement than traditional scholarship. (Slides: [Slideshare](https://www.slideshare.net/audreylaplante1/social-barriers-to-digital-scholarship-for-arts-and-humanities-researchers))
![]({{ site.baseurl }}/assets/img/laplante-simssaxvii.png)

Next up, we were delighted to have special guest [Jada Watson](https://uniweb.uottawa.ca/members/2879) come give a talk about her research. She is a Professor at the University of Ottawa, and shared her research using discographic metadata to study identity in country music. She introduced us to her [SongData](https://songdata.ca/) project, studying genres and networks through data. (Slides: [Powerpoint]({{ site.baseurl }}/assets/files/watson-simssaxvii.pptx) and [PDF]({{ site.baseurl }}/assets/files/watson-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/watson-simssaxvii.png)


The final set of presentations concerned the new SIMSSA Database. A successor of the ELVIS database, it's designed to make symbolic files accessible and reusable. First I (Emily Hopkins) gave an introduction of our data model. This was originally developed by Cory McKay and presented at DLfM ([McKay et al, 2017](https://simssa.ca/publications)). This included an comparison with the [IFLA-LRM](https://www.ifla.org/publications/node/11412) in terms of describing a "musical work", as well as how we track provenance and out feature-based content search. (Slides: [Powerpoint]({{ site.baseurl }}/assets/files/hopkins2-simssaxvii.pptx) and [PDF]({{ site.baseurl }}/assets/files/hopkins2-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/hopkins-simssaxvii.png)

Next up, Gustavo Polins Pedro and Yaolong Ju introduced the actual interface for the database. This included our search and upload functions, as well as the ways we use Wikidata, VIAF, and various controlled vocabularies to try to improve the quality and interoperability of our content. (Slides: [Keynote]({{ site.baseurl }}/assets/files/ju-polins_pedro-simssaxvii.key) and [PDF]({{ site.baseurl }}/assets/files/ju-polins_pedro-simssaxvii.pdf))
![]({{ site.baseurl }}/assets/img/polins_pedro-simssaxvii.png)
![]({{ site.baseurl }}/assets/img/ju-simssaxvii.png)

Finally, Ichiro gave a big-picture presentation about building a larger infrastructure for music discovery, connecting all the different sources available out there and making them queryable. (Slides: [PDF]({{ site.baseurl }}/assets/files/fujinaga2-simssaxvii.pdf)). We then ended the day with a group discussion.
![]({{ site.baseurl }}/assets/img/fujinaga-simssaxvii.png)


Thanks so much to everyone who presented, and special thanks to Vi-an Tran, Martha Thomae, Néstor Nápoles, and Yaolong Ju for their help with set-up, lunch, photos, note-taking, and more.

Happy Holidays to those celebrating, and see you in 2019!
