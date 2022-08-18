
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp

import time
import data

link="https://uttorreon.mx"
driver = webdriver.Chrome(r'D:\\chromedriver\\chromedriver.exe')
driver.get(link)

elem_email = driver.find_element(By.NAME, "email")
elem_pass = driver.find_element(By.NAME, "password")
elem_but = driver.find_element(By.CLASS_NAME,"btn")

elem_email.send_keys("19170074")
elem_pass.send_keys("VANA931127HCLLVN07")
elem_but.click()

elem_name = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[1]/ul/li[2]/div/div[2]/div[1]")
print(elem_name.text)

elem_link=driver.find_element(By.CSS_SELECTOR, "#mCSB_1_container > ul > li.xn-openable > a")
elem_link.click()

elem_academy = driver.find_element(By.CLASS_NAME,"item-text")
print(elem_academy.text)