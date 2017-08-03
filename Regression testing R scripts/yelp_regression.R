#dsouza{c,d,m}@indiana.edu
##***************************************************************************************
#*    Title: yelp-review-analysis
#*    Author: Max Woolf
#*    Availability: https://github.com/minimaxir/yelp-review-analysis/blob/master/yelp_review_analysis.r"
#***************************************************************************************

library(caret)

data_reviews <-read.csv("yelp_regression.csv",header=T)
data_reviews$is_positive = as.factor(ifelse(data_reviews$stars >= 4, "1", "0"))

# Logistic Regression + Cross-Validation
trainIndex <- unlist(createDataPartition(data_reviews$is_positive, p = 0.75))
reviews_reg_logit = glm(is_positive ~ review_length + pos_words + neg_words, family = "binomial", data=data_reviews[trainIndex,])
predicted_prob_pos = predict(reviews_reg_logit,data_reviews[-trainIndex,])

# Truth Table
threshold <- 0.50 # if predicted probability is greater than 0.5, say that the review is positive.
accuracy <- sum(ifelse(predicted_prob_pos > threshold,1,0)==data_reviews$is_positive[-trainIndex]) / length(data_reviews$is_positive[-trainIndex]) # 0.75
accuracy

#[1] 0.6089626