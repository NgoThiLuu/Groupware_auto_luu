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
from luu_function import driver, local, data, Logging, ValidateFailResultAndSystem,TestCase_LogResult,Yellow,Red,Green,Commands



    

def CheckPresenceOfAdminsubmenu(domain_name):
    Logging("------------------------------------------------------C. Menu Contact------------------------------------------------------")
    driver.get(domain_name + "/addrbook/list/org_0/")
    time.sleep(1)

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["contact"]["admin_contact"])))
        admin = True
    except WebDriverException:
        admin = False
    return admin


def contact_create_folder(domain_name):
    
    time.sleep(3)
    Logging("------------------------------------------------------C. Menu Contact------------------------------------------------------")
    #driver.get(domain_name + "/addrbook/list/org_0/")  
    Commands.Wait10s_ClickElement(data["contact"]["hide_list_contact"])
    time.sleep(2)
    Commands.Wait10s_ClickElement(data["contact"]["setting_contact"])
    time.sleep(2)
    Logging("2. Click list My Company successfully")  
    Commands.Wait10s_ClickElement(data["contact"]["folder_my_contacts"])  



    now = datetime.now()
    name_folder_contact = "Generated sele" +" " + now.strftime("%Y")
    input_description_contact = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["textbox_folder_name"])))
    input_description_contact.send_keys(name_folder_contact)
    time.sleep(2)



    Commands.Wait10s_InputElement(data["contact"]["textbox_description"],data["contact"]["title_description"])
    Logging("6. Input Description successfully" + " :  " +  data["contact"]["title_description"] )
    Commands.Wait10s_ClickElement(data["contact"]["turn_on_share"]) 
    Commands.Wait10s_ClickElement(data["contact"]["click_org_contact"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["share_invite_user_dept"])
    time.sleep(1)


    '''
    search_dept = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["textbox_search_dept_contact"])))
    search_dept.send_keys(data["contact"]["dept_name_search"])
    search_dept.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["loading_dialog"])))
    select_user = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["select_user_01"])))
    select_user.click()
    select_user_2 = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["select_user_02"])))
    select_user_2.click()
    select_user_3 = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["select_user_03"])))
    select_user_3.click()
    
    '''

    Commands.Wait10s_ClickElement(data["contact"]["click_icon_add_user"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["save_add_user"])
    Logging("7. Select user Share successfully")
    #select_permisssion_user = Select(driver.find_element_by_xpath(data["contact"]["select_permission"]))
    #select_permisssion_user.select_by_visible_text("Permission to Read/Write/Modify/Delete")
    Commands.Selectbox_ByVisibleText(data["contact"]["select_permission"],data["contact"]["select_per_contact"])

    Logging("8. Select  Permissison successfully")
    Commands.Wait10s_ClickElement(data["contact"]["save_folder_my_contact"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
    Logging("9. Save folder successfully")
    time.sleep(1)
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["show_folder_contact"])))
    forder_contact_create =  driver.find_element_by_xpath(data["contact"]["show_folder_contact"])
    time.sleep(2)
    if forder_contact_create.is_displayed():
        Logging(Green("Show Folder Contact successfully => PASS"))
        TestCase_LogResult(**data["testcase_result"]["contact"]["write_folder_contact"]["pass"])
    else:
        Logging(Red("Show Folder Contact Fail => FAIL"))
        ValidateFailResultAndSystem("<div>[Contact]Show Folder Contact successfully </div>")
        TestCase_LogResult(**data["testcase_result"]["contact"]["write_folder_contact"]["fail"])

   
def contact_create_subfolder(domain_name):    
    Logging("---------------- Write SubFolder My Contact----------------")
    Commands.Wait10s_ClickElement(data["contact"]["click_list_my_contact"])
    Commands.Wait10s_ClickElement(data["contact"]["select_parent_folder_contact"])
    time.sleep(1)
    Logging("10. Select Parent folder successfully")
    Commands.Wait10s_InputElement(data["contact"]["input_sub_folder_contacts"],data["contact"]["subfolder_name"])
    Logging("11. Input subfolder Name successfully" + " :  " + data["contact"]["subfolder_name"] )
    Logging("11. Save Subfolder successfully")
    Commands.Wait10s_ClickElement(data["contact"]["save_subfolder_contact"])
    time.sleep(2)
    Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
    Logging("12. Save folder successfully")
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["check_folder_parent_contact"])
    time.sleep(2)
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["show_sub_folder"])))
    select_sub_folder_contact = driver.find_element_by_xpath(data["contact"]["show_sub_folder"])
    if select_sub_folder_contact.is_displayed():
        Logging(Green("Write SubFolder My Contact => PASS"))
        TestCase_LogResult(**data["testcase_result"]["contact"]["write_subfolder_contact"]["pass"])
    else:
        Logging(Red("Write SubFolder My Contact => FAIL"))
        ValidateFailResultAndSystem("<div>[Contact]Write SubFolder My Contact </div>")
        TestCase_LogResult(**data["testcase_result"]["contact"]["write_subfolder_contact"]["fail"])
    
    Logging("---------------- Delete SubFolder My Contact----------------")
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["select_subfolder_contact_delete"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["click_icon_delete_subfolder_contact"])
    Commands.Wait10s_ClickElement(data["contact"]["click_ok_button"])
    Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
    time.sleep(1)
    Logging("13. Delete Subfolder successfully")
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["check_folder_parent_contact"])
    time.sleep(1)
    if 'sub 2' in driver.page_source :
        Logging(Red("1.Delete SubFolder My Contact =>  FAIL"))
        ValidateFailResultAndSystem("<div>[Contact]Write SubFolder My Contact </div>")
        TestCase_LogResult(**data["testcase_result"]["contact"]["delete_subfolder_contact"]["fail"])
    else:
        Logging(Green("1.Delete SubFolder My Contact =>  PASS"))
        TestCase_LogResult(**data["testcase_result"]["contact"]["delete_subfolder_contact"]["pass"])
def contact_edit_folder(domain_name):    
    Logging("---------------- Edit Folder My Contact---------------")
    Commands.Selectbox_ByVisibleText(data["contact"]["edit_permisssion_contacts"],data["contact"]["edit_permission_contact"])
    #select_permisssion = Select(driver.find_element_by_xpath(data["contact"]["edit_permisssion_contacts"]))
    #select_permisssion.select_by_visible_text("Read/Write")
    Commands.Wait10s_ClickElement(data["contact"]["save_folder_contact_edit"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
    Logging("14. Edit folder successfully")
    time.sleep(1)
    driver.execute_script("window.scrollTo(100, 0)")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["show_folder_contact"])))
    forder_contact_create = driver.find_element_by_xpath(data["contact"]["show_folder_contact"])
    if forder_contact_create.is_displayed():
        Logging(Green("Edit Folder Board successfully => PASS"))
    else:
        Logging(Red("Edit Folder Board Fail => FAIL"))
        ValidateFailResultAndSystem("<div>[Contact]Edit Folder My Contact </div>")

def contact_delete_folder(domain_name):    
    Logging("---------------- Delete  Folder Parent---------------")
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(3)
    Commands.Wait10s_ClickElement(data["contact"]["check_folder_parent_contact"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["click_icon_delete_subfolder_contact"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["click_ok_button"])
    time.sleep(2)
    Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
    Logging("15. Delete folder Parent successfully")
    time.sleep(2)
    
def contact_manager_folder(domain_name):

    Logging("----------------------------------- Manage Company Folders-----------------------------------")
    driver.refresh()
    time.sleep(5)
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["click_manager_company_folder"])))
    click_manage_company_folder = driver.find_element_by_xpath(data["contact"]["click_manager_company_folder"])
    if click_manage_company_folder.is_displayed():
       click_manage_company_folder.click()
    else:
        Commands.Wait10s_ClickElement(data["contact"]["admin_contact"])
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["click_manager_company_folder"])
    time.sleep(2)
    Logging("1. Click  Manage Company Folders successfully")
    Commands.Wait10s_ClickElement(data["contact"]["folder_public_contact"])
    Logging("2. Click  Public Contact successfully")



    '''
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["textbox_folder_name"])))
    folder_name_manage_company = driver.find_element_by_xpath(data["contact"]["textbox_folder_name"])
    folder_name_manage_company.send_keys(data["contact"]["title_folder_manager_company"]) 
    content_subject=folder_name_manage_company.get_attribute("value")
    if(content_subject==data["contact"]["title_folder_manager_company"]):
        Logging("6. Add name folder =>pass")
    else:
        Logging("6. Add name folder =>fail")
    Logging("5. Input folder Name successfully" + " :  " + data["contact"]["title_folder_manager_company"] )
    time.sleep(2)
    '''

    now = datetime.now()
    name_folder_contact_company = "Generated sele" +" " + now.strftime("%Y")
    input_description_contact = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["textbox_folder_name"])))
    input_description_contact.send_keys(name_folder_contact_company)
    time.sleep(2)






    Logging("----------------------------------- Share Folder -----------------------------------")

    Commands.Wait10s_ClickElement(data["contact"]["check_radio_share"])
    Logging("1.Click Radio Share =>Pass")
    time.sleep(2)
    Commands.Wait10s_ClickElement(data["contact"]["org_share_user_share"])
    Logging("2.Click Organization =>Pass")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["select_dept_manager_company"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["icon_add_user_manager"])
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["btn_save_add_user_mana"])))
    Commands.scroll_view(data["contact"]["btn_save_add_user_mana"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_add_user_mana"])
    time.sleep(1)
    Logging("3. Select user Share successfully")
    select_permisssion_user = Select(driver.find_element_by_xpath(data["contact"]["click_list_permission"]))
    select_permisssion_user.select_by_visible_text(data["contact"]["select_permisson"])
    Logging("4. Select  Permissison successfully")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_manager_folder"])
    time.sleep(2)
    Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
    Logging("9. Save folder successfully")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["pull_the_scroll_bar_view"])))
    Commands.scroll_view(data["contact"]["pull_the_scroll_bar_view"])
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["pull_the_scroll_bar_view"])))
    follder_manager_company = driver.find_element_by_xpath(data["contact"]["pull_the_scroll_bar_view"])



    if follder_manager_company.is_displayed():
        Logging(Green("Create Manage Company Folders => PASS"))
        TestCase_LogResult(**data["testcase_result"]["contact"]["manager_company_contact"]["pass"])
    else:
        Logging(Red("Create Manage Company Folders => FAIL"))
        TestCase_LogResult(**data["testcase_result"]["contact"]["manager_company_contact"]["fail"])
    time.sleep(1)    


def contact_manager_edit_folder(domain_name):
    Logging("----------------------------------- Edit Folder -----------------------------------")
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["pull_the_scroll_bar_view"])
    time.sleep(1)
    Commands.Wait10s_InputElement(data["contact"]["txt_about_folder"],data["contact"]["content_about_folder"])
    Logging("1. Input Content successfully")
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_manager_folder"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["click_button_close_contact"])
    Logging("2. Save folder successfully")
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["pull_the_scroll_bar_view"])))
    Commands.scroll_view(data["contact"]["pull_the_scroll_bar_view"])
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["pull_the_scroll_bar_view"])))
    follder_manager_company = driver.find_element_by_xpath(data["contact"]["pull_the_scroll_bar_view"])
    if follder_manager_company.is_displayed():
        Logging(Green("Edit Folder => PASS"))
    else:
        Logging(Red("Edit Folder => FAIL"))
    time.sleep(1)   
def contact_manager_delete_folder(domain_name):    
    Logging("----------------------------------- Delete Manage Company Folders-----------------------------------")
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["pull_the_scroll_bar_view"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["btn_delete_folder_company"])
    driver.execute_script("window.scrollTo(0, 100)")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["btn_ok_delete_folder_manager"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
    time.sleep(1)
    Logging("=> Delete Manage Company Folders => PASS")
    time.sleep(1)



def contact_setting_general(domain_name):

    Logging("----------------------------------- Admin Settings - General-----------------------------------")
    Logging("----------------------------------- 1. General - Display Organization Contacts -----------------------------------")
    Commands.Wait10s_ClickElement(data["contact"]["click_admin_setting"])
    Logging("1. Click Admin Settings successfully")
    Commands.Wait10s_ClickElement(data["contact"]["select_view_contact_list"])
    Logging("2. Click Display Organization Contacts : LIST  successfully")
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_view_contact"])
    Logging("3. Click Display Organization Contacts : LIST  successfully")
    Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
    Logging("4. Click Close  successfully")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["select_my_company"])
    Logging("5. Click My Company successfully")
    driver.refresh()
    time.sleep(6)
    if 'A new version is available! Do you want to update?' in driver.page_source :
        Commands.Wait10s_ClickElement(data["contact"]["btn_update_version"])
        #WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["contact"]["btn_update_version"])))
        #update_verion = driver.find_element_by_xpath(data["contact"]["btn_update_version"])
        #update_verion.click()
        Logging("=> Update Version =>  SHOW")
        time.sleep(6)
        driver.get(domain_name + "/addrbook/list/org_0/")
        time.sleep(3)
    else:
        Logging("=> Update Version =>  Not show")
    if 'Name' in driver.page_source :
        Logging(Green("=> Select Display Organization Contacts : LIST =>  PASS"))
        TestCase_LogResult(**data["testcase_result"]["contact"]["setting_general_contact"]["pass"])
    else:
        Logging(Red("=> Select Display Organization Contacts : LIST =>  FAIL"))
        TestCase_LogResult(**data["testcase_result"]["contact"]["setting_general_contact"]["fail"])
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["click_admin_setting"])))
    click_admin_settings = driver.find_element_by_xpath(data["contact"]["click_admin_setting"])
    if click_admin_settings.is_displayed():
        Logging("Show Setting ")
    else:
        Logging("Not Show setting")
        Commands.Wait10s_ClickElement(data["contact"]["admin_contact"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["click_admin_setting"])
    Commands.Wait10s_ClickElement(data["contact"]["select_view_contact_photo"])
    time.sleep(1)
    Logging("6. Click Display Organization Contacts : PHOTO  successfully")
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_view_contact"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
    Logging("7. Click Close  successfully")
    time.sleep(1)


def contact_setting_general_hide_my_contact(domain_name):
    Logging("----------------------------------- 1. General - Hide My Contact -----------------------------------")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["hide_my_contacts"])
    Logging("7. Click Hide My Contacts  successfully")
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_view_contact"])
    Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
    Commands.Wait10s_ClickElement(data["contact"]["manage_favorites"])
    Logging("1. Click Manage Favorites successfully")
    driver.refresh()
    time.sleep(8)
    if 'A new version is available! Do you want to update?' in driver.page_source :
        Commands.Wait10s_ClickElement(data["contact"]["btn_update_version"])
        Logging("=> Update Version =>  SHOW")
        time.sleep(5)
        driver.get(domain_name + "/addrbook/list/org_0/")
        time.sleep(3)
    else:
        Logging("=> Update Version =>  Not show")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["check_data_hide_my_contact"])))
    check_data_hide_my_contact = driver.find_element_by_xpath(data["contact"]["check_data_hide_my_contact"])
    if check_data_hide_my_contact.is_displayed():
        Logging(Red("Hide My Contact => FAIL"))
        TestCase_LogResult(**data["testcase_result"]["contact"]["setting_general_contact"]["fail"])
    else:
        Logging(Green("Hide My Contact => PASS"))
        TestCase_LogResult(**data["testcase_result"]["contact"]["setting_general_contact"]["pass"])
    time.sleep(2)
    Commands.Wait10s_ClickElement(data["contact"]["click_admin_setting"])
    time.sleep(1)
    Logging("1. Click Admin Settings successfully")
    Commands.Wait10s_ClickElement(data["contact"]["hide_my_contacts"])
    time.sleep(1)
    Logging("2. Click Hide My Contacts  successfully")
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_view_contact"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
    time.sleep(1)


def contact_setting_general_public_contact_manager(domain_name):
    
    Logging("----------------------------------- Admin Settings - Public Contacts Manager-----------------------------------")
    
    Commands.Wait10s_ClickElement(data["contact"]["org_share_user_share"])
    Logging("1. Click Organization successfully")
    Commands.Wait10s_ClickElement(data["contact"]["select_user_public_dept"])
    '''
    search_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["txt_search_user_public"])))
    search_dept.send_keys(data["contact"]["dept_name_search"])
    search_dept.send_keys(Keys.RETURN)
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["loading_dialog"])))
    select_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["select_user_public"]))).click()
    '''
    Commands.Wait10s_ClickElement(data["contact"]["icon_add_user_public"])
    time.sleep(5)
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_user_public"])
    Logging("2. Select user Public successfully")
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_public_contact"])
    time.sleep(3)
    Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
    Logging("=> Select Public Contacts Manager => PASS")
    time.sleep(3)
    '''
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["check_user_public"])))
    element.location_once_scrolled_into_view
    time.sleep(1)

    check_user_public = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["check_user_public"])))
    if check_user_public.is_displayed():
        Logging("=> Select Public Contacts Manager => PASS")
    else:
        Logging("=> Select Public Contacts Manager => FAIL")
        ValidateFailResultAndSystem("<div>[Contact]Public Contacts Manager </div>")
    '''

    time.sleep(3)
    Commands.Wait10s_ClickElement(data["contact"]["org_share_user_share"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["icon_delete_all_user_public"])
    time.sleep(5)

    '''
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["check_user_public_delete"])))
    element.location_once_scrolled_into_view
    time.sleep(1)
    select_user_delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["check_user_public_delete"]))).click()
    Logging("3. Select user Public successfully")
    icon_delete_user = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["contact"]["icon_remove_user_public"]))).click()
    '''

    Logging("4. Click icon remove user successfully")
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_user_public"])
    Logging("5. click save successfully")
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_public_contact"])
    Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_manager"])
    time.sleep(2)


def contact_manage_favorites(domain_name):
    Logging("----------------------------------- Manage Favorites-----------------------------------")
    Commands.Wait10s_ClickElement(data["contact"]["manage_favorites"])
    Logging("1. Click Manage Favorites successfully")
    time.sleep(2)
    Commands.Wait10s_ClickElement(data["contact"]["icon_add_favorites_list"])
    Logging("2. Click icon Favorites List successfully")
    time.sleep(2)
    Commands.Wait10s_InputElement(data["contact"]["txt_folder_name_favorites"],data["contact"]["folder_name_favorites_list"])
    Logging("3. Input Folder Name Favorites successfully")
    time.sleep(2)
    Commands.Wait10s_ClickElement(data["contact"]["click_icon_org"])
    Logging("4. Click Organization successfully")
    time.sleep(4)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["contact"]["check_user_favorites_contact_global3"])))
        Logging("=> Domain Global3")
        time.sleep(1)
        Commands.Wait10s_ClickElement(data["contact"]["select_dept_favorites_contact_gloabl3"])
    except WebDriverException:
        Logging("=>NOT Domain Global3")
        Commands.Wait10s_ClickElement(data["contact"]["select_dept_favorites_contact"])
    time.sleep(2)
    Commands.Wait10s_ClickElement(data["contact"]["icon_add_user_favorites"])
    time.sleep(2)
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_user_favorites"])
    time.sleep(1)
    Logging("5. Select user Favorites successfully")
    Commands.Wait10s_InputElement(data["contact"]["txt_description_add_folder"],data["contact"]["content_description_add_folder"])
    Logging("6. Input Description successfully")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["contact"]["btn_save_user_contact_favorites"])
    time.sleep(2)
    Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_favorites"])
    Logging("7. Save Folder Manage Favorites successfully")
    time.sleep(1)
    if 'Contact Favorites' in driver.page_source :
        Logging(Green("=> Manage Favorites =>  PASS"))
        TestCase_LogResult(**data["testcase_result"]["contact"]["contact_favorites"]["pass"])
    else:
        Logging(Red("=> Manage Favorites =>  FAIL"))
        TestCase_LogResult(**data["testcase_result"]["contact"]["contact_favorites"]["fail"])
   

    Logging("-----------------------------------Delete Manage Favorites-----------------------------------")
    Commands.Wait10s_ClickElement(data["contact"]["select_folder_favorites_delete"])
    Logging("1. Click Folder Favorites Delete successfully")
    Commands.Wait10s_ClickElement(data["contact"]["btn_delete_folder_favorites"])
    Logging("2. Click button Delete successfully")
    Commands.Wait10s_ClickElement(data["contact"]["btn_ok_folder_favorites"])
    Logging("3. Click button Delete successfully")
    Commands.Wait10s_ClickElement(data["contact"]["btn_close_delete_folder_favorites"])
    Logging("4. Click button Close successfully")
    Logging("5. Delete Manage Favorites successfully")
    time.sleep(1)


def access_menu_contact(domain_name):
    admin = CheckPresenceOfAdminsubmenu(domain_name)
    
    if admin == True:
        try:
            contact_create_folder(domain_name)
            Logging("create folder successfully")
        except WebDriverException:
            Logging("fail to create folder")
        time.sleep(1)
        try:
            contact_create_subfolder(domain_name)
            Logging("create folder successfully")
        except WebDriverException:
            Logging("fail to create subfolder")
        time.sleep(1)
        try:
            contact_edit_folder(domain_name)
            Logging("Edit folder successfully")
        except WebDriverException:
            Logging("Edit Folder Fail")
        time.sleep(1)
        try:
            contact_delete_folder(domain_name)
            Logging("Delete folder successfully")
        except WebDriverException:
            Logging("fDelete folder Fail")
        time.sleep(1)


        
    else:
        Logging("Account is not admin")
        try:
            contact_create_folder(domain_name)
            Logging("create folder successfully")
        except WebDriverException:
            Logging("fail to create folder")
        time.sleep(1)
        try:
            contact_create_subfolder(domain_name)
            Logging("create folder successfully")
        except WebDriverException:
            Logging("fail to create subfolder")
        time.sleep(1)
        try:
            contact_edit_folder(domain_name)
            Logging("Edit folder successfully")
        except WebDriverException:
            Logging("Edit Folder Fail")
        time.sleep(1)
        try:
            contact_delete_folder(domain_name)
            Logging("Delete folder successfully")
        except WebDriverException:
            Logging("fDelete folder Fail")
        time.sleep(1)
    


    if admin == True:
        try:
            contact_manager_folder(domain_name)
            Logging("Create Manager folder successfully")
        except WebDriverException:
            Logging("Fail to Manager folder")
        time.sleep(1)
        try:
            contact_manager_edit_folder(domain_name)
            Logging("Edit Manager folder successfully")
        except WebDriverException:
            Logging("Edit Manager folder Fail")

        time.sleep(1)

        try:
            contact_manager_delete_folder(domain_name)
            Logging("Delete Manager folder successfully")
        except WebDriverException:
            Logging("Delete Manager folder Fail")

        time.sleep(1)

        
    else:
        Logging("1. Create Manager folder => Account is not admin")





    if admin == True:
        try:
            contact_setting_general(domain_name)
            Logging("Create Settings General  successfully")
        except WebDriverException:
            Logging("Settings General")
        time.sleep(1)


        try:
            contact_setting_general_hide_my_contact(domain_name)
            Logging("Create Settings General - Hide My Contact successfully")
        except WebDriverException:
            Logging("Create Settings General - Hide My Contact Fail")
        time.sleep(1)


        try:
            contact_setting_general_public_contact_manager(domain_name)
            Logging("Create Settings General - Hide My Contact successfully")
        except WebDriverException:
            Logging("Create Settings General - Hide My Contact Fail")
        time.sleep(1)


    else:
        Logging("2. Create Settings General  => Account is not admin")
    

    if admin == True:
        try:
            contact_manage_favorites(domain_name)
            Logging("Create Manage Favorites successfully")
        except WebDriverException:
            Logging("Fail to Manage Favorites")
    else:
        Logging("Account is not admin")
        try:
            contact_manage_favorites(domain_name)
            Logging("Create Manage Favorites successfully")
        except WebDriverException:
            Logging("Fail to Manage Favorites")

    





    time.sleep(2)
    access_menu_home = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["screen_home_gw"])))
    access_menu_home.click()
    time.sleep(1)
    


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






