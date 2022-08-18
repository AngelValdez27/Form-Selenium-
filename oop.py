from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.select import Select
from preferences import Init
import time

class Uno:
    __url:str
    __path:str
    __time:int
    __delay:int
    __elements:any
    __driver:any
    
    def __init__(self):
        self.__init_data()
    
    def __init_data(self):
        init = Init()
        temp_preferences = init.get_preferences()
        self.__url = temp_preferences.driver.url
        self.__path = temp_preferences.driver.path
        self.__time = temp_preferences.driver.time
        self.__delay = temp_preferences.driver.delay
        self.__elements = temp_preferences.elements
        
    def get_url(self):
        self.__driver=webdriver.Chrome(executable_path=self.__path)
        self.__driver.get(self.__url)

    def set_data(self):
        for data in self.__elements:
                element = WebDriverWait(self.__driver,5).until(exp.element_to_be_clickable
                ((By.XPATH,data.xpath)))
                if data.event == "input":
                    element.send_keys(data.value)
                else:
                    element.click()
                time.sleep(self.__delay)

    def close(self):
        time.sleep(self.__time)
        self.__driver.close()




   