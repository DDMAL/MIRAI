# [MIRAI](https://miraiqc.ca/)

This is the repository for the MIRAI website distributed via GitHub Pages. It is a static website built using Jekyll, meaning that there is no backend presence, and the entirety of the site is stored in this repository, blog contents included. The formatting was adapted from the previous statamic theme, with adjustments to the blog, navbar, and responsiveness.


## Contents

- [Local Setup](#local-setup)
- [CMS](#cms)
  - [CMS Navigation](#cms-navigation)
  - [Organization](#organization)
  - [Media](#media)
- [Troubleshooting](#troubleshooting)

## Local Setup

You will need to download a full [Ruby development environment](https://jekyllrb.com/docs/installation/) to install Jekyll. Follow steps 1 and 2 of [these instructions](https://jekyllrb.com/docs/) after installing Ruby.

Assuming you have [Git](https://www.atlassian.com/git/tutorials/install-git) installed, open a terminal and clone the repository into any known location on your computer. The documents folder is recommended, though it is up to you.

```
git clone https://github.com/DDMAL/MIRAI.git
```

Enter the directory with `cd MIRAI`, and pull from the repository to your local folder. Specifically, pull from the 'master' branch, the branch used by GitHub Pages to host the site.

```
git pull origin master
```

At this point, the site is able to be edited and run locally. Assuming steps 1 and 2 of the Jekyll documentation were followed correctly, run:

```
bundle exec jekyll serve --watch
```

The built site can then be viewed at 'localhost:4000/'. The `--watch` option automatically checks for updates to the local files and can be immediately viewed by refreshing the page. `--watch` is not supported by Windows, thus the command above will need to be rerun after each edit.

If any changes need to be made to the 'Gemfile' at the root directory, run:

```
bundle install
```

to install any updated or newly-added gems for the build. Then, the site can be rebuilt with `bundle exec jekyll serve --watch`.

<!-- ## CMS

<br>

![](readme-img/SIMSSA-to-Forestry.png)

<br>  

The content management system (CMS) used for this site is [Forestry](https://forestry.io/). This is where blog entries and website contents are added, edited, and maintained. Contact [Evan Savage](mailto:evan.savage@mail.mcgill.ca) or [Emily Hopkins](mailto:emily.hopkins@mcgill.ca) to gain access to the CMS.

Blog entries and website content are written in Markdown, which make it easy to add text, links, images, and lists to a new post. Here is a [Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) to consult for any necessary formatting.

In the picture above, you can see how each of the links for navigation on the SIMSSA website correspond to an editable tab on the sidebar of the CMS. The next section will explain in further detail how each component is edited and what output should be expected.

### CMS Navigation

Any content that needs to be added or adjusted on the SIMSSA site can mostly be done in the Forestry CMS. When selecting any of the tabs on the sidebar, you will either be taken to a Markdown file or folder. When editing or adding a new Markdown file, the default editing style is a What-You-See-Is-What-You-Get (WYSIWIG [wiss-e-wig]) editor. Formatting for each paragraph, header, link, etc. will automatically take place, and explicit Markdown syntax will automatically be reflected in the editor. If it is preferred, click on the ellipsis in the upper right hand corner to change to edit in 'Raw' mode, where the Markdown is explicitly written. Markdown files can also be injected with HTML if the default styling is not satisfactory.

<br>  

![](readme-img/wysiwyg-vs-raw.png)

<br>  


Every Markdown file has a number of fields in the leftmost column to edit which are referred to as Front Matter. This information is used for automatically placing content where the CMS suggests it should be added. Each tab on the sidebar is restricted to a subset of Front Matter templates respectively that require the content manager to add titles, descriptors, and other information for organizing the new content properly.

<br>  

![](readme-img/participant-example.png)

<br>  

In the example above, selecting the group "co-investigator" from the dropdown for __Project Group__ automatically will place the individual in that respective group on the website. Other details such as "link" and "institution" are not required, but they can be used to link to others' work and provide more context.

Some tabs such as "Participants" and "Projects" only include editable Front Matter as their respective Markdown files contain little information other than names, affiliations, and links to external websites. There is no need for a body of content for those files. Otherwise, tabs like "Workshops" and "Blog" include Front Matter and Markdown editing for correctly filing and editing entire pages.

### Organization

For most of the tabs on the sidebar in Forestry, there is a corresponding Markdown file for each at the root of the respective tab's folder. For example, the **Opportunities** tab features a file called **opportunities.md** within it. This is the the landing page that a user will see when selecting "Opportunities" from the navigation bar on the actual website.

The folder architecture automatically appends to the URL based on the progression from the root URL through each child folder. The front matter for the **opportunities.md** file at the root of the Opportunities folder requires a "permalink" field since we would like to see that page at "simssa-website/opportunities/" instead of "simssa-website/opportunities/opportunities/". The permalink should only need to be specified for landing pages found within the subfolder they are representing with the same name. Here's a quick example:

* Opportunities [folder]
  * opportunities.md (permalink: /opportunities/) ---|
  * postdoc-analysis.md <--------------------------|
  * summer-developers.md <-----------------------|

The **postdoc-analysis.md** and **summer-developers.md** files are linked to from **opportunities.md**, and their URLs will immediately be correct without the need for a permalink since they are a subset of the opportunities landing page inside the opportunities folder. As folders are nested in an increasing website architecture, the same principle applies, and each parent folder will be one further step back in the entire URL.

### Media

Blog posts, workshops, and individual pages often include images and downloads on the SIMSSA website, and Forestry includes a "Media" area to upload these files. On the sidebar under "Site", select "Media" to view all of the existing media present in the website's repository. By selecting the "Upload" button in the top right corner, you can upload any files directly to the CMS/repository for later usage in various posts.

When writing or editing a Markdown entry that will include an image or file, hit `ctrl+shift+u` to open the Media folder. Then, you can select any existing media and drop it right into the new post; Forestry handles the file path automatically, and it should not need to be altered. Images will be center-justified when posted to the website.

## Troubleshooting

If you are having any difficulties with setup, the CMS, or local development, please feel free to email [Evan Savage](mailto:evan.savage@mail.mcgill.ca) or use the issues tab found in this repository. -->
