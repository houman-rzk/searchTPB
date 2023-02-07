#!/usr/bin/env python3

import os
import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = webdriver.FirefoxOptions()
options.headless = True

if sys.argv[1] == "-t":
    site=sys.argv[2]
    fileName=sys.argv[3]
    options.set_preference('network.proxy.type', 1)
    options.set_preference('network.proxy.socks', '127.0.0.1')
    options.set_preference('network.proxy.socks_port', 9050)
else:
    site=sys.argv[1]
    fileName=sys.argv[2]

driver = webdriver.Firefox(options = options)
driver.get(site)

pageSource = driver.page_source

file = open(fileName, "w")
file.write(pageSource)
file.close()

driver.quit()
os.remove('geckodriver.log')
