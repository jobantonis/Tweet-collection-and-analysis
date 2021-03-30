
library(tidyverse)
library(stringr)
library(data.table)
tweets <- read.csv("data/dataset1/DataCollection_Twitter.csv")

tweets$Reply.count <- as.numeric(sub("k", "e3", tweets$Reply.count, fixed = TRUE))
tweets$Retweets <- as.numeric(sub("k", "e3", tweets$Retweets, fixed = TRUE))
tweets$Like.count <- as.numeric(sub("k", "e3", tweets$Like.count, fixed = TRUE))

tweets <- tweets %>% 
  mutate(Reply.count = replace(Reply.count, is.na(Reply.count), "0")) %>% 
  mutate(Retweets = replace(Retweets, is.na(Retweets), "0")) %>% 
  mutate(Like.count = replace(Like.count, is.na(Like.count), "0"))

tweetscom <- str_remove_all(tweets$Comment, "Replying to ")
tweets["Comment_clean"] <- tweetscom
tweetsand <- str_remove_all(tweets$Comment_clean, " and ")
tweets["Comment_clean"] <- tweetsand
tweetsother <- str_remove_all(tweets$Comment_clean, " other ")
tweets["Comment_clean"] <- tweetsother
tweetsothers <- str_remove_all(tweets$Comment_clean, " others")
tweets["Comment_clean"] <- tweetsothers
tweets$Comment_clean <- gsub(" ?@\\w+ ?", "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('[0-9]+', "", tweets$Comment_clean)
tweets$Comment_clean <- gsub("[\r\n]" , "", tweets$Comment_clean)

tweets$Responding <- gsub("Quote.*" , "", tweets$Responding)

tweets$Comment <- NULL
tweets <- tweets[, c(1, 2, 3, 8, 4, 5, 6, 7)]

tweets$Comment_clean <- ifelse(tweets$Comment_clean == "", tweets$Responding, tweets$Comment_clean)
tweets$Responding <- NULL

tweets$Comment_clean <- trimws(tweets$Comment_clean)

tweets$Timestamp <- gsub("T" , ", ", tweets$Timestamp)
tweets$Timestamp <- gsub("Z" , "", tweets$Timestamp)
tweets$Timestamp <- gsub(".000" , "", tweets$Timestamp)

tweets$UserName <- match(tweets$UserName, unique(tweets$UserName))
tweets$Handle <- NULL

tweets$Comment_clean <- str_remove_all(tweets$Comment_clean, "[€«©œâƒÃ¯$˜¥¡™]")

tweets <- tweets[!duplicated(tweets$Comment_clean), ]
row.names(tweets) <- NULL

write.csv(tweets, "./gen/data-preparation/output/tweet_data_cleaned.csv", row.names = FALSE)
