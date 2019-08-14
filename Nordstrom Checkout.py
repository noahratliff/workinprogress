from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from random import randint
from timeit import default_timer
#from pyvirtualdisplay import Display
from selenium.webdriver.firefox.options import Options







PASTEDPATH = 'C://YOUR//DOUBLE//SLASHED//PATH//INSIDE//THESE//QUOTES'







options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options, 
executable_path=PASTEDPATH)
print("Firefox Headless Browser Invoked")

#display = Display(visible=0, size=(1366, 768))
#display.start()
#driver = webdriver.chromedriver(executable_path = "C:\\Users\\peter\\AppData\\Local\\Programs\\Python\\Python36\\selenium\\webdriver\\chromedriver\\chromedriver.exe")

#driver = webdriver.Firefox(executable_path = "C:\\Users\\peter\\AppData\\Local\\Programs\\Python\\Python36\\selenium\\webdriver\\firefox\\geckodriver.exe")

#driver = webdriver.PhantomJS(executable_path=r"C:\\Users\\peter\\AppData\\Local\\Programs\\Python\\Python36\\selenium\\webdriver\\phantomjs\\bin\\phantomjs.exe")

#url = input('Copy and paste a website link to extract from including https://: ')

url = 'https://shop.nordstrom.com/s/steve-madden-lorax-venetian-loafer-men/4841571?origin=category-personalizedsort&fashioncolor=BURGUNDY%20VELVET'
#url = 'https://shop.nordstrom.com/s/hunter-original-high-gloss-boot-women/4931976?origin=shoppingbag'
#url = 'https://shop.nordstrom.com/s/ugg-neumel-chukka-boot-men/3242739?origin=topnav&cm_sp=Top%20Navigation-_-Men-_-Boots'
driver.get(url)
print('done')
driver.set_window_size(2000, 1500)

time.sleep(.25)
driver.save_screenshot('earlyfail.png')
size = driver.find_element_by_xpath("//div[contains(@class,'drop-down-select title')and contains(.,'Size')]]")
size.click()


selectedSize = input('Please input the choice size: ')
choices = driver.find_element_by_xpath("//div[@class='option' and contains(.,'"+selectedSize+"')]")
i = 1
while i == 1:
    try:
        choices.click()
    except:
        break
        
print(choices)

#COME BACK TO SIZE
driver.save_screenshot('1.png')
addToBag = driver.find_element_by_xpath("//button[contains(.,'Add to Bag')]")
addToBag.click()
driver.save_screenshot('2.png')

time.sleep(.25)
checkout = driver.find_element_by_xpath("//a[contains(.,'Checkout')]")
checkout.click()
driver.save_screenshot('3.png')

ShopBag = driver.find_element_by_xpath("//a[@name='Top Nav / shopping bag']")
ShopBag.click()

checkout = driver.find_element_by_xpath("//a[contains(@id,'proceedCheckoutButton')]")
checkout.click()

email = input('Please enter your email for the nordstrom account: ')
try:
    emailLoc = driver.find_element_by_xpath("//input[@data-ng-model='login.emailAddress']")
except:
    driver.save_screenshot('4.png')
emailLoc.click()
emailLoc.send_keys(email)

passwd = input('Please enter your password for the nordstrom account: ')
passwdLoc = driver.find_element_by_xpath("//input[@name='password']")
passwdLoc.send_keys(passwd, Keys.ENTER)

goToPayment = driver.find_element_by_xpath("//input[contains(@value,'Sign In and Check Out')]")
goToPayment.click()

ccv = input('Please input the CCV for the credit card connected with the account')
ccvLoc = driver.find_element_by_xpath("//input[@id='credit-ccv']")
ccvLoc.send_keys(ccv)

review = driver.find_element_by_xpath("//input[@value='Review Order']")
review.click()

#placeOrder = driver.find_element_by_xpath("//a[contains(.,'Place Order')]")
#placeOrder.click()


#POSSIBLE SHIPPING METHOD HERE




























