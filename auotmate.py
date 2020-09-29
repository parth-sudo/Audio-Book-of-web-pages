from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Yadnesh/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver.get('https://en.wikipedia.org/wiki/Lionel_Messi')

searcher = driver.find_element_by_tag_name('p')
searcher.click()