# -*- coding: utf-8 -*-


import pandas as pd
from selenium import webdriver
from time import sleep
global driver
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import messagebox
import concurrent.futures
import time

def Search_In (text, word):
    
    count = 0
    if (word in text):
        if(word == "hiring" or word == "join us"):
            count = count + 2
        else:
            count = count + 1
    return count

def fixer (path):
    return fr'{path}'



def Search_job(acc_username, acc_password, path):

    
    Data = list()
    url = list()
    final_links = list()
    results = list()
    ind_words = list()
    strength = 0
    indicator = list()
    options = Options()
    

    options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")


    linker = fixer(path)
    Linkdin_Url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"

    driver = webdriver.Chrome(r'C:/Users/97252/Desktop/אורעד/pythonApp/chromedriver.exe',options=options)
    driver.get(Linkdin_Url)
    

    driver.find_element_by_id("username").send_keys(acc_username)
    driver.find_element_by_id("password").send_keys(acc_password)
    driver.find_element_by_css_selector(".btn__primary--large").click()



    driver.find_element_by_css_selector(".mh1").click() 
    sleep(1)
    driver.find_element_by_css_selector('.artdeco-dropdown__content--is-open').click()

    
    driver.set_page_load_timeout(200)
    for i in range(20):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)
        
    sleep(1)

    url = driver.find_elements_by_class_name('relative')
    for j in url:
        if(j.get_attribute('data-id') != None and "jobPosting" not in j.get_attribute('data-id') and "urn:li:company" not in j.get_attribute('data-id') and "event" not in j.get_attribute('data-id') and "member" not in j.get_attribute('data-id')):
            fix = j.get_attribute('data-id')
            if("aggregate" in fix):
                final_links.append("https://www.linkedin.com/feed/update/" + fix[18:53])
            else: final_links.append("https://www.linkedin.com/feed/update/"+j.get_attribute('data-id'))   
    sleep(1)
    
    
    ind_words=["משרת סטודנט", "ג׳וניור", "ג'וניור","משרות","junior","ללא ניסיון","hire","hiring","join us","work with","position"]
    
    
    for link in final_links:
        driver.get(link)
        Data = driver.find_elements_by_css_selector(".feed-shared-update-v2__commentary")
        sleep(0.10)
        for string in Data:
            con = string.text
            if ("כולא" not in con and 'a new' not in con):
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    count1 = [executor.submit(Search_In, con, word) for word in ind_words]
                    for total in concurrent.futures.as_completed(count1):
                        strength = strength + total.result()
                sleep(0.05)
                if(strength > 0):
                    results.append(link)
                    indicator.append(strength)
        strength = 0
                    
            
    
    df = pd.DataFrame(list(zip(results, indicator)), columns=['Links','Rate'])
    df = df.sort_values('Rate', ascending=False)
    df.to_csv(linker+'\links_for_jobs2.csv', index = False)
    

    driver.close()
    driver.quit()
    

    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                                                   

