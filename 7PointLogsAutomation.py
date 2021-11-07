# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 09:17:58 2021

@author: WRSmi
"""

from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
import time;
import datetime;



#web module
def Automate(Name, Notes):  
    PATH = "C:\Program Files (x86)\chromedriver.exe";
    driver = webdriver.Chrome(PATH);
    current_time = datetime.datetime.now()

    
    #setup website
    driver.get("https://www.7pointops.com/login")
    time.sleep(1);
    
    
    #login
    email = driver.find_element_by_id("userName") ;
    email.send_keys("*********");
    
    Pass = driver.find_element_by_id("password") ;
    Pass.send_keys("******");
    
    Pass.send_keys(Keys.RETURN)
    time.sleep(1);
    
    
    
    #select the daily logs
    driver.find_element_by_css_selector('div[class="panel-footer text-center"]').click();
    time.sleep(.5);
    #selects the opening report
    driver.find_element_by_css_selector('a[href="/dailylogs/entry/1435/0"]').click();
    time.sleep(.3);
    
    
    #Fills in the form
    year = current_time.year;
    mon =current_time.month;
    day = current_time.day;
    
    title = driver.find_element_by_tag_name('textarea')
    title.send_keys(mon,'/',day,'/',year," PRCC Opening Checklist");
    
    employee = driver.find_element_by_id("ques14523");
    employee.send_keys(Name);
    
    hours = driver.find_element_by_css_selector("input.ng-valid-hours")
    hours.send_keys(current_time.hour)
    
    minutes = driver.find_element_by_css_selector("input.ng-valid-minutes")
    hours.send_keys(datetime.datetime.now().minute)
    
    #Checking all the boxes
    driver.find_element_by_id('opt22228').click();
    driver.find_element_by_id('opt22739').click();
    driver.find_element_by_id('opt22252').click();
    checks = driver.find_elements_by_css_selector('input[type="checkbox" i]')
    for x in checks:
        x.click();
    
    #Observations
    observations = driver.find_element_by_id('ques14527');
    observations.send_keys(Notes);

 
Name = input('  Who is working? ');
Notes = input('  Type the closing notes: ');
if (Name != ""):  
    Automate(Name, Notes);
