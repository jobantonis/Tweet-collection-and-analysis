# Rutte's influence on taking a shot

__What effect did the Dutch government's press conferences have on the attitude of their citizens towards the corona-vaccin?__

## Motivation
Currently, the COVID-19 pandemic has a large effect on society. The social network Twitter is a way which users can voice their opnions via the use of tweets. To detect the sentiment towards the corona-vaccine in the Netherlands, this scraper will scrape Twitter based on several different keywords, around the time where the Dutch government holds press conferences to Dutch citizens about COVID-19 regulations. The hypothesis of our research is that there might be an influence on the opinion of citizens about the vaccine leading up to, during and after the speeches. This will be anlysed via a sentiment analysis by using the data from the scraper build.

## Method and results

First, introduce and motivate your chosen method, and explain how it contributes to solving the research question/business problem.

Second, summarize your results concisely. Make use of subheaders where appropriate.

## Repository overview

Provide an overview of the directory structure and files.

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
