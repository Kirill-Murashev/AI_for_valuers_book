# Sample of ROC-analysis
# enable libraries
library(ggplot2)
library(dplyr)
library(pROC)

#set seed
set.seed(19190709)

# create own function for ROC
appraiserRoc <- function(labels, scores){
  labels <- labels[order(scores, decreasing=TRUE)]
  data.frame(TPR=cumsum(labels)/sum(labels),
             FPR=cumsum(!labels)/sum(!labels), labels)
}

# create function 
sim_parts_data <- function(N, noise=100){
  x <- runif(N, min=0, max=100)
  y <- 122 - x/2 + rnorm(N, sd=noise)
  bad_parts <- factor(y > 100)
  data.frame(x, y, bad_parts)
}

# create dataset
parts_data <- sim_parts_data(2000, 10)

# create rule for test subset
test_set_idx <- sample(1:nrow(parts_data), size=floor(nrow(parts_data)/4))

# create training and test subsets
test_set <- parts_data[test_set_idx,]
training_set <- parts_data[-test_set_idx,]

# plot graph
test_set %>% 
  ggplot(aes(x=x, y=y, col=bad_parts)) + 
  scale_color_manual(values=c("green", "red")) + 
  geom_point() + 
  ggtitle("Quality related to x")

# compare link and response
fit_glm <- glm(bad_parts ~ x, training_set, family=binomial(link="logit"))

glm_link_scores <- predict(fit_glm, test_set, type="link")

glm_response_scores <- predict(fit_glm, test_set, type="response")

score_data <- data.frame(link=glm_link_scores, 
                         response=glm_response_scores,
                         bad_parts=test_set$bad_parts,
                         stringsAsFactors=FALSE)

score_data %>% 
  ggplot(aes(x=link, y=response, col=bad_parts)) + 
  scale_color_manual(values=c("green", "red")) + 
  geom_point() + 
  geom_rug() + 
  ggtitle("Both link and response scores put cases in the same order")

# plot ROC
plot(roc(test_set$bad_parts, glm_response_scores, direction="<"),
     col="orange", lwd=3, main="The turtle finds its way", xlim = c(1, 0))
glm_simple_roc <- appraiser_roc(test_set$bad_parts=="TRUE", glm_link_scores)
with(glm_simple_roc, points(1 - FPR, TPR, col=1 + labels))

# plot ROC for 99% negative cases
N <- 2000
P <- 0.01
rare_success <- sample(c(TRUE, FALSE), N, replace=TRUE, prob=c(P, 1-P))
guess_not <- rep(0, N)
plot(roc(rare_success, guess_not), print.auc=TRUE)
appr_roc <- appraiserRoc(rare_success, guess_not)
with(appr_roc, lines(1 - FPR, TPR, col="blue", lty=2))
