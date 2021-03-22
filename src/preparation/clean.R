
library(tidyverse)
library(stringr)
library(gsheet)
tweets <- read.csv("data/dataset1/tweet_data.csv")

tweets <- tweets %>% 
  mutate(Reply_count = replace(Reply_count, is.na(Reply_count), "0")) %>% 
  mutate(Retweets = replace(Retweets, is.na(Retweets), "0")) %>% 
  mutate(Like_count = replace(Like_count, is.na(Like_count), "0"))

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





tweets$Comment_clean <- gsub('???' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('«' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('©' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('o' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('T???' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('â' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('f' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('Ã' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('¯' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('$' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('~' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('¥' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('¡' , "", tweets$Comment_clean)


save(tweets,file="./gen/data-preparation/output/tweet_data_cleaned.RData")
