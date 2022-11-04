from email import header
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import time

driver = webdriver.Firefox()

driver.get('https://startit.rs/poslovi/')

search_job = driver.find_element(By.ID,"autocomplete")

#Searching for a keyword, locating a dropdown search element and activating the search 
search_job.send_keys('python')

d = driver.find_element(By.CLASS_NAME, "autocomplete-suggestion")

print('d--->',d)
print('-----------')

d.click()

timeout = 10


i=0

while i < 10:
    try:
        time.sleep(3)
        elements = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.TAG_NAME, "article")))
        for e in elements:
            element = e.text
            print (element)
            break
    except StaleElementReferenceException:
        pass
    i += 1

    # finally:
    #     driver.quit()
        
driver.close()












