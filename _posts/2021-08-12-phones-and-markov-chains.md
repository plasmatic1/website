---
layout: single
title:  "Phones and Markov Chains"
date:   2021-08-11 18:31:14 -0400
categories: contest math
---

{% include mathjax.html %}

Recently, I competed in the [Noctem Virtual II (Div. 1)](https://www.noctemdevelopment.org/NoctemVirtualII.html), where
 I encounted a very interesting expected value problem.  The statement is as follows:

> You are given two arrays of integers $$A$$ and $$B$$ (where $$|A|=|B|,1 \le A_i,B_i \le 10$$), along with an integer $$K\ (2 \le K \le 10)$$, and
> you want to transform $$A$$ into $$B$$.  However, the only operation you can perform is the following:

> Pick a random index $$1 \le i \le |A|$$ where $$A_i \neq B_i$$, and convert $$A_i$$ to any one of $$\{A_i, A_i+1, A_i+2, \ldots, A_i+K-1\}$$.
> Note that if a value ever goes above $$9$$, it loops back to $$0$$.

> Constraints: $$1 \le |A| \le 10^5$$

:)