import time, json, random
import logging
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException,NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from datetime import datetime
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from random import choice
#from random import randint
import re,sys
#from sys import exit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import pathlib
from pathlib import Path
import os
from sys import platform
import luu_log_in,luu_board_setting,luu_project_setting,luu_contact_setting,luu_approval_admin,luu_resource_add_category,luu_builder_setting_admin,luu_editor
from luu_function import execution_log, fail_log, error_log, Logging,testcase_log




def Luu_Execution(domain_name):
    error_menu = []
    #error_screenshot = []

    '''
    try:
        luu_log_in.log_in_domain(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("luu_log_in.log_in_domain")
    '''
    
    

    try:
        luu_board_setting.access_menu_board(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("luu_board_setting.access_menu_board")
    
    try:
        luu_project_setting.access_menu_project(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("luu_project_setting.access_menu_project")
    
    try:
        luu_contact_setting.access_menu_contact(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("luu_contact_setting.access_menu_contact")
    
    try:
        luu_approval_admin.access_menu_approval(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("luu_approval_admin.access_menu_approval")
    
    try:
        luu_resource_add_category.access_menu_resource(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("luu_resource_add_category.access_menu_resource")
    
    try:
        luu_builder_setting_admin.admin_menu_menubuilder(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("luu_builder_setting_admin.admin_menu_menubuilder")

    try:
        luu_builder_setting_admin.write_menu_menubuilder(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("luu_builder_setting_admin.write_menu_menubuilder")
    
    

    try:
        luu_editor.editor_menu_task(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("luu_editor.editor_menu_task")
    
    luu_log = {
        "execution_log": execution_log,
        "fail_log": fail_log,
        "error_log": error_log,
        "error_menu": error_menu
    }

    return luu_log

def Luu_My_Execution(domain_name):
    
    luu_log_in.log_in_domain(domain_name)
    luu_board_setting.access_menu_board(domain_name)
    #luu_project_setting.access_menu_project(domain_name)
    #luu_contact_setting.access_menu_contact(domain_name)
    #luu_approval_admin.access_menu_approval(domain_name)
    #luu_resource_add_category.access_menu_resource(domain_name)
    #luu_builder_setting_admin.admin_menu_menubuilder(domain_name)
    #luu_builder_setting_admin.write_menu_menubuilder(domain_name)
    #luu_editor.editor_menu_task(domain_name)


    luu_log = {
        "execution_log": execution_log,
        "fail_log": fail_log,
        "error_log": error_log
    }

    return luu_log
    

Luu_My_Execution("http://qavn.hanbiro.net/ngw/app/#")

