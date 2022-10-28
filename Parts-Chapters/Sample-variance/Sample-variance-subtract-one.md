Why we need to subtract one when calculate sampling variance
================
Cyrill A. Murashev,
2022-10-28

## Subject

It is well known that you must subtract one from the number of
observations in the denominator of the formula when calculating the
sampling variance. More often than not, it is enough just to know that
it is necessary to do this additional action. In fact, most functions in
R and Python (as well as in other languages) do this automatically.
Spreadsheets also have a built-in means of calculating sampling
variance. However, given the need to provide evidence of the valuation
process, it is incumbent on the appraiser to understand what he or she
is doing. This article has two purposes: the first is to explain the
essence of this operation, the second is to give rigorous mathematical
proof of its necessity.

## General description of the issue and rationale for adjusting the number of observations

To give you a mathematically rigorous answer, it’s because that makes
the sample variance an ‘unbiased estimator’. Sample standard deviation
with $\textstyle{n-1}$ is biased which is easily proven with [Jensen’s
inequality](https://en.wikipedia.org/wiki/Jensen's_inequality). But who
can understand what it means. However, there is a fairly simple
explanation. The point is that the appraiser works with the sample in
order to make statistical inferences about the general population, not
about the sample itself. When estimating a parameter, we come up with
some kind of plausible estimator which is a function of all the data we
have. Such an estimate for the variance would be

$\displaystyle{\hat\theta = \frac{1}{n-1} \sum_{i=1}^{n}(X_{i}-\overline{X_{n}}).}$

You should note that the data points are subtracted by its sample mean,
not the population mean. It means that you’ve lost 1 degree of freedom
by calculating the sample mean in advance of estimating the sample
variance. This may not be entirely clear to those appraisers who do not
have a mathematical background. I can tell you some brief explanation:
if you know the sample mean, you don’t have to know **all** the data
points. You only need $\textstyle{n-1}$ data points and the sample mean
will fill up the last one and this takes away a degree of freedom. At
first glance, it’s difficult to wrap the head around why it has to do
with calculating the sample variance. So, the concept of the degrees of
freedom doesn’t provide comprehensive clarification in the question.
However, to form an initial understanding, it is enough to know that the
need to subtract one is due to the fact that the appraiser is working
with a sample, but is estimating the general population. This requires
him to remove one degree of freedom and fill it with the sample mean.
Keep in mind that this does not rectify the biasedness of sample
standard deviation. However, there is no unique form of standard
deviation that is unbiased throughout all distributions, which is why we
stick with sample standard deviation. It’s better than dividing by
$\textstyle{n}$ after all.

## Mathematical justification

Now we turn to the mathematical proof of the need to subtract the one.
We will also justify why it is the very one and not any other number.
First, we need to define ‘biasedness’ and it is represented as follows:

$\displaystyle{E(\hat\theta)-\theta,}$

where $\textstyle{\theta}$ is the parameter we want to estimate and
$\textstyle{\hat\theta}$ is the estimator we devised to estimate the
parameter. Therefore, in the case of estimating the population variance
$\textstyle{\sigma^{2}}$, the natural estimator will be the sample
variance (with no correction, thus biased):

$\displaystyle{\frac{1}{n} \sum_{i=1}^{n}(X_{i}-\overline{X_{n}})^{2},}$

where the upperscript $\textstyle{'n'}$ just tells us the sample size is
$\textstyle{n}$. Because we call an estimator an *‘unbiased’ estimator*
if there is no bias, the following mathematical property needs to hold:

$\displaystyle{B(\hat\theta) = E(\hat\theta) - \theta = 0 \Rightarrow E(\hat\theta) = 0.}$

Now let’s prove that the sample variance with no correction
$\textstyle{\widetilde{\sigma^{2}}}$ is a biased estimator of the
population variance $\textstyle{\sigma^{2}}$.

$\displaystyle{E (\widetilde{\sigma^{2}}) = E \biggl[ \frac{1}{n}\sum_{i=1}^{n}(X_{i} - \overline{X_{n}})^{2} \biggr] = \frac{1}{n}E \biggl[ \sum_{i=1}^{n}(X_{i}^{2} - 2X_{i}\overline{X_{n}}+\overline{X^{2}}) \biggr]}$

Since the expectation is linear and summation is also linear, we can
distribute and also freely change the order of expectation and summation
just as follows:

$\displaystyle{= \frac{1}{n} \biggl[ \sum_{i=1}^n E(X_{i}^{2}) - 2E \biggl( \sum_{i=1}^{n} (X_{i} \overline{X_{n}}) \biggr) + \sum_{i=1}^{n} E(\overline{X_{n}^{2}}) \biggr].}$

Since we assume all variables $\textstyle{X_{1}, X_{2}, \ldots, X_{n}}$
are all independent and identically distributed random variables
(i.i.d.), $\textstyle{E(X_{i}^{2})}$ or $\textstyle{E(X_{i})}$ are all
identical regardless of the subscript. And for the middle term, the
summation does not affect the sample mean so the sample mean comes out
of the summation.

$\displaystyle{= \frac{1}{n} \biggl[n(\sigma^{2} + \mu^{2}) - 2E \biggl(\overline{X_{n}} \sum_{i=1}^{n} X_{i} \biggr) + n \biggl(\frac{\sigma^{2}}{n} +\mu^{2} \biggr) \biggr]}$

Now $\textstyle{\sum_{i=1}^{n} X_{i}}$ is equal to
$\textstyle{n \overline{X}_{n}}$.

$\displaystyle{= \frac{1}{n} \biggl[ n (\sigma^{2} +\mu^{2}) - 2E(n \overline{X^{2}_{n}}) +\sigma^{2} +n \mu^{2} \biggr] = \frac{1}{n} \biggl[ (n+1)\sigma^{2} +2n\mu^{2} - 2n \biggl( \frac{\sigma^{2}}{n} +\mu^{2} \biggr) \biggr] = \frac{n-1}{n}\sigma^{2}}$

Now when we divide the sum of squares
$\sum_{i=1}^{n} (X_{i} - \overline{X_{n}})^{2}$ by $n$ (sample variance
with no correction) and take the expectation, then we get
$\textstyle{\frac{n-1}{n}\sigma^{2}}$.

$\displaystyle{E\biggl[\frac{1}{n} \sum_{i-1}^{n} (X_{i} - \overline{X_{n}})^{2}\biggr] = \frac{n-1}{n}\sigma^{2}}$

Therefore, in order for the sample variance to be ‘unbiased’,

$\displaystyle{\frac{n}{n-1}E\biggl[\frac{1}{n}\sum_{i=1}^{n} (X_{i} - \overline{X_{n}})^{2} \biggr] = \sigma^{2}}$

$\displaystyle{\Rightarrow E\biggl[\frac{n}{n-1} \times \frac{1}{n} \sum_{i=1}^{n} (X_{i} - \overline{X_{n}})^{2} \biggr] = \sigma^{2}}$

Now we have the ***sample variance with adjustment***.

$\displaystyle{\Rightarrow E\biggl[\frac{1}{n-1} \sum_{i=1}^{n} (X_{i} - \overline{X_{n}})^{2} \biggr] = \sigma^{2}}$

You can also easily start from the sample variance with correction and
take the expectation to prove that it is *unbiased*. This is where the
denominator comes from and why it specifically has to be 1. Just to make
it *unbiased*.

However, you should always keep in mind that this is the variance,
***not** the standard deviation*. The square root of the unbiased sample
variance is what we call *sample standard deviation* and it is **not**
unbiased. We just use it because, as I said before, we don’t have a
uniform representation of standard deviation that is unbiased for every
distribution. Moreover, dividing it by $\textstyle{n-1}$ gives enough
justification for the variance and ameliorates the biasedness than using
$n$ which is much better.

## The meaning of the concept of the unbiasedness of an estimator

If an estimator is unbiased, then the mean of estimates of many many
samples will converge to the parameter. In terms of the unbiased sample
variance, if you take many many samples and calculate variances for
**all** samples and take the mean, it will be close enough to the
population variance. However, if an estimator is biased, then as you
take more samples, the estimates will deviate from the true population
value.

I will add an R script that clarifies my point.

``` r
set.seed(19190709) 
mat0 <- matrix(0, nrow = 40, ncol = 2000) 
for (i in 1:2000) { 
  mat0[,i] <- rnorm(40, 5, 8) 
} 
 
biased_variances <- apply(mat0, 2, function(x) sum((x - mean(x))^2 / length(x))) 
unbiased_variances <- apply(mat0, 2, function(x) sum((x - mean(x))^2) / (length(x)-1)) 
```

This is an example where the each column of the matrix is one sample of
a normal distribution with mean 5 and variance 64. I calculated the
biased variance of each sample and also the unbiased variance of each
sample and took their expectations. Here is the output:

``` r
mean(biased_variances) 
```

    ## [1] 62.84786

``` r
mean(unbiased_variances)
```

    ## [1] 64.45934

The mean of the unbiased variances is closer to the population variance
64 than the that of the biased variances. This wouldn’t matter if the
sample size were large. This is another thing you need to check when you
want to figure out if an estimator is good. Check this out: [Consistent
estimator](https://en.wikipedia.org/wiki/Consistent_estimator)). I will
not go over this subject as it is not related directly to the question.

So, you can see empirically that the unbiased variance yields a better
estimate of the population variance.
