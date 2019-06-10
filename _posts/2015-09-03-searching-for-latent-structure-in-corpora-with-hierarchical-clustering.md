---
title: Searching for Latent Structure in Corpora with Hierarchical Clustering
layout: post
permalink: /blog/:title/
author: ehopkins
upload: ""
categories:
  - VIS
  - Hierarchical Structuring
  - dendrograms
  - Analysis
---

_Guest post from Alex Morgan, PhD student at McGill_

Over the summer we’ve been working to integrate hierarchical clustering into our [VIS Music Analysis Framework](http://vis-framework.readthedocs.org/en/vis-framework-2.0.0/) to help us reveal latent structure in musical corpora. Hierarchical clustering is a type of machine learning that groups data sets by how similar they are to one another. In hierarchical clustering, we begin with _n_ groups each containing one data set. In the example below, each starting group is the intervallic profile of a two-voice piece by Josquin, Lassus, or Morley. The two most similar groups are then merged with one another, leaving us with _n_ - 1 groups. This process is repeated until all of the starting singleton groups are merged into one big group. Then, we look at the visual representation of this hierarchical clustering, called a dendrogram, and focus on the intermediary stages of grouping to see if any meaningful clusters emerged. Put simply, dendrograms can help knowledgeable researchers reveal latent structure in large corpora.
<br>
![Dendrogram]({{ site.url }}/assets/img/36_JLM_Duets_annotated.png)
<br>
The dendrogram above illustrates the clustering of the interval profiles of 36 separate duets, twelve each by Josquin, Lassus, and Morley numbered 1-12, 13-24, and 25-36 respectively. The grouping suggests that each of the three composers has a relatively regular and distinct intervallic vocabulary. Lassus’s twelve duets in particular demonstrate the highest density of similarity clustering meaning that they are the most similar to one another according to this analysis metric.

We are thrilled to include these experimental tools in the VIS analysis framework as they will help us quantify similarity between composers, modes, genres, time periods, etc. and eventually may point to a probable composer for pieces of uncertain authorship, as well as reveal potentially false attributions.
