---
title: JavaScript Image Processing Modules for Rodan
layout: post
permalink: /blog/:title/
date: 2012-07-03 12:00:00 +0000
author: Brian Stern
---

This post will present a suite of JavaScript-based image processing modules, designed to operate on scaled-down versions or full-size portions of high-resolution music score images. These modules include binarisation, rotation, cropping, segmentation (for staff removal), and despeckling. For the Rodan project, it is essential to enable the users to correct the automated image processing algorithms in real-time, on the client-side. This is not possible with full-size images, as their high resolution causes long program execution times, but the scaled or partial images can provide useful previews for how an algorithm will run on the original file. When the user has finished adjusting the preview, the parameters of the operation they have performed (angle of rotation, binarisation threshold, etc.) are sent to a server-side program to run on the full image.
