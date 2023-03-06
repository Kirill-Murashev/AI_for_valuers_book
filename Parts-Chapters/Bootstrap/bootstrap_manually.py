# CI




# Percentile

import numpy as np

def percentile_bootstrap(data, statistic, alpha=0.05, n_bootstraps=1000):
    """
    Perform a percentile bootstrap on the data and compute the confidence interval for a given statistic.

    Parameters:
    data (array-like): The original data to be bootstrapped.
    statistic (function): A function that computes the statistic of interest on a data sample.
    alpha (float): The desired level of confidence, between 0 and 1.
    n_bootstraps (int): The number of bootstrap samples to generate.

    Returns:
    A tuple containing the lower and upper bounds of the confidence interval.
    """

    # Generate n_bootstraps bootstrap samples
    bootstraps = []
    for i in range(n_bootstraps):
        sample = np.random.choice(data, size=len(data), replace=True)
        bootstraps.append(statistic(sample))

    # Compute the empirical percentiles of the bootstrap distribution
    lower_percentile = np.percentile(bootstraps, 100 * alpha / 2)
    upper_percentile = np.percentile(bootstraps, 100 * (1 - alpha / 2))

    # Return the confidence interval as a tuple
    return lower_percentile, upper_percentile

This function takes in three required parameters: the original data to be bootstrapped (data), a function that computes the statistic of interest on a data sample (statistic), and the desired level of confidence for the confidence interval (alpha). It also takes an optional parameter specifying the number of bootstrap samples to generate (n_bootstraps), which defaults to 1000.

The function first generates n_bootstraps bootstrap samples by sampling from the original data with replacement. It then applies the statistic function to each bootstrap sample to compute the value of the statistic of interest. Next, it computes the lower and upper bounds of the confidence interval using the empirical percentiles of the bootstrap distribution, as determined by the desired level of confidence alpha. Finally, it returns the confidence interval as a tuple containing the lower and upper bounds.

To use this function, you would need to provide your own data and statistic arguments. For example, if you wanted to estimate the confidence interval for the mean of a dataset x, you could use the following code:
    
    lower, upper = percentile_bootstrap(x, np.mean)
print(f"95% confidence interval for the mean: [{lower:.2f}, {upper:.2f}]")

This would call the percentile_bootstrap function with the dataset x and the np.mean function as the statistic argument, and return the 95% confidence interval for the mean as a tuple containing the lower and upper bounds. The f-string is used to print the confidence interval with two decimal places.

# Smoothed

import numpy as np

def smoothed_bootstrap(data, n_bootstraps=1000, alpha=0.05):
    """
    Computes smoothed bootstrap for mean and standard deviation of data.
    
    Parameters:
    -----------
    data : array-like
        The data to be analyzed.
    n_bootstraps : int, optional
        The number of bootstrap samples to generate. Default is 1000.
    alpha : float, optional
        The significance level used for computing confidence intervals. Default is 0.05.
    
    Returns:
    --------
    A tuple containing:
        - The smoothed bootstrap mean and its confidence interval.
        - The smoothed bootstrap standard deviation and its confidence interval.
    """
    n = len(data)
    bootstrap_means = []
    bootstrap_stds = []
    for i in range(n_bootstraps):
        sample_indices = np.random.choice(range(n), size=n, replace=True)
        bootstrap_mean = np.mean(data[sample_indices])
        bootstrap_std = np.std(data[sample_indices])
        bootstrap_means.append(bootstrap_mean)
        bootstrap_stds.append(bootstrap_std)
    
    smoothed_means = []
    smoothed_stds = []
    for i in range(n_bootstraps):
        kernel_weights = np.exp(-(i - np.arange(n_bootstraps))**2 / (2 * (alpha * n_bootstraps)**2))
        smoothed_mean = np.sum(kernel_weights * bootstrap_means) / np.sum(kernel_weights)
        smoothed_std = np.sum(kernel_weights * bootstrap_stds) / np.sum(kernel_weights)
        smoothed_means.append(smoothed_mean)
        smoothed_stds.append(smoothed_std)
    
    mean_ci = np.percentile(smoothed_means, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    std_ci = np.percentile(smoothed_stds, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return (np.mean(smoothed_means), mean_ci), (np.mean(smoothed_stds), std_ci)

# Here is an explanation of the code:

#    The smoothed_bootstrap function takes in the data to be analyzed, the number of bootstrap samples to generate (n_bootstraps), and the     significance level used for computing confidence intervals (alpha).
#    The function generates n_bootstraps bootstrap samples from the data and computes the mean and standard deviation of each sample.
#    The function then computes a smoothed bootstrap estimate for the mean and standard deviation by applying a Gaussian kernel to the bootstrap means and standard deviations. The kernel width is controlled by the alpha parameter.
#    Finally, the function computes confidence intervals for the smoothed bootstrap mean and standard deviation using the percentiles of the smoothed bootstrap estimates.
#    The function returns a tuple containing the smoothed bootstrap mean and its confidence interval, and the smoothed bootstrap standard deviation and its confidence interval.

#You can use this function like this:
    
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean, std = smoothed_bootstrap(data)
print(f"Smoothed bootstrap mean: {mean[0]:.2f} ({mean[1][0]:.2f}, {mean[1][1]:.2f})")
print(f"Smoothed bootstrap standard deviation: {std[0]:.2f} ({std[1][0]:.2f}, {std[1][1]:.2f})")


# Basic 

import numpy as np

def bootstrap_mean_std(data, n_bootstrap=1000):
    """Calculate the bootstrap mean and standard deviation of a dataset.
    
    Parameters
    ----------
    data : array-like
        The dataset for which to calculate the bootstrap mean and standard deviation.
    n_bootstrap : int, optional
        The number of bootstrap samples to generate. Default is 1000.
    
    Returns
    -------
    tuple
        A tuple containing the bootstrap mean and standard deviation.
    """
    n = len(data)
    bootstrap_means = np.zeros(n_bootstrap)
    bootstrap_stds = np.zeros(n_bootstrap)
    for i in range(n_bootstrap):
        bootstrap_sample = np.random.choice(data, size=n, replace=True)
        bootstrap_means[i] = np.mean(bootstrap_sample)
        bootstrap_stds[i] = np.std(bootstrap_sample, ddof=1)
    bootstrap_mean = np.mean(bootstrap_means)
    bootstrap_std = np.mean(bootstrap_stds)
    return (bootstrap_mean, bootstrap_std)

# This function takes in a dataset as an array-like object and the number of bootstrap samples to generate (default is 1000). It then generates n_bootstrap bootstrap samples by randomly sampling from the dataset with replacement. For each bootstrap sample, it calculates the mean and standard deviation and stores them in bootstrap_means and bootstrap_stds, respectively. Finally, it calculates the mean of the bootstrap means and the mean of the bootstrap standard deviations and returns them as a tuple. Note that we use ddof=1 in the calculation of the standard deviation to compute the sample standard deviation.


# Bayesian

import numpy as np

def bayesian_bootstrap(data, num_samples=1000):
    """
    Perform Bayesian bootstrap on data.
    
    Parameters
    ----------
    data : array_like
        Input data.
    num_samples : int, optional
        Number of samples to generate.
    
    Returns
    -------
    resamples : ndarray
        Array of resampled data.
    """
    
    # Generate uniform weights for each data point
    weights = np.ones_like(data) / len(data)
    
    # Generate resamples by drawing samples with replacement
    # using the weights as probabilities
    resamples = np.zeros((num_samples, len(data)))
    for i in range(num_samples):
        resamples[i] = np.random.choice(data, size=len(data), replace=True, p=weights)
    
    return resamples

# To use this function, simply pass in your data as an array and specify the number of samples you want to generate (default is 1000). The function will return an array of resampled data with shape (num_samples, len(data)).

# Here's an example usage:

# Generate some random data
data = np.random.normal(loc=0, scale=1, size=100)

# Perform Bayesian bootstrap
resamples = bayesian_bootstrap(data)

# Calculate mean and standard deviation of resampled data
mean = np.mean(resamples, axis=1)
std = np.std(resamples, axis=1)

# Print results
print("Mean:", np.mean(data))
print("95% credible interval for mean:", np.percentile(mean, [2.5, 97.5]))
print("Standard deviation:", np.std(data))
print("95% credible interval for standard deviation:", np.percentile(std, [2.5, 97.5]))



Confidence intervals are a statistical measure used to estimate the range of values within which a population parameter is likely to fall. The following are some common methods used to calculate confidence intervals:

    Standard Error Method: This method involves calculating the standard error of the sample mean and using it to construct a confidence interval.

    T-distribution Method: This method is used when the sample size is small or the population standard deviation is unknown. It involves using the t-distribution instead of the normal distribution to construct the confidence interval.

    Bootstrap Method: This method involves generating a large number of bootstrap samples from the original sample and using these samples to estimate the confidence interval.

    Bayesian Method: This method involves using prior knowledge or assumptions about the population to construct the confidence interval.

    Asymptotic Method: This method is used when the sample size is large and involves using the central limit theorem to construct the confidence interval.

    Exact Method: This method is used when the sample size is small and the population follows a normal distribution. It involves using the exact distribution of the sample mean to construct the confidence interval.

The choice of method depends on the nature of the data, the size of the sample, and the assumptions made about the population.



import numpy as np
from scipy.stats import scoreatpercentile

def asymptotic_ci(bootstrap_statistics, ci=95):
    """
    Calculate the confidence interval of a statistic using the asymptotic method.

    Parameters:
        bootstrap_statistics (array-like): The statistics calculated on the bootstrap samples.
        ci (int): The confidence interval to calculate. Defaults to 95%.

    Returns:
        A tuple containing the lower and upper bounds of the confidence interval.
    """
    # Calculate the empirical quantiles of the bootstrap statistics
    alpha = (100 - ci) / 2
    lower = scoreatpercentile(bootstrap_statistics, alpha)
    upper = scoreatpercentile(bootstrap_statistics, 100 - alpha)

    return lower, upper


Percentile

def appr_percentile_bootstrap(data, stat_func=np.mean, num_samples=20000, sample_size=None, alpha=0.05):
    """
    Perform a percentile bootstrap on the data and compute the confidence interval for a given statistic.

    Parameters:
    data (array-like): The original data to be bootstrapped.
    statistic (function): A function that computes the statistic of interest on a data sample.
    alpha (float): The desired level of confidence, between 0 and 1.
    n_bootstraps (int): The number of bootstrap samples to generate.

    Returns:
    A tuple containing the lower and upper bounds of the confidence interval.
    """
    
    if sample_size is None:
        sample_size = len(data)
    
    # Generate n_bootstraps bootstrap samples
    bootstraps = []
    for i in range(num_samples):
        sample = np.random.choice(data, sample_size, replace=True)
        bootstraps.append(stat_func(sample))
        
    # Compute the statistic and empirical percentiles of the bootstrap distribution
    bootstrap_statistics = np.apply_along_axis(stat_func, axis = 0, arr=bootstraps)
    statistic = np.mean(bootstrap_statistics)
    lower_percentile = np.percentile(bootstraps, 100 * alpha / 2)
    upper_percentile = np.percentile(bootstraps, 100 * (1 - alpha / 2))

    # Return the confidence interval as a tuple
    return statistic, lower_percentile, upper_percentile

# apply the 'appr_percentile_bootstrap' function to data
tp_percentile_bootstrap_mean = appr_percentile_bootstrap(data['price'])
tp_percentile_bootstrap_std  = appr_percentile_bootstrap(data['price'], stat_func = appr_sam_std)
up_percentile_bootstrap_mean = appr_percentile_bootstrap(data['price_m'])
up_percentile_bootstrap_std  = appr_percentile_bootstrap(data['price_m'], stat_func = appr_sam_std)

# extract single balues from tuple
tp_perb_mean, tp_perb_mean_lowCI, tp_perb_mean_upperCI = tp_percentile_bootstrap_mean
tp_perb_std, tp_perb_std_lowCI, tp_mean_perb_upperCI = tp_percentile_bootstrap_std
up_perb_mean, up_perb_mean_lowCI, up_perb_mean_upperCI = up_percentile_bootstrap_mean
up_perb_std, up_perb_std_lowCI, up_mean_perb_upperCI = up_percentile_bootstrap_std

# output the result to the user
print(f'The mean price obtained by the percentile bootstrap is {tp_perb_mean:.2f} \
with 95% confidence interval [{tp_perb_mean_lowCI:.2f}, {tp_perb_mean_upperCI:.2f}].')
print(f'The standard deviation of the price obtained by the percentile bootstrap is {tp_perb_std:.2f} \
with 95% confidence interval [{tp_perb_std_lowCI:.2f}, {tp_mean_perb_upperCI:.2f}].')
print(f'The mean unit price obtained by the percentile bootstrap is {up_perb_mean:.2f} \
with 95% confidence interval [{up_perb_mean_lowCI:.2f}, {up_perb_mean_upperCI:.2f}].')
print(f'The standard deviation of the unit price obtained by the percentile bootstrap is {up_perb_std:.2f} \
with 95% confidence interval [{up_perb_std_lowCI:.2f}, {up_mean_perb_upperCI:.2f}].')


def appr_bayesian_bootstrap(X, statistic=np.mean, n_replications=2000, resample_size=None, low_mem=False, alpha=0.05):
    """Simulate the posterior distribution of the given statistic.

    Parameter X: The observed data (array like)

    Parameter statistic: A function of the data to use in simulation (Function mapping array-like to number)

    Parameter n_replications: The number of bootstrap replications to perform (positive integer)

    Parameter resample_size: The size of the dataset in each replication
    
    Parameter low_mem(bool): Generate the weights for each iteration lazily instead of in a single batch. Will use
    less memory, but will run slower as a result.

    Returns: Statistoc for the samples from the posterior
    """
    
    if resample_size is None:
        resample_size = len(X)
    
    if isinstance(X, list):
        X = np.array(X)
    samples = []
    if low_mem:
        weights = (np.random.dirichlet([1] * len(X)) for _ in range(n_replications))
    else:
        weights = np.random.dirichlet([1] * len(X), n_replications)
    for w in weights:
        sample_index = np.random.choice(range(len(X)), p=w, size=resample_size)
        resample_X = X[sample_index]
        s = statistic(resample_X)
        samples.append(s)
        
    samples_sorted = sorted(samples)
    window_size = int(len(samples) - round(len(samples)*alpha))
    smallest_window = (None, None)
    smallest_window_length = float('inf')
    for i in range(len(samples_sorted) - window_size):
        window = samples_sorted[i+window_size-1], samples_sorted[i]
        window_length = samples_sorted[i+window_size-1] - samples_sorted[i]
        if window_length < smallest_window_length:
            smallest_window_length = window_length
            smallest_window = window
            
    posterior_statistic = np.mean(samples)         
            
    return posterior_statistic, smallest_window[1], smallest_window[0]

# apply the 'appr_bayesian_bootstrap' function to data
tp_bayesian_bootstrap_mean = appr_bayesian_bootstrap(data['price'])
tp_bayesian_bootstrap_std  = appr_bayesian_bootstrap(data['price'], statistic = np.std)
up_bayesian_bootstrap_mean = appr_bayesian_bootstrap(data['price_m'])
up_bayesian_bootstrap_std  = appr_bayesian_bootstrap(data['price_m'], statistic = np.std)

# extract single balues from tuple
tp_bayb_mean, tp_bayb_mean_lowCI, tp_bayb_mean_upperCI = tp_bayesian_bootstrap_mean
tp_bayb_std, tp_bayb_std_lowCI, tp_mean_bayb_upperCI = tp_bayesian_bootstrap_std
up_bayb_mean, up_bayb_mean_lowCI, up_bayb_mean_upperCI = up_bayesian_bootstrap_mean
up_bayb_std, up_bayb_std_lowCI, up_mean_bayb_upperCI = up_bayesian_bootstrap_std


# output the result to the user
print(f'The mean price obtained by the bayesian bootstrap is {tp_bayb_mean:.2f} \
with 95% confidence interval [{tp_bayb_mean_lowCI:.2f}, {tp_bayb_mean_upperCI:.2f}].')
print(f'The standard deviation of the price obtained by the bayesian bootstrap is {tp_bayb_std:.2f} \
with 95% confidence interval [{tp_bayb_std_lowCI:.2f}, {tp_mean_bayb_upperCI:.2f}].')
print(f'The mean unit price obtained by the bayesian bootstrap is {up_bayb_mean:.2f} \
with 95% confidence interval [{up_bayb_mean_lowCI:.2f}, {up_bayb_mean_upperCI:.2f}].')
print(f'The standard deviation of the unit price obtained by the bayesian bootstrap is {up_bayb_std:.2f} \
with 95% confidence interval [{up_bayb_std_lowCI:.2f}, {up_mean_bayb_upperCI:.2f}].')

