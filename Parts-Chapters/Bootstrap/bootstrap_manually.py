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
