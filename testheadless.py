import os
import sys

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

driver = webdriver.Firefox(executable_path = "C:\\Users\\peter\\AppData\\Local\\Programs\\Python\\Python36\\selenium\\webdriver\\firefox\\geckodriver.exe")

# Set the MOZ_HEADLESS environment variable which casues Firefox to start in headless mode.
os.environ['MOZ_HEADLESS'] = '1'

# Select your Firefox binary.
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout)

# Start selenium with the configured binary.
driver = webdriver.Firefox(firefox_binary=binary)

# Visit this webpage.
driver.get("https://intoli.com/blog/running-selenium-with-headless-firefox/")

# Grab the heading element from the response.
heading_element = driver.find_element_by_xpath('//*[@id="heading-breadcrumbs"]')

# Print the title in the terminal.
if heading_element:
    print(heading_element.get_property('textContent').strip())
else:
    print("Heading element not found!")

driver.quit()
