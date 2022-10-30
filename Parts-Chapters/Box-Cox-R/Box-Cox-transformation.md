Application of the Box-Cox transformation in valuation
================
Cyrill A. Murashev,
2022-10-30

## Abstract

The ability to work with numerical data is an essential skill for an
appraiser. Price or cost per object or unit (e.g. square meter or foot,
lot, etc.), area, power, mileage, chronological age, and more are all
measured numerically. Appraisers work with numbers all the time.
Recently, there has been a trend toward more evaluations using
mathematical apparatus, methods of mathematical statistics, and machine
learning. Today, appraiser more often use a frequentist approach to
probability rather than a Bayesian approach. In this regard, they are
often faced with the following problem. Many statistical tests and
methods assume a normal distribution of data. But the economic data that
appraisers usually deal with are most likely to have a distribution
other than normal. This poses a definite problem. The purpose of this
paper is to give appraisers a tool to overcome this problem. The Box-Cox
transformation in many cases allows you to transform the data in such a
way that their distribution is normal. This will allow you to apply
parametric methods. This paper consists of three parts. The first
contains a general theoretical description of the method. In the second,
we will apply the basic method implementation to the data of residential
real estate in Almaty. The third part will focus on some of the more
difficult practical issues, in particular, we will consider the
possibility of applying a two-parameter transformation model. I used the
R language to write this paper. The use of Python to perform the Box-Cox
transformation is discussed in a later paper.

## General description

### The concept of Power transform

In [statistics](https://en.wikipedia.org/wiki/Statistics), a power
transform is a family of functions applied to create a [monotonic
transformation](https://en.wikipedia.org/wiki/Monotonic_function) of
data using [power
functions](https://en.wikipedia.org/wiki/Power_function). It is a [data
transformation](https://en.wikipedia.org/wiki/Data_transformation_(statistics))
technique used to [stabilize
variance](https://en.wikipedia.org/wiki/Variance-stabilizing_transformation),
make the data more [normal
distribution](https://en.wikipedia.org/wiki/Normal_distribution)-like,
improve the validity of measures of association (such as the [Pearson
correlation](https://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient)
between variables), and for other data stabilization procedures.

### Definition

The power transformation is defined as a continuously varying function,
with respect to the power parameter $\textstyle{\lambda}$, in a
piece-wise function form that makes it continuous at the point of
singularity $\textstyle{(λ = 0)}$. For data vectors
$\textstyle{(y_{1}, \ldots, y_{n})}$ in which each
$\textstyle{y_{i} > 0}$, the power transform is $$
\displaystyle{\begin{equation}
y_{i}^{(\lambda)} = 
\begin{cases}
\frac{y_{i}^{\lambda}-1}{\lambda(GM(y))^{\lambda-1}}, &if\ \lambda \neq 0 \\
GM(y) \ln y_{i}, &if\ \lambda = 0 \\
\end{cases}
\end{equation}}
$$

where

$$
\displaystyle{\begin{equation}
GM(y)= \biggl(\prod_{i=1}^{n}y_{i} \biggr)^\frac{1}{n} = \sqrt[n]{y_{1},y_{2}\cdots,y_{n}}
\end{equation}}
$$

is the [geometric mean](https://en.wikipedia.org/wiki/Geometric_mean) of
the observations $\textstyle{y_{1},\ldots,y_{n}}$. The case for
$\textstyle{\lambda = 0}$ is the limit as $\textstyle{\lambda}$
approaches $\textstyle{0}$. To see this, note that

$$
\displaystyle{\begin{equation}
y_{i}^{\lambda} = exp(\lambda \ln(y_{i})) = 1 + \lambda \ln(y_{i}) + O((\lambda \ln(y_{i}))^{2}).
\end{equation}}
$$

Then

$$
\displaystyle{\begin{equation}
\frac{y_{i}^{\lambda}-1}{\lambda} = \ln(y_{i}+O(\lambda)),
\end{equation}}
$$

and everything but $\textstyle{\ln(y_{i})}$ becomes negligible for
$\textstyle{\lambda}$ sufficiently small. You can include R code in the
document as follows:

``` r
summary(cars)
```

    ##      speed           dist       
    ##  Min.   : 4.0   Min.   :  2.00  
    ##  1st Qu.:12.0   1st Qu.: 26.00  
    ##  Median :15.0   Median : 36.00  
    ##  Mean   :15.4   Mean   : 42.98  
    ##  3rd Qu.:19.0   3rd Qu.: 56.00  
    ##  Max.   :25.0   Max.   :120.00

## Including Plots

You can also embed plots, for example:

![](Box-Cox-transformation_files/figure-gfm/pressure-1.png)<!-- -->

Note that the `echo = FALSE` parameter was added to the code chunk to
prevent printing of the R code that generated the plot.

## \## Bibliography

nocite: \| Wikipedia (n.d.) —

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-Wiki:Power-transform" class="csl-entry">

Wikipedia. n.d. “Power Transform.” Accessed October 30, 2022.
<https://en.wikipedia.org/wiki/Power_transform>.

</div>

</div>
