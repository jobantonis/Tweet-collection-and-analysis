# Rutte's influence on taking a shot

__What effect do the Dutch government's press conferences have on the attitude of their citizens towards the covid-vaccin?__

## Motivation
> “Social media are implicated in many of contemporary society's most pressing issues, from influencing public opinion, to organizing social movements, to identifying economic trends.”     (p. 1, Hemphill Hedstrom & Leonard, 2021).

Since March 2020, the Netherlands has been dealing with the coronacrisis. During the coronacrisis the Dutch prime minister, Mark Rutte, and the deputy prime minister, Hugo de Jonge, communicated by means of press conferences to inform the public on the (updated) regulations. As the coronacrisis took the world by storm not a lot of information was available concerning the semantics of the virus and its implications. This caused a number of problems for the Dutch government. 

Firstly, regulations were set based on data provided by the rivm which was not always up to date. There have been instances where data was lagging behind and regulations (e.g. closing businesses and implementing a curfew) were based on this data. Secondly, there was a so called 'arms-race' set in by big pharma to develop a vaccin as soon as possible. Due to the quick development of the covid-vaccines, clinical trials were kept to a bare minimum. These reasons led the Dutch public to skepticism and distrust towards the government, their regulations and the vaccins developed by big pharma. In the Netherlands, it is clear that opinions about Corona, the regulations and the vaccine are divided. Part of the population is protesting and thinks corona is one big hoax, and part of the population 'believes' in the Corona virus being a true pandemic (Erdbrink, 2021). These different opinions lead to different sentiments towards vaccines as well. The social network Twitter is a medium where users can voice their opinions via the use of tweets.

This research sets out to analyse the sentiment of the Dutch public towards a covid vaccin. It is important to know where the general public stands in order to measure the effectiveness of government communication, and to develop a fitting strategy to communicate the distribution and administering of a vaccin. In this research tweets will be scraped based on a set timeframe surrounding each press conference and predetermined covid related keywords. Tweets are preprocessed before computing sentiment scores. Hash symbol (#), mention symbol (@), URLs, extra spaces, and paragraph breaks are cleaned. Punctuations and numbers are included. Advance-level preprocessing, such as (i) correction of incorrectly spelled spelt words, (ii) conversion of abbreviations to their original forms, are bypassed to avoid analysis bottleneck.

## Method and results

Our method consists of 5 steps to analyze sentiment data.

#### Step 1 - Data collection

The first step consists of the data collection. In this research data will be collected from Twitter using a bespoke scraper, which will be utilised on different timeframes and targeted on tweets with covid related keywords. The data will consequently be saved as a csv file.
The script preprocessed the data by:


#### Step 2 - Data Preparation

The second step consists of data preperation and cleaning. A script has been provided that cleans the csv files extracted from the scraper. After the cleaner has been utilised, data will be ready for analysis.
The script cleaned/labeled the data by:
- Removing NA and non-numerical depictions of numbers (1.9k to 1900)
- Removing all white space and non-valuable text elements
- Removing Extended, Commercial /trade symbols, and mathematical ASCII symbols
- Remove duplicate tweets (literal same content)
- Adjusting timestamp
- Encoding usernames using numerical values

In the end, the data cleaning and normalization process leaves us with 67.6 % of original data of total tweets.

#### Step 3 - Sentiment detection

In the third step, each tweet's text field is examined for subjectivity. Tweet text with subjective expressions are retained and objective expressions are discarded. 

#### Step 4 - Sentiment classification

The fourth step classifies each subjective string into groups: positive, negative and neutral based upon their polarity scores. The existing sentiment lexicon used was useful in conjunction with the textual context of the tweets.

#### Step 5 - Presentation of output

After sentiment classification, the goal of fifth step is to structure the data in a visual and informative manner. The text results are displayed in an array of different graphs.

The outcome of the sentiment analysis is devided into three different plots that indicate the overall fluctuations in positive, negative and neutral tweet sentiments during the press conference. The amount of tweets increased drastically around 19 november 2020. During this time the Dutch government [announced](https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/kamerstukken/2020/11/16/kamerbrief-over-aankoop-covid-19-vaccins/kamerbrief-over-aankoop-covid-19-vaccins.pdf) during that time, that they were going to buy the corona-vaccins for the Dutch citizens. In addition to that, in hindsight this was all leading up to the [press conference](https://www.rijksoverheid.nl/actueel/nieuws/2020/12/14/lockdown-om-contacten-tot-een-minimum-te-beperken) at 15-12-2020 were eventually a harsh lock-down in the Netherlands would be announced. Our experiments on twitter sentiment analysis show that there were more positive tweets about the corona-vaccin in total compared to negative and neutral. Like any other method, our proposed method also faces the constraints of real opinions compared to the social media opinions scenario.
![Image of Keywords in Tweets](https://github.com/jobantonis/Tweet-collection-and-analysis/blob/main/images/Image_Number_Tweets_Keywords.PNG)

We discover the sentiment of the tweets correlating negatively with an press conference and observe a change in sentiment toward the coronavaccin from either negative or positive to neutral longer into the pandemic. The results shown large portion of the records were objective which was approximately between 60 and 45 percent. From this study we can say that people's reactions vary day to day from posting their feelings on social media specifically Twitter. Unfortunately, the pandemic is still far from over and the dynamics of this analysis may very well change in the future.
![Image of Sentimentanalysis](https://github.com/jobantonis/Tweet-collection-and-analysis/blob/main/images/Image_Vaccine_Sentiment_Status.PNG | width=100)

## Repository overview

Overview of the of the directory structure and files:

├── README.md
├── App
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── output
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─── RUN RMD FILE TO RENDER APP.txt
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─── Polarity_over_time_app.Rmd   
├── makefile                                                                      
├──.gitignore                                       
├── data                                             
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── dataset1                                     
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─── DataCollection_Twitter.csv                  
├── gen                                              
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── analysis                                     
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ output                                        
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── sentiment_analysis_visualizations.ipynb
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─── data-preparation                            
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ output                                   
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── .gitattributes
├── prerequistites                                                                                                        
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─── custom_urls.py
├── src                                              
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── collect                                      
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── client_secret_needed                    
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Collect.py                             
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Upload.py                             
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── .DS_Store                                  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── preparation                                  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── clean.R                                                      
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── analysis                                  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── sentiment_analysis.py
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── .DS_Store                                    
└── images                                                                                               
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Image_Number_Tweets_Keywords.PNG                                                 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Image_Vaccine_Sentiment_Status.PNG                                               

When entering the main branch of the Github repository, several files and folders can immediately be seen. There are two folders, named
"data" & "src". Next to this, a ```
.gitignore
         ```, a ```
README.md
         ``` (which contains all text seen above and below) and a ```
client_secrets.json
         ``` file can be seen. Entering the "src" folder, one is greeted with two subfolders named "collect" and "preparation". The "collect" folder contains two files named ```
Collection.py
         ``` .  ```
Collection.py
         ``` contains the webscraper used to scrape the Twitter data and writes the collected data to the "data" folder. The "preparation" folder contains: ```
clean.R
         ```. The ```
clean.R
         ``` code contains the cleaning script, which cleans up the data retrieved by ```
data/dataset1/DataCollection_Twitter.csv 
         ``` . The "analysis" folder contains 1 file: ```
sentiment_analysis.py
         ``` which allows the cleaned data to be analyzed for sentiment within the tweets and the levels of polarity.

## Running instructions

Collect | Save dataset |  Clean | Analysis 
------------ | ------------- | ------------- |------------- 
collection.py | upload.py | clean.R | Sentiment.py
Python & Selenium | Rstudio | Rstudio | Python

To start off, the webscraper (```
Collection.py
         ```) will need to be run. For this to work, the chromedriver for Selenium will need to be [installed](https://chromedriver.chromium.org/downloads). Other than that, no further input is required and the webscraper should be able to run if the chromedriver is installed correctly. The dataset is uploaded the data to one's github. Then, the data can be extracted from the github ```
data/dataset1/DataCollection_Twitter.csv 
         ``` . Then, one can run ```
clean.R
         ``` in order to run the cleaning script, which will automatically work (for info on what packages to install, please see the header "Dependencies for cleaning data & sentiment analyis" below). A clean dataset is then downloaded, and any analysis can be done on it. If sentiment analysis is also done, make sure to import the correct file when starting the analysis. The sentiment analysis can be ran using ```
sentiment_analysis.py
         ``` file.

## More resources
Academic background information about the dataset creation: The dataset contains keywords indicated by the research of Ramírez-Sáyago (2020) to find relevant tweets about the COVID-19 virus. However the COVID-vaccine is the main focus in this dataset, therefore the keywords of Ramírez-Sáyago (2020) are combined with "vaccin(e)" behind it. However the keywords "coronavirus" and "corona" were not used in this research. The research of Kruspe et al., (2020) did use these keywords to their sentiment analysis, therefore these keywords were also added combined with the keyword "vaccine" in the composition of the dataset.

Some part of the Dutch population is protesting and thinks corona is one big hoax, this sentiment analysis does not touch upon it's relationship between the believes of Twitter uses in this hoax or not. The latter is described in [this](https://www.nytimes.com/2020/10/29/world/europe/covid-19-netherlands.html) actricle in the New York times.

## About

This study was conducted as part of the course, [Online Data Collections (oDCM)](https://odcm.hannesdatta.com/) from Tilburg University. The cleaned data by the scraper built will then be used for the course, [Data Prep and Workflow Management (dPrep)](https://dprep.hannesdatta.com/) from Tilburg University. All team members of team 1 were involved in the process of building, developing, optimizing, cleaning and finally documenting and analyzing the data. Team members: Anouk van Gestel, Job Antonis, Marc Lefebvre, Raul Kleinherenbrink and Lieke Adams.

## Dependencies for scraper

Python
Py packages: import ```
getpass
         ```, ```
time
         ```, ```
selenium.webdriver.common.keys
         ```, ```
selenium.webdriver.chrome
         ```,
Use this [link](https://chromedriver.chromium.org/downloads) to download the Selenium Chrome webdriver. Make sure to select the correct version for Chrome.

## Dependencies for cleaning data & sentiment analysis

R
R packages: install.packages```
stringr
         ```, ```
tidyverse
         ```, ```
data.table
         ```.


Python
Py packages: import ```
matplotlib.pyplot
         ```, ```
pandas
         ```, ```
numpy
         ```, ```
datetime
         ``` , ```
csv
         ```, ```
matplotlib.dates
         ```.

