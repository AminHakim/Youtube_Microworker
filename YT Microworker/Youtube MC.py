import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

#open target website with webdriver
website = 'https://accounts.google.com/v3/signin/identifier?dsh=S-956189849%3A1672190739295496&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&ec=65620&hl=en&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AeAAQh7iyXHUDzcy2jSPZZ5Aw_Mb2e1UplE3mNoFmsbULYR_sahiq4y4IKpfsrZwsrRzhkInklj40g'
path = '\Python310\Chromedriver'
driver = webdriver.Chrome(executable_path=r'C:\Python310\Chromedriver\chromedriver.exe')
driver.get(website)

#wait
time.sleep(2)

#fill Youtube username and password
username = "dakepp05@gmail.com"
password = "xcxcxcxc"

#automated fill in email and password
driver.find_element("xpath", "//input[@class='whsOnd zHQkBf']").send_keys(username)

#wait
time.sleep(2)

#click next
click_next = driver.find_element("xpath", '(//span[@jsname="V67aGc"])[2]').click()

#wait
time.sleep(30)

#automated fill in username and password
#driver.find_element("xpath", '//*[@name="data[User][username]"]').send_keys(username)
#driver.find_element("xpath", '//*[@name="data[User][password]"]').send_keys(password)




