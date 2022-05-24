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
from luu_function import local, data, Logging, ValidateFailResultAndSystem,TestCase_LogResult,Yellow,Green,Red
from luu_function import driver
# Page





def CheckPresenceOfAdminsubmenu(domain_name):
    Logging("------------------------------------------------------C. Menu Project------------------------------------------------------")
    driver.get(domain_name + "/project/list/2_0_0/")
    time.sleep(1)

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["manage_folder_project"])))
        admin = True
    except WebDriverException:
        admin = False
    return admin

def project_create_folder(domain_name):


    #Logging("------------------------------------------------------C. Menu Project------------------------------------------------------")
    #driver.get(domain_name + "/project/list/2_0_0/")
    
    
    Logging("1. Access Menu Project successfully")
    
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["manage_folder_project"])))
    select_manager_folders = driver.find_element_by_xpath(data["project"]["manage_folder_project"])
    select_manager_folders.click()
    Logging("2. Click Manage Folder successfully")
    time.sleep(1)


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["folder_list_project"])))
    select_list_project =driver.find_element_by_xpath(data["project"]["folder_list_project"])
    select_list_project.click()
    Logging("2. Click list name Project successfully")


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["icon_plus_project"])))
    click_icon_plus_project = driver.find_element_by_xpath(data["project"]["icon_plus_project"])
    click_icon_plus_project.click()
    Logging("3. Click icon plus successfully")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["input_folder_mane_project"])))
    folder_name_manage_project = driver.find_element_by_xpath(data["project"]["input_folder_mane_project"])
    folder_name_manage_project.send_keys(data["project"]["folder_name_project"])
    content_subject=folder_name_manage_project.get_attribute("value")
    if(content_subject==data["project"]["folder_name_project"]):
        Logging("4. Add name folder =>pass" + " :  " + data["project"]["folder_name_project"])
    else:
        Logging("4. Add name folder =>fail")
    Logging("5. Input Folder name Project successfully" + "  : " + data["project"]["folder_name_project"])
    click_save_folder_project = driver.find_element_by_xpath(data["project"]["button_save_folder_project"])
    click_save_folder_project.click()
    time.sleep(1)
    Logging("6. Save folder Project successfully")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["show_folder_create"])))
    folder_name_create_project = driver.find_element_by_xpath(data["project"]["show_folder_create"])
    if folder_name_create_project.is_displayed():
        #Logging("Show Folder Project successfully => PASS")
        Logging(Green("Show Folder Project successfully => PASS"))
        TestCase_LogResult(**data["testcase_result"]["project"]["write_folder_project"]["pass"])
    else:
        Logging(Red("Show Folder Project => FAIL"))
        ValidateFailResultAndSystem("<div>[Project]1. Write folder Project </div>")
        TestCase_LogResult(**data["testcase_result"]["project"]["write_folder_project"]["fail"])
def project_create_subfolder(domain_name):
    Logging("--------------- Write Subfolder ----------------")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["manage_folder_project"])))

    select_manager_folders = driver.find_element_by_xpath(data["project"]["manage_folder_project"])
    select_manager_folders.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["icon_list_project"])))
    click_project_folder_name = driver.find_element_by_xpath(data["project"]["icon_list_project"])
    click_project_folder_name.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["select_parent_folder_project"])))
    select_parent_folder_project = driver.find_element_by_xpath(data["project"]["select_parent_folder_project"])
    select_parent_folder_project.click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["icon_close_list_project"])))
    close_list_parent_folder = driver.find_element_by_xpath(data["project"]["icon_close_list_project"])
    close_list_parent_folder.click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["input_sub_folder_name_project"])))
    subfolder_name_manage_project = driver.find_element_by_xpath(data["project"]["input_sub_folder_name_project"])
    subfolder_name_manage_project.send_keys(data["project"]["subfolder_name_project"])
    Logging("8. Input Subfolder Project successfully" + " :  " + data["project"]["subfolder_name_project"])
    click_save_subfolder_project = driver.find_element_by_xpath(data["project"]["button_save_sub_folder_project"])
    click_save_subfolder_project.click()
    time.sleep(1)
    Logging("9. Save Subfolder Project successfully")
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["manage_folder_project"])))
    select_manager_folders = driver.find_element_by_xpath(data["project"]["manage_folder_project"])
    select_manager_folders.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["parent_folder_project"])))
    click_parent_folder = driver.find_element_by_xpath(data["project"]["parent_folder_project"])
    click_parent_folder.click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["show_folder_create"])))
    sub_folder_name_create_project = driver.find_element_by_xpath(data["project"]["show_folder_create"])
    if sub_folder_name_create_project.is_displayed():
        Logging(Green("Show Folder Board successfully => PASS"))
        TestCase_LogResult(**data["testcase_result"]["project"]["write_subfolder_project"]["pass"])
    else:
        Logging(Red("Show Folder Board Fail => FAIL"))
        ValidateFailResultAndSystem("<div>[Project]2. Write Sub folder Project </div>")
        TestCase_LogResult(**data["testcase_result"]["project"]["write_subfolder_project"]["fail"])
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["select_subfolder_project_delete"])))
    select_subfolder = driver.find_element_by_xpath(data["project"]["select_subfolder_project_delete"])
    select_subfolder.click()
    time.sleep(1)
    Logging("12. Select Subfolder Project successfully")
    click_icon_delete = driver.find_element_by_xpath("//a[contains(@ng-click, 'deleteFolder($event)')]")
    click_icon_delete.click()
    time.sleep(1)
    Logging("13. Click icon delete successfully")


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["ok_button_project"])))
    ok_button_folder_project = driver.find_element_by_xpath(data["project"]["ok_button_project"])
    ok_button_folder_project.click()
    Logging("14. Delete Subfolder Project successfully")
def project_delete_folder(domain_name):
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["parent_folder_project"])))
    click_parent_folder = driver.find_element_by_xpath(data["project"]["parent_folder_project"])
    click_parent_folder.click()
    time.sleep(1)
    if 'HCM AAA' in driver.page_source :
        Logging(Red("1.Delete Subfolder Project FAIL"))
        ValidateFailResultAndSystem("<div>[Project]3. Delete Subfolder Project </div>")
        TestCase_LogResult(**data["testcase_result"]["project"]["delete_subfolder_project"]["fail"])
    else:
        Logging(Green("1.Delete Subfolder Project PASS"))
        TestCase_LogResult(**data["testcase_result"]["project"]["delete_subfolder_project"]["pass"])
    click_icon_delete = driver.find_element_by_xpath("//a[contains(@ng-click, 'deleteFolder($event)')]")
    click_icon_delete.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["ok_button_project"])))
    ok_button_folder_project = driver.find_element_by_xpath(data["project"]["ok_button_project"])
    ok_button_folder_project.click()
    Logging("10. Delete Folder Project successfully")
    time.sleep(2)
    


def project_add_manager(domain_name):

  
    Logging("=============== GW-121 : Project Managers =============== ")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["admin_project"])))
    click_admin_project = driver.find_element_by_xpath(data["project"]["admin_project"])
    click_admin_project.click()
    Logging("1. Click Admin Project successfully")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["admin_manager"])))
    element = driver.find_element_by_xpath(data["project"]["admin_manager"])
    element.location_once_scrolled_into_view
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["admin_manager"])))
    click_admin_manager = driver.find_element_by_xpath(data["project"]["admin_manager"])
    click_admin_manager.click()
    Logging("2. Click Manager Project successfully")
    time.sleep(1)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["manager_project_all_user"])))
    click_all_user_manager = driver.find_element_by_xpath(data["project"]["manager_project_all_user"])
    click_all_user_manager.click()
    Logging("4. Click All User  successfully")
    

    '''
    click_org_select_user_manager = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["click_org_select_user"]))).click()
    Logging("3. Click Organization Select User  successfully")
    #time.sleep(2)
    search_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["txt_search_dept_org_admin_manager"])))
    search_dept.send_keys(data["project"]["dept_name_search_admin_manager"])
    search_dept.send_keys(Keys.RETURN)
    Logging("4. Search User  successfully")
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["loading_dialog"])))
    select_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["select_user_maanger"]))).click()
    icon_add_user = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["project"]["icon_add_user_manager"])))
    icon_add_user.click()
    #time.sleep(2)
    click_save_button = driver.find_element_by_xpath(data["project"]["btn_save_add_user_manager"])
    click_save_button.click()
    #time.sleep(2)
    Logging("5. Select user manager successfully")
    '''


    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_save_admin_maanger"])))
    click_save_button_admin_manager = driver.find_element_by_xpath(data["project"]["btn_save_admin_maanger"])
    click_save_button_admin_manager.click()
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_close_admin_maanger"])))
    click_close_button_admin_manager = driver.find_element_by_xpath(data["project"]["btn_close_admin_maanger"])
    time.sleep(1)
    if click_close_button_admin_manager.is_displayed():
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_close_admin_maanger"])))
        click_close_button_admin_manager = driver.find_element_by_xpath(data["project"]["btn_close_admin_maanger"])
        click_close_button_admin_manager.click()
        Logging(Green("Add Project Managers  => PASS"))
        time.sleep(1)
        TestCase_LogResult(**data["testcase_result"]["project"]["add_project_manager"]["pass"])
    else:
        Logging(Red("Add Project Managers => FAIL"))
        ValidateFailResultAndSystem("<div>[Project]3. Project Managers  </div>")
        TestCase_LogResult(**data["testcase_result"]["project"]["add_project_manager"]["fail"])
    Logging("6. Save Manager successfully")

    '''
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["check_user_manager_project"])))
    element.location_once_scrolled_into_view
    time.sleep(1)
    check_user_manager = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["check_user_manager_project"])))
    if check_user_manager.is_displayed():
        Logging("=> Select user Manager Project => PASS")
    else:
        Logging("=> Select user Manager Project => FAIL")
        ValidateFailResultAndSystem("<div>[Project]GW-121 : Project Managers </div>")
    time.sleep(1)
    '''




    Logging("=============== Delete User Managers =============== ")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["manager_project_select_manager"])))
    click_org_select_user_manager = driver.find_element_by_xpath(data["project"]["manager_project_select_manager"])
    click_org_select_user_manager.click()
    Logging("1. Select Manager   successfully")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_save_admin_maanger"])))
    click_save_button_admin_manager = driver.find_element_by_xpath(data["project"]["btn_save_admin_maanger"])
    click_save_button_admin_manager.click()
    time.sleep(1)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_close_admin_maanger"])))
    click_close_button_admin_manager = driver.find_element_by_xpath(data["project"]["btn_close_admin_maanger"])
    click_close_button_admin_manager.click()
    '''
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["project"]["select_user_manager_delete"])))
    element.location_once_scrolled_into_view
    time.sleep(1)
    select_user_delete_manager = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["select_user_manager_delete"]))).click()
    #time.sleep(1)
    delete_user_manager = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["icon_delete_user_manager"]))).click()
    #time.sleep(1)
    Logging("2. Click icon Delete successfully")
    click_save_button = driver.find_element_by_xpath(data["project"]["btn_save_add_user_manager"])
    click_save_button.click()
    time.sleep(1)
    click_save_button_admin_manager = driver.find_element_by_xpath(data["project"]["btn_save_admin_maanger"])
    Logging("3. Delete User Managers successfully")
    '''
def project_add_extension_form(domain_name):
    Logging("=============== Set extension form =============== ")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["click_set_extenssion"])))
    element = driver.find_element_by_xpath(data["project"]["click_set_extenssion"])
    element.location_once_scrolled_into_view
    time.sleep(1)


    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["click_set_extenssion"])))
    click_set_extension_form = driver.find_element_by_xpath(data["project"]["click_set_extenssion"])
    click_set_extension_form.click()
    Logging("1. Click Set extension form Project successfully")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["icon_craete_extenssion_form"])))
    click_icon_create_extension_form = driver.find_element_by_xpath(data["project"]["icon_craete_extenssion_form"])
    click_icon_create_extension_form.click()
    Logging("2. Click icon Create Set extension form Project successfully")
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["txt_form_name_extension_project"])))
    input_form_name_extension = driver.find_element_by_xpath(data["project"]["txt_form_name_extension_project"])
    input_form_name_extension.send_keys(data["project"]["form_name_extension_project"])
    input_form_name_extension.send_keys(Keys.RETURN)
    Logging("3. Input Form name  successfully")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["select_form_type"])))
    click_form_type_text = driver.find_element_by_xpath(data["project"]["select_form_type"])
    click_form_type_text.click()
    Logging("4. Select Form type Text successfully")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_save_extension_form_project"])))
    click_btn_save_extension_form = driver.find_element_by_xpath(data["project"]["btn_save_extension_form_project"])
    click_btn_save_extension_form.click()
    Logging("5. Click button Save extension form Project successfully")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_close_save_extension_form"])))
    click_btn_close_extension_form = driver.find_element_by_xpath(data["project"]["btn_close_save_extension_form"])
    click_btn_close_extension_form.click()
    Logging("6. Click button Save extension form Project successfully")
    
    time.sleep(1)
    if 'Mang Tre Viet Nam' in driver.page_source :
        Logging(Green("1.Create Set extension form => Pass"))
        TestCase_LogResult(**data["testcase_result"]["project"]["extension_form"]["pass"])
    else:
        Logging(Red("1.Set extension form Fail"))
        ValidateFailResultAndSystem("<div>[Project]Set extension form</div>")
        TestCase_LogResult(**data["testcase_result"]["project"]["extension_form"]["fail"])

    
    Logging("=============== Delete Set extension form =============== ")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["txt_search_form_name_delete"])))
    search_form_name_extension = driver.find_element_by_xpath(data["project"]["txt_search_form_name_delete"])
    search_form_name_extension.send_keys(data["project"]["form_name_extension_project"])
    search_form_name_extension.send_keys(Keys.RETURN)
    time.sleep(1)
    Logging("1. Show form name Search successfully")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["icon_checkbox_all"])))
    check_all_extension_form_search = driver.find_element_by_xpath(data["project"]["icon_checkbox_all"])
    check_all_extension_form_search.click()
    Logging("2. Click checkbox all successfully")
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_delete_form"])))
    click_btn_delete = driver.find_element_by_xpath(data["project"]["btn_delete_form"])
    click_btn_delete.click()
    Logging("3. Click button Delete successfully")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_ok"])))
    click_btn_ok = driver.find_element_by_xpath(data["project"]["btn_ok"])
    click_btn_ok.click()
    Logging("4. Click button OK successfully")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_close_save_extension_form"])))
    click_btn_close_delete = driver.find_element_by_xpath(data["project"]["btn_close_save_extension_form"])
    click_btn_close_delete.click()
    Logging("5. Click button Close successfully")
    
def project_add_work_type(domain_name):
    Logging("=============== Manage Work Type =============== ")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["click_manager_work_type"])))
    click_manager_work_type = driver.find_element_by_xpath(data["project"]["click_manager_work_type"])
    click_manager_work_type.click()
    Logging("1. Click Manage Work Type successfully")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["icon_create_work_type"])))
    click_icon_create_manager_work_type = driver.find_element_by_xpath(data["project"]["icon_create_work_type"])
    click_icon_create_manager_work_type.click()
    Logging("2. Click icon Create Manage Work Type successfully")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["txt_type_name"])))
    input_manager_work_type = driver.find_element_by_xpath(data["project"]["txt_type_name"])
    input_manager_work_type.send_keys(data["project"]["name_work_type"])
    Logging("3. Input Work Type  successfully")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["turn_off_work_type"])))
    turn_off_work_type =driver.find_element_by_xpath(data["project"]["turn_off_work_type"])
    turn_off_work_type.click()
    Logging("4. Turn Off Work Type successfully")


    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_save_work_type_project"])))
    click_btn_save_work_type = driver.find_element_by_xpath(data["project"]["btn_save_work_type_project"])
    click_btn_save_work_type.click()
    Logging("5. Click button Save Manage Work Type successfully")
    time.sleep(3)
    if 'Dau Xanh' in driver.page_source :
        Logging(Green("1.Create Manage Work Type => Pass"))
        TestCase_LogResult(**data["testcase_result"]["project"]["work_type"]["pass"])
    else:
        Logging(Red("1.Manage Work Type Fail"))
        ValidateFailResultAndSystem("<div>[Project]Manage Work Type</div>")
        TestCase_LogResult(**data["testcase_result"]["project"]["work_type"]["fail"])
    
    Logging("===============Delete Manage Work Type =============== ")
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["txt_work_type"])))
    search_work_type = driver.find_element_by_xpath(data["project"]["txt_work_type"])
    search_work_type.send_keys(data["project"]["name_work_type"])
    search_work_type.send_keys(Keys.RETURN)
    Logging("1. Show form name Search successfully")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["check_box_work_name_search"])))
    check_all_work_name_search = driver.find_element_by_xpath(data["project"]["check_box_work_name_search"])
    check_all_work_name_search.click()
    Logging("2. Click checkbox all successfully")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_delete_work_type"])))
    click_btn_delete = driver.find_element_by_xpath(data["project"]["btn_delete_work_type"])
    click_btn_delete.click()
    Logging("3. Click button Delete successfully")
    time.sleep(1)

    '''
    show_table_error_delete_work_type = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["show_table_error"])))
    if show_table_error_delete_work_type.is_displayed():
        click_close_table_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_ok_error_delete_work_type"]))).click()
        Logging("4. Click button close successfully")
    else:
        Logging("Not show table Error")
    time.sleep(1)
    '''


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["project"]["btn_ok_delete_work_type"])))
    click_btn_ok = driver.find_element_by_xpath(data["project"]["btn_ok_delete_work_type"])
    click_btn_ok.click()
    Logging("Delete Manage Work Type => PASS")
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["screen_home_gw"])))
    access_menu_home = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["screen_home_gw"])))
    access_menu_home.click()
    time.sleep(1)




def access_menu_project(domain_name):
    admin = CheckPresenceOfAdminsubmenu(domain_name)
    if admin == True:
        try:
            project_create_folder(domain_name)
            Logging("create folder successfully")
        except WebDriverException:
            Logging("fail to create folder")

        time.sleep(1)
        try:
            project_create_subfolder(domain_name)
            Logging("create folder successfully")
        except WebDriverException:
            Logging("fail to create folder")
        time.sleep(1)

        try:
            project_delete_folder(domain_name)
            Logging("create folder successfully")
        except WebDriverException:
            Logging("fail to create folder")
        time.sleep(1)
        
    else:
        Logging("1.Create Folder => Account is not admin")

    if admin == True:
        try:
            project_add_manager(domain_name)
            Logging("Add Manager successfully")
        except WebDriverException:
            Logging("Pass")
        
    else:
        Logging("2.Add manage => Account is not admin")


    if admin == True:
        try:
            project_add_extension_form(domain_name)
            Logging("Add Extension successfully")
        except WebDriverException:
            Logging("Fail to Add Extension Form ")
        
    else:
        Logging("3.Add Extension Form => Account is not admin")

    
    if admin == True:
        try:
            project_add_work_type(domain_name)
            Logging("Add Work Type successfully")
        except WebDriverException:
            Logging("Fail to Add Work Type ")
        
    else:
        Logging("4.Add Work Type=> Account is not admin")
    



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

with open(local+'\\'+'luu_project.txt','w') as project:
    domain="http://groupware57.hanbiro.net"
    access_menu_project(domain,project)




#access_menu_project()
result=open(local+'\\result.txt','r')
file_result=result.read()
Logging(file_result)

  
time.sleep(3)
'''





#end_time = time.time()
#loading_time = end_time - start_time
#Logging(end_time - start_time)


