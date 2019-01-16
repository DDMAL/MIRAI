---
title: Introducing "VIS"
author: Catherine Motuz
layout: post
permalink: /blog/:title/
---

In a collaborative project between musicologists and computer programmers, there is a decision to be made about who learns what. Should programmers learn enough about music that they can translate the questions of musicologists into code, or should musicologists and theorists learn how to use analytic software such as music21 (which involves some basic programming skills) in order to ask their own questions? The time commitment is enormous on both sides.

Even Humdrum, whose music encoding notation is so intuitive that it is possible to sing or play directly from it, starts to look technical when it comes to asking questions. For instance, this is how one would search a piece for French 6th chords:

solfa file | extract -i '\**solfa' | ditto | grep '6-.\*4+' | grep 2

The advantage to this system is that one can ask basically anything, but the disadvantage is that it requires a 40-chapter handbook. Some of us figure it out eventually, but the combination of the time it takes to input pieces and the skill it takes to write queries has proved too daunting for many a music scholar. A few newer developments such as the MIDI to Humdrum converter has made the process of building a corpus much quicker, but the theorist or musicologist who can use the Humdrum toolkit in even a simple way remains the exception.

All this is of course to emphasize just how lucky the ELVIS project has been to recruit Chritopher Antila, a music theory student who learned to program in recent years during his studies at Waterloo University. Christopher became our music21 expert this summer, putting his skills into learning both the program and its language (python). This allowed him not only to put the first musical queries into music21 but, realizing the need for musicologists and theorists to do this on their own, to build a GUI, or Graphical User Interface, for the parts of music21 that pertain to ELVIS research. This gives the non-technical team a less daunting learning curve and will allow us very soon to all ask questions to the data set.

Christopher's program is called "VIS," which stands for "vertical interval sequences" and means "power" in Latin. It includes a form to fill out to conduct the processes of uploading and analyzing files in music21, and what is even better, is able to convert the results of queries back into music notation using [Lilypond](http://www.lilypond.org/), a music typesetting program, as well as into helpful graphs. This is what musicologists and theorists dream of! Being a theorist himself, Christopher was able to optimize the GUI to ask the questions that matter most. But enough for an introduction please do take a tour of his work! A description of VIS as well as the very first query results can be found on [Christopher's own web page](https://web-crantila.rhcloud.com/?q=node/5).

Anyone interested in the VIS files themselves can visit the [VIS github](https://github.com/crantila/vis).
