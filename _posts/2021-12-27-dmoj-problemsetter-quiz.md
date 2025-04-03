---
layout: single
title:  "DMOJ Problemsetter Quiz Guide"
date:   2021-12-27 16:19:00 -0400
categories: contest
---

{% include mathjax.html %}

![unclear.png]({{ site.baseurl }}/assets/blog_psetter_quiz/unclear.png)

<p style="text-align: center; font-style: italic;">Seems like someone is frustrated</p>

---

DMOJ is quite complicated, so it can be difficult to find all the information necessary to begin setting problems
especially if you don't clone your own instance of the judge. Thus, this post is a guide to the questions on the
DMOJ problemsetter quiz for those that need a bit of a hand :)

Where possible, I try to link to the relevant documentation and not give the answer directly.

---

First and foremost, the problem setter quiz is
[here](https://docs.google.com/forms/d/e/1FAIpQLSeU59cCdTbbGAwuGnLzcps6xbp1c-GF9pbwtsJg9z5xtZ8Eiw/viewform)

Now, let's go over the questions:

> Email
>
> DMOJ Handle

😛

> What should you put in the field if you wanted a memory limit of 512 MB?

Memory limits are given in Kilobytes.

> What does enabling short circuit do?

If you're familiar with problems that use subtasks, short-circuiting will terminate judging if a subtask fails.

> What is the difference (permission-wise) between a creator, curator, and a tester?

Relevant documentation [here](https://docs.dmoj.ca/#/site/managing_problems).

> What is the difference between the points for these two problems?
> 
> ![3 vs 3p]({{ site.baseurl }}/assets/blog_psetter_quiz/partial.png)

`p` is for partial points!

> What format does DMOJ use for its problem statements and math equation rendering?

I'm not sure about the exact name, but it's just Latex.  If you're familiar with Polygon, it's almost the same system 
except `~` are used instead of `$` to denote inline math.

> How would you ensure your data is correct for the following input specification using asserts? (Write out a working program using the language of your choice)
> 
> ![asserts]({{ site.baseurl }}/assets/blog_psetter_quiz/assert.png)

If you want a bit more context on the problem, [this](https://dmoj.ca/problem/wac3p7) is the problem that the question 
uses.  Other than that, the question is pretty straightforward- you just write a program to read the input and check if all the 
constraints are satisfied using assertions.

Note that you don't have to check for formatting for this question, just that the contraints are satisfied.

> Should input and output data end with a newline?

If you don't do this I'll eat all of your food.

> How would you type out the following expression in a problem statement?
> 
> ![math]({{ site.baseurl }}/assets/blog_psetter_quiz/math.png)

Remember how DMOJ uses latex?

[Here's](https://texnique.xyz/) a little practice website if you're interested :)

> When using a generator to create test data, what does the output stream and error stream represent, respectively?

Relevant documentation [here](https://docs.dmoj.ca/#/problem_format/generator).

> What is the difference between these checkers: an absolute floating point error and a relative floating point error?

Make sure to read up on [approximation error](https://en.wikipedia.org/wiki/Approximation_error), though you should 
avoid using floating-point checkers when possible, since the innacuracy isn't fun.

> Where can you find problem examples utilizing different graders?

Relevant documentation [here](https://docs.dmoj.ca/#/problem_format/problem_examples).

> True or False: Checking the "Pretest?" box in the Edit Test Data page will mark the case as a sample case.

This question is a bit of a joke that comes from some recent DMOJ lore.
If you're familiar with pretest/systest platforms such as Codeforces, you should be able to answer this from common
sense alone.

> Using your preferred language, print an array of integers called "arr" on a single line, space separated, and to standard error.

Again, a pretty straightforward programming task.  There isn't much to say here.

> What is the difference between the output prefix length and the output limit length?

Try submitting something incorrect on [DMOJ](https://dmoj.ca) and you may notice that the judge lets you see part of 
your output- this is the output prefix length.  The output limit length is just the maximum output size the judge will
accept.  This is especially useful when using custom checkers so that they don't try and read an output that's too large.

> Is setting a zero point value for a case legal?

Hint: Sample test cases

> Fill in the blank: Generators ____ have a fixed seed.

I'll answer this with an example: if you were debugging a generator, would you like if it behaved differently every 
time it ran?

> What is the difference between the line-by-line checker and the unordered checker?

[Make sure to read up on your checkers!](https://docs.dmoj.ca/#/problem_format/custom_checkers) However, you won't be 
seeing these two checkers often though.

> Fill in the blank: You should use ____ media uploader for problem statements.

The DMOJ site has a media uploader for images and other files in problem statements, use it!

---

I hope this was useful!