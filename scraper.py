import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

title_search = input('Please insert search keyword: ')

def search_funct():

    driver = webdriver.Firefox()
    driver.get('https://www.delfi.rs/')
    time.sleep(3)
    driver.find_element(By.ID,'autocomplete-input').send_keys(title_search)


    action =ActionChains(driver)
    time.sleep(1)
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


    wait = WebDriverWait(driver,1)
    time.sleep(2)
    wait.until(EC.url_changes('https://www.delfi.rs/'))

    driver.find_element(By.CLASS_NAME,'modal-title')

    soup = BeautifulSoup(driver.page_source, "html.parser")



    search_result = soup.find_all('h1')
    s = [' '.join(s.getText().split()) for s in search_result]
    print(s)
    print('----------')
    print(s[1][0])
    if s[1][0] != 0:
        try:
        
            d = driver
            print(d.page_source)
            soup = BeautifulSoup(driver.page_source,'html.parser')
            find_by_class = soup.find_all(class_="body")
            print(find_by_class)
            e = [[",".join(e.getText().split())] for e in find_by_class if " ".join(e.getText().split()) != "Premium:"]
            print(e)
        except:
            pass
    else:
        print('No matches, please type in correct keyword!')
    


    driver.close()

search_funct()
