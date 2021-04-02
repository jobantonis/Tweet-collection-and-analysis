#OVERALL BUILD RULES
all: data_cleaned analyzed
data_cleaned: gen/data-preparation/output/tweet_data_cleaned.csv
analyzed: gen/analysis/output/sentiment_tweets.csv
 


.PHONY: clean
#INDIVIDUAL RECIPES

#Write results in app form

#Analyze data
gen/analysis/output/sentiment_tweets.csv:
	Python src/analysis/sentiment_analysis.py

#Clean data

gen/data-preparation/output/tweet_data_cleaned.csv: data/dataset1/DataCollection_Twitter.csv 					    
	Rscript src/preparation/clean.R
	

#Clean directory
 





