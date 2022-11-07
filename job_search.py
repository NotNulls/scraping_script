from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import time
import json


driver = webdriver.Firefox()

driver.get('https://startit.rs/poslovi/')

search_job = driver.find_element(By.ID,"autocomplete")

#Searching for a keyword, locating a dropdown search element and activating the search 
search_job.send_keys('python')

d = driver.find_element(By.CLASS_NAME, "autocomplete-suggestion")


d.click()

timeout = 10


i=0
results = []
results_final = []

time.sleep(3)



links = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.TAG_NAME,"article")))


try:
    for l in links:
            results.append(l.text)
except StaleElementReferenceException:
    print (StaleElementReferenceException)
finally:
    for r in results:
        if "PYTHON" in r:
            r = r.replace("\n", "")
            results_final.append(r)
        if "python" in r:
            r = r.replace("\n", "")
            results_final.append(r)
        if "Python" in r:
            r = r.replace("\n", "")
            results_final.append(r)
    
    
    driver.close()

    print('----results_final----')
    print(results_final)


file = open('results.json', mode= 'w+', encoding='utf-8')
print('----> results')
for r in results_final:
    file.write(json.dumps(r)+",\n")










