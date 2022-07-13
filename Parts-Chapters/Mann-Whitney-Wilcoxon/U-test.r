# Mann-Whitney-U-test, also known as Wilcoxon-Mann-Whitney test
# Not to be confused with Wilcoxon signed-rank test for dependent samples

# activate libraries
library(tidyverse)
library(moments)
library(ggplot2)
library(gamlss)
library(normtest)
library(nortest)
library(pROC)

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

# Calculate AUC

# create vector for labels
almatyFlats$labels <- rep(0, length(almatyFlats$price.m))

# set values by condition
almatyFlats$labels[almatyFlats$furniture > 0] <- 1

# create function to calculate AUC
auc_wmw <- function(labels, scores){
  labels <- as.logical(labels)
  pos <- scores[labels]
  neg <- scores[!labels]
  U <- as.numeric(wilcox.test(pos, neg)$statistic)
  U/(length(pos) * length(neg))
}

# apply auc_wmw to data
auc_wmw(almatyFlats$labels, almatyFlats$price.m)

# create function to calculate AUC in different way
auc_wmw2 <- function(labels, scores){
  labels <- as.logical(labels)
  n1 <- sum(labels)
  n2 <- sum(!labels)
  R1 <- sum(rank(scores)[labels])
  U1 <- R1 - n1 * (n1 + 1)/2
  U1/(n1 * n2)
}

# apply auc_wmw2 to data
auc_wmw2(almatyFlats$labels, almatyFlats$price.m)

# create function for drawing rectangles
rectangle <- function(x, y, width, height, density=12, angle=45, ...) 
  polygon(c(x,x+width,x+width,x), c(y,y,y+height,y+height), 
          density=density, angle=angle, ...)

# create function to prepare data for plotting
u_illustration_part1 <- function(labels, scores){
  # put cases in order by score
  sort_order <- order(scores)
  labels <- labels[sort_order]
  scores <- scores[sort_order]
  
  # count the cases
  n <- length(labels)
  
  # find overall rank for each case by score
  ranks <- rank(scores)
  
  # start with an empty plot
  plot(c(0, n), c(0, n), type='n', xlim = c(0, 2500),
       xlab="rank", ylab="case", asp=1)
  
# plot bars representing ranks of all cases
  mapply(rectangle, x=0, y=(n - 1):0,  # starting from the top 
         width=ranks, height=1, 
         density=NA, lwd=2, col=c("red", "green")[1 + labels])
# set labels   
  legend("topright", legend=c("negative cases (no furniture & equipment)", "positive cases (with furniture & equipment)"), 
         text.col=c("red", "green"), bty='o', box.lwd=1, inset=0.1)
}

# apply function to data
u_illustration_part1(labels=almatyFlats$labels, scores=almatyFlats$price.m)

# create function to stack positive cases
u_illustration_part2 <- function(labels, scores){
  # sort the cases
  sort_order <- order(scores)
  labels <- labels[sort_order]
  scores <- scores[sort_order]
  
  # count positive and negative cases
  n1 <- sum(labels)  # number of positive cases
  n2 <- sum(!labels) # number of negative cases
  
  # find the overall ranks for the positive cases
  ranks <- rank(scores)
  pos_ranks <- ranks[as.logical(labels)]
  
  # how far to slide each bar to make stairsteps on the right hand edge
  x_offset <- n2 + (1:n1) - pos_ranks
  
  # start with an empty plot  
  plot(c(0, n2 + n1), c(0, n1), type='n', asp=1,
       xlab="n2 + n1 divisions", ylab="n1 divisions")
  
  # plot bars for ranks of positive cases
  mapply(rectangle, x=x_offset, y=(n1 - 1):0, 
         width=pos_ranks, height=1,
         density=NA, border="darkgreen", lwd=2, col="green")
  
  # mark the area we remove, and the area we keep
  rectangle(n2, 0, n1, n1, density=10, col="red", lwd=1)
  rectangle(0, 0, n2, n1, density=0, col="black", lty=2, lwd=3)
  
  # draw a scaled version of the "official" ROC curve on top
  roc_obj <- roc(labels, scores)
  roc_df <- with(roc_obj, data.frame(FPR=rev(1 - specificities), 
                                     TPR=rev(sensitivities)))
  with(roc_df, lines(n2*FPR, n1*TPR, type='l', lwd=4, col="blue"))
}

# apply function to data
u_illustration_part2(labels=almatyFlats$labels, scores=almatyFlats$price.m)

AUC.1 <- auc_wmw(almatyFlats$labels, almatyFlats$price.m)
AUC.2 <- auc_wmw2(almatyFlats$labels, almatyFlats$price.m)
AUC <- mean(AUC.1, AUC.2)
RBC <- AUC - (1-AUC)
