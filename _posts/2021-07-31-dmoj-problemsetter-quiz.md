---
layout: single
title:  "DMOJ Problemsetter Quiz Guide"
date:   2021-07-31 18:31:14 -0400
categories: contest
---

{% include mathjax.html %}

Unfortunately, this blog is still heavily work in progress, so I'll just give a gist of the idea, what it was inspired from,
 and some of its pitfalls (or rather, its one major drawback).

This trick allows us to solve problems with 2D range updates and queries offline with only one log factor above its 1D equivalent.
  Thus, it is quite niche but can be very useful in certain sitautions.

Lazy D&C is inspired from the 'segment tree over time' (often introduced as an offline solution to
dynamic connectivity with DSU) and 'lazy segment tree without propagation' tricks.  Here, we run D&C similar to a
segment tree but offline across one of the dimensions (similar to the 'time' dimension in the 'segment tree over time' trick).

When we encounter a query that covers a whole range in our D&C, we apply all updates that are within (or cover) that range to it.
Similarly, when we hit an update that covers a whole range, we apply it to all queries that are within (or cover) that range.
Otherwise, we break them into halves at the midpoint of the current range and
push them to the next layer of the D&C.

Some of this may feel confusing and out of place, but reading up on the offline D&C solution to APIO '19 P3 (Street Lamps) may be
helpful in conceptualizing what the idea is.

If you are also in need of some code here is a [problem (and solution)](https://mosesxu.ca/dmojsols/view/coci18c2p5/cpp) that uses this technique if you
are curious.

Lastly, the biggest pitfall of the technique is that it requires you to apply and undo updates/queries multiple times, which gives it
quite a large constant factor.

