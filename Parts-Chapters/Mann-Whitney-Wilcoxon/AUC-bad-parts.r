# Calculate AUC for big dataset

# activate libraries
library(xtable)

# set options
options(digits=22)
set.seed(19190709)

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

# compare link and response
fit_glm <- glm(bad_parts ~ x, training_set, family=binomial(link="logit"))

glm_link_scores <- predict(fit_glm, test_set, type="link")

glm_response_scores <- predict(fit_glm, test_set, type="response")

# create object for plotting ROC-curve on original data set
roc_full_resolution <- roc(test_set$bad_parts, glm_response_scores)

# round scores
rounded_scores <- round(glm_response_scores, digits=1)

# create object for plotting ROC-curve on rounded scores
roc_rounded <- roc(test_set$bad_parts, rounded_scores)

# plot ROC-curve on original data
plot(roc_full_resolution, print.auc=TRUE)

# plot ROC-curve on rounded data
lines(roc_rounded, col="red", type='b')
text(0.4, 0.43, labels=sprintf("AUC: %0.3f", auc(roc_rounded)), col="red")

# create function for AUC calculation
appraiser_auc <- function(TPR, FPR){
  # inputs already sorted, best scores first 
  dFPR <- c(diff(FPR), 0)
  dTPR <- c(diff(TPR), 0)
  sum(TPR * dFPR) + sum(dTPR * dFPR)/2
}

# create  function for rank comparison
rank_comparison_auc <- function(labels, scores, plot_image=TRUE, ...){
  score_order <- order(scores, decreasing=TRUE)
  labels <- as.logical(labels[score_order])
  scores <- scores[score_order]
  pos_scores <- scores[labels]
  neg_scores <- scores[!labels]
  n_pos <- sum(labels)
  n_neg <- sum(!labels)
  M <- outer(sum(labels):1, 1:sum(!labels), 
             function(i, j) (1 + sign(pos_scores[i] - neg_scores[j]))/2)
  
  AUC <- mean (M)
  if (plot_image){
    image(t(M[nrow(M):1,]), ...)
    library(pROC)
    with( roc(labels, scores),
          lines((1 + 1/n_neg)*((1 - specificities) - 0.5/n_neg), 
                (1 + 1/n_pos)*sensitivities - 0.5/n_pos, 
                col="blue", lwd=2, type='b'))
    text(0.5, 0.5, sprintf("AUC = %0.4f", AUC))
  }
  
  return(AUC)
}

# create function for calculation AUC as probability
auc_probability <- function(labels, scores, N=1e5){
  pos <- sample(scores[labels], N, replace=TRUE)
  neg <- sample(scores[!labels], N, replace=TRUE)
  # sum( (1 + sign(pos - neg))/2)/N # does the same thing
  (sum(pos > neg) + sum(pos == neg)/2) / N # give partial credit for ties
}

# apply all functions to data
results <- data.frame(
  `Full Resolution` = c(
    auc = as.numeric(auc(roc_full_resolution)),
    appraiser_auc = appraiser_auc(rev(roc_full_resolution$sensitivities),
                                  rev(1 - roc_full_resolution$specificities)),
    rank_comparison_auc = rank_comparison_auc(test_set$bad_parts,
                                              glm_response_scores, 
                                              main="Full-resolution scores (no ties)"),
    auc_probability = auc_probability(as.logical(test_set$bad_parts), glm_response_scores)
  ),
  `Rounded Scores` = c( 
    auc = as.numeric(auc(roc_rounded)),
    appraiser_auc = appraiser_auc(rev(roc_rounded$sensitivities),
                                  rev(1 - roc_rounded$specificities)),
    rank_comparison_auc = rank_comparison_auc(test_set$bad_parts, rounded_scores,
                                              main="Rounded scores (ties in all segments)"),
    auc_probability = auc_probability(as.logical(test_set$bad_parts), rounded_scores)
  )
)

# export table to LaTeX
xtable(results, digits = 22)
