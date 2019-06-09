from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options

class backlinks:
	def find(url):
		try:
			domain=url.split("//")[-1].split("/")[0].split("www.")[-1]
			path = os.path.dirname(os.path.abspath(__file__))
			driverpath = path + '\\chromedriver.exe'
			options = Options()
			options.add_argument('--headless')
			options.add_argument('--disable-gpu')
			driver = webdriver.Chrome(driverpath, chrome_options=options)

			driver.get('https://www.semrush.com/analytics/backlinks/overview/{0}:root_domain'.format(domain))

			elements = driver.find_elements_by_xpath("//a[@data-ga-event-name='total backlinks']")
			for element in elements:
				total = element.get_attribute('innerHTML').strip()
				try:
					t = int(total)
					if(t==0):
						driver.quit()
						return [-1,total]
					elif(t<=2):
						driver.quit()
						return [0,total]
					else:
						driver.quit()
						return [1,total]
				except:
					driver.quit()
					return [1,total]
			driver.quit()
			return [-1,0]
		except:
			driver.quit()
			return [-1,0]

