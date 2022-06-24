# Mann-Whitney-U-test, also known as Wilcoxon-Mann-Whitney test
# Not to be confused with Wilcoxon signed-rank test for dependent samples

# activate libraries
library(tidyverse)
library(moments)
library(ggplot2)
library(gamlss)
library(normtest)
library(nortest)

# set constants
options('scipen'=2, 'digits'=3)
set.seed(19190709)

# set work catalog
setwd('/home/kaarlahti/TresoritDrive/Methodics/My/AI_for_valuers/Book/AI_for_valuers_book/Parts-Chapters/Mann-Whitney-Wilcoxon/')

# create data set from file, create subset with needed variables,
# change the type of object to a more convenient and modern one
almatyFlats <- read.csv('almaty-apts-2019-1.csv',
                        header = TRUE, sep = ',',
                        dec = '.')
myvars <- c('price.m', 'furniture')
almatyFlats <- almatyFlats[myvars]
as_tibble(almatyFlats)

# calculation of the total number of observations,
# as well as depending on the equipment 
n.total <- nrow(almatyFlats)
n.non.equip <- NROW(almatyFlats$furniture[ which(almatyFlats$furniture == 0)])
n.equip <- NROW(almatyFlats$furniture[ which(almatyFlats$furniture > 0)])

# create function for second Nowiczkij formula
kHistNowiczkij2 <- function(x, na.omit = FALSE){ # create function, ignore missed values
  n   <- NROW(x)                                 # calculate n
  kurt = kurtosis(x)                             # calculate kurtosis
  kn2 = round((((kurt^4)*(n^2))^(1/5))*(1/3))    # calculate k
  return(kn2)                                    # return k  
}                                                # end of function

# calculation numbers of k for different types of observations
k.all.data <- kHistNowiczkij2(almatyFlats$price.m)
k.non.equip <- kHistNowiczkij2(almatyFlats$price.m[ which(almatyFlats$furniture == 0)])
k.equip <-kHistNowiczkij2(almatyFlats$price.m[ which(almatyFlats$furniture > 0)])

# plot the histogram, combined with the density curve of the theoretical
# normal distribution for all observations
histDist(almatyFlats$price.m,
         density = TRUE,
         nbins = kHistNowiczkij2(almatyFlats$price.m),
         xlab = 'price per meter, kaz tenge',
         ylab = 'probability',
         main = 'Price per meter histogram, all observations')

# plot the histogram, combined with the density curve of the theoretical
# normal distribution for observations without equipment
histDist(almatyFlats$price.m[ which(almatyFlats$furniture == 0)],
         density = TRUE,
         nbins = kHistNowiczkij2(almatyFlats$price.m[ which(almatyFlats$furniture == 0)]),
         xlab = 'price per meter, kaz tenge',
         ylab = 'probability',
         main = 'Price per meter histogram, observations witout equipment')

# plot the histogram, combined with the density curve of the theoretical
# normal distribution for observations with equipment
histDist(almatyFlats$price.m[ which(almatyFlats$furniture > 0)],
         density = TRUE,
         nbins = kHistNowiczkij2(almatyFlats$price.m[ which(almatyFlats$furniture > 0)]),
         xlab = 'price per meter, kaz tenge',
         ylab = 'probability',
         main = 'Price per meter histogram, observations witout equipment')

# summaries
summary(almatyFlats$price.m)
summary(almatyFlats$price.m[ which(almatyFlats$furniture == 0)])
summary(almatyFlats$price.m[ which(almatyFlats$furniture > 0)])

# plot boxplots
nequiped <- subset(almatyFlats, furniture == 0)
equiped <- subset(almatyFlats, furniture > 0)
boxplot(nequiped$price.m, equiped$price.m,
        ylab = 'price per meter',
        names =c('not equiped', 'equiped'))
rm(nequiped)
rm(equiped)

# normality tests for non equipped observations
# Shapiro-Wilk test for normality
shapiro.test(almatyFlats$price.m[ which(almatyFlats$furniture == 0)])
# Shapiro-Francia test for normality
sf.test(almatyFlats$price.m[ which(almatyFlats$furniture == 0)])
# Anderson-Darling test for normality
ad.test(almatyFlats$price.m[ which(almatyFlats$furniture == 0)])
# Adjusted Jarque-Bera test for normality
ajb.norm.test(almatyFlats$price.m[ which(almatyFlats$furniture == 0)])
# Lilliefors (Kolmogorov-Smirnov) test for normality
lillie.test(almatyFlats$price.m[ which(almatyFlats$furniture == 0)])

# normality tests for equipped observations
# Shapiro-Wilk test for normality
shapiro.test(almatyFlats$price.m[ which(almatyFlats$furniture > 0)])
# Shapiro-Francia test for normality
sf.test(almatyFlats$price.m[ which(almatyFlats$furniture > 0)])
# Anderson-Darling test for normality
ad.test(almatyFlats$price.m[ which(almatyFlats$furniture > 0)])
# Adjusted Jarque-Bera test for normality
ajb.norm.test(almatyFlats$price.m[ which(almatyFlats$furniture > 0)])
# Lilliefors (Kolmogorov-Smirnov) test for normality
lillie.test(almatyFlats$price.m[ which(almatyFlats$furniture > 0)])

# perform Mann-Whitney U-test
wilcox.test(almatyFlats$price.m[ which(almatyFlats$furniture == 0)],
            almatyFlats$price.m[ which(almatyFlats$furniture > 0)])