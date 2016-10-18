from selenium import webdriver

browser = webdriver.Chrome('/usr/bin/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title

