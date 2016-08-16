import time

from selenium import webdriver


driver = webdriver.PhantomJS()

driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print driver.find_element_by_id('content').text

driver.close()
