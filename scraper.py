import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

title_search = input('Please insert search keyword: ')

<<<<<<< HEAD
def search_funct():
=======


def search_a_book():

    title_search = input('Please insert search keyword: ')
    print('Seeking. Please wait.')
>>>>>>> b13faf7 (Implemented headless mode. Added requirements.txt)

    option = Options()
    option.headless = True
    option.add_argument('window-size=1600x1000')

    driver = webdriver.Firefox(options=option)
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
<<<<<<< HEAD
        print('No matches, please type in correct keyword!')
=======
        print('Please enter a relevant keyword!')
        driver.quit()        
        search_a_book()

    data_frame = pd.DataFrame(data)
    data_frame.columns = ['Title','Author','Price']
    print(data_frame)
    csv = data_frame.to_csv("csv_results_delfi_book_scraper",index_label="No.", na_rep=None)
    #print(delfi_book_scraper)

    driver.quit()

>>>>>>> b13faf7 (Implemented headless mode. Added requirements.txt)
    


    driver.close()

search_funct()
