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
import luu_function
from luu_function import local, data, Logging, ValidateFailResultAndSystem,TestCase_LogResult,Green,Yellow,Red
from luu_function import driver

# Page



def CheckPresenceOfAdminsubmenu(domain_name):
    Logging("------------------------------------------------------C. Menu Approval------------------------------------------------------")
    driver.get(domain_name + "/approval/list/progress/ireq/")
    time.sleep(2)
    Logging("1. Access Menu Approval successfully")
    click_list_in_progress = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_list_in_progress_approval"])))
    click_list_in_progress.click()
    #time.sleep(1)
    #click_admin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["admin_approval"])))
    #click_admin.click()
    #time.sleep(1)
    #Logging("2. Click Admin successfully")
   
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["admin_approval"])))
        admin = True
    except WebDriverException:
        admin = False
    return admin






def approval_write_all_form(domain_name):
    Logging("------------------------------------------------------Menu Approval------------------------------------------------------")
    time.sleep(2)
    #access_menu_approval = driver.find_element_by_xpath("//span[contains(.,'Approval')]")
    #access_menu_approval.click()
    #driver.get(domain_name + "/approval/list/progress/ireq/")
    #Logging("1. Access Menu Approval successfully")
    
    '''
    list_in_progress = driver.find_element_by_xpath(data["approval"]["list_data_in_progress_approval"])
    click_list_in_progress = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_list_in_progress_approval"])))
    if  list_in_progress.is_displayed():
        click_list_in_progress.click()
        Logging("2. Click list In Progress successfully")
    else:
        Logging("2. Click list In Progress Fail")
    Logging("1. Click List Hide In Progress successfully")
    '''
    
    
    #click_admin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["admin_approval"])))
    #click_admin.click()
    #time.sleep(1)
    #Logging("2. Click Admin successfully")
    Logging("---------------- Write All Form ------------------")
    click_all_from = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_all_form"])))
    click_all_from.click()
    time.sleep(1)
    Logging("3. Click All Forms successfully")
    total=driver.find_elements_by_class_name("message-footer > .pull-left")[0].text
    Logging("---  Total All Form before create new : " + total)
    time.sleep(2)
    click_icon_create_all_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["icon_create_all_form"])))
    click_icon_create_all_form.click()
    click_form_selection = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["form_selection"])))
    click_form_selection.click()
    click_folder_approval = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["folder_approval"])))
    click_folder_approval.click()
    Logging("5. Click folder approval successfully")
    click_agreement_route = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["agreement_route"])))
    click_agreement_route.click()
    Logging("6. Click Agreement Route successfully")
    click_common = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_common"])))
    click_common.click()
    Logging("7. Click Common successfully") 
    click_button_confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["button_confirm"])))
    click_button_confirm.click()
    Logging("8. Click button confirm successfully")
    form_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_form_name"])))
    form_name.send_keys(data["approval"]["form_name"])
    title_form_name=form_name.get_attribute("value")
    if(title_form_name==data["approval"]["form_name"]):
        Logging("7. Add Form Name =>pass")
    else:
        Logging("7. Add Form Name =>fail")
    Logging("8. Input Add Form Name successfully" + " :  " + data["approval"]["form_name"] )
    click_doc_no = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["icon_button_doc_no"])))
    click_doc_no.click()
    driver.execute_script("window.scrollTo(0, 100)")
    time.sleep(2)   
    click_save_doc_no = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["button_save_doc_no"])))
    click_save_doc_no.click()
    time.sleep(1)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    content_input.send_keys(data["approval"]["content_form_name"])
    driver.switch_to.default_content()
    click_button_save_all_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_button_save_all_form"])))
    click_button_save_all_form.click()
    time.sleep(2)
    Logging("9. Input Content All Form successfully")
    Logging("10. Save All Form successfully")
    time.sleep(2)
    total1=driver.find_elements_by_class_name("message-footer > .pull-left")[0].text
    total=so(total)
    total1=so(total1)    
    Logging("---  Total all form after create : ")
    time.sleep(2)
    Logging(total1)
    if total1== total +1 :
        Logging(" ***  Total All Form displayed correctly")
        Logging(Green("Write All Form => ---------PASS"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_form"]["pass"])
    else:
        Logging(Red(" Write All Form => ---- FAIL "))
        ValidateFailResultAndSystem("<div>[Approval]2. Write All Form </div>")
        TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_form"]["fail"])
    
    Logging("----------------Search Form by Type ------------------")
    click_detail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_deatail_search_all_form"])))
    click_detail.click()
    Logging("1. Click Details successfully")
    select_agreement_route = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_agreement_search_all_form"])))
    select_agreement_route.click()
    Logging("2. Click Agreement Route successfully")
    btn_search_type_all_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_search_all_form"])))
    btn_search_type_all_form.click()
    Logging("3. Click Button Search by Type successfully")
    click_detail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_deatail_search_all_form"])))
    click_detail.click()
    time.sleep(2)
    total2=driver.find_elements_by_class_name("message-footer > .pull-left")[0].text
    total2=so(total2)
    Logging("---  Total all form after search : ")
    time.sleep(1)
    Logging(total2)
    if total2 <= total1 :
        Logging("Search Form by Type => ---------PASS")
        TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_form"]["pass"])
    else:
        Logging(" Search Form by Type => ---- FAIL ")
    
    Logging("----------------Delete All Form ------------------")
    search_form_name= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_search_approval_form"])))
    search_form_name.send_keys(data["approval"]["search_form_delete"])
    search_form_name.send_keys(Keys.RETURN)
    Logging("1. Show form name Search successfully")
    click_checkbox_all = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["checkbox_all_form"])))
    click_checkbox_all.click()
    Logging("2. Click checkbox all Form successfully")
    click_btn_delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_delete_all_form"])))
    click_btn_delete.click()
    Logging("3. Click button Delete successfully")
    click_btn_ok = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_ok_delete_form"])))
    click_btn_ok.click()
    Logging("5.Search and Delete  All Form successfully")

    Logging("----------------Create Form Section------------------")
    click_btn_more = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_more"])))
    click_btn_more.Click()
    Logging("1. Click button More successfully")
    time.sleep(1)
    click_form_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["form_section"])))
    click_form_section.click()
    Logging("2. Click Form Section successfully")
    time.sleep(1)
    click_parent_folder = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["list_parent_folder"])))
    click_parent_folder.click()
    Logging("3. Click Parent Folder successfully")
    time.sleep(1)
    click_approval_in_parent_folder = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["parent_folder_click_approval"])))
    click_approval_in_parent_folder.click()
    Logging("4. Click Approval in Parent folder successfully")
    click_agreement_route = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_agreement_route"]))).click()
    Logging("5. Click Agreement Route successfully")
    folder_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_folder_name_section"])))
    folder_name.send_keys(data["approval"]["folder_name_section"])
    Logging("6. Input Folder name Form Section successfully")
    click_btn_save_form_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_save_folder_name_section"])))
    click_btn_save_form_section.click()
    Logging("7. Click butotn Save successfully")
    Logging("----------------Check Create Form Section and Delete Form Section------------------")
    click_btn_more = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_more"]))).click()
    Logging("1. Click button More successfully")
    click_form_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["form_section"])))
    click_form_section.click()
    Logging("2. Click Form Section successfully")
    time.sleep(1)
    click_folder_approval_check_data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["form_section_check_data"])))
    click_folder_approval_check_data.click()
    Logging("3. Click Approval check data successfully")
    time.sleep(1)
    click_agreement_route_check_data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["form_section_select_agreement_route_check_data"])))
    click_agreement_route_check_data.click()
    Logging("4. Click Agreement Route  check data successfully")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["view_section_form_check_data"])))
    element.location_once_scrolled_into_view
    Logging("5.Create Form Section successfully")
    click_form_section_delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["view_section_form_check_data"])))
    click_form_section_delete.click()
    Logging("6.Click Form Section successfully")
    btn_delete_form_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["delete_section_form"])))
    btn_delete_form_section.click()
    Logging("7.Click button Delete Form Section successfully")
    time.sleep(1)
    btn_ok_delete_form_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_ok_delete_section_form"])))
    btn_ok_delete_form_section.click()
    Logging("8.Click button OK - Delete Form Section successfully")



def approval_write_all_official_form(domain_name):
    time.sleep(4)
    Logging("-------------- Write All Official Forms ------------------")  
    click_admin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["admin_approval"])))
    click_admin.click()
    time.sleep(1)
    Logging("2. Click Admin successfully")


    click_all_official_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["all_official_form"])))
    click_all_official_form.click()
    Logging("1. Click All Official Forms successfully")
    click_button_create_a_new_approval_route = driver.find_element_by_xpath(data["approval"]["create_a_new_approval_route"])
    click_button_create_a_new_approval_route.click()
    Logging("2. Click Create a new Approval Route successfully")
    official_name = driver.find_element_by_xpath(data["approval"]["click_textbox_name_official_forms"])
    official_name.send_keys(data["approval"]["official_forms_name"])
    title_official_name=official_name.get_attribute("value")
    if(title_official_name==data["approval"]["official_forms_name"]):
        Logging("3. Input Official Forms Name =>pass")
    else:
        Logging("3. Input Official Forms Name =>fail")
    Logging("4. Input Input Official Forms Name successfully" + " :  " + data["approval"]["official_forms_name"] )
    time.sleep(1)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    content_input.send_keys(data["approval"]["content_form_name_official_forms"])
    driver.switch_to.default_content()
    time.sleep(2)
    Logging("5. Input Content All Form successfully")
    click_button_save_official_name = driver.find_element_by_xpath(data["approval"]["button_save_all_offcial_form"])
    click_button_save_official_name.click()
    Logging("6. Save All Official Forms successfully")
    time.sleep(2)
    if 'QA Luu' in driver.page_source :
        Logging(Green("=>  1. Write All Official Forms  PASS"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_official_form"]["pass"])
    else:
        Logging(Red("=>  1. Write All Official Forms  FAIL"))
        ValidateFailResultAndSystem("<div>[Approval] Write All Official Forms  </div>")
        TestCase_LogResult(**data["testcase_result"]["approval"]["write_all_official_form"]["fail"])
    Logging("-------------Delete All Official Forms - Admin---------------")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_official_forms_delete"])))
    element.location_once_scrolled_into_view
    time.sleep(2)
    click_checkbox_official_delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_official_forms_delete"])))
    click_checkbox_official_delete.click()
    Logging("1. Click checkbox Delete All Official Forms Admin successfully")
    click_btn_delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_delete_official_forms"])))
    click_btn_delete.click()
    time.sleep(1)
    Logging("2. Click button Delete successfully")
    click_btn_confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_confirm_delete_approval_routes_admin"])))
    click_btn_confirm.click()
    Logging("3. Click button confirm successfully")
    
    Logging("=> Delete Default Approval Routes - Admin successfully")
def approval_view_all_approvals(domain_name):
   
    Logging("----------------- View All Approvals ------------------")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["all_approvals"])))
    element.location_once_scrolled_into_view
    time.sleep(2)
    click_all_approval = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["all_approvals"])))
    click_all_approval.click()
    Logging("1. Click All Approvals successfully")
    '''
    click_comprehensive_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["comprehensive_search"])))
    click_comprehensive_search.send_keys(data["approval"]["title_approvals"])
    click_comprehensive_search.send_keys(Keys.RETURN)
    '''
    #Logging("2. Search Approvals successfully")
    select_a_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_a_approval"])))
    select_a_title.click()
    try:
        click_textbox_input_pw = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_input_secrutity_pw"])))
        click_textbox_input_pw.send_keys(data["approval"]["secrutity_pw"])
        time.sleep(1)
        btn_confirm_security_pw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_confirm_secrutity_pw"])))
        btn_confirm_security_pw.click()
        Logging(" Input Password successfully") 
    except WebDriverException:
        Logging("NOT SHOW Security Pasword ")



    Logging("3. View All Approvals successfully")
    time.sleep(1)
    if 'References' in driver.page_source :
        Logging(Green("=> 1.View All Approvals=> ---------- PASS"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["view_all_approval"]["pass"])
    else:
        Logging(Red("=> 1.View All Approvals =>---------- FAIL"))
        ValidateFailResultAndSystem("<div>[Approvals]2. View All Approvals </div>")
        TestCase_LogResult(**data["testcase_result"]["approval"]["view_all_approval"]["fail"])
    
def approval_view_official_documentation(domain_name):
    Logging("--------------- View Official Documentation ------------------")
    click_official_documentation = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["official_documentation"])))
    click_official_documentation.click()
    Logging("1. Click Official Documentation successfully")
    '''
    time.sleep(3)
    click_official_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["textbox_input_search"])))
    click_official_search.send_keys(data["approval"]["search_title_official_documentation"])
    click_official_search.send_keys(Keys.RETURN)
    time.sleep(3)
    Logging("2. Search Official Documentation successfully")
    '''
    select_a_title_official_documentation = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_official_documenttation"])))
    select_a_title_official_documentation.click()
    Logging("3. View Official Documentation successfully")
    time.sleep(2)
    if 'Print' in driver.page_source :
        Logging(Green(" => 1.View Official Documentation =>  PASS"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["view_official_documentation"]["pass"])
    else:
        Logging(Red("=>1.View Official Documentation => FAIL"))
        ValidateFailResultAndSystem("<div>[Approvals]View Official Documentation </div>")
        TestCase_LogResult(**data["testcase_result"]["approval"]["view_official_documentation"]["fail"])

def approval_arbitrary_decision(domain_name):
    Logging("-------------- Arbitrary Decision Settings -----------------")
    click_arbitrary_decision = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_arbitrary_decision"])))
    click_arbitrary_decision.click()
    Logging("1. Click Arbitrary Decision successfully")
    search_org_arbitrary_decision = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["search_user_arbitrary_decision"])))
    search_org_arbitrary_decision.send_keys(data["approval"]["search_user"])
    search_org_arbitrary_decision.send_keys(Keys.RETURN)
    time.sleep(1)
    Logging("6. Search user successfully")
    select_user_arbitrary_decision = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_user_arbitrary_decision"])))
    select_user_arbitrary_decision.click()
    Logging("3. Select user successfully")
    time.sleep(1)
    click_save_arbitrary_decision = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["button_click_save_arbitrary_decision"])))
    click_save_arbitrary_decision.click()
    Logging("3. Arbitrary Decision Settings successfully")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["show_arbitrary_decision"])))
    element.location_once_scrolled_into_view
    time.sleep(1)
    user_arbitrary = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["approval"]["show_arbitrary_decision"])))
    if user_arbitrary.is_displayed():
        Logging(Green("=> Arbitrary Decision Settings =>--------- PASS"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["arbitrary_decison"]["pass"])
    else:
        Logging(Red("=> Arbitrary Decision Settings=>---------- FAIL"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["arbitrary_decison"]["fail"])
    Logging("-------------Delete User Arbitrary Decision Settings ---------------")
    click_user_delete_arbitrary = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_user_delete_arbitrary_decision"])))
    click_user_delete_arbitrary.click()
    Logging("1. Click User Delete Change Approval Route successfully")
    click_save_arbitrary_decision = driver.find_element_by_xpath(data["approval"]["button_click_save_arbitrary_decision"])
    click_save_arbitrary_decision.click()
    Logging("2. Delete Change Approval Route successfully")
    


'''
def approval_change_approval_route(domain_name):
    Logging("------------- Change Approval Route ---------------")
    click_change_approval_route = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["change_approval_route"])))
    click_change_approval_route.click()
    Logging("1. Click Change Approval Route successfully")
    time.sleep(1)
    click_folder_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["dept_user_change_approval"]))).click()
    select_user_change_approval_route = driver.find_element_by_xpath(data["approval"]["select_user_change_approval_route"])
    select_user_change_approval_route.click()
    Logging("3. Select user Change Approval Route successfully")
    time.sleep(1)
    click_save_change_approval_route = driver.find_element_by_xpath(data["approval"]["button_click_save_change_approval_route"])
    click_save_change_approval_route.click()
    time.sleep(1)
    Logging("3. Add User Change Approval Route successfully")
    time.sleep(2)
'''



    
def approval_default_approval_route(domain_name):
    Logging("------------- Default Approval Routes - Admin---------------")
    click_approval_default_approval_routes = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_default_approval_routes_admin"])))
    click_approval_default_approval_routes.click()
    time.sleep(1)
    Logging("1. Click Default Approval Route Admin successfully")
    click_create_a_new_approval_route_admin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_create_a_new_approval_route_admin"])))
    click_create_a_new_approval_route_admin.click()
    Logging("2. Click Create a new approval Route successfully")
    input_approval_route_name_admin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_approval_route_name_admin"])))
    input_approval_route_name_admin.send_keys(data["approval"]["approval_route_name_admin"])
    click_org_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["icon_org_default_approval_name_admin"])))
    click_org_default_approval_routes.click()
    Logging("5. Click Org successfully")

    '''
    search_org_default_approval_routes_admin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["search_user_org_default_admin"])))
    search_org_default_approval_routes_admin.send_keys(data["approval"]["user_search_org_approval"])
    search_org_default_approval_routes_admin.send_keys(Keys.RETURN)
    time.sleep(1)
    Logging("6. Search user successfully")
    time.sleep(3)
    '''

    select_dept_default_approval_routes = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["dept_defaul_approval_admin"])))
    select_dept_default_approval_routes.click()
    select_user_org_default_approval_routes = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_user_default_approval_admin"])))
    select_user_org_default_approval_routes.click()
    time.sleep(1)
    Logging("7. Select user successfully")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_save_org_app_default_admin"])))
    element.location_once_scrolled_into_view
    save_user_org_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_save_org_app_default_admin"])))
    save_user_org_default_approval_routes.click()
    Logging("9. Save user successfully")
    click_save_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_save_defaul_approval_routes"])))
    click_save_default_approval_routes.click()
    Logging("10. Save Default Approval Routes successfully")
    Logging("-------------Delete Default Approval Routes - Admin---------------")
    driver.execute_script("window.scrollTo(0, 100)")
    time.sleep(2)
    click_checkbox_delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_approval_routes_type_admin"])))
    click_checkbox_delete.click()
    Logging("1. Click checkbox Delete Default Approval Routes Admin successfully")
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(2)
    click_btn_delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_delete_approval_routes_admin"])))
    click_btn_delete.click()
    Logging("2. Click button Delete successfully")
    click_btn_confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_confirm_delete_approval_routes_admin"])))
    click_btn_confirm.click()
    Logging("3. Click button confirm successfully")
    Logging("=> Delete Default Approval Routes - Admin successfully")
    

    time.sleep(1)
    Logging("------------- Set Official Seal - Admin ---------------")
    click_set_official_seal_admin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_value_set_official_seal"])))
    click_set_official_seal_admin.click()
    Logging("1. Click Set Official Seal successfully")
    time.sleep(1)
    get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["file_set_official_seal"])))
    get_file.send_keys(luu_function.file_img)
    Logging("2. Attch Signature Image successfully")
    click_save_set_official_seal_admin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_save_set_official_seal"])))
    click_save_set_official_seal_admin.click()
    Logging("3. Click button Save Set Official Seal successfully")
    time.sleep(1)
    check_show_image_set_official_seal = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_data_save_set_official_seal"])))
    if check_show_image_set_official_seal.is_displayed():
        Logging("=> Add Set Official Seal =>--------- PASS")
    else:
        Logging("=> Add Set Official Seal=>---------- FAIL")
    Logging("------------- Delete Set Official Seal - Admin ---------------")
    check_show_image_set_official_seal = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_data_save_set_official_seal"])))
    check_show_image_set_official_seal.click()
    click_save_set_official_seal_admin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_save_set_official_seal"])))
    click_save_set_official_seal_admin.click()
    





    '''
    Logging("------------- Search Discarded Documents - Admin ---------------")
    time.sleep(1)
    click_discarded_documents = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_discarded_documents"]))).click()
    time.sleep(2)
    click_discarded_documents_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_search_discarded_document"])))
    click_discarded_documents_search.send_keys(data["approval"]["comprehensive_search_documet"])
    click_discarded_documents_search.send_keys(Keys.RETURN)
    time.sleep(5)
    time.sleep(2)
    if 'Luu' in driver.page_source :
        Logging(" => 1.View Official Documentation =>  PASS")
    else:
        Logging("=>1.View Official Documentation => FAIL")
    time.sleep(2)
    Logging("1. Search Discarded Documents successfully")

    '''


def approval_default_approval_route_setting(domain_name):

    Logging("------------- Default Approval Routes-Setting---------------")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_sttings_approval"])))
    element.location_once_scrolled_into_view
    time.sleep(2)
    click_approval_settings = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_sttings_approval"])))
    click_approval_settings.click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
    Logging("1. Click Settings successfully")
    click_approval_default_approval_routes= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_default_approval_routes"])))
    click_approval_default_approval_routes.click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
    Logging("2. Click Default Approval Route successfully")
    time.sleep(1)
    click_create_a_new_approval_route = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["create_default_approval_routes"])))
    click_create_a_new_approval_route.click()
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
    #click_create_a_new_approval_route = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["create_default_approval_routes"])))
    #click_create_a_new_approval_route.click()
    click_create_a_new_approval_route = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["create_default_approval_routes"])))
    click_create_a_new_approval_route.click()
    time.sleep(1)
    Logging("3. Click button Create a new Approval Route successfully")
    input_approval_route_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["input_appproval_route_name"])))
    input_approval_route_name.send_keys(data["approval"]["approval_route_name"])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["loading_dialog"])))
    title_approval_route_name=input_approval_route_name.get_attribute("value")
    if(title_approval_route_name==data["approval"]["approval_route_name"]):
        Logging("3. Input Approval Route Name =>pass")
    else:
        Logging("3. Input Approval Route Name =>fail")
    Logging("4. Input Approval Route Name successfully" + " :  " + data["approval"]["approval_route_name"] )
    click_org_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_org_default_approval_routes"])))
    click_org_default_approval_routes.click()
    Logging("5. Click Org successfully")
    search_org_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["search_user_approval_in_org"])))
    search_org_default_approval_routes.send_keys(data["approval"]["user_search_org_approval"])
    search_org_default_approval_routes.send_keys(Keys.RETURN)
    time.sleep(2)
    Logging("6. Search user successfully")
    select_user_org_default_approval_routes = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_user_defaul_setting"])))
    select_user_org_default_approval_routes.click()

    '''
    time.sleep(1)
    #select_dept_org_default_approval_routes = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_dept_defaul_setting"]))).click()
    time.sleep(1)
    select_user_org_default_approval_routes = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, data["approval"]["user_reviewer_01"])))
    select_user_org_default_approval_routes.click()
    time.sleep(1)
    add_user_org_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["icon_add_user"])))
    add_user_org_default_approval_routes.click()
    Logging("8. Add user successfully")
    time.sleep(2)
    try:
        check_show_sub_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_show_sub_dept"])))
        if check_show_sub_dept.is_displayed():
            click_sub_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_ok_select_sub_dept"]))).click()
            Logging("=> Select Sub Dept => --------PASS")
        else:
            Logging("=> Sub Dept not show  ")
            
    except WebDriverException:
        Logging("Not Show sub Dept ")
    '''



    time.sleep(1)
    Logging("7. Select user successfully")
    add_user_org_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["icon_add_user"])))
    add_user_org_default_approval_routes.click()
    Logging("8. Add user successfully")
    save_user_org_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["button_save_reviewers_approval"])))
    save_user_org_default_approval_routes.click()
    Logging("9. Save user successfully")
    click_save_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_save_default_approval_route"])))
    click_save_default_approval_routes.click()
    Logging("10. Save Default Approval Routes successfully")
    click_close_default_approval_routes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_close_default_approval_route"])))
    click_close_default_approval_routes.click()
    Logging("11. Close successfully")
    time.sleep(2)
    if 'Luu Luu Test' in driver.page_source :
        Logging(Green("=> 1. Default Approval Routes => ------------PASS"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["default_approval_routes_setting"]["pass"])
    else:
        Logging(Red("=> 1. Default Approval Routes => ------------ FAIL"))
        ValidateFailResultAndSystem("<div>[Approvals]Default Approval Routes</div>")
        TestCase_LogResult(**data["testcase_result"]["approval"]["default_approval_routes_setting"]["fail"])
    
    Logging("-------------Delete Default Approval Routes-Setting---------------")
    click_checkbox_all = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_check_all_approval_routes"])))
    click_checkbox_all.click()
    Logging("1. Click checkbox Delete Default Approval Routes successfully")
    time.sleep(1)
    click_btn_delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_delete_approval_routes"])))
    click_btn_delete.click()
    Logging("2. Click button Delete successfully")
    click_btn_confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_confirm"])))
    click_btn_confirm.click()
    Logging("3.Delete  Delete Default Approval Routes successfully")
    

def approval_manage_my_folder_setting(domain_name):
    Logging("------------- Manage My Folder---------------")
    click_manager_my_folder = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["setting_manager_my_folder"])))
    click_manager_my_folder.click()
    Logging("1. Click Manage My Folder successfully")
    time.sleep(1)
    click_my_folder = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_my_folder"])))
    click_my_folder.click()
    Logging("2. Click My Folder successfully")
    time.sleep(1)
    folder_name_approval = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_folder_name_approval"])))
    folder_name_approval.send_keys(data["approval"]["folder_name_approval"])
    Logging("3. Input Folder Name successfully")
    save_button_folder_approval = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_save_folder_approval"])))
    save_button_folder_approval.click()
    Logging("4. Click Button Save Folder successfully")
    time.sleep(2)
    if 'Hoa Giay' in driver.page_source :
        Logging(Green("=> 1. Add Manage My Folder => ------------PASS"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["manager_my_folder_setting"]["pass"])
    else:
        Logging(Red("=> 1. Add Manage My Folder => ------------ FAIL"))
        ValidateFailResultAndSystem("<div>[Approvals]Manage My Folder</div>")
        TestCase_LogResult(**data["testcase_result"]["approval"]["manager_my_folder_setting"]["fail"])
    Logging("-------------Delete Manage My Folder---------------")
    click_my_folder_delete = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_my_folder_delete"])))
    click_my_folder_delete.click()
    Logging("1. Click My Folder Delete successfully")
    click_icon_delete_my_folder = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["icon_delete_my_folder"])))
    click_icon_delete_my_folder.click()
    Logging("2. Click icon Delete My Folder successfully")
    Logging("=> Delete My Folder successfully")
    

def approval_display_setting(domain_name):
    
    Logging("-------------Display Settings ---------------")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_display_settings"])))
    element.location_once_scrolled_into_view
    time.sleep(2)
    click_display_settings = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_display_settings"])))
    click_display_settings.click()
    Logging("1. Click Display Settings successfully")
    
    '''
    click_org_elect_deputy_user = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["icon_org_select_deputy_user"]))).click()
    Logging("2. Click Select Deputy User successfully")
    search_org_user_deputy = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["search_user_deputy"])))
    search_org_user_deputy.send_keys(data["approval"]["user_search_org_approval"])
    search_org_user_deputy.send_keys(Keys.RETURN)
    time.sleep(1)
    Logging("3. Search user successfully")
    time.sleep(3)
    select_user_deputy = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_user_deputy"])))
    select_user_deputy.click()
    time.sleep(3)
    time.sleep(1)
    Logging("4. Select user Deputy successfully")
    '''

    click_org_user_with_permission_to_read = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_org_user_with_per_to_read"])))
    click_org_user_with_permission_to_read.click()
    Logging("5. Click Select Deputy User successfully")


    '''
    search_user_per_to_read = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_search_user_per_to_read"])))
    search_user_per_to_read.send_keys(data["approval"]["user_search_org_approval"])
    search_user_per_to_read.send_keys(Keys.RETURN)
    time.sleep(1)
    Logging("6. Search user Permission to read successfully")
    '''


    select_dept_per_to_read = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_dept_per_to_read"])))
    select_dept_per_to_read.click()
    select_user_per_to_read = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["select_user_to_read"])))
    select_user_per_to_read.click()
    add_user_per_to_read = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["icon_add_user_per_to_read"])))
    add_user_per_to_read.click()
    time.sleep(1)
    try:
        check_show_sub_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_show_sub_dept"])))
        if check_show_sub_dept.is_displayed():
            click_sub_dept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_ok_select_sub_dept"])))
            click_sub_dept.click()
            Logging("=> Select Sub Dept => --------PASS")
        else:
            Logging("=> Sub Dept not show  ")
            
    except WebDriverException:
        Logging("Not Show sub Dept ")
    Logging("7. Add user successfully")
    save_user_per_to_read = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_save_add_user_to_read"])))
    save_user_per_to_read.click()
    Logging("8. Save user successfully")
    get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["approval"]["txt_attach_signature_image"])))
    get_file.send_keys(luu_function.file_img)
    Logging("2. Attch Signature Image successfully")
    click_btn_save_signature_image = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_save_signature_image"])))
    click_btn_save_signature_image.click()
    Logging("3. Click Button save successfully")
    click_close_save_signature_image = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_close_signature"])))
    click_close_save_signature_image.click()
    Logging("4. Click Button Close successfully")
    time.sleep(1)
    check_signature_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["approval"]["check_data_signature_approval"])))
    if check_signature_image.is_displayed():
        Logging(Green("=> Change Signature Image  => --------PASS"))
        TestCase_LogResult(**data["testcase_result"]["approval"]["display_settings"]["pass"])
    else:
        Logging(Red("=> Change Signature Image  => --------FAIL"))
        ValidateFailResultAndSystem("<div>[Approvals]Change Signature Image</div>")
        TestCase_LogResult(**data["testcase_result"]["approval"]["display_settings"]["fail"])

    Logging("-------------Delete Display Settings ----------------")
    click_org_user_with_permission_to_read = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_org_user_with_per_to_read"])))
    click_org_user_with_permission_to_read.click()
    time.sleep(1)
    click_icon_delete_user_to_read = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["approval"]["click_icon_delete_user_per"])))
    click_icon_delete_user_to_read.click()
    save_user_per_to_read = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_save_add_user_to_read"])))
    save_user_per_to_read.click()
    click_icon_delete_signature_image = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["delete_signature_image"])))
    click_icon_delete_signature_image.click()
    Logging("1. Click Icon Delete successfully")
    click_btn_confirm_delete_signature_image = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_confirm_delete_signature"])))
    click_btn_confirm_delete_signature_image.click()
    Logging("2. Click Button Confirm successfully")
    Logging("=> Delete Signature Image  => --------PASS")
    click_btn_save_signature_image = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_save_signature_image"])))
    click_btn_save_signature_image.click()
    Logging("3. Click Button save successfully")
    click_close_save_signature_image = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["approval"]["btn_close_signature"])))
    click_close_save_signature_image.click()
    Logging("4. Click Button Close successfully")
    Logging("=> Delete Display Settings  => --------PASS")
    

def access_menu_approval(domain_name):
    admin = CheckPresenceOfAdminsubmenu(domain_name)

    '''
    if admin == True:
        try:
            approval_write_all_form(domain_name)
            Logging("Create all Form successfully")
        except WebDriverException:
            Logging("Fail to Create all Form")
        
    else:
        Logging("1.Write All Form => Account is not admin")
    '''

    if admin == True:
        try:
            approval_write_all_official_form(domain_name)
            Logging("Create All Official Form successfully")
        except WebDriverException:
            Logging("Fail to Create All Official Form")
        
    else:
        Logging("2.Write All Official Forms => Account is not admin")

    if admin == True:
        try:
            approval_view_all_approvals(domain_name)
            Logging("View All Approval  successfully")
        except WebDriverException:
            Logging("Fail to View All Approval ")
        
    else:
        Logging("3.View All Approvals => Account is not admin")

    if admin == True:
        try:
            approval_view_official_documentation(domain_name)
            Logging("View Official Documentation  successfully")
        except WebDriverException:
            Logging("Fail to Official Documentation ")
        
    else:
        Logging("4.View Official Documentation in Admin => Account is not admin")

    
    if admin == True:
        try:
            approval_arbitrary_decision(domain_name)
            Logging("Create Arbitrary Decision successfully")
        except WebDriverException:
            Logging("Fail to Arbitrary Decision ")
        
    else:
        Logging("5.Create Arbitrary Decision => Account is not admin")
    
    '''
    if admin == True:
        try:
            approval_change_approval_route(domain_name)
            Logging("Change Approval Route Admin successfully")
        except WebDriverException:
            Logging("Fail to Change Approval Route Admin ")
        
    else:
        Logging("6.Change Approval Route => Account is not admin")


    '''


    if admin == True:
        try:
            approval_default_approval_route(domain_name)
            Logging("Change Default Approval Routes Admin successfully")
        except WebDriverException:
            Logging("Fail to Default Approval Routes Admin ")
        
    else:
        Logging("7.Default Approval Routes in Admin => Account is not admin")


    if admin == True:
        try:
            approval_default_approval_route_setting(domain_name)
            Logging("Change Default Approval Routes Setting successfully")
        except WebDriverException:
            Logging("Fail to Default Approval Routes Setting ")
        
    else:
        Logging("User Change Default Approval Routes")
        try:
            approval_default_approval_route_setting(domain_name)
            Logging("Change Default Approval Routes Setting successfully")
        except WebDriverException:
            Logging("Fail to Default Approval Routes Setting ")



    if admin == True:
        try:
            approval_manage_my_folder_setting(domain_name)
            Logging("Create Manage My Folder successfully")
        except WebDriverException:
            Logging("Fail to Manage My Folder ")
        
    else:
        Logging("User create Manage My Folder")
        try:
            approval_manage_my_folder_setting(domain_name)
            Logging("Create Manage My Folder successfully")
        except WebDriverException:
            Logging("Fail to Manage My Folder ")


    if admin == True:
        try:
            approval_display_setting(domain_name)
            Logging("Create Display Settings successfully")
        except WebDriverException:
            Logging("Display Settings successfully ")
        
    else:
        Logging("User create Display Settings ")
        try:
            approval_display_setting(domain_name)
            Logging("Create Display Settings successfully")
        except WebDriverException:
            Logging("Display Settings successfully ")





    time.sleep(2)
    access_menu_home = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["screen_home_gw"])))
    access_menu_home.click()
    time.sleep(1)
    
time.sleep(3)

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
with open(os.path.dirname(Path(__file__).absolute())+'\\'+'luu_approval.txt','w') as approval:
    domain="http://qa.hanbiro.net"
    access_menu_approval(domain,approval)



result=open(os.path.dirname(Path(__file__).absolute())+'\\result.txt','r')
file_result=result.read()
Logging(file_result)
'''
  