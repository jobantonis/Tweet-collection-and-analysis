# install.packages('twitteR', dependencies=T);
# install.packages('ggplot2', dependencies=T);
# install.packages('XML', dependencies=T);
# install.packages('plyr', dependencies=T);
# install.packages('doBy', dependencies=T);
# install.packages('tm', dependencies=T);
# install.packages('RJSONIO', dependencies=T)
# install.packages('RWeka')
# install.packages('base64enc')
install.packages("purrr")
library(twitteR);
library(ggplot2);
library(plyr);
library(doBy);
library(RJSONIO)
library(stringr)


library(readr)

text <- read_csv(file.choose())
#get rid of all non-ASCII characters
gsub("[^\x01-\x7F]", "", text)

library(tm)
library(xml2)
library(dplyr)
library(purrr)

sentiment_nl <- read_xml("https://raw.githubusercontent.com/clips/pattern/master/pattern/text/nl/nl-sentiment.xml"
                         ) %>% 
  as_list() %>% 
  .[[1]] %>% 
  map_df(function(x) {
    tibble::enframe(attributes(x))
  }) %>% 
  mutate(id = cumsum(str_detect("form", name)))  %>% 
  unnest(value) %>% 
  pivot_wider(id_cols = id) %>% 
  mutate(form = tolower(form), # lowercase all words to ignore case during matching
         polarity = as.numeric(polarity),
         subjectivity = as.numeric(subjectivity),
         intensity = as.numeric(intensity),
         confidence = as.numeric(confidence))

pos.words <- subset(sentiment_nl, sentiment_nl$polarity > 0.5)
neg.words <- subset(sentiment_nl, sentiment_nl$polarity < 0.5)
neu.words <- subset(sentiment_nl, sentiment_nl$polarity == 0.5)

score.sentiment = function(sentences, pos.words, neg.words, .progress='none')
{
  require(plyr)
  require(stringr)
  scores = laply(sentences, function(sentence, pos.words, neg.words) {
    sentence = gsub('[^A-z ]','', sentence)
    sentence = gsub('[[:punct:]]', '', sentence)
    sentence = gsub('[[:cntrl:]]', '', sentence)
    sentence = gsub('\\d+', '', sentence)
    sentence = tolower(sentence)
    word.list = str_split(sentence, '\\s+')
    words = unlist(word.list)
    pos.matches = match(words, pos.words)
    neg.matches = match(words, neg.words)
    pos.matches = !is.na(pos.matches)
    neg.matches = !is.na(neg.matches)
    score = sum(pos.matches) - sum(neg.matches)
    return(score)
  }, pos.words, neg.words, .progress=.progress )
  scores.df = data.frame(score=scores, text=sentences)
  return(scores.df)
}


# score.sentiment = function(sentences, pos.words, neg.words, .progress='none')
#   {
#     require(plyr)
#     require(stringr)
#     scores = laply(sentences, function(sentence, pos.words, neg.words) {
#       sentence = gsub('[^A-z ]','', sentence)
#       sentence = gsub('[[:punct:]]', '', sentence)
#       sentence = gsub('[[:cntrl:]]', '', sentence)
#       sentence = gsub('\\d+', '', sentence)
#       sentence = tolower(sentence)
#       word.list = str_split(sentence, '\\s+')
#       words = unlist(word.list)
#       pos.matches = match(words, pos.words)
#       neg.matches = match(words, neg.words)
#       pos.matches = !is.na(pos.matches)
#       neg.matches = !is.na(neg.matches)
#       score = sum(pos.matches) - sum(neg.matches)
#       return(score)
#     }, pos.words, neg.words, .progress=.progress )
#     scores.df = data.frame(score=scores, text=sentences)
#     return(scores.df)
# }

sample = c(text$responding)
result = score.sentiment(text$sample, pos.words, neg.words)
result
#sample=c("You're awesome and I love you","I hate and hate and hate. So angry. Die!","Impressed and amazed: you are peerless in your achievement of unparalleled mediocrity.")
#result=score.sentiment(text$, pos.words, neg.words)
#result
