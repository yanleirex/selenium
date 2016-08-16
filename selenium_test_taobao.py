import time
import requests
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('https://s.taobao.com/search?q=surface&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.7724922.8452-taobao-item.1&ie=utf8&initiative_id=tbindexz_20160228')
time.sleep(7)
print driver.page_source
driver.get_screenshot_as_file('2.jpg')
driver.close()
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "============================================================================================================================"
resp = requests.get('https://s.taobao.com/search?q=surface&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.7724922.8452-taobao-item.1&ie=utf8&initiative_id=tbindexz_20160228')
print resp.text
