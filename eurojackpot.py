from datetime import date 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv

"""
Eurojackpot data scraping tool
by Benjamin Hartman
All rights reserved. 
"""

def startDrivers(url):
	"""
	Starts the driver, goes to the url and
	returns the driver element
	"""
	driver = webdriver.Chrome()
	driver.get(url)
	return driver

def changeDate(driver, week, year):
	"""
	Changes the date of the Veikkaus search bar into the desired date
	and clicks on refresh so that the right data is shown on the website
	"""
	week = str(week)
	year = str(year)
	weekinput = driver.find_element_by_id('input-week')
	yearinput = driver.find_element_by_id('input-year')
	refreshbutton = driver.find_element_by_id('nav__week-search')

	a = ActionChains(driver)
	a.move_to_element(weekinput)
	a.click()
	a.send_keys(Keys.BACK_SPACE)
	a.send_keys(Keys.BACK_SPACE)
	a.send_keys(week)
	a.perform()

	a.reset_actions()
	a.move_to_element(yearinput)
	a.click()
	a.send_keys(Keys.BACK_SPACE)
	a.send_keys(Keys.BACK_SPACE)
	a.send_keys(Keys.BACK_SPACE)
	a.send_keys(Keys.BACK_SPACE)
	a.send_keys(year)
	a.perform()

	a.reset_actions()
	a.move_to_element(refreshbutton)
	a.click()
	a.perform()

def getNumbers(driver, row):
	"""
	Looks for the unordered list in the HTML that contains the numbers and
	separates the list into a list of primary numbers (first five) and secondary
	numbers (last two). Puts the primaries and the secondaries together, prints the total
	row and returns it. 
	"""
	row = []
	sleep(1)
	ols = driver.find_elements_by_tag_name('ol')
	primary = ols[0]
	secondary = ols[1]
	numbers = primary.find_elements_by_tag_name('li')
	for num in numbers:
		row.append(num.text)
	numbers2 = secondary.find_elements_by_tag_name('li')
	for num in numbers2:
		row.append(num.text)
	print(row)
	return row


def main():
	endyear = input('Enter end year of scraping: ')
	endweek = input('Enter end week of scraping: ')
	row = []


	#URL of Veikkaus website with statistics over numbers
	url = 'https://www.veikkaus.fi/fi/tulokset#!/tarkennettu-haku/eurojackpot'

	today = date.today().isocalendar()
	year = today[0]
	week = today[1]
	print('Today is week',week, 'of', year)
	week -= 1
	print('Starting scraping from week', week)
	
	driver = startDrivers(url)
	with open('results.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['Week', 'Year', 'no1', 'no2', 'no3', 'no4', 'no5', 'extra1', 'extra2'])
		while (year, week) != (int(endyear), int(endweek)):
			print(week, year)
			if week != 1:
				changeDate(driver, week, year)
				row = getNumbers(driver, row)
				row.insert(0, year)
				row.insert(0, week)
				writer.writerow(row)
				week -= 1
			elif week == 1:
				changeDate(driver, week, year)
				row = getNumbers(driver, row)
				row.insert(0, year)
				row.insert(0, week)
				writer.writerow(row)
				year -= 1
				week = 52
		file.close()
	return

main()