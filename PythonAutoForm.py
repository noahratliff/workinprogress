from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from random import randint
from timeit import default_timer

start = default_timer()

duration = (default_timer() - start)

driver = webdriver.Firefox(executable_path="INSERT PATH TO GECKO DRIVER")

driver.get("http://va.milesplit.com/articles/226702/vote-who-should-take-over-the-milestat-snapchat-for-milestates")
x = 0
time.sleep(35)
while x < 10000:
		elm = driver.find_elements_by_xpath("/html/body/div[2]/main/div[2]/div/article/div[2]/h2/a")
		if elm:
			elm3 = driver.find_element_by_xpath("//input[contains(@id,'PDI_answer45185587')]")
			elm3.click()
		if not elm:
			driver.implicitly_wait(10)
			driver.get("http://va.milesplit.com/articles/226702/vote-who-should-take-over-the-milestat-snapchat-for-milestates")
			driver.implicitly_wait(10)
		elm7 = driver.find_elements_by_xpath("/html/body/div[2]/main/div[2]/div/article/div[2]/h2/a")
		if elm7:
			driver.implicitly_wait(10)
			elm4 = driver.find_element_by_xpath("//span[contains(.,'Vote')]")
			elm4.click()
		if not elm7:
			driver.get("http://va.milesplit.com/articles/226702/vote-who-should-take-over-the-milestat-snapchat-for-milestates")
			driver.implicitly_wait(10)
		elm8 = driver.find_elements_by_xpath("/html/body/div[2]/main/div[2]/div/article/div[2]/h2/a")
		if elm8:
			driver.implicitly_wait(10)
			elm5 = driver.find_element_by_xpath("//a[contains(.,'Return To Poll')]")
			elm5.click()
			x = x+1
			print (x)
		if not elm8:
			driver.get("http://va.milesplit.com/articles/226702/vote-who-should-take-over-the-milestat-snapchat-for-milestates")
			driver.implicitly_wait(10)
		del elm
		del elm7
		del elm8
		


