from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://vnexpress.net/')
with open("test.html", "w", encoding='utf-8') as fOut:
    fOut.write(driver.page_source)
driver.close()
