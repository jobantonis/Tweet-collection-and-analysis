# Rutte's influence on taking a shot

__What effect do the Dutch government's press conferences have on the attitude of their citizens towards the corona-vaccin?__

## Motivation
Since March 2020, the Netherlands has been dealing with the coronacrisis. During the coronacrisis the Dutch prime minister, Mark Rutte, and the deputy prime minister, Hugo de Jonge, communicated by means of press conferences to inform the public on the (updated) regulations. As the coronacrisis took the world by storm not a lot of information was available concerning the semantics of the virus and its implications. This caused a number of problems for the Dutch government. Firstly, regulations were set based on data provided by the rivm which was not always up to date. There have been instances where data was lagging behind and regulations (e.g. closing business and implementing a curfew) were based on this data. Secondly, there was a so called 'arms-race' set in by big pharma to develop a vaccin as soon as possible. Due to the quick development of the covid-vaccines, clinical trials were kept to a bare minimum. These reasons led the Dutch public to skepticism and distrust towards the government, their regulations and the vaccins developed by big pharma.

This research sets out to analyse the sentiment of the Dutch public towards a covid vaccin. It is important to know where the general public stands in order to measure the effectiveness of government communication, and to develop a fitting strategy to communicate the distribution and administering of a vaccin. In this research tweets will be scraped based on a set timeframe surrounding each press conference and predetermined covid related keywords.

## Method and results

Our method consists of 5 steps to analyze sentiment data.

### Step 1 - Data collection

Step 1 consists of the data collection. In this research data will be collected using a bespoke scraper, which will be utilised on different timeframes and targeted on tweets with covid related keywords. The data will consequently be saved as a csv file.

### Step 2 - Data Preparation

Step 2 consists of data cleaning and preparation. In order to correctly 

### Step 3 - Sentiment detection

### Step 4 - Sentiment classification

### Step 5 - Presentation of output

**Second, summarize your results concisely. Make use of subheaders where appropriate.**

## Repository overview

When entering the main branch of the Github repository, several files and folders can immediately be seen. There are two folders, named "data" & "src". Next to this, a .gitignore file, a README.md file (which contains all text seen above and below) and a "client_secrets.json" file can be seen. Entering the "src" folder, one is greeted with two subfolders named "collect" and "preparation". The "collect" folder contains two files named "Collection.py" and "Upload.py". "Collection.py" contains the webscraper used to scrape the Twitter data and writes the collected data to the "data" folder. "Upload.py" contains the code which allows the scraped data to be uploaded to a drive in a CSV file. The "preparation" folder contains 2 files: "download.py" and "clean.R". The file "download.py" contains a code which retrieves data from the drive, and saves it into the "data" folder. The "clean.R" code contains the cleaning script, which cleans up the data retrieved by "download.py". **ADD SENTIMENT ANALYSIS THING HERE**

## Running instructions

To start off, the webscraper (collect.py) will need to be run. For this to work, the chromedriver for Selenium will need to be installed (link to download can be found under the header "Dependencies for scraper". Other than that, the webscraper should be able to run if the chromedriver is installed correctly. Then, upload.py will need to be run. The code will need to be edited in order to upload the data to one's personal drive. Then, using the download.py file, the data can be extracted from the drive (do not forget to edit the code so that it extracts the data from the personal drive given in the upload.py file). Then, one can run clean.R in order to run the cleaning script, which will automatically work (for info on what packages to install, please see the header "Dependencies for cleaning data & sentiment analyis" below). A clean dataset is then downloaded, and any analysis can be done on it. If sentiment analysis is also done, make sure to import the correct file when starting the analysis.

## More resources

The research of Ramírez-Sáyago (2020) inidicated keywords to use in finding relevant tweets about the COVID-19 virus. However in this study the COVID-vaccine will be the main focus, hence indicating that the keywords are the keywords of Ramírez-Sáyago (2020) with "vaccin(e)" behind it. However the keywords "coronavirus" and "corona" were not used in this research. The research of Kruspe et al., (2020) add these keywords to their sentiment analysis, therefore these keywords were added combined with the keyword "vaccine".

## About

This study was conducted as part of the course, Online Data Collections (oDCM) from Tilburg University. The cleaned data by the scraper build will then be used for the course, Data Prep and Workflow Management from Tilburg University. All team members of team 1 were involved in the process of building, developing, optimizing, cleaning and eventually reporting the scraper(data). Team members; Anouk van Gestel, Job Antonis, Marc Lefebvre, Raul Kleinherenbrink and Lieke Adams.

## Dependencies for scraper

Python
Py packages: import "getpass", "time", "selenium.webdriver.common.keys", "selenium.webdriver.chrome",
https://chromedriver.chromium.org/downloads

# Dependencies for cleaning data & sentiment analysis

R
R packages: install.packages("stringr"), ("tidyverse"), ("data.table")

**Gnu make?
Makefiles**

