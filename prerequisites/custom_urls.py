#!/usr/bin/env python
# coding: utf-8

# In[ ]:


dates = ["(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2021-03-11 since:2021-03-05",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2021-02-26 since:2021-02-20",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2021-02-05 since:2021-01-30",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2021-01-23 since:2021-01-17",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2021-01-15 since:2021-01-09",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-12-11 since:2020-12-05",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-11-20 since:2020-11-14",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-11-06 since:2020-10-31",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-10-30 since:2020-10-24",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-10-16 since:2020-10-11",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-10-10 since:2020-09-25",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-09-21 since:2020-09-15",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-09-04 since:2020-08-29",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-08-21 since:2020-08-15",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-08-09 since:2020-08-03",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-07-25 since:2020-07-19",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-06-27 since:2020-06-23",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-06-22 since:2020-06-16",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-06-15 since:2020-06-09",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-06-08 since:2020-06-07",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-06-06 since:2020-05-31",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-05-30 since:2020-05-24",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-05-23 since:2020-05-19",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-05-18 since:2020-05-12",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-05-11 since:2020-05-02",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-05-01 since:2020-04-25",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-04-24 since:2020-04-21",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-04-20 since:2020-04-14",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-04-18 since:2020-04-12",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-04-06 since:2020-04-01",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-03-30 since:2020-03-24",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-03-22 since:2020-03-21",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-03-20 since:2020-03-19",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-03-18 since:2020-03-13",
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-03-12 since:2020-03-10", 
         "(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2020-03-09 since:2020-03-03"]

