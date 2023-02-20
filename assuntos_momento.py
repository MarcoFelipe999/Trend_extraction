
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

def extracao_twitter():
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    link = 'https://twitter.com/explore/tabs/trending'
    driver.get(url=link)
    print('Tendências de Brasil')
    sleep(5)
    elements = driver.find_elements(By.XPATH, "//div[@data-testid='trend']//span")
    trend_list = [ ]
    for trend_element in elements:
        name = trend_element.text
        trend_list.append(name)

    for trend_att in trend_list:
        print(trend_att)



extracao_twitter()




