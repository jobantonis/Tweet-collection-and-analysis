

## Data cleaning script

### import packages

#library(tm)
library(tidyverse)

library(stringr)
library(data.table)
tweets=data.frame(fread('https://spreadsheets.google.com/feeds/download/spreadsheets/Export?key=1fPcAKAf5qEycTAOjiqvDuKLo7kRGuk2NJaFkpRRbw2w&hl&exportFormat=csv'))



### Remove NA

```{r}
tweets <- tweets %>% 
  mutate(Reply.count = replace(Reply.count, is.na(Reply.count), "0")) %>% 
  mutate(Retweets = replace(Retweets, is.na(Retweets), "0")) %>% 
  mutate(Like.count = replace(Like.count, is.na(Like.count), "0"))

```

### Clean Comment column

```{r}
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

```

### Clean Responding column


tweets$Responding <- gsub("Quote.*" , "", tweets$Responding)


### Remove Comment column and add Comment_clean to correct position


tweets$Comment <- NULL
tweets <- tweets[, c(1, 2, 3, 8, 4, 5, 6, 7)]


### Add Responding to empty spaces Comment_clean and remove Responding column

tweets$Comment_clean <- ifelse(tweets$Comment_clean == "", tweets$Responding, tweets$Comment_clean)
tweets$Responding <- NULL


### Remove white spaces

tweets$Comment_clean <- trimws(tweets$Comment_clean)


### In timestamp: Replace T with , and Z with ""

```{r}
tweets$Timestamp <- gsub("T" , ", ", tweets$Timestamp)
tweets$Timestamp <- gsub("Z" , "", tweets$Timestamp)
tweets$Timestamp <- gsub(".000" , "", tweets$Timestamp)

```

### Encoding usernames to numerical values

```{r}
tweets$UserName <- match(tweets$UserName, unique(tweets$UserName))
tweets$Handle <- NULL

```

### Removing non-textual ASCII characters

```{r}
tweets$Comment_clean <- gsub('€' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('«' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('©' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('œ' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('™️' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('â' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('ƒ' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('Ã' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('¯' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('$' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('˜' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('¥' , "", tweets$Comment_clean)
tweets$Comment_clean <- gsub('¡' , "", tweets$Comment_clean)
```

write.table(tweets, 'gen/data-preparation/temp/tweets.csv', row.names=FALSE)
