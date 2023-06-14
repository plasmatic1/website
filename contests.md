---
layout: single
title: Contest Highlights
permalink: /contests/

toc: true
toc_label: Contests
---

Problemsetting and contest hights from my years in competitive programming :)

## Problem Setting

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

Additional: [my DMOJ problems](https://dmoj.ca/user/Plasmatic/solved).

## Contest Highlights

_DMOJ and CF content is auto-fetched.  Auto-fetched content last updated {{ site.data.fetch_time.time_display }}._

### External

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
