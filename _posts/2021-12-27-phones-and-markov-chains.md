---
layout: single
title:  "Problem Takeup: Phones and Markov Chains"
date:   2021-12-27 17:45:00 -0400
categories: contest
---

{% include mathjax.html %}

Around four months ago, I competed in the [Noctem Virtual II (Div. 1)](https://www.noctemdevelopment.org/NoctemVirtualII.html),
where I encounted a very interesting expected value problem.

The statement is as follows:

> You are given two arrays of integers $$A$$ and $$B$$ (where $$|A|=|B|,0 \le A_i,B_i \le 9$$), along with an integer $$K\ (2 \le K \le 10)$$, and
> you want to transform $$A$$ into $$B$$.  However, the only operation you can perform is the following:
>
> Pick a random index $$1 \le i \le |A|$$ where $$A_i \neq B_i$$, and change $$A_i$$ to one of $$\{A_i, A_i+1, \ldots, A_i+K-1\}$$
> uniformly randomly.
> Note that if a value ever goes above $$9$$, it loops back to $$0$$.
> 
> Your goal is to compute the expected number of operations to transform $$A$$ into $$B$$.
>
> Constraints: $$1 \le |A| \le 10^5$$

The first thing you may notice is that operations are independent between digits, meaning that all you really need to do
is to calculate the expected number of operations per digit and just sum those together.  This lets us focus on the case 
where $$|A|=|B|=1$$, which is the only one that really matters.

There are many ways to approach this problem, but one that I found quite interesting (and the one that we did in-contest)
was to think of the current value of $$A_1$$ as a state, and the operation on each digit $$A_1$$ can take on as transitions 
to other states (each with probabilities).  In other words, a Markov chain!

If we let $$P(i)$$ denote the probability $$A_1$$ becomes $$B_1$$ after exactly $$i$$ operations, our answer is:

$$\sum_{i=0}^\infty iP(i)$$

Observe that our system is an [Absorbing Markov chain](https://en.wikipedia.org/wiki/Absorbing_Markov_chain), which tells 
us that $$\lim\limits_{n \to \infty} P(n) = 0$$ since eventually every system ends up at the state $$B_1$$, and quite quickly too,
since the lowest probability of a transition is only $$10\%$$.  Thus, if we just wanted to approximate the answer to a 
sufficiently precise value, we could use a simple dynamic programming to compute $$P(1), P(2), \ldots, P(k)$$ for some 
large enough $$k$$, and we would be done. Unfortunately, the original problem asks us to output the 
answer modulo a large prime, so this approach would not work as we need the exact value.

---

For the full solution, we need to try something else.  Let's first try and rephrase our formula from earlier.  Let $$Q(i)$$ 
be the probability that we need to take at least $$i$$ operations to reach $$B_1$$.  Notice that
$$Q(i) = 1 - \sum_{j=0}^{i-1} P(j) = \sum_{j=i}^\infty P(j)$$ since $$\sum_{i=0}^\infty P(i) = 1$$.  This then gives us 
the following expression

$$\sum_{i=0}^\infty iP(i) = \sum_{i=1}^\infty Q(i)$$

since you may notice that by summing all $$Q(i)$$, $$P(1)$$ is counted once, $$P(2)$$ is counted twice, $$P(3)$$ is counted
three times, etc.

Next, let $$M$$ denote the matrix of transitions for the system.  In particular, $$M_{i,j} = 1/K$$ if $$i \neq B_1$$ and 
there exists $$0 \le x < k$$ such that $$i + x \equiv j \pmod{10}$$, and is $$0$$ otherwise.

Lastly, let the vector $$\alpha$$ represent the initial state of our system, so $$\alpha_i = \begin{cases} 1 & i = A_1 \\ 0
& i \neq A_1 \end{cases}$$.

Let $$\text{vsum}(v) = \sum_{i=0}^9 v_i$$.  Notice that if we multiply a state vector by $$M$$, it effectively preforms 
the operation on every possible state of the system that the vector represents.  Additionally, if there was a possibility
that the system was in the state $$B_1$$, that probability "exits" the system.  Mathematically, this means that
$$\text{vsum}(Mv) = \text{vsum}(v) - v_{B_1}$$ for all vectors $$v$$.  This combined with the notion that $$(M^k\alpha)_i$$
denotes the probability that the system is in state $$i$$ after $$k$$ operations allows us to deduce that 
$$Q(k) = \text{vsum}(M^k\alpha)$$.

We now get:

$$\sum_{i=1}^\infty Q(i) = \sum_{i=1}^\infty \text{vsum}(M^k\alpha)$$

and since $$\text{vsum}(v + w) = \text{vsum}(v) + \text{vsum}(w)$$,

$$= \text{vsum}\left( \sum_{i=1}^\infty M^k\alpha \right)$$

$$= \text{vsum}\left( \alpha \left( \sum_{i=1}^\infty M^k \right) \right)$$

Now, to the last and most interesting part of the solution: notice that the sum with $$M^k$$ looks awfully like a 
geometric series- because it is!  Additionally, since we're working in a matrix field, we're actually able to just use
the formula for the sum of an infinite geometric series to find the sum!

$$= \text{vsum}\left( \frac M{I - M} \alpha \right)$$

I'm not sure on the specifics of why this works, since the proof for the formula is already quite involved for just 
reals, but we can build some intuition on when/why this works by looking at other number systems.  My thoughts are that 
other than commutativity, (in this case, real-valued) matrices share many algebraic properties with the real numbers
which means that they'll behave nicely with a lot of theorems that we expect from the real numbers, either directly or
with a bit of generalizing.

As for when this formula applies to matrices $$M$$, if we can expect for the sum 
$$M + M^2 + M^3 + \ldots$$ to converge, then the formula should work.  For example, other Absorbing Markov chains.