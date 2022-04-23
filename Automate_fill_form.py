import time as t
import random
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Function for interacting with web interfaces
def health_travel(temperature):
    RadioButtonClick = web.find_element_by_css_selector("input[type='radio'][value='Value']").click() 
    t.sleep(4)

    textbox = web.find_element_by_css_selector('input[aria-labelledby="QuestionId_re8865ca7664940f58f276cd4834dfcf6 QuestionInfo_re8865ca7664940f58f276cd4834dfcf6"]')
    textbox.send_keys(temperature)

    web.save_screenshot('./screenshot/submitted1.png')
    web.quit()#Important! Remeber to exit to prevent any memory leak.

#Options for web browsing
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--profile-directory=Default")
options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
#options.add_argument("headless")

#Initialising the webdriver
#web = webdriver.Phantomjs()
web = webdriver.Chrome(chrome_options=options)
web.execute_script("Object.defineProperty(navigator, 'web', {get: () => undefined})")
web.delete_all_cookies()
web.get('') #replace with website
timeout = 5

try:
    element_present = EC.presence_of_element_located((By.ID, 'meridies-input'))
    WebDriverWait(web, timeout).until(element_present)

except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")

temp = ['35.6', '36.2', '36.3', '36.5', '36.6', '36.7', '36.8', '36.9']
Rantemp = random.choice(temp) 
health_travel(Rantemp)

sys.exit('Automation Done')