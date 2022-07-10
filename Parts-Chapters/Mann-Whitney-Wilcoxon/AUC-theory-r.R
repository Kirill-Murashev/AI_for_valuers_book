# Geometric interpretation of AUC

# activate libraries
library(pROC)
library(xtable)
# create dataset
category <- c(1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0)
prediction <- rev(seq_along(category))
prediction[9:10] <- mean(prediction[9:10])

# create ROC object&dataframe and calculate AUC
roc_obj <- roc(category, prediction)
auc(roc_obj)
roc_df <- data.frame(
  TPR=rev(roc_obj$sensitivities), 
  FPR=rev(1 - roc_obj$specificities), 
  labels=roc_obj$response, 
  scores=roc_obj$predictor)

# export table to LaTeX
xtable(roc_df)

# create function for plotting rectangles
rectangle <- function(x, y, width, height, density=12, angle=45, ...) 
  polygon(c(x,x+width,x+width,x), c(y,y,y+height,y+height), 
          density=density, angle=angle, ...)

# add dFPR and dTPR columns
roc_df <- transform(roc_df, 
                    dFPR = c(diff(FPR), 0),
                    dTPR = c(diff(TPR), 0))

# plot empty graph from 0 to 1 for each axis
plot(0:10/10, 0:10/10, type='n', xlab="FPR", ylab="TPR",
     main = 'ROC-curve and rectangles under it')
abline(h=0:10/10, col="lightblue")
abline(v=0:10/10, col="lightblue")

# create function for AUC calculation
appraiser_auc <- function(TPR, FPR){
  # inputs already sorted, best scores first 
  dFPR <- c(diff(FPR), 0)
  dTPR <- c(diff(TPR), 0)
  sum(TPR * dFPR) + sum(dTPR * dFPR)/2
}

# apply function to data
with(roc_df, appraiser_auc(TPR, FPR))

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

# apply function to data
rank_comparison_auc(labels=as.logical(category), scores=prediction)

# create function for calculation AUC as probability
auc_probability <- function(labels, scores, N=1e7){
  pos <- sample(scores[labels], N, replace=TRUE)
  neg <- sample(scores[!labels], N, replace=TRUE)
  # sum( (1 + sign(pos - neg))/2)/N # does the same thing
  (sum(pos > neg) + sum(pos == neg)/2) / N # give partial credit for ties
}

# apply function to data
auc_probability(as.logical(category), prediction)
