
---

After learning about some D&C techniques around a year ago, I came up with an extension to the trick that
allows you to perform divide and conquer on range updates and queries without the need for lazy propagation.  There are
some requirements for the operations, but I think it is quite interesting and versatile even though the constant factor
is quite high.

As with all tricks in competitive programming this is probably already well-known in China, but I'm sharing about it as
I have not seen it anywhere yet.

## Motivating Problem

This was a technique I first used to solve [this problem](https://dmoj.ca/problem/coci18c2p5), and the statement
is as follows:

## Recap of CDQ

## Adding Laziness

## Pitfalls

Unfortunately, the constant factor for this technique is quite high as each query needs to be applied and then removed
multiple times.


Selfnote: keeping this thing on the bottom here so I remember how to do syntax highlighting.  I think I'll be needing it.

{% highlight ruby %}
    def print_hi(name)
    puts "Hi, #{name}"
    end
    print_hi('Tom')
    #=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Some math: $$1+1=2$$.

$$\frac{3}{2} = 1.5$$
