from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, TimeoutException, WebDriverException, InvalidSessionIdException
import pandas as pd




def search_a_book():

    title_search = input('Please insert search keyword: ')
    print('Seeking. Please wait.')

    option = Options()
    option.headless = True
    option.add_argument('window-size=1600x1000')

    driver = webdriver.Firefox(options=option)
    driver.get('https://www.delfi.rs/')
    driver.maximize_window()
    driver.find_element(By.ID,'autocomplete-input').send_keys(title_search)

    wait = WebDriverWait(driver, 10)

    action =ActionChains(driver)
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    cookie_catch =wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="uslovi"]')))
    cookie_catch.click()

    search_result = driver.find_elements(By.CSS_SELECTOR, '.title-full-width h1')
    s = [' '.join(s.text.split()) for s in search_result]

    list_of_pages = driver.find_elements(By.CLASS_NAME, "page-link")


    data = []

    #Check what the first result digit is. If > 0 means it has result hits. Proceeds further...
    #print (s[0][0])

    no_search_results = s[0][0]

    if int(no_search_results) != 0:
        
        for _ in range(len(list_of_pages[1:-1])):    
            soup = BeautifulSoup(driver.page_source, "html.parser")
            find_by_class = soup.find_all(class_="body")
                
            for i in find_by_class:
                
                title = ["".join(i.text) for i in i.find_all("a",class_="")][0]
                author = ', '.join([(i.text) for i in i.find_all("a",class_="")][1:])
                
                try:
                    price = [i.text.split() for i in i.find_all("span",class_="usteda1")][0][3]
                except (IndexError):
                    price = [i.text.split() for i in i.find_all("span",class_="price")][0][3]
                driver.implicitly_wait(2)
                

                data.append([title,author, price])
            try:
                driver.maximize_window()
                next_page = driver.find_element(By.CSS_SELECTOR,'.pagination .page-item:last-child .page-link')
                next_page.click()
            except (StaleElementReferenceException, ElementClickInterceptedException,TimeoutException, WebDriverException, InvalidSessionIdException):
                pass
        
        print('.............................')
    else:
        print('Please enter a relevant keyword!')
        driver.quit()        
        search_a_book()

    data_frame = pd.DataFrame(data)
    data_frame.columns = ['Title','Author','Price']
    print(data_frame)
    csv = data_frame.to_csv("csv_results_delfi_book_scraper",index_label="No.", na_rep=None)
    #print(delfi_book_scraper)

    driver.quit()

    


