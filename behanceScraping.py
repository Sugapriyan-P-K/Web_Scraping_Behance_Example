from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget

driver = webdriver.Chrome('C:/Users/sugap/Downloads/chromedriver_win32/chromedriver.exe') # driver path
driver.get('https://www.behance.net/')

# need to do
# only 3hrs of work to do
forLogin = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-controls='hamburger-menu']"))).click()
login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Log In')]"))).click()


email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))) # need to view the source of the page
email.clear()
email.send_keys("yourEmail@gmail.com") # your email goes here
continues = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))).click()

password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))) # need to view the source of the page
password.clear()
password.send_keys("password") # Your Password Goes here
continues = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))).click()


not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'not now')]"))).click()

search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Search']"))).click()
search.clear()
keyword = "resume" # to be given
search.send_keys(keyword)
search.send_keys(Keys.ENTER)

driver.execute_script("window.scrollTo(0, 4000);")

images = driver.find_element(By.TAG_NAME,"img")
images = [image.get_attribute("src") for image in images]


path = os.getcwd()
path = os.path.join(path, keyword + "s")
os.mkdir(path)


counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

# till now clicking the search bar is completed
# 16 min for each problem totally 2 and half hour