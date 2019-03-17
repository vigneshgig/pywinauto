import pywinauto.keyboard
import pywinauto
import pywinauto.mouse
import win32api
import time
from pywinauto import Desktop, Application
chrome_dir = r'"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
import pymongo
import glob
import os
client = pymongo.MongoClient('localhost',27017)
db = client['ausceo']
new = client['ausceonew']
chrome = Application(backend='uia')
#--incognito
chrome.start(chrome_dir + ' --force-renderer-accessibility  --start-maximized '
             'https://domain.com') 
path  =  'D:\\Download\\'
html_files = [f for f in os.listdir(path) if f.endswith('.html')]
html_files = [d[:4] for d in html_files]   
cursor = db['ausceo'].find(no_cursor_timeout=True)
i = 0
for data in cursor:
    print(data["company_name"])
    if data['company_name'][:4] in html_files:
        pass
    else:
        time.sleep(15)
        pywinauto.mouse.click(button='left',coords=(830,129))
        #830 129 search click
        time.sleep(5)
        company_name = data["company_name"].replace(' ',r"{VK_SPACE}")
        pywinauto.keyboard.SendKeys(company_name)
        time.sleep(7)
        #811 160    click
        pywinauto.mouse.click(button='left',coords=(811,160))
        #1150 50
        time.sleep(11)
        pywinauto.mouse.click(button='left',coords=(1150,50))
    # # time.sleep(5)
    # pywinauto.mouse.click(button='left',coords=(830,129))
    # time.sleep(5)
    # ceo_name = data["ceo_name"].replace('Ms ','').replace('Mr ','').replace(' ',r"{VK_SPACE}")
    # pywinauto.keyboard.SendKeys(ceo_name)
    # time.sleep(10)
    # pywinauto.mouse.click(button='left',coords=(811,160))
    # time.sleep(10)
    # # 513 376
    # pywinauto.mouse.click(button='left',coords=(513,376))
    # time.sleep(10)
    # pywinauto.keyboard.SendKeys(company_name)
    # time.sleep(10)
    # pywinauto.mouse.click(button='left',coords=(509,442))
    # time.sleep(10)
    # print(data['company_name'])
        i=i+1
        print('--------------',i,'----------------------------')
cursor.close()
