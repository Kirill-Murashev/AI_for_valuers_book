#  Handling of outliers when working with open market data: Part I



## Abstract
The best practice in valuation is to work with data that is directly observable in open markets. This assertion is based on, among other things, the statements of __[IFRS 13 Fair Value Mesurement](https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2022/issued/part-a/ifrs-13-fair-value-measurement.pdf?bypass=on)__, __[IVS 2022](https://www.rics.org/contentassets/542170a3807548a28aebb053152f1c24/ivsc-effective-31-jan-2022.pdf)__, and __[RVGS 2022](https://www.rics.org/globalassets/rics-website/media/upholding-professional-standards/sector-standards/valuation/2021-11-25_rics-valuation--global-standards-effective-2022.pdf)__. One of the problems of market data is the problem of __[outliers](https://en.wikipedia.org/wiki/Outlier)__, i.e. observations whose value of a feature differs significantly from the rest. This material contains no theory.  It is aimed at handling of outliers using the Python language. We will work on the example of the residential real estate market in Almaty (Republic of Kazakhstan). As we work on this topic, we will consider the following questions:
<ul>
<li>what are the basic ways of handling outliers?</li>
<li>how to detect and handle outliers using Python?</li>
</ul>
In all, we will look at three simple ways to handle outliers. Python is more a language for business and professional activities than for science. A number of more complex methods of handling outliers will be discussed in a separate material containing code in R. In this paper we will limit ourselves to the following methods: 
<ol>
<li>the aprroach based on the empirical relations of the Normal distribution (The z-score approach);</li>
<li>Tukey's fences (or the inter-quartile range (IQR) proximity rule);</li>
<li>the quantile-based approach.</li>
</ol>
This list of methods is not exhaustive. However, they will help cover the needs of an appraiser who is beginning to apply machine learning and mathematical statistics methods to his or her work.


## Possible ways to handle outliers
Before we proceed directly to work with the data, let us answer the question of what can be done with the observations identified as outliers at all. The choice of how to deal with an outlier should depend on the cause. Some estimators are highly sensitive to outliers, notably __[estimation of covariance matrices](https://en.wikipedia.org/wiki/Estimation_of_covariance_matrices)__. But this article is intended for appraisers just beginning to learn about the application of artificial intelligence methods. Therefore, it will consider only some basic ways of solving the outliers problem. With this simplification, we can identify the following approaches to the handling of outliers.

**Retention** Even when a normal distribution model is appropriate to the data being analyzed, outliers are expected for large sample sizes and should not automatically be discarded if that is the case. The application should use a classification algorithm that is robust to outliers to model data with naturally occurring outlier points. 

**Exclusion** Deletion of outlier data is a controversial practice frowned upon by many scientists. While mathematical criteria provide an objective and quantitative method for data rejection, they do not make the practice more scientifically or methodologically sound, especially in small sets or where a normal distribution cannot be assumed. Rejection of outliers is more acceptable in areas of practice where the underlying model of the market being measured and the usual distribution of measurement error are confidently known. An outlier resulting from a data collection error or clear error in the source may be excluded, but it is desirable that the source is at least verified. In any case, appraiser must clear disclose data about the initial set of observations as well as the reason of its part exclusion.

The two common approaches to exclude outliers are __[truncation](https://en.wikipedia.org/wiki/Truncation_(statistics))__ (or __[trimming](https://en.wikipedia.org/wiki/Trimmed_estimator)__) and __[Winsorizing](https://en.wikipedia.org/wiki/Winsorizing)__ (or winsorization as well as capping). Trimming discards the outliers whereas Winsorising replaces the outliers with the nearest 'nonsuspect' data.
<ul>
<li><b>Truncation</b> This method excludes the outlier values from our analysis. By applying this technique, we lose some data. Its main advantages are its simplest and fastest nature. The more outliers, the less reliable the final model will be, because it will be based on an increasingly smaller sample.</li>
    <li><b>Winsorizing</b> &#151 is the transformation of statistics by limiting extreme values in the statistical data to reduce the effect of possibly spurious outliers. Note that winsorizing is not equivalent to aforementioned simply excluding data, which is a simpler procedure, called trimming or truncation, but is a method of censoring data. </li>
</ul>

**Treating outliers as a missing value** By assuming outliers as the missing observations, treat them accordingly, i.e, same as those of missing values. You can read, for example, __[this brief introduction](https://www.analyticsvidhya.com/blog/2021/04/how-to-handle-missing-values-of-categorical-variables/)__ to the possible ways to handle missing values. Let me remind you that we are now looking at the very basics of machine learning in valuation.  Therefore, all of the methods, articles, and materials referenced in this paper are intended as an introduction to the topic.

Of course, there are a number of other more sophisticated methods. However, it is possible to limit yourself to these methods outlined above to begin to handle outliers successfully.

## Possible ways to detect outliers
First of all, it should be said that it is hardly possible to draw up an exhaustive list of methods for identifying outliers. We can only mention some well-known well-developed methods such as __[Chauvenet's criterion](https://en.wikipedia.org/wiki/Chauvenet%27s_criterion)__, __[Peirce's criterion](https://en.wikipedia.org/wiki/Peirce%27s_criterion)__, __[Local Outlier Factor](https://en.wikipedia.org/wiki/Local_Outlier_Factor)__, __[Modified Thompson Tau test](https://en.wikipedia.org/wiki/Studentized_residual#Distribution)__, __[Grubbs's test](https://en.wikipedia.org/wiki/Grubbs%27s_test)__, __[Dixon's Q test](https://en.wikipedia.org/wiki/Dixon%27s_Q_test)__, __[Rosner's Outlier Test](https://vsp.pnnl.gov/help/vsample/rosners_outlier_test.htm)__. etc. But in this paper, we will consider some of the simplest and most intuitive methods that do not require special knowledge of mathematical statistics and machine learning. Therefore, we will limit ourselves to three methods, the choice of which depends on the distribution of the data in the sample.

### Normal or approximately normal distribution
In this case we can use **empirical relations of Normal distribution (The z-score approach)**. The data points which fall below $\bar y - 3\sigma$ or above $\bar y + 3\sigma$ are outliers, where $\bar y$ and $\sigma$ are the mean and the standard deviation respectively.

![Fig.-Characteristics-of-a-Normal-Distribution](attachment:The_Normal_Distribution.svg)

This figure was taken from the Wikipedia article __['Standard score'](https://en.wikipedia.org/wiki/Standard_score)__.

### Skewed distribution
In this case we should prefer **Tukey's fences (or the Inter-Quartile Range (IQR) proximity rule)**. The data points which fall below $Q1 – 1.5\cdot IQR$ or above $Q3 + 1.5\cdot IQR$ are outliers, where $Q1$ and $Q3$ are the $0.25$ and $0.75$ quantiles of the dataset respectively, and IQR represents the inter-quartile range and given by $Q3 – Q1$.

![IQR-tukeys-fences.png](attachment:IQR-tukeys-fences.png)

This figure was taken from article __['Practical Guide to Outlier Detection Methods'](https://towardsdatascience.com/practical-guide-to-outlier-detection-methods-6b9f947a161e)__.

### Unknown distribution
It's reasonable to use **The percentile-based approach** in such a case. *For example*, we can set by ourselves that data points that are greater than from 0.99 quantile and less than 0.01 auantile are considered to be an outlier.

![PR_and_NCE.gif](attachment:PR_and_NCE.gif)

## Practical implementation in Python

### The z-score approach
Key assumption: the features are normally or approximately normally distributed.

Step 1: import necessary dependencies.


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

Step 2: Import data and create the dataset.


```python
almatyApts = pd.read_csv('almaty-apts-2019-1.csv')
almatyApts.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>price</th>
      <th>price_m</th>
      <th>total_square</th>
      <th>living_square</th>
      <th>ratio_livtot</th>
      <th>rooms</th>
      <th>level</th>
      <th>total_levels</th>
      <th>not_ground_floor</th>
      <th>...</th>
      <th>concrete</th>
      <th>part_furniture</th>
      <th>full_furniture</th>
      <th>year</th>
      <th>walls</th>
      <th>condition</th>
      <th>price_m_k</th>
      <th>furniture</th>
      <th>district_name</th>
      <th>district_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>631</th>
      <td>632</td>
      <td>22300000</td>
      <td>586842</td>
      <td>38.0</td>
      <td>18.0</td>
      <td>0.47</td>
      <td>1</td>
      <td>3</td>
      <td>9</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1994</td>
      <td>m</td>
      <td>good</td>
      <td>586.8</td>
      <td>0</td>
      <td>NBH samal-2</td>
      <td>60</td>
    </tr>
    <tr>
      <th>1634</th>
      <td>1635</td>
      <td>17800000</td>
      <td>287097</td>
      <td>62.0</td>
      <td>45.0</td>
      <td>0.73</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2007</td>
      <td>k</td>
      <td>high</td>
      <td>287.1</td>
      <td>0</td>
      <td>NBH kulager</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2254</th>
      <td>2255</td>
      <td>9000000</td>
      <td>152542</td>
      <td>59.0</td>
      <td>45.0</td>
      <td>0.76</td>
      <td>2</td>
      <td>6</td>
      <td>6</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2007</td>
      <td>m</td>
      <td>good</td>
      <td>152.5</td>
      <td>0</td>
      <td>NBH zhuldyz</td>
      <td>6</td>
    </tr>
    <tr>
      <th>309</th>
      <td>310</td>
      <td>17500000</td>
      <td>312500</td>
      <td>56.0</td>
      <td>34.0</td>
      <td>0.61</td>
      <td>2</td>
      <td>9</td>
      <td>9</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1984</td>
      <td>p</td>
      <td>good</td>
      <td>312.5</td>
      <td>1</td>
      <td>NBH aksaj-4</td>
      <td>23</td>
    </tr>
    <tr>
      <th>346</th>
      <td>347</td>
      <td>18000000</td>
      <td>428571</td>
      <td>42.0</td>
      <td>18.1</td>
      <td>0.43</td>
      <td>1</td>
      <td>3</td>
      <td>5</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1985</td>
      <td>p</td>
      <td>high</td>
      <td>428.6</td>
      <td>2</td>
      <td>NBH aksaj-4</td>
      <td>23</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 34 columns</p>
</div>



Step 3: calculate some descriptive statistics.


```python
StatsNumeric = almatyApts["price_m"].describe()
print(StatsNumeric)
```

    count      2355.000000
    mean     361554.016561
    std       95947.203330
    min      117000.000000
    25%      300000.000000
    50%      344432.000000
    75%      400000.000000
    max      928571.000000
    Name: price_m, dtype: float64


Step 4: plot the histogram for the unit price feature.


```python
import warnings
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
plt.subplot(1,2,1)
sns.distplot(almatyApts['price_m'])
plt.show()
```


    
![png](output_21_0.png)
    


Step 5: calculate the values of both boundaries


```python
UpBound = almatyApts['price_m'].mean() + 3*almatyApts['price_m'].std()
LoBound = almatyApts['price_m'].mean() - 3*almatyApts['price_m'].std()
print("The upper boundary is", UpBound)
print("The lower boundary is", LoBound)
```

    The upper boundary is 649395.6265495487
    The lower boundary is 73712.40657147043


We see that the lower bound is less than the minimum value in the dataset. Thus, the outliers are only in the right tail of the empirical distribution.

Step 6: outliers identification.


```python
outliersList = almatyApts[(almatyApts['price_m'] > UpBound) | (almatyApts['price_m'] < LoBound)]
StatsOutliers = outliersList["price_m"].describe()
print(StatsOutliers)
```

    count        43.000000
    mean     737249.046512
    std       66137.416560
    min      653846.000000
    25%      684188.000000
    50%      720588.000000
    75%      771665.000000
    max      928571.000000
    Name: price_m, dtype: float64


We found that 43 observations were outliers. All of them are in the right tail of the empirical distribution. Let's plot a histogam of their unit price values.


```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
plt.subplot(1,2,1)
sns.distplot(outliersList['price_m'])
plt.show()
```


    
![png](output_28_0.png)
    


Let's try to apply to the dataset both trimming and vinsorization. After that, we will compare the results.

Step 7: trimming of outliers.


```python
almatyAptsTrim = almatyApts[(almatyApts['price_m'] <= UpBound) & (almatyApts['price_m'] >= LoBound)]
StatsTrim = almatyAptsTrim["price_m"].describe()
print(StatsTrim)
```

    count      2312.000000
    mean     354566.608997
    std       81379.022681
    min      117000.000000
    25%      300000.000000
    50%      342857.000000
    75%      394759.750000
    max      649351.000000
    Name: price_m, dtype: float64


Let's plot a histogram of trimmed data.


```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
plt.subplot(1,2,1)
sns.distplot(almatyAptsTrim['price_m'])
plt.show()
```


    
![png](output_33_0.png)
    


Step 8: winsorization.


```python
almatyAptsWinsor = almatyApts
almatyAptsWinsor['price_m'] = np.where(
    almatyAptsWinsor['price_m'] > UpBound,
    UpBound,
    np.where(
        almatyAptsWinsor['price_m'] < LoBound,
        LoBound,
        almatyAptsWinsor['price_m']
    )
)
```


```python
StatsWinsor = almatyAptsWinsor["price_m"].describe()
print(StatsWinsor)
```

    count      2355.000000
    mean     359949.898914
    std       89779.757996
    min      117000.000000
    25%      300000.000000
    50%      344432.000000
    75%      400000.000000
    max      649395.626550
    Name: price_m, dtype: float64



```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
plt.subplot(1,2,1)
sns.distplot(almatyAptsWinsor['price_m'])
plt.show()
```


    
![png](output_37_0.png)
    


As you can see, all extreme values were equalized to the upper boundary value; and they have formed one group. 


```python

```
