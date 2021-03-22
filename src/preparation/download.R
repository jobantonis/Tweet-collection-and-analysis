library(gsheet)

tweet_data <- gsheet2tbl('https://docs.google.com/spreadsheets/d/1fPcAKAf5qEycTAOjiqvDuKLo7kRGuk2NJaFkpRRbw2w/edit#gid=147348610')
tweets_df <- tweet_data

write.csv(tweets_df,"data/dataset1/tweet_data.csv", row.names = FALSE)
