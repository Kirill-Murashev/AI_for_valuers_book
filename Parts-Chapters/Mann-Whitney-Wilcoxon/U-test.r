# Mann-Whitney-U-test, also known as Mann-Whitney-Wilcoxon test
# Not to be confused with Wilcoxon signed-rank test for dependent samples

# activate libraries
library(tidyverse)
library(moments)
library(RCurl)

# set constants
options("scipen"=999, "digits"=3)
set.seed(19190709)

# set work catalog
setwd("/home/kaarlahti/TresoritDrive/Methodics/My/AI_for_valuers/Book/AI_for_valuers_book/Parts-Chapters/Mann-Whitney-Wilcoxon/")

# create data set from file, create subset with needed variables,
# change the type of object to a more convenient and modern one
almatyFlats <- read.csv('almaty-apts-2019-1.csv', header = TRUE, sep = ",", dec = ".")
myvars <- c("price.m", "furniture")
almatyFlats <- almatyFlats[myvars]
as_tibble(almatyFlats)

hist(almatyFlats$price.m[ which(almatyFlats$furniture == 0)], freq = FALSE)
