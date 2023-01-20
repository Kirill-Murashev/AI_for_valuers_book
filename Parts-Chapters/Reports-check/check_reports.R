library(dplyr)
library(ggplot2)
library(vcd)
library(boot)

# read data
reports <- read.csv("~/TresoritDrive/Methodics/My/AI_for_valuers/Book/AI_for_valuers_book/Parts-Chapters/Reports-check/ds.csv")
reports <- na.omit(reports)
reports <- reports %>%
rename("method" = "Method")

glimpse(reports)
reports <- mutate(reports, 
                  violation = factor(violation, labels = c("No", "Yes")),
                  app_region = factor(app_region),
                  app_sex = factor(app_sex),
                  obj_region = factor(obj_region),
                  obj_type = factor(obj_type),
                  method = factor(method))

fit <- glm(violation ~ app_region + app_sex + app_age + app_experience +
             obj_region + obj_type + obj_square_quantile + obj_price_quantile +
             obj_unit_price_quantile + analogues_num + factors_num +
             ratio_aan_to_ean, reports, family = "binomial")

coef(fit)
summary <- summary(fit)$coefficients
