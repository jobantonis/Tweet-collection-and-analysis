# Rutte's influence on taking a shot

__What effect do the Dutch government's press conferences have on the attitude of their citizens towards the corona-vaccin?__

## Motivation
Since March 2020, the Netherlands has been dealing with the coronacrisis. During the coronacrisis the Dutch prime minister, Mark Rutte, and the deputy prime minister, Hugo de Jonge, communicated by means of press conferences to inform the public on the (updated) regulations. As the coronacrisis took the world by storm not a lot of information was available concerning the semantics of the virus and its implications. This caused a number of problems for the Dutch government. Firstly, regulations were set based on data provided by the rivm which was not always up to date. There have been instances where data was lagging behind and regulations (e.g. closing business and implementing a curfew) were based on this data. Secondly, there was a so called 'arms-race' set in by big pharma to develop a vaccin as soon as possible. Due to the quick development of the covid-vaccines, clinical trials were kept to a bare minimum. These reasons led the Dutch public to skepticism and distrust towards the government, their regulations and the vaccins developed by big pharma.

This research sets out to analyse the sentiment of the Dutch public towards a covid vaccin. It is important to know where the general public stands in order to measure the effectiveness of government communication, and to develop a fitting strategy to communicate the distribution and administering of a vaccin. In this research tweets will be scraped based on a set timeframe surrounding each press conference and predetermined covid related keywords.

## Method and results

First, introduce and motivate your chosen method, and explain how it contributes to solving the research question/business problem.

In order to answer the main research motive, Twitter data has to be scraped. This was done through the use of a webscraper, built up in Python. After the collection process, a data cleaning script was written using R, which is used to clean the Twitter data. This data is cleaned in several ways, including the filtering of unreadable symbols and creating anonymity by replacing Twitter usernames by numbers. Afterwards, the cleaned data was exported to a CSV file, which was then used to conduct a sentiment analysis in R. This sentiment analysis is important for answering the research question, since it allows for an understanding of what the overall attitude towards the COVID-19 vaccine on Dutch Twitter is.

Second, summarize your results concisely. Make use of subheaders where appropriate.

## Repository overview

When entering the main branch of the Github repository, several files and folders can immediately be seen. There are two folders, named "data" & "src". Next to this, a .gitignore file and a README.md file (which contains all text seen above and below) can be seen. Entering the "src" folder, one is greeted with two subfolders named "collect" and "preparation". The "collect" folder contains two files named "Collection.py" and "Upload.py". "Collection.py" contains the webscraper used to scrape the Twitter data and writes the collected data to the "data" folder. "Upload.py" contains the code which allows the scraped data to be uploaded to a drive in a CSV file. The "preparation" folder contains 2 files: "download.py" and "clean.R". The file "download.py" contains a code which retrieves data from the drive, and saves it into the "data" folder. The "clean.R" code contains the cleaning script, which cleans up the data retrieved by "download.py". *ADD SENTIMENT ANALYSIS THING HERE*

## Running instructions

Explain to potential users how to run/replicate your workflow. Touch upon, if necessary, the required input data, which (secret) credentials are required (and how to obtain them), which software tools are needed to run the workflow (including links to the installation instructions), and how to run the workflow. Make use of subheaders where appropriate.

## More resources

The research of Ramírez-Sáyago (2020) inidicated keywords to use in finding relevant tweets about the COVID-19 virus. However in this study the COVID-vaccine will be the main focus, hence indicating that the keywords are the keywords of Ramírez-Sáyago (2020) with "vaccin(e)" behind it. However the keywords "coronavirus" and "corona" were not used in this research. The research of Kruspe et al., (2020) add these keywords to their sentiment analysis, therefore these keywords were added combined with the keyword "vaccine".

## About

This study was conducted as part of the course, Online Data Collections (oDCM) from Tilburg University. The cleaned data by the scraper build will then be used for the course, Data Prep and Workflow Management from Tilburg University. All team members of team 1 were involved in the process of building, developing, optimizing, cleaning and eventually reporting the scraper(data). Team members; Anouk van Gestel, Job Antonis, Marc Lefebvre, Raul Kleinherenbrink and Lieke Adams.

## Dependencies for scraper

Python
Py packages: import "getpass", "time", "selenium.webdriver.common.keys", "selenium.webdriver.chrome",  

# Dependencies for cleaning data & sentiment analysis

R
R packages: install.packages("?")
Gnu make?
Makefiles
Detailed installation instructions from: tilburgsciencehub.com and our lecturer Hannes Datta
