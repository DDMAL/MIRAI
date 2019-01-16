---
title: Working with jSymbolic and ELVIS
layout: post
permalink: /blog/:title/
author: ehopkins
categories:
  - jSymbolic
  - Java
  - ELVIS
  - jMIR
---

Cory McKay is one of our SIMSSA Co-Investigators, and a professor at Marianapolis College. Along with Tristano Tenaglia, one of our research assistants, he’s been doing some great work with [jSymbolic](http://jmir.sourceforge.net/) software and ways of using it with our [ELVIS Project](http://elvisproject.ca/) tools. He presented his latest news at a lab meeting the other week and we’re sharing it with you here, too.

jSymbolic extracts statistical descriptors from symbolic music files. These descriptors include the familiar categories of pitch, melody, texture, rhythm, instrumentation, dynamics, and chords (coming soon!). Currently jSymbolic reads MIDI and MEI files, and saves features as ACE XML (with Weka ARFF and CSV coming soon).

![A sample of some of the information extracted.]({{ site.baseurl }}/assets/img/jSymbolicMendelssohn-20150806125434.jpg)

These features have some fun applications in terms of machine learning and doing research and analysis with ELVIS — check out Cory’s presentation below for more detail and some neat examples of what we can do.

[PDF]({{ site.baseurl }}/assets/files/jSymbolicELVIS.pdf) and [Powerpoint]({{ site.baseurl }}/assets/files/jSymbolicELVIS.pptx)



Up next Cory and Tristano are in the final stages of preparing a new release of jSymbolic. They’ll also be working towards enabling jSymbolic to read MEI neumes.
