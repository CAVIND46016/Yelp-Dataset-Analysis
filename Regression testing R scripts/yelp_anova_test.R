#dsouza{c,d,m}@indiana.edu
yelp <- (read.csv("yelp_regression.csv"))

fit<-lm(stars~ review_length ,data=yelp)
anova(fit)

fit1<- lm(stars~ pos_words +neg_words,data=yelp)
anova(fit1)


fit2<-lm(stars~ +review_length+pos_words+neg_words ,data=yelp)
anova(fit2)

anova(fit,fit1,fit2)

# Output:
# Analysis of Variance Table
# 
# Model 1: stars ~ review_length
# Model 2: stars ~ pos_words + neg_words
# Model 3: stars ~ +review_length + pos_words + neg_words
# Res.Df   RSS Df Sum of Sq        F    Pr(>F)    
# 1  19547 35277                                    
# 2  19546 32378  1   2898.70 1752.278 < 2.2e-16 ***
#   3  19545 32332  1     46.17   27.912 1.283e-07 ***
#   ---
#   Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1


