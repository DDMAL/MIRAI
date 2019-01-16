---
title: JPEGs vs TIFFs and browsing the Cantus Database
layout: post
date: 2011-10-11 12:00:00 +0000
author: cmotuz
permalink: /blog/:title/
---

First of all, a hearty congratulations to SIMSSA's Wendy Liu and lab-partner Saining Li for their [good citizenship award at the Montreal Hackathon](http://www.mcgilldaily.com/2011/10/coding-coffee-and-concrete-innovation/), for improving their wikinotes.ca site to make note sharing more accessible to students.

The question of the week is: How does the quality of an image affect a computer's success at Optical Music Recognition (OMR)? Most of the images of music put up on the Internet are in the forms .jpeg or .pdfs that began their existence as .jpeg files. The problem with .jpeg is that it involves "lossy compression," or compression by discarding bits of data. Jpegs are clever because they discard data that the eye tends not to notice at a distance or in web viewing, but when we try to manipulate the file or blow it up to many times its size, this loss of data becomes apparent: little halos appear around notes and, most importantly to OMR, faint items such as the stems of neumes can become unclear. While OMR will eventually work even on images of lower quality, after cataloguing the first 28 jpegs from the [Salzinnes Antiphonal](http://salzinnes.simssa.ca/), we've decided that it would be worth teaching the computer based on the highest quality images we can get hold of to begin with, and will be starting again using uncompressed .tiff files.

While waiting for these files to arrive (they are so big it makes most sense to send them on CDs by post than to upload them!), I took a look at the information we have on the texts in the Salzinnes Antiphonal - what could be a daunting task were it not for the [CANTUS Database](http://cantusdatabase.org/). Here, thanks again to the work of Judy Dietz and her team, I found that every chant in Salzinnes has been catalogued with the ms page number, feast, genre, transcription of the manuscript text and much more all available for download. Most useful to us at this point is the text transcriptions, but how the information will be integrated into the whole project has yet to be seen.
