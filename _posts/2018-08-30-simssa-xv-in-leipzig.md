---
title: 'A Trip to Leipzig: SIMSSA XV and IAML'
layout: post
permalink: /blog/:title/
author: ehopkins
categories:
- SIMSSA Workshop
- Music Libraries
- Libraries
- OMR
- Verovio
- BSB
upload: ""
---

Our fifteenth SIMSSA Workshop took place in Leipzig on 28 July 2018 immediately following the annual congress of the [International Association of Music Librarians](http://iaml2018.info/home/)! Many of our partners and collaborators work in music libraries so it was a great chance to meet some of them and update each other on our work. In addition to my work for SIMSSA, I am also doing my MLIS, so it was really wonderful to get to meet so many people working on different aspects of librarianship and music. It was also fascinating to get a chance to learn more about Leipzig's history as a centre for classical music and also as part of East Germany.

![]({{ site.baseurl }}/assets/img/nikolaikirche.png)

<small>_The Nikolaikirche downtown. Bach worked here as well as the St. Thomas church, and it was also the site of the Monday demonstrations, peaceful protests against the German Democratic Republic from 1989-1991._</small>

The IAML Congress started on 22 July and continued all week, with SIMSSA XV taking place on Saturday. There was also some time to explore Leipzig (see image below of a mural in Plazwig.) There were too many interesting talks to cover everything, but I'll share some personal highlights below.

![]({{ site.baseurl }}/assets/img/plazwig.png)

I got to attend a [RISM](http://www.rism.info/home/) training session led by Jennifer Ward on their online music cataloging software, [Muscat](http://www.rism.info/community/muscat/). This was especially interesting to me for our work in the lab designing the new and improved SIMSSA Database this summer (more on that later...). One of the most interesting features is how Muscat integrates [VIAF](http://viaf.org/) data into its cataloging practises. [VIAF](http://viaf.org/) is the Virtual International Authority File, uniting the collections and cataloging processes of libraries around the world with unique identifiers, making it possible to have linked data approaches to music databases.

[![]({{ site.baseurl }}/assets/img/muscat-logo.png)](http://www.rism.info/community/muscat/)

[Carolyn Doi](https://library.usask.ca/people/carolyn-doi.php) presented on research she's doing with [Sean Luyk](https://www.library.ualberta.ca/staff/sean-luyk) through a SSHRC-funded project called _Sounds of home: local music collecting and collections in Canada_. In the presentation, Carolyn shared some results from the midway point of their project, highlighting survey responses from libraries with local music collections. Their project includes documenting and describing local music collections, exploring who uses them and for what purposes, and ways to support local collections. This includes asking questions about respectful ways to engage with communities and music from traditionally marginalized groups and underrepresented communities. How can music be preserved in a respectful and inclusive way?

[Lynnsey Weissenberger](http://www.lynnseyweissenberger.com/) shared her work on LITMUS, the Linked Irish Traditional Music Database, a project of the [Irish Traditional Music Archive](https://www.itma.ie/). This two-year project involves the development of a traditional music database and an appropriate linked data ontology for Irish traditional music to go with it. Linked data triples allow for the description of relationships between tunes or other source materials -- for examples, stories or poems associated with a tune, or which collections it can be found in. This database also makes use of [Traditional Knowledge labels](https://loc.gov/item/2015655578) (Here is an example of these labels in context in a Library of Congress entry: [Passamaquoddy War song; Trading song](https://loc.gov/item/2015655578)). There is also great potential for the work done on LITMUS to be used for databases of other traditional music in the future.

[![]({{ site.baseurl }}/assets/img/litmus-logo.png)](https://litmus.itma.ie/)

Cecile Cecconi presented on _Music and Linked Open Data: Results and Lessons Learned from the DOREMUS project._ [Doremus](http://www.doremus.org/) is short for Doing Reusable Musical Data. Their work includes an ontology for linked data, multilingual controlled vocabularies, and different approaches to music metadata. The Doremus ontology is available on GitHub [here](https://github.com/DOREMUS-ANR/doremus-ontology). Cecconi also discussed [Yam++](http://yamplusplus.lirmm.fr/), a web tool for ontology and thesaurus matching, and even demonstrated a [Doremus chatbot](https://github.com/D2KLab/music-chatbot) that uses natural language processing to try to answer music questions.

[![]({{ site.baseurl }}/assets/img/doremus-logo.png)](http://www.doremus.org/)

After the main congress was over, SIMSSA XV took place on Saturday, in the University Library at the Hochschule für Musik und Theater.

![]({{ site.baseurl }}/assets/img/simssaxv.png)

First up, Ichiro Fujinaga gave a brief welcome and introduction to the workshop. Next, I (Emily Hopkins) presented an overview of the SIMSSA project, including a technical explanation of our goals as well as an update on current research projects, including Karen' Desmond's [Measuring Polyphony Project](http://measuringpolyphony.org/). Slides are available [here]({{ site.baseurl }}/assets/files/hopkins_simssaxv.pdf).

Jürgen Diet gave a talk on [The OMR Project of the Bavarian State Library]({{ site.baseurl }}/assets/files/diet_simssaxv.pdf). He gave an overview of their OMR project, including hiring Sanu Pulimootil to work on the project. They tested OMR software such as Audiveris, Capella Scan, SharpEye, and SmartScore. From this, they developed a set of OMR results using the BSB's digitized score collection, and then built a search interface that uses a keyboard for musical queries (see below).

![]({{ site.baseurl }}/assets/img/bsb_search.png)

Cory McKay introduced [SIMSSA DB: A Database for Computational Musicological Research]({{ site.baseurl }}/assets/files/mckay_simssaxv.pdf).
This database is for storing and organizing symbolic music files and research studies, dealing with the best ways of handling metadata for a wide range of musical materials. His presentation gave an overview of the considerations that went into the new data model as well as the progress we've made this summer. Here is the entity-relationship diagram for the database:

![]({{ site.baseurl }}/assets/img/simssadb_erd.png)

Next, Laurent Pugin gave us an update on the latest developments in [Verovio](https://www.verovio.org/index.xhtml), including harmonic annotations, better handling of trill extensions and text that extends across multiple barlines, and PDF score output. You can see his slides [here]({{ site.baseurl }}/assets/files/pugin_simssaxv.pdf). He also showed a neat example of how you can separate the layers of different kinds of symbols. Here they are highlighted:

![]({{ site.baseurl }}/assets/img/verovio1.png)

And then separated into layers like the kind we use for our OMR process:

![]({{ site.baseurl }}/assets/img/verovio2.png)

Finally, Ichiro Fujinaga gave a detailed overview of how the SIMSSA OMR process works, showcasing the progress our summer students have made in the lab this year at McGill.

After the workshop, several workshop participants went out for lunch at a nearby restaurant.

![]({{ site.baseurl }}/assets/img/simssaxv_lunch.png)

<small>_*L-R:* Emily Hopkins (McGill), Sonia Wronkowska (National Library of Poland), André Avorio (Alexander Street Press), Laurent Pugin (RISM-CH), Jane Gottlieb (The Juilliard School), Ichiro Fujinaga (McGill), Barbara Dobbs Mackenzie (RILM), Craig Sapp (Stanford University), Cory McKay (Marianapolis College), Erin Conor (University of Washington, and Tim Crawford (Goldsmiths, University of London))._</small>

It was a real pleasure to attend my first IAML and visit Leipzig. Thank you to everyone I met and also who attended the SIMSSA Workshop -- be sure to let us know if you're ever in Montreal!

I will leave you with a final picture of the smallest Montreal IAML delegate paying her respects to Leipzig's most famous resident.

![]({{ site.baseurl }}/assets/img/bach_baby.png)
