#OVERALL BUILD RULES
all: data_cleaned downloaded 
data_cleaned: gen/data-preparation/tweet_data_cleaned.RData
downloaded: data/dataset1/tweet_data.csv


#Clean data
gen/data-preparation/tweet_data_cleaned.RData: data/dataset1/tweet_data.csv \
					       src/preparation/clean.R
	Rscript src/preparation/clean.R

#Download data

data/dataset1/tweet_data.csv: src/preparation/download.R
	Rscript src/preparation/download.R
	







