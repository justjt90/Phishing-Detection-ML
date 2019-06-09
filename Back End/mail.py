from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from threading import Thread
import threading

class Mail_google:
	def checkHeader(header):
		try:
			header=header.replace("\n","\\n").replace("\r","\\r").replace("'","\\'")
			path = os.path.dirname(os.path.abspath(__file__))
			driverpath = path + '\\chromedriver.exe'
			options = Options()
			options.add_argument('--headless')
			options.add_argument('--disable-gpu')
			driver = webdriver.Chrome(driverpath,chrome_options=options)
			#header=header.replace("\n","\\n").replace("\r","\\r")
			driver.get("https://toolbox.googleapps.com/apps/messageheader/analyzeheader")
			driver.execute_script("document.getElementsByClassName('mdl-textfield__input')[0].innerHTML='{0}'".format(header))
			#time.sleep(20)

			driver.find_elements_by_xpath("//input[@type='submit']")[0].click()
			try:
				time = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "//span[@style='color:green;']"))).get_attribute("innerHTML").strip()
			except:
				time = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "//span[@style='color:red;']"))).get_attribute("innerHTML").strip()

			elements = driver.find_elements_by_xpath("//tbody")[0].find_elements_by_class_name("mdl-data-table__cell--non-numeric")
			
			CheckMail.value_dict["time"]=time

			for i in range(0,len(elements),2):
				CheckMail.value_dict[elements[i].get_attribute("innerHTML").strip()]=elements[i+1].get_attribute("innerHTML").strip()
			
			if "SPF:" not in CheckMail.value_dict:
				CheckMail.value_dict["SPF:"]="fail"

			if "DKIM:" not in CheckMail.value_dict:
				CheckMail.value_dict["DKIM:"]="fail"

			if "DMARC:" not in CheckMail.value_dict:
				CheckMail.value_dict["DMARC:"]="fail"
			
			driver.quit()

		except Exception as e:
			CheckMail.value_dict["time"]=-1
			CheckMail.value_dict["SPF:"]="fail"
			CheckMail.value_dict["DKIM:"]="fail"
			CheckMail.value_dict["DMARC:"]="fail"
			driver.quit()
			print(e)



class Mail_tracker:
	def checkHeader(header):
		try:
			header=header.replace("\n","\\n").replace("\r","\\r").replace("'","\\'")
			path = os.path.dirname(os.path.abspath(__file__))
			driverpath = path + '\\chromedriver.exe'
			options = Options()
			options.add_argument('--headless')
			options.add_argument('--disable-gpu')
			driver = webdriver.Chrome(driverpath, chrome_options=options)
			
			driver.get("https://www.iptrackeronline.com/email-header-analysis.php")
			driver.execute_script("document.getElementsByTagName('textarea')[0].innerHTML='{0}'".format(header))
			driver.find_elements_by_xpath("//input[@type='submit']")[0].click()
			element = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "//div[@class='three-columns']")))
			texts = driver.find_elements_by_xpath("//input[@size='40']")
			
			CheckMail.value_dict["IP"]=texts[0].get_attribute("value")
			CheckMail.value_dict["Hostname"]=texts[1].get_attribute("value")
			CheckMail.value_dict["Organization"]=texts[2].get_attribute("value")
			CheckMail.value_dict["Country"]=texts[3].get_attribute("value")
			CheckMail.value_dict["City"]=texts[4].get_attribute("value")
			CheckMail.value_dict["Longitude"]=texts[-3].get_attribute("value")
			CheckMail.value_dict["Latitude"]=texts[-4].get_attribute("value")
			driver.quit()


		except Exception as e:
			driver.quit()
			print(e)
			CheckMail.value_dict["IP"]="n/a"
			CheckMail.value_dict["Hostname"]="n/a"
			CheckMail.value_dict["Organization"]="n/a"
			CheckMail.value_dict["Country"]="n/a"
			CheckMail.value_dict["City"]="n/a"
			CheckMail.value_dict["Longitude"]="n/a"
			CheckMail.value_dict["Latitude"]="n/a"
		
		



class CheckMail:
	value_dict={}
	def run(header):
		print(header)
		thread1 = threading.Thread(target = Mail_google.checkHeader,args=([header]))
		thread1.daemon=True
		thread1.start()
		thread2 = threading.Thread(target = Mail_tracker.checkHeader,args=([header]))
		thread2.daemon=True
		thread2.start()
		thread1.join()
		thread2.join()
		return CheckMail.value_dict

