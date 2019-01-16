---
title: Gearing up to show SIMSSA to the world
layout: post
date: 2011-11-04 12:00:00 +0000
permalink: /blog/:title/
author: cmotuz
---

It's been a busy week here in the lab as we all prepare for the presentation of the SIMSSA project at the [AMS Conference](http://www.ams-net.org/sanfrancisco/) next week.

Our .tiff files have arrived and Remi and Laura have been back in [gamera](http://gamera.informatik.hsnr.de/), once again teaching the computer to distinguish between a podatus and a c-clef, a custos and a punctum inclinatum, and pitches in general from the random specs of dirt and discolouration on each page of music. I had a go on the program too at last, only to find myself proceeding at a snail's pace in comparison to the other two. When I complained, Laura came in and showed me a myriad tricks and shortcuts she had found to speed things up, in particular how to tell the computer to approve the classification of many instances of the same object at once instead of sorting through one by one. Instantly my time was cut into a third of what it was before - thank you Laura!

But mostly I've been filling my role as a resident musicologist, learning the finer details of chant classification and how to pass on that knowledge in terms a computer can understand. Especially interesting has been expanding the numbers in the "Position" column of the Salzinnes catalogue. For instance, when the computer sees a number "#": IF genre is H or V, THEN # = "verse #" EXCEPT when cantus number is can9000, THEN it's "doxology." Andrew has programmed these instructions so that not only are the abbreviations for each chant expanded into prose (see Oct. 18 post for an example), but some of the fields are searchable. Meanwhile Alastair has been programming the computer to be able to search the full texts to the chants in Salzinnes. The next step is to integrate everything together into [DIVA](http://ddmal.github.io/diva.js/), so that searching and browsing can happen within the same system. Today we need to put ourselves in the mindframe of a chant specialist, to try to predict what priorities people may have when looking up information.
