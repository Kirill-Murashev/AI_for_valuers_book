#  Handling of outliers when working with open market data: Part I



__[Cyrill A. Murashev](https://github.com/Kirill-Murashev)__, 2022-11-14

## Abstract
The best practice in valuation is to work with data that is directly observable in open markets. This assertion is based on, among other things, the statements of __[IFRS 13 Fair Value Mesurement](https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2022/issued/part-a/ifrs-13-fair-value-measurement.pdf?bypass=on)__, __[IVS 2022](https://www.rics.org/contentassets/542170a3807548a28aebb053152f1c24/ivsc-effective-31-jan-2022.pdf)__, and __[RVGS 2022](https://www.rics.org/globalassets/rics-website/media/upholding-professional-standards/sector-standards/valuation/2021-11-25_rics-valuation--global-standards-effective-2022.pdf)__. One of the problems of market data is the problem of __[outliers](https://en.wikipedia.org/wiki/Outlier)__, i.e., observations whose value of a feature differs significantly from the rest. This material contains no theory.  It is aimed at handling of outliers using the Python language. We will work on the example of the residential real estate market in Almaty (Republic of Kazakhstan). As we work on this topic, we will consider the following questions:
<ul>
<li>what are the basic ways of handling outliers?</li>
<li>how to detect and handle outliers using Python?</li>
</ul>
In all, we will look at three simple ways to handle outliers. Python is more a language for business and professional activities than for science. A number of more complex methods of handling outliers will be discussed in a separate material containing code in R. In this paper we will limit ourselves to the following methods: 
<ol>
<li>the aprroach based on the empirical relations of the Normal distribution (The z-score approach);</li>
<li>Tukey's fences (or the interquartile range (IQR) proximity rule);</li>
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

![Fig. Characteristics of a Normal Distribution](The_Normal_Distribution.svg)

This figure was taken from the Wikipedia article __['Standard score'](https://en.wikipedia.org/wiki/Standard_score)__.

### Skewed distribution
In this case we should prefer **Tukey's fences (or the Inter-Quartile Range (IQR) proximity rule)**. The data points which fall below $Q1 – 1.5\cdot IQR$ or above $Q3 + 1.5\cdot IQR$ are outliers, where $Q1$ and $Q3$ are the $0.25$ and $0.75$ quantiles of the dataset respectively, and IQR represents the inter-quartile range and given by $Q3 – Q1$.

![Fig. IQR (Tukey's fences.png](IQR-tukeys-fences.png)

This figure was taken from article __['Practical Guide to Outlier Detection Methods'](https://towardsdatascience.com/practical-guide-to-outlier-detection-methods-6b9f947a161e)__.

### Unknown distribution
It's reasonable to use **The percentile-based approach** in such a case. *For example*, we can set by ourselves that data points that are greater than from 0.99 quantile and less than 0.01 auantile are considered to be an outlier.

![Fig. PR and NCE.gif](PR_and_NCE.gif)

## Practical implementation in Python

### The z-score approach
Key assumption: the features are normally or approximately normally distributed.

Step 1: import necessary dependencies.


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
```


```python
sns.set_theme(style='ticks')
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
      <th>444</th>
      <td>445</td>
      <td>26000000</td>
      <td>342105</td>
      <td>76.0</td>
      <td>58.0</td>
      <td>0.76</td>
      <td>4</td>
      <td>10</td>
      <td>12</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1991</td>
      <td>m</td>
      <td>good</td>
      <td>342.1</td>
      <td>2</td>
      <td>NBH aksaj-2</td>
      <td>19</td>
    </tr>
    <tr>
      <th>1858</th>
      <td>1859</td>
      <td>22000000</td>
      <td>456432</td>
      <td>48.2</td>
      <td>25.2</td>
      <td>0.52</td>
      <td>2</td>
      <td>1</td>
      <td>5</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1984</td>
      <td>k</td>
      <td>high</td>
      <td>456.4</td>
      <td>1</td>
      <td>NBH 11</td>
      <td>44</td>
    </tr>
    <tr>
      <th>2332</th>
      <td>2333</td>
      <td>17500000</td>
      <td>426829</td>
      <td>41.0</td>
      <td>32.0</td>
      <td>0.78</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1989</td>
      <td>k</td>
      <td>good</td>
      <td>426.8</td>
      <td>2</td>
      <td>NBH koktem-1</td>
      <td>56</td>
    </tr>
    <tr>
      <th>323</th>
      <td>324</td>
      <td>25000000</td>
      <td>287356</td>
      <td>87.0</td>
      <td>55.0</td>
      <td>0.63</td>
      <td>4</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1990</td>
      <td>p</td>
      <td>good</td>
      <td>287.4</td>
      <td>0</td>
      <td>NBH aksaj-3a</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1212</th>
      <td>1213</td>
      <td>23000000</td>
      <td>410714</td>
      <td>56.0</td>
      <td>40.0</td>
      <td>0.71</td>
      <td>2</td>
      <td>2</td>
      <td>5</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1993</td>
      <td>k</td>
      <td>good</td>
      <td>410.7</td>
      <td>2</td>
      <td>NBH taugulь-2</td>
      <td>52</td>
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
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
ax = plt.subplot(1,1,1)
sns.distplot(almatyApts['price_m'])
ax.set_xlabel('price per one square meter, kaz tenge')
ax.title.set_text('Histogram of the initial data')
plt.show()
```


    
![png](output_23_0.png)
    


Step 5: calculate the values of both boundaries


```python
UpBoundZ = almatyApts['price_m'].mean() + 3*almatyApts['price_m'].std()
LoBoundZ = almatyApts['price_m'].mean() - 3*almatyApts['price_m'].std()
print("The upper boundary is", UpBoundZ)
print("The lower boundary is", LoBoundZ)
```

    The upper boundary is 649395.6265495487
    The lower boundary is 73712.40657147043


We see that the lower bound is less than the minimum value in the dataset. Thus, the outliers are only in the right tail of the empirical distribution.

Step 6: outliers identification.


```python
outliersListZ = almatyApts[(almatyApts['price_m'] > UpBoundZ) | (almatyApts['price_m'] < LoBoundZ)]
StatsOutliersZ = outliersListZ["price_m"].describe()
print(StatsOutliersZ)
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
ax = plt.subplot(1,1,1)
sns.distplot(outliersListZ['price_m'])
ax.set_xlabel('price per one square meter, kaz tenge')
ax.title.set_text('Histogram of outliers identified by The z-score approach')
plt.show()
```


    
![png](output_30_0.png)
    


Let's try to apply to the dataset both trimming and vinsorization. After that, we will compare the results.

Step 7: trimming of outliers.


```python
almatyAptsZTrim = almatyApts[(almatyApts['price_m'] <= UpBoundZ) & (almatyApts['price_m'] >= LoBoundZ)]
StatsTrimZ = almatyAptsZTrim["price_m"].describe()
print(StatsTrimZ)
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
ax = plt.subplot(1,1,1)
sns.distplot(almatyAptsZTrim['price_m'])
ax.set_xlabel('price per one square meter, kaz tenge')
ax.title.set_text('Histogram of data trimmed by The z-score approach')
plt.show()
```


    
![png](output_35_0.png)
    


Step 8: winsorization.


```python
almatyApts['price_m_zw'] = np.where(
    almatyApts['price_m'] > UpBoundZ,
    UpBoundZ,
    np.where(
        almatyApts['price_m'] < LoBoundZ,
        LoBoundZ,
        almatyApts['price_m']
    )
)
```


```python
StatsWinsorZ = almatyApts['price_m_zw'].describe()
print(StatsWinsorZ)
```

    count      2355.000000
    mean     359949.898914
    std       89779.757996
    min      117000.000000
    25%      300000.000000
    50%      344432.000000
    75%      400000.000000
    max      649395.626550
    Name: price_m_zw, dtype: float64



```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
ax = plt.subplot(1,1,1)
sns.distplot(almatyApts['price_m_zw'])
ax.set_xlabel('price per one square meter, kaz tenge')
ax.title.set_text('Histogram of data winsorized by The z-score approach')
plt.show()
```


    
![png](output_39_0.png)
    


As you can see, all extreme values were equalized to the upper boundary value; and they have formed one group. 

Now we can compare the initial, trimmed and winsorized data.


```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
plt.subplots_adjust(wspace=0.05,
                    hspace=0.8)
ax1 = plt.subplot(3,2,1)
sns.distplot(almatyApts['price_m'])
ax2 = plt.subplot(3,2,2)
sns.boxplot(data=almatyApts, x = 'price_m', whis=[0, 100],
            width=.6, palette="vlag", orient='h')
sns.stripplot(data=almatyApts, x = 'price_m',
              size=4, color=".3", linewidth=0)
ax3 = plt.subplot(3,2,3)
sns.distplot(almatyAptsZTrim['price_m'])
ax4 = plt.subplot(3,2,4)
sns.boxplot(data=almatyAptsZTrim, x = 'price_m', whis=[0, 100],
            width=.6, palette="vlag", orient='h')
sns.stripplot(data=almatyAptsZTrim, x = 'price_m',
              size=4, color=".3", linewidth=0)
ax5 = plt.subplot(3,2,5)
sns.distplot(almatyApts['price_m_zw'])
ax6 = plt.subplot(3,2,6)
sns.boxplot(data=almatyApts, x = 'price_m_zw', whis=[0, 100],
            width=.6, palette="vlag", orient='h')
sns.stripplot(data=almatyApts, x = 'price_m_zw',
              size=4, color=".3", linewidth=0)
ax3 = plt.subplot(3,2,3)
ax1.title.set_text('Histogram of the initial data')
ax2.title.set_text('Boxplot of the initial data')
ax3.title.set_text('Histogram of the data trimmed by The z-approach')
ax4.title.set_text('Boxplot of the data trimmed by The z-approach')
ax5.title.set_text('Histogram of the data winsorized by The z-approach')
ax6.title.set_text('Boxplot of the data winsorized by The z-approach')
plt.show()
```


    
![png](output_42_0.png)
    


### Tukey's fences
This approach is preferable when we deal with a skewed distribution. The first four steps are the same as in The z-score approach.

Step 5: plot a Box&Whiskers diagram for the skewed feature.


```python
f, ax = plt.subplots(figsize=(29, 8))
sns.boxplot(data=almatyApts, x = 'price_m', whis=[0, 100],
            width=.6, palette="vlag", orient='h')
sns.stripplot(data=almatyApts, x = 'price_m',
              size=4, color=".3", linewidth=0)
ax.set_xlabel('price per one square meter, kaz tenge')
ax.title.set_text('Boxplot of the initial data')
```


    
![png](output_45_0.png)
    


Step 6: calculate 0.25th and 0.75th quantiles.


```python
quantile25 = almatyApts['price_m'].quantile(0.25)
quantile75 = almatyApts['price_m'].quantile(0.75)
iqr = quantile75 - quantile25
print(quantile25)
print(quantile75)
print(iqr)
```

    300000.0
    400000.0
    100000.0


Step 7: calculate the upper and lower limits.


```python
UpLimT = quantile75 + 1.5 * iqr
LoLimT = quantile25 - 1.5 * iqr
print('The upper limit is', UpLimT)
print('The lower limit is', LoLimT)
```

    The upper limit is 550000.0
    The lower limit is 150000.0


Step 8: find and describe the outliers.


```python
outliersListT = almatyApts[(almatyApts['price_m'] > UpLimT) | (almatyApts['price_m'] < LoLimT)]
StatsOutliersT = outliersListT['price_m'].describe()
print(StatsOutliersT)
```

    count       115.000000
    mean     639633.139130
    std       98451.845579
    min      117000.000000
    25%      576419.500000
    50%      610526.000000
    75%      693907.000000
    max      928571.000000
    Name: price_m, dtype: float64


We found that this approach gave us more than twice outliers number relatively to Z-approach. The next difference is that now we have outliers in both tails of distribution. Thus, we will get a very strange histogram.


```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
ax = plt.subplot(1,1,1)
sns.distplot(outliersListT['price_m'])
ax.set_xlabel('price per one square meter, kaz tenge')
ax.title.set_text('Histogram of outliers identified by The Tukey\'s fence approach')
plt.show()
```


    
![png](output_53_0.png)
    


Step 9: trimming of outliers.


```python
almatyAptsTTrim = almatyApts[(almatyApts['price_m'] <= UpLimT) & (almatyApts['price_m'] >= LoLimT)]
StatsTrimT = almatyAptsTTrim["price_m"].describe()
print(StatsTrimT)
```

    count      2240.000000
    mean     347277.633036
    std       70778.126308
    min      152542.000000
    25%      298665.750000
    50%      338983.000000
    75%      388396.250000
    max      549451.000000
    Name: price_m, dtype: float64


Let's plot a histogram of trimmed data


```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
ax1 = plt.subplot(1,1,1)
sns.distplot(almatyAptsTTrim['price_m'])
ax1.title.set_text('Histogram of the trimmed data')
plt.show()
```


    
![png](output_57_0.png)
    


Step 10: winsorization.


```python
almatyApts['price_m_tw'] = np.where(
    almatyApts['price_m'] > UpLimT,
    UpLimT,
    np.where(
        almatyApts['price_m'] < LoLimT,
        LoLimT,
        almatyApts['price_m']
    )
)
```


```python
StatsWinsorT = almatyApts['price_m_tw'].describe()
print(StatsWinsorT)
```

    count      2355.000000
    mean     357007.175372
    std       81712.076941
    min      150000.000000
    25%      300000.000000
    50%      344432.000000
    75%      400000.000000
    max      550000.000000
    Name: price_m_tw, dtype: float64



```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
ax = plt.subplot(1,1,1)
sns.distplot(almatyApts['price_m_tw'])
ax.set_xlabel('price per one square meter, kaz tenge')
ax.title.set_text('Histogram of data winsorized by The Tukey\'s fence approach')
plt.show()
```


    
![png](output_61_0.png)
    


As you can see, all extreme values were also equalized to the upper boundary value; and they have formed one group which now is rather heavy. 

Let's compare the initial, trimmed and winsorized data.


```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
plt.subplots_adjust(wspace=0.05,
                    hspace=0.8)
ax1 = plt.subplot(3,2,1)
sns.distplot(almatyApts['price_m'])
ax2 = plt.subplot(3,2,2)
sns.boxplot(data=almatyApts, x = 'price_m', whis=[0, 100],
            width=.6, palette="vlag", orient='h')
sns.stripplot(data=almatyApts, x = 'price_m',
              size=4, color=".3", linewidth=0)
ax3 = plt.subplot(3,2,3)
sns.distplot(almatyAptsTTrim['price_m'])
ax4 = plt.subplot(3,2,4)
sns.boxplot(data=almatyAptsTTrim, x = 'price_m', whis=[0, 100],
            width=.6, palette="vlag", orient='h')
sns.stripplot(data=almatyAptsTTrim, x = 'price_m',
              size=4, color=".3", linewidth=0)
ax5 = plt.subplot(3,2,5)
sns.distplot(almatyApts['price_m_tw'])
ax6 = plt.subplot(3,2,6)
sns.boxplot(data=almatyApts, x = 'price_m_tw', whis=[0, 100],
            width=.6, palette="vlag", orient='h')
sns.stripplot(data=almatyApts, x = 'price_m_tw',
              size=4, color=".3", linewidth=0)
ax3 = plt.subplot(3,2,3)
ax1.title.set_text('Histogram of the initial data')
ax2.title.set_text('Boxplot of the initial data')
ax3.title.set_text('Histogram of the data trimmed by The t-approach')
ax4.title.set_text('Boxplot of the data trimmed by The t-approach')
ax5.title.set_text('Histogram of the data winsorized by The t-approach')
ax6.title.set_text('Boxplot of the data winsorized by The t-approach')
plt.show()
```


    
![png](output_64_0.png)
    


### The quantile-based approach
This approach should be suitable when we deal to unknown distribution. Its technique works by setting a particular threshold value, which decides based on our problem statement. The key assumption lays into the fact that we always maintain a symmetry. It means that if we remove $1\,\%$ from the right tail, we also drop by $1\,\%$  in the left one. The first four steps are the same as in the previous two subsections.

Step 5: calculate the upper and the lower limits.


```python
treshold = 0.01
UpLimQ = almatyApts['price_m'].quantile(1-treshold)
LoLimQ = almatyApts['price_m'].quantile(treshold)
print('The upper limit is', UpLimQ)
print('The lower limit is', LoLimQ)
```

    The upper limit is 718750.0
    The lower limit is 195881.13999999998


Step 6: find and describe the outliers.


```python
outliersListQ = almatyApts[(almatyApts['price_m'] > UpLimQ) | (almatyApts['price_m'] < LoLimQ)]
StatsOutliersQ = outliersListQ['price_m'].describe()
print(StatsOutliersQ)
```

    count        47.000000
    mean     473841.978723
    std      308406.127848
    min      117000.000000
    25%      182085.500000
    50%      195238.000000
    75%      771053.000000
    max      928571.000000
    Name: price_m, dtype: float64


As you can see, we got approximately as many outliers as in The z-approach. Due to aforementioned assumption, we got outliers from both tails. Thus, a histogram will show a bimodal distribution of outliers.


```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
ax = plt.subplot(1,1,1)
sns.distplot(outliersListQ['price_m'])
ax.set_xlabel('price per one square meter, kaz tenge')
ax.title.set_text('Histogram of outliers identified by The quantile approach')
plt.show()
```


    
![png](output_71_0.png)
    


Step 7: trimming the outliers.


```python
almatyAptsQTrim = almatyApts[(almatyApts['price_m'] <= UpLimQ) & (almatyApts['price_m'] >= LoLimQ)]
StatsTrimQ = almatyAptsQTrim["price_m"].describe()
print(StatsTrimQ)
```

    count      2308.000000
    mean     359267.389948
    std       85057.611260
    min      196429.000000
    25%      301724.000000
    50%      344438.000000
    75%      397727.000000
    max      718750.000000
    Name: price_m, dtype: float64



```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
ax1 = plt.subplot(1,1,1)
sns.distplot(almatyAptsQTrim['price_m'])
ax1.title.set_text('Histogram of the data trimmed by The quantile approach (treshold = 0.01)')
plt.show()
```


    
![png](output_74_0.png)
    


Step 8: winsorization.


```python
almatyApts['price_m_qw'] = np.where(
    almatyApts['price_m'] > UpLimQ,
    UpLimQ,
    np.where(
        almatyApts['price_m'] < LoLimQ,
        LoLimQ,
        almatyApts['price_m']
    )
)
```


```python
StatsWinsorQ = almatyApts['price_m_qw'].describe()
print(StatsWinsorQ)
```

    count      2355.000000
    mean     361113.177648
    std       92853.319961
    min      195881.140000
    25%      300000.000000
    50%      344432.000000
    75%      400000.000000
    max      718750.000000
    Name: price_m_qw, dtype: float64



```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
ax1 = plt.subplot(1,1,1)
sns.distplot(almatyApts['price_m_qw'])
ax1.title.set_text('Histogram of the data winsorized by The quantile approach (treshold = 0.01)')
plt.show()
```


    
![png](output_78_0.png)
    


The comparison of the initial, trimmed and winsorized data.


```python
warnings.filterwarnings('ignore')
plt.figure(figsize=(29,8))
plt.subplots_adjust(wspace=0.05,
                    hspace=0.8)
ax1 = plt.subplot(3,2,1)
sns.distplot(almatyApts['price_m'])
ax2 = plt.subplot(3,2,2)
sns.boxplot(data=almatyApts, x = 'price_m', whis=[0, 100],
            width=.6, palette="vlag", orient='h')
sns.stripplot(data=almatyApts, x = 'price_m',
              size=4, color=".3", linewidth=0)
ax3 = plt.subplot(3,2,3)
sns.distplot(almatyAptsQTrim['price_m'])
ax4 = plt.subplot(3,2,4)
sns.boxplot(data=almatyAptsQTrim, x = 'price_m', whis=[0, 100],
            width=.6, palette="vlag", orient='h')
sns.stripplot(data=almatyAptsQTrim, x = 'price_m',
              size=4, color=".3", linewidth=0)
ax5 = plt.subplot(3,2,5)
sns.distplot(almatyApts['price_m_qw'])
ax6 = plt.subplot(3,2,6)
sns.boxplot(data=almatyApts, x = 'price_m_qw', whis=[0, 100],
            width=.6, palette="vlag", orient='h')
sns.stripplot(data=almatyApts, x = 'price_m_qw',
              size=4, color=".3", linewidth=0)
ax3 = plt.subplot(3,2,3)
ax1.title.set_text('Histogram of the initial data')
ax2.title.set_text('Boxplot of the initial data')
ax3.title.set_text('Histogram of the data trimmed by The q-approach')
ax4.title.set_text('Boxplot of the data trimmed by The q-approach')
ax5.title.set_text('Histogram of the data winsorized by The q-approach')
ax6.title.set_text('Boxplot of the data winsorized by The q-approach')
plt.show()
```


    
![png](output_80_0.png)
    



```python

```
