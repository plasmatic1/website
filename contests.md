---
layout: single
title: Competitive Programming
permalink: /contests/

toc: true
toc_label: Contests
---

As competitive programming has been one of my biggest hobbies in the past few years, here I list some of my contest highlights and achievements
I am proud of.

_DMOJ and CF content is auto-fetched.  Auto-fetched content last updated {{ site.data.fetch_time.time_display }}._

## Problem Setting

Outside of competition, I also spend a lot of time organizing and preparing programming competitions and currently plan to work on some tools
that can help improve the experience of problem-setting as it is often very time-consuming and difficult.

<table>
    <tr>
        <th>Contests</th>
    </tr>
    {% for contest in site.data.problemsetting %}
        <tr>
            <td>
                <a href="{{ contest.url }}">{{ contest.name }}</a>
            </td>
        </tr>
    {% endfor %}
</table>

I also have some standalone problems on the DMOJ judge that were either uploaded for fun or as part of class quizzes at Olympiads School.
  You can find these [here](https://dmoj.ca/user/Plasmatic/solved) after scrolling down a bit.

## Contest Highlights

Contest highlights :)

### Other

<table>
    <tr>
        <th>Contest</th>
        <th>Rank</th>
    </tr>
    {% for contest in site.data.other_contests %}
        <tr>
            <td>
                <a href="{{ contest.url }}">{{ contest.name }}</a>
            </td>
            <td>{{ contest.rank }}</td>
        </tr>
    {% endfor %}
</table>

### Codeforces

<table>
    <tr>
        <th>Contest</th>
        <th>Handle</th>
        <th>Rank</th>
    </tr>
    {% for contest in site.data.cf_contests %}
        <tr>
            <td>
                <a href="https://codeforces.com/contest/{{ contest.key }}">{{ contest.name }}</a>
            </td>
            <td>
                <a href="https://codeforces.com/profile/{{ contest.handle }}">{{ contest.handle }}</a>
            </td>
            <td>{{ contest.rank }}</td>
        </tr>
    {% endfor %}
</table>

### DMOJ

<table>
    <tr>
        <th>Contest</th>
        <th>Handle</th>
        <th>Rank</th>
    </tr>
    {% for contest in site.data.dmoj_contests %}
        <tr>
            <td>
                <a href="https://dmoj.ca/contest/{{ contest.key }}">{{ contest.name }}</a>
            </td>
            <td>
                <a href="https://dmoj.ca/user/{{ contest.handle }}">{{ contest.handle }}</a>
            </td>
            <td>{{ contest.rank }} / {{ contest.tot_participants }}</td>
        </tr>
    {% endfor %}
</table>

## Online Judge Profiles

<table>
    <tr>
        <th>Handle</th>
        <th>Max Rating</th>
        <th>Rating</th>
    </tr>

    {% assign accounts = site.data.auto_accounts | concat: site.data.accounts %}
    {% for handle in accounts %}
        <tr>
            <td>
                <a href="{{ handle.url }}">{{ handle.display }}</a>
            </td>
            <td>{{ handle.max_rating }}</td>
            <td>{{ handle.rating }}</td>
        </tr>
    {% endfor %}
</table>
