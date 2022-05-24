import time, json, random
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from random import randint
import re
from sys import exit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import pathlib
from pathlib import Path
import os
from sys import platform
from luu_function import driver, local, data, Logging, ValidateFailResultAndSystem,TestCase_LogResult,Yellow,Green,Red,WaitElementLoaded,Wait10s_ClickElement,Wait10s_InputElement



    

def board_create_folder(domain_name):
   

    Logging("------------------------------------------------------B. Menu Board------------------------------------------------------")
    driver.get(domain_name + "/board/list/comp_0/")
    Wait10s_ClickElement(data["board"]["list_icon_hide_company_board"])
    Logging("2. Hide list Company Board successfully")

    time.sleep(1)
    Logging("-------------- Write Folder My Board --------------")
    Wait10s_ClickElement(data["board"]["setting_board"])
    Logging("3. Click settings successfully")
    time.sleep(1)
    
    Wait10s_ClickElement(data["board"]["click_my_board"])
    Logging("4. Click My Board successfully")
    #Wait10s_InputElement(data["board"]["input_folder_name_board"],data["board"]["folder_name_board_setting"])
    folder_name_board = driver.find_element_by_xpath(data["board"]["input_folder_name_board"])
    folder_name_board.send_keys(data["board"]["folder_name_board_setting"])
    content_subject=folder_name_board.get_attribute("value")
    if(content_subject==data["board"]["folder_name_board_setting"]):
        Logging("5. Add name folder =>pass" + " :  " + data["board"]["folder_name_board_setting"])
    else:
        Logging("5. Add name folder =>fail")
        ValidateFailResultAndSystem("<div>[Board]1. Input folder name </div>")
    input_description_board = driver.find_element_by_xpath(data["board"]["textbox_description_board"])
    input_description_board.send_keys(data["board"]["description_board"])
    time.sleep(1)
    Logging("5. Input Description successfully")
    Wait10s_ClickElement(data["board"]["check_use_comment"])
    Logging("6. Check Use comment successfully")
    Wait10s_ClickElement(data["board"]["turnon_share"])
    Wait10s_ClickElement(data["board"]["click_org_board"])
    time.sleep(1)
    Wait10s_ClickElement(data["board"]["select_user_01"])
    Wait10s_ClickElement(data["board"]["icon_add_user"])
    time.sleep(1)

    Wait10s_ClickElement(data["board"]["save_add_user"])
    Logging("7. Add user successfully")

    
    time.sleep(1)
    select_permisssion = Select(driver.find_element_by_xpath(data["board"]["select_permisssion_board"])) 
    select_permisssion.select_by_visible_text("Read/Write/Modify/Delete")
    Logging("8. Select  Permissison successfully")
    time.sleep(1)
    Wait10s_ClickElement(data["board"]["save_button_folder_board"])
    Logging("9. Save Folder Board successfully")
    time.sleep(1)
    Wait10s_ClickElement(data["board"]["click_button_close_board"])
    Logging("10. Click button Close successfully")
    time.sleep(1)
    
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["board"]["show_folder_board"])))
    element = driver.find_element_by_xpath(data["board"]["show_folder_board"])
    element.location_once_scrolled_into_view
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["board"]["show_folder_board"])))
    forder_board_create = driver.find_element_by_xpath(data["board"]["show_folder_board"])
    if forder_board_create.is_displayed():
        Logging(Green("=> Show Folder Board successfully => PASS"))
        TestCase_LogResult(**data["testcase_result"]["board"]["write_folder_myboard"]["pass"])
        
    else:
        Logging(Red("=> Show Folder Board Fail => FAIL"))
        ValidateFailResultAndSystem("<div>[Board]2. Write folder name </div>")
        TestCase_LogResult(**data["testcase_result"]["board"]["write_folder_myboard"]["fail"])
       
    time.sleep(1)


def board_create_subfolder(domain_name):
    Logging("-------------- Write SubFolder My Board ---------------")
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(2)    
    Wait10s_ClickElement(data["board"]["icon_list_parent_board"])
    time.sleep(1)
    Wait10s_ClickElement(data["board"]["parent_folder_board"])
    time.sleep(1)
    Logging("11. Select Parent Folder successfully")

    Wait10s_InputElement(data["board"]["input_sub_folder_board"],data["board"]["subfolder_name_board_setting"])
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["board"]["input_sub_folder_board"])))
    #folder_name_board = driver.find_element_by_xpath(data["board"]["input_sub_folder_board"])
    #folder_name_board.send_keys(data["board"]["subfolder_name_board_setting"])
    Logging("11. Input Subfolder successfully" + " :  " + data["board"]["subfolder_name_board_setting"])


    Wait10s_ClickElement(data["board"]["save_button_folder_board"])
    Logging("12. Save Folder Board successfully")
    Wait10s_ClickElement(data["board"]["click_button_close_board"])
    Logging("13. Click button Close successfully")
    time.sleep(2)    
    driver.execute_script("window.scrollTo(100, 0)")

    Wait10s_ClickElement(data["board"]["parent_folder_in_folder_list"])
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["board"]["select_sub_folder"])))
    select_sub_folder_board = driver.find_element_by_xpath(data["board"]["select_sub_folder"])
    if select_sub_folder_board.is_displayed():
        Logging(Green("=> Show Folder Board successfully => PASS"))
        TestCase_LogResult(**data["testcase_result"]["board"]["write_sub_folder_myboard"]["pass"])
    else:
        Logging(Red("=> Show Folder Board Fail => FAIL"))
        ValidateFailResultAndSystem("<div>[Board]3. Write SubFolder My Board </div>")
        TestCase_LogResult(**data["testcase_result"]["board"]["write_sub_folder_myboard"]["fail"])
    Logging("-------------- Delete SubFolder My Board ----------------")
    Wait10s_ClickElement(data["board"]["select_sub_folder"])
    Logging("15. Select subfolder successfully")
    time.sleep(2)
    Wait10s_ClickElement(data["board"]["select_sub_folder_delete"])
    Logging("16. Select icon delete subfolder successfully")
    Wait10s_ClickElement(data["board"]["click_ok_button"])
    Wait10s_ClickElement(data["board"]["click_button_close_board"])
    Logging("17. Delete Sub Folder successfully")
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(1) 
    Wait10s_ClickElement(data["board"]["select_folder_parent"])
    time.sleep(1)
    if 'Sub 01' in driver.page_source :
        Logging(Red("=> .Delete SubFolder My Board =>------- FAIL"))
        ValidateFailResultAndSystem("<div>[Board]4. Delete SubFolder My Board </div>")
        TestCase_LogResult(**data["testcase_result"]["board"]["delete_sub_folder_myboard"]["fail"])
    else:
        Logging(Green("=> .Delete SubFolder My Board =>------- PASS"))
        TestCase_LogResult(**data["testcase_result"]["board"]["delete_sub_folder_myboard"]["pass"])

def board_edit_folder(domain_name):    
    Logging("--------------- Edit Folder My Board ----------------")
    Wait10s_ClickElement(data["board"]["folder_board_edit"])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["board"]["select_folder_type_anonymous"])))
    select_use_anonymous = driver.find_element_by_xpath(data["board"]["folder_board_edit"])
    select_use_anonymous.click()
    Wait10s_ClickElement(data["board"]["btn_save_folder"])
    Logging("19. Save Folder Board successfully")
    time.sleep(1)
    Wait10s_ClickElement(data["board"]["click_button_close_board"])
    Logging("20. Edit Folder Board  successfully")
    time.sleep(2)
    driver.execute_script("window.scrollTo(100, 0)")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["board"]["show_folder_board"])))
    forder_board_create = driver.find_element_by_xpath(data["board"]["show_folder_board"])
    if forder_board_create.is_displayed():
        Logging(Green("=> Edit Folder My Board => PASS"))
        TestCase_LogResult(**data["testcase_result"]["board"]["edit_folder_myboard"]["pass"])
    else:
        Logging(Red("=> Edit Folder My Board => FAIL"))
        ValidateFailResultAndSystem("<div>[Board]5. Edit Folder My Board </div>")
        TestCase_LogResult(**data["testcase_result"]["board"]["edit_folder_myboard"]["fail"])
    time.sleep(1)
def board_delete_folder(domain_name):
    time.sleep(1)
    Wait10s_ClickElement(data["board"]["setting_board"])
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(2)
    Wait10s_ClickElement(data["board"]["select_folder_parent"])
    time.sleep(3)
    driver.execute_script("window.scrollTo(100, 0)")
    Wait10s_ClickElement(data["board"]["icon_delete_folder_pa"])
    time.sleep(1)
    Wait10s_ClickElement(data["board"]["click_ok_button"])
    time.sleep(1)
    Wait10s_ClickElement(data["board"]["click_button_close_board"])
    Logging("21. Delete Folder Board  successfully")
    #end_time = time.time()
    #loading_time = end_time - start_time
    #Logging(end_time - start_time)
    time.sleep(2)
    
    access_menu_home = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["screen_home_gw"])))
    access_menu_home.click()
    time.sleep(3)
time.sleep(1)

def access_menu_board(domain_name):
    try:
        board_create_folder(domain_name)
        Logging("Create folder successfully")
    except WebDriverException:
        Logging("fail to create folder")

    time.sleep(1)

    try:
        board_create_subfolder(domain_name)
        Logging("Create Subfolder successfully")
    except WebDriverException:
        Logging("Create Subfolder Fail")

    time.sleep(1)


    try:
        board_edit_folder(domain_name)
        Logging("Edit folder successfully")
    except WebDriverException:
        Logging("Edit folder Fail")

    time.sleep(1)

    try:
        board_delete_folder(domain_name)
        Logging("Delete folder successfully")
    except WebDriverException:
        Logging("Delete Folder Fail")

    time.sleep(1)












def is_Displayed(driver,xpath):
    try:
        driver.find_elements_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
    
def so(total):
    num = re.sub(r'\D', "", total)
    return int(num)



'''

with open(local+'\\'+'luu_board.txt','w') as board:
    domain="http://qa.hanbiro.net"
    access_menu_board(domain,board)



result=open(local+'\\result.txt','r')
file_result=result.read()
Logging(file_result)

'''






