---
title: 'New Release: Diva.js 4.0 is here!'
layout: post
permalink: /blog/:title/
author: ehopkins
categories:
  - diva
  - diva.js
  - DDMAL
  - software
  - new release
  - document image viewer
  - IIIF
upload: ""
---

Last week, we released Diva.js 4.0 (Document Image Viewer with AJAX), a new version of our open-source document image viewer. [Evan Magoni](https://github.com/magoni) is the lead developer on Diva in [our lab here at McGill](https://ddmal.music.mcgill.ca/), and we’re excited to share what he’s been working on. Using Diva on their own websites, libraries, archives, and museums can present high-resolution document page images in a user-friendly interface that has been optimized for speed and flexibility.

[![]({{ site.url }}/assets/img/diva-website600.png)](http://ddmal.github.io/diva.js/)

Some highlights of version 4.0 include:

-  support for the [International Image Interoperability Framework](http://iiif.io/) (IIIF). Supporting this standardized format makes Diva part of the larger movement to enhance and promote sharing of archival image collections.

- “Book Layout” view, presenting document images as openings, or facing pages.

Several demos are available at [http://ddmal.github.io/diva.js/try/](http://ddmal.github.io/diva.js/try/)

[![]({{ site.url }}/assets/img/screenshot600.png)](http://ddmal.github.io/diva.js/try/iiif-highlight-pages/)

Other improvements include:

- Improved integration with existing web applications, including [Cantus Ultimus](http://cantus.simssa.ca/), the [Rodan Client](https://github.com/DDMAL/Rodan) (still a work in progress), and the [MEIx Editor](https://github.com/DDMAL/meix.js). Duke University also uses Diva for its [digital collections](http://library.duke.edu/digitalcollections/earlymss_emsgk01025/).
- New plugins: Autoscroll (animated page scrolling), Page Alias (pages may have multiple identifiers), IIIF Metadata (displays document metadata from IIIF manifest), IIIF Highlight (displays annotations from a IIIF manifest)
- Improved build system with [Gulp](http://gulpjs.com/)
- Support for switching documents without reloading the viewer
- Numerous bug fixes and optimizations

For more information and documentation visit [http://ddmal.github.io/diva.js/](http://ddmal.github.io/diva.js/)

![]({{ site.url }}/assets/img/divalogo.png)

Diva.js is developed by the [Distributed Digital Music Archives and Libraries laboratory](https://ddmal.music.mcgill.ca/), part of the [Music Technology Area of the Schulich School of Music at McGill University](http://www.music.mcgill.ca/musictech/) and is funded by the [Social Sciences and Humanities Research Council of Canada](http://www.sshrc-crsh.gc.ca/home-accueil-eng.aspx).
