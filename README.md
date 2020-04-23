# Eurojackpot

A python script that scrapes the web for Eurojackpot results and exports the data into a .csv file.

## Getting started

The project uses Selenium to gather information from Veikkaus' website. Instructions on how to install Selenium can be found on [Selenium's website](https://selenium-python.readthedocs.io/installation.html). The webdriver that is used in the project is Chrome. As expected, internet connection is required for this to work since we are using Chrome to access Veikkaus' database. 

##Running the program

In order to run this program given everything is set up, just navigate to the folder in the terminal and type:

``python eurojackpot.py``



##Worth mentioning

- The project was made to test the usability of web scraping with Selenium, mostly by personal interest. No user input is checked, no errors are handled etc, which means the program is easily broken if e.g. the dates are put in the wrong format. 

- Errors can occurr if the internet connectíon is too slow. As of now, the program waits one second after refreshing the results before it searches for the results, however, given the internet connection is *really* slow, this can cause multiple rows occurring many times. In worst case scenarios, this can crash the program. This shouldn't be common but is worth mentioning. 

- The Veikkaus website for some reason has a gap in the recorded results around 2016. Errors will occurr if you try to stretch the end date too far, but the data will still be in the .csv file

- The program iterates through the years assuming that there is always 52 weeks in a year. However for some years (e.g. 2015) the year has 53 weeks, which may result in a few weeks data loss. 
