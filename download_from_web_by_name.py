from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
import os
import urllib
import urllib.request as urllib2
import subprocess

#Opens up web driver and goes to Google Images
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
path =r"C:\chromedriver.exe"
browser = webdriver.Chrome(path,options=options)
browser.maximize_window()
browser.get('https://www.google.com/')
search = browser.find_element_by_name('q')
name = "Namita Thapar"
search.send_keys(name,Keys.ENTER)

# //*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img

# goes to images
elem = browser.find_element_by_link_text('Images')
elem.get_attribute('href')
elem.click()

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = browser.execute_script('return document.body.scrollHeight')
while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = browser.execute_script('return document.body.scrollHeight')
    try:
        browser.find_element(By.XPATH,'//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

#create download folder
try:
    os.mkdir(name)
except FileExistsError:
    pass

for i in range(1, 22):
    #gets images
    elem1 = browser.find_element_by_id('islmp')

    #gets the first image
    sub = elem1.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')
    sub.get_attribute('href')
    sub.click()

    #here i tried to click on the image and open it, so I can download that large version. But it still downloads the smaller size.
    elem1 = browser.find_element_by_id('islmp')
    sub1=elem1.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img')
    
    # //*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img
    
    #download sub1
    src = sub1.get_attribute('src')
    try:
        if src != None:
            src  = str(src)
            print(src)
            urllib2.urlretrieve(src, os.path.join(name,name+'-'+str(i)+'.jpg'))
        else:
            raise TypeError
    except TypeError:
        print('*************************************************')


# To call the rename_files python script by passing the name of person, in case we want to rename all files to same person name with iterator 
os.system('python rename_files.py '+name)
# os.system('python move_to_gallary.py '+name)
