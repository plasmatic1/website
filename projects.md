---
layout: single
title: Projects 
permalink: /projects/

toc: true
toc_label: Projects
---

## Competitive Programming

As a competitive programmer, naturally I have many related projects.

### Competitive Programming Tools

A suite of competitive programming tools, including a system for automated execution of code on test case, automatic
fetching of templates, and stress-testing.  There is also support for a variety of different generators and custom checkers.

Currently, there exists two versions of the tool, the original being a VSCode extension, and the current one being a console-based
Python module that can be easily integrated into existing text editors and IDEs such as Vim.  Below are the links to their respective
repositories.

* {% include repo_link.html name="cp-tools-console" label="Python Module" %}
* {% include repo_link.html name="competitive-programming-tools" label="VSCode Extension" %}

#### Competition Environment

For competitions and practice, I use a customized [Vim](https://www.vim.org/) setup with many plugins.  Full configuration and setup script can be found on
{% include repo_link.html name="competitive-programming-dotfiles" label="Github" %}.

### Judge Solutions

I maintain a list of most of my judge solutions that others can browse if they are stuck or want to see alternatives implementations of a problem 😊

* {% include repo_link.html name="dmoj-solutions" %}
* {% include repo_link.html name="other-judge-solutions" %}

#### Solution Downloader

One of my planned projects is a solution downloader that can aggregate code from many different judges, removing the need to manually organize solutions.
Unfortunately, it's currently still in development.

### Templates

Recently, I've begun work on a more formal codebook using [online-judge-tools/verification-helper](https://github.com/online-judge-tools/verification-helper) to
 ensure correctness of algorithms and generate documentation.

* {% include repo_link.html name="templates" %}

### Miscellaneous

* Auto CPP
  * Tool that automatically downloads submissions on problems and sends them through [MOSS](https://theory.stanford.edu/~aiken/moss/) to help catch cheaters.
  * {% include repo_link.html name="autocpp" %}
* Rating badges
  * Rating SVG badges for your GitHub about page (or anywhere else that accepts them).  However, currently only DMOJ is supported.
  * {% include repo_link.html name="dmoj-rating-badges" %}
* Generators
  * I also maintain a semi-complete list of generator files I've used.  The repository is currently private but may be made public in the future.

### Planned
* Generator-Lib
  * A generator suite compatible with `testlib.h` that has helpers to generate more complex data such as graphs.
* DMOJ-Polygon
  * An idea I have to help port Polygon packages into files compatible with the DMOJ judge.

## Website

What you're reading right now :).  This website is made with Jekyll along with some automated data fetching done in Python.

* {% include repo_link.html name="website" %}

The old version of my website (made with Django) is available {% include repo_link.html name="website-old" label="here" %} as well.

## Minecraft

Previously, I made a few server plugins using the Bukkit/Spigot API.  Minecraft has and will always be one of my favourite games,
so it was very rewarding to try out various the ideas I had :)

* KitsPlus
  * A Bukkit/Spigot plugin that implements a robust interface for KitPVP
  * {% include repo_link.html name="kitsplus2" %} - V2 rewritten in Kotlin
  * {% include repo_link.html name="IntellijProjects" %} - Original contained within this repository
* Discord Bridge
  * A bridge service that connects Minecraft server chat to discord
  * {% include repo_link.html name="DiscordChat" host="gitlab" username="FrostTaco" %}
* IntelliJ Projects
  * A compilation of most of my older plugin projects, all contained within one repository because they shared some common files :P
  * {% include repo_link.html name="IntellijProjects" %}

## Miscellaneous

### BetterWeb

A browser extension intended to use NLP and neural networks to detect bias in news articles.  Unfortunately, the project is currently inactive and unfinished.

* {% include repo_link.html name="BetterWeb" username="betterweb-team" %}