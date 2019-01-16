---
title: 'CIRMMT Workshop: Masataka Goto visits McGill'
layout: post
permalink: /blog/:title/
author: ehopkins
categories:
  - CIRMMT
  - Diva
  - Diva.js
  - cantus ultimus
  - UI
  - UX
  - interface
  - github
  - IIIF
upload: ""
---

As part of [CIRMMT’s Distinguished Lectures series](http://www.cirmmt.org/activities/distinguished-lectures), [Masataka Goto](https://staff.aist.go.jp/m.goto/) visited McGill University. He gave a talk on Thursday afternoon, and the next day introduced the[ _CIRMMT Workshop on usability and user experience for music information systems_](http://www.cirmmt.org/activities/workshops/research/usability2015/hpp) where many SIMSSA researchers and developers also presented.

Dr. Goto's Thursday lecture on [“Frontiers of Music technologies: Singing synthesis and active music listening”](http://www.cirmmt.org/activities/distinguished-lectures/goto) covered many different aspects of music technology, both in terms of music creation and appreciation. The music creation part included the singing synthesis system [VocaListener](https://staff.aist.go.jp/t.nakano/VocaListener/), the robot singer system [VocaWatcher](https://staff.aist.go.jp/t.nakano/VocaWatcher/) (pictured below), and a discussion of the influence of singing synthesis superstar [Hatsune Miku](http://vocaloid.wikia.com/wiki/Hatsune_Miku).

![]({{ site.baseurl }}/assets/img/vocawatcheryoutube.png)
Screenshot from [VocaWatcher demonstration on Youtube](https://www.youtube.com/watch?v=wJ5IYs6CATkhttp://)

On the music appreciation side, we were introduced to [Songle](http://songle.jp/), an active music listening web service, and [Songrium](http://songrium.jp/), oriented towards music browsing.

The next day, Dr. Goto introduced the CIRMMT _Workshop on usability and user experience for music information systems_.  Since user interfaces are a huge part of what we work on at SIMSSA, several of our developers, researchers, and software testers had a chance to present on their work.

First, Nina Penner and I (Emily Hopkins) gave a presentation called [“Musicologists on GitHub: User experience and the ELVIS Database.”]({{ site.baseurl }}/assets/files/MusicologistsOnGitHubCIRMMTSept25.pdf) We discussed  our experience helping to test the [ELVIS Database](http://database.elvisproject.ca/) and demonstrated some of the new features we influenced as testers. We discussed learning to use [GitHub](https://github.com/) to report issues that arose during testing, trying to bridge the gap between music researchers (who aren't necessarily coders) and developers (who aren't always music specialists).

![]({{ site.baseurl }}/assets/img/ninaascii.png)
_Nina makes sure we can enter all the characters required for entering composer and piece names properly._
<br>
<br>
Next, Alex Parmentier offered the developer’s perspective on the the same project in [“ELVIS database: Challenges in designing intuitive UI for crowd-sourced content.”]({{ site.baseurl }}/assets/files/AlexP.pdf) In particular, he talked about some of the conceptual work that went into the most [recent database changes](https://simssa.ca/blog/elvis-database-better-than-ever), in particular how to manage the differences between our mental models of musical information (on the left) and how the database stores that same information (on the right).

![]({{ site.baseurl }}/assets/img/mentalvsdatabase.png)

Designing a good interface means bridging the gap between these models so that our users are able to understand and start using the database quickly and intuitively.

Later, Reiner Krämer showed us some of his recent research, inspired by searching the ELVIS database and imagining new ways of visualizing data in [“Mapping Melodic Successions: Josquin’s Four-Voice Motets.”]({{ site.baseurl }}/assets/files/Reiner.pdf) Drawing on [Donald Knuth's](http://www-cs-faculty.stanford.edu/~uno/) work in using state transition networks (STN) to map character relations in _Les Misérables_, Reiner is mapping melodic successions with an eye towards expanding the process to study voice leading. Here's a screenshot of Josquin's _Ave maria...virgo serena_, showing the melodic succession network for the soprano part.

![]({{ site.baseurl }}/assets/img/avemaria.png)

The actual STN is visualized using [D3.js](http://d3js.org/), and is interactive: you can zoom in and out, and change the location of pitches. This visualization is very flexible, and can be extended to represent horizontal and vertical intervallic data and voice-leading procedures.

Other projects from our lab were featured, too, with presentations on the Cantus Ultimus project and [Diva image viewer](http://ddmal.github.io/diva.js/). William Bain talked about “Designing for usability in the Cantus Ultimus Project”, covering recent improvements to the interface for the [Cantus website](http://cantus.simssa.ca/). Additionally, Evan Magoni talked about his work on our image viewer [Diva](http://ddmal.github.io/diva.js/) (pictured below) in [“Fitting manuscripts into the browser with Diva.js: Building an intuitive interface for exploring virtual documents”]({{ site.baseurl }}/assets/files/EvanMagoni.pdf).

![]({{ site.baseurl }}/assets/img/diva.png)

He compared several different models of online document viewers, including the [Internet Archive](https://archive.org/index.php), [Early English Books Online](http://eebo.chadwyck.com/home), [e-codices](http://www.e-codices.unifr.ch/en), and the [Qatar Digital Library](http://www.qdl.qa/en). He highlighted how these viewers compare with Diva, including some of Diva's advantages and goals for the future. (Highlights of our most recent release were detailed in a [previous post](https://simssa.ca/blog/new-release-diva-js-4-0).)

In addition to the software development and testing team, information science researchers also contributed to the presentations. Ariane Legault-Vienne and Audrey Laplante, both from the [École de bibliothéconomie et des sciences de l'information](http://www.ebsi.umontreal.ca/accueil/) at the [Université de Montréal](http://www.umontreal.ca/), discussed an important interface for music research in “Searching for music materials in libraries: Discovery tools as seen through the eyes of users.” The final contribution was from David Weigl and Catherine Guastavino, “Applying the stratified model of relevance interactions to music information retrieval.” They surveyed existing literature to identify gaps in the research on different kinds of music information retrieval.

After the presentations, Masataka Goto led us in a round-table discussion of “Grand challenges in music research in the 21st century.” Great thanks to Masataka Goto and CIRMMT, and to all our presenters as well!  
