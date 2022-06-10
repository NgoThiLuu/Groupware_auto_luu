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
from luu_function import local, data, Logging, ValidateFailResultAndSystem,TestCase_LogResult,Red,Yellow,Green,Commands
from luu_function import driver


# Page


time.sleep(3)

def CheckPresenceOfAdminsubmenu(domain_name):
    Logging("------------------------------------------------------Menu Task------------------------------------------------------")
    driver.get(domain_name + "/task/diary/list/pdefault/")
    time.sleep(1)

    try:
        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_create_task"])))
        editor = True
    except WebDriverException:
        editor = False
    return editor


def editor_table_task(domain_name):
    

    Logging("------------------------------------------------------B. Editor - Menu Task------------------------------------------------------")
    #driver.get(domain_name + "/task/diary/list/pdefault/")
    try:
        click_btn_close_clock_in = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["menubuilder"]["btn_close_clock_in"])))
        click_btn_close_clock_in.click()
    except WebDriverException:
        Logging("Not show Clock In")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_create_task"])
    time.sleep(1)
    Logging("1. Click Create Task successfully")
    time.sleep(1)
    if 'Automatically saved file found' in driver.page_source :
        Commands.Wait10s_ClickElement(data["editor"]["show_noti_task_auto"])
        Logging("1. Click Automatically saved file found")
    else:
        Logging("2. Not show Automatically saved file found")

    time.sleep(1)
    Commands.Wait10s_InputElement(data["editor"]["txt_name_task"],data["editor"]["name_task"])
    time.sleep(1)
    Logging("2. Input Title Task successfully")
    time.sleep(1)

    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["content_editor_task"])
    driver.switch_to.default_content()
    time.sleep(2)
    Logging("3. Input Content Editor successfully")
    Commands.Wait10s_ClickElement(data["editor"]["click_table"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["click_table_2"])
    Commands.Wait10s_ClickElement(data["editor"]["click_column"])
    Logging("4. Create Table In Editor successfully")
    time.sleep(1)
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])

    count_line = int(len(driver.find_elements_by_xpath(data["editor"]["line_count"])))
    Logging("Total Row in Table:" + str(count_line))
   
    time.sleep(1)
    Logging("=========== Text Color -  Border width - Border style - Text format: bold/italic/underline ============ ")
    time.sleep(1)
    Commands.Wait10s_InputElement(data["editor"]["content_column1_row1"],data["editor"]["name_content_column1_row1"])
    Logging("5. Input Content Column 1- Row 1 In Editor successfully")
    Commands.Wait10s_ClickElement(data["editor"]["content_column2_row1"])
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["icon_txt_text_corlor"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["select_color_red"])
    Logging("5. Select Corlor => Pass")
    time.sleep(1)
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["bold_text"])
    Logging("Click Icon Bold => Pass")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["italic_text"])
    time.sleep(1)
    Logging("Click Icon Italic => Pass")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["underline_text"])
    time.sleep(1)
    Logging("Click Icon Underline => Pass")
    
    Commands.Wait10s_ClickElement(data["editor"]["click_table"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["table_properties"])
    Commands.Wait10s_clearElement(data["editor"]["txt_border_width_task"])
    #txt_border_width = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["txt_border_width_task"])))
    #txt_border_width.clear()
    #txt_border_width.send_keys(data["editor"]["number_border_width"])
    Commands.Wait10s_InputElement(data["editor"]["txt_border_width_task"],data["editor"]["number_border_width"])
    Logging("6. Input Border Width In Editor successfully")

    Commands.Wait10s_ClickElement(data["editor"]["table_properties_advanced"])
    Logging("7. Click tab Advanced Table Properties successfully")
    Commands.Wait10s_ClickElement(data["editor"]["list_select_border_style"])
    Commands.Wait10s_ClickElement(data["editor"]["select_border_style_soild"])
    Logging("8. Click tab Advanced Table Properties successfully")
    Commands.Wait10s_ClickElement(data["editor"]["click_btn_save_table_properties"])
    Logging("9. Set Table Properties successfully")
    Commands.Wait10s_ClickElement(data["editor"]["click_icon_align"])
    Commands.Wait10s_ClickElement(data["editor"]["select_align_center"])
    Logging("10. Select align Center successfully")
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement(data["editor"]["content_column2_row1"],data["editor"]["name_content_column2_row1"])
    time.sleep(1)
    Logging("6. Input Content Column 2- Row 1 In Editor successfully")

    Logging("===========  Insert Image  ============ ")
    Commands.Wait10s_ClickElement(data["editor"]["content_column3_row1"])
    driver.switch_to.default_content()
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["click_icon_align"])
    Commands.Wait10s_ClickElement(data["editor"]["select_align_center"])
    Logging("10. Select align Center successfully")
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement(data["editor"]["content_column3_row1"],data["editor"]["name_content_column3_row1"])
    time.sleep(1)
    Logging("7. Input Content Column 3- Row 1 In Editor successfully")
    Commands.Wait10s_ClickElement(data["editor"]["content_column3_row2"])
    driver.switch_to.default_content()
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["icon_insearch_image_editor"])
    Logging("11. Click icon Insert  successfully")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["insert_image_upload"])
    time.sleep(1)
    get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["drop_image_editor"])))
    get_file.send_keys(luu_function.file_img)
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_save_insert_image"])
    time.sleep(1)
    Logging("=> Upload  Image successfully")
    Logging("8. Input Content Column 3- Row 2 In Editor successfully")
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["content_column4_row1"])
    driver.switch_to.default_content()
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["click_icon_align"])
    Commands.Wait10s_ClickElement(data["editor"]["select_align_center"])
    Logging("10. Select align Center successfully")
    driver.switch_to.default_content()
    time.sleep(1)
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement(data["editor"]["content_column4_row1"],data["editor"]["name_content_column4_row1"])
    Logging("9. Input Content Column 4- Row 1 In Editor successfully")
    Logging("===========  Insert Link  ============ ")
    Commands.Wait10s_ClickElement(data["editor"]["content_column4_row2"])
    driver.switch_to.default_content()
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["icon_link_edit"])
    Logging("10. Click Icon Link successfully")
    Commands.Wait10s_InputElement(data["editor"]["txt_url_edit_table"],data["editor"]["name_url"])
    Logging("=> Input URL successfully")
    time.sleep(2)
    Commands.Wait10s_InputElement(data["editor"]["txt_to_display"],data["editor"]["name_text_to_display"])
    Logging("=> Input URL successfully")
    Commands.Wait10s_ClickElement(data["editor"]["btn_save_insert_link_table"])
    Logging("=> Click button save Insert Link successfully")
    Logging("10. Input Content Column 4- Row 2 In Editor successfully")
    Logging("===========  Insert Row After  ============ ")
    driver.execute_script("window.scrollTo(0, 100)")
    time.sleep(1)
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_ClickElement(data["editor"]["content_column4_row3"])
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["click_table"])
    Commands.Wait10s_ClickElement(data["editor"]["table_row"])
    Logging("11. Click value row successfully")
    Commands.Wait10s_ClickElement(data["editor"]["insert_row_after"])
    Logging("11. Click Insert Row After successfully")
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])

    count_line_insert = int(len(driver.find_elements_by_xpath(data["editor"]["line_count"])))
    Logging("Total Insert Row After:" + str(count_line_insert))
    time.sleep(1)

    if count_line_insert== count_line +1 :
        Logging(" ***  Total Insert Row After correctly")
    else:
        Logging(" Total Insert Row After => Fail ")

    time.sleep(1)

    Logging("=========== Row Properties: Background color - Border Color - Border style ============ ")
    Commands.Wait10s_ClickElement(data["editor"]["content_column1_row4"])
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(2)
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    #editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    #driver.switch_to.frame(editor_frame)
    Commands.Wait10s_InputElement(data["editor"]["content_column1_row4"],data["editor"]["name_content_column1_row4"])

    Logging("1. Input Content Column 4- Row 1 In Editor successfully")
    Commands.Wait10s_hold_moveElement(data["editor"]["content_column1_row4"],data["editor"]["content_column5_row4"])
    Logging("2. Highlight lines successfully")
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["click_table"])
    Commands.Wait10s_ClickElement(data["editor"]["table_row"])
    Logging("3. Click value row successfully")
    Commands.Wait10s_ClickElement(data["editor"]["row_properties"])
    Logging("4. Click Row properties successfully")
    Commands.Wait10s_ClickElement(data["editor"]["table_properties_advanced"])
    Logging("5. Click tab Advanced Table Properties successfully")
    Commands.Wait10s_ClickElement(data["editor"]["icon_background_color"])
    Logging("6. Click icon Background Color successfully")
    Commands.Wait10s_ClickElement(data["editor"]["select_color_light_blue_background"])
    Logging("7. Select Corlor => Pass")
    Commands.Wait10s_ClickElement(data["editor"]["list_select_border_style"])
    Commands.Wait10s_ClickElement(data["editor"]["select_border_style_soild"])
    Logging("8. Select Border style successfully")
    Commands.Wait10s_ClickElement(data["editor"]["icon_border_color"])
    Commands.Wait10s_ClickElement(data["editor"]["select_color_light_red_border"])
    Logging("9. Select Corlor => Pass")
    Commands.Wait10s_ClickElement(data["editor"]["click_btn_save_table_properties"])
    Logging("10. Click button Save Row Properties successfully")
    Logging("===========  Merge / Split cells  ============ ")
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])

    Commands.Wait10s_ClickElement(data["editor"]["content_column5_row2"])
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)
    Logging("1. Click  Column 5- Row 2 In Editor successfully")
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_hold_moveElement(data["editor"]["content_column5_row2"],data["editor"]["content_column5_row3"])
    Logging("2. Highlight lines successfully")
    driver.switch_to.default_content()
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["click_table"])
    Commands.Wait10s_ClickElement(data["editor"]["table_cell"])
    Logging("3. Click Table - Cells successfully")
    Commands.Wait10s_ClickElement(data["editor"]["merge_cells"])
    Logging("4. Click Merge cells successfully")
    Logging("=>  Merge cells successfully")
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["btn_save_task"])
    time.sleep(4)
    if 'Content Editor' in driver.page_source :
        Logging(Green("1. Create table in Editor successfully "))
        TestCase_LogResult(**data["testcase_result"]["editor"]["create_table"]["pass"])
    else:
        Logging(Red("2. Create table in Editor Fail"))
        ValidateFailResultAndSystem("<div>[Editor]1 : Table Performance</div>")
        TestCase_LogResult(**data["testcase_result"]["editor"]["create_table"]["fail"])
    


def editor_copy_paste_task(domain_name):
    Logging("===========  GW-630 : Copy paste  ============ ")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_more"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_modify"])
    Logging("1. Click button Modify successfully")
    time.sleep(1)
    if 'Automatically saved file found' in driver.page_source :
        Commands.Wait10s_ClickElement(data["editor"]["show_noti_task_auto"])
        Logging("1. Click Automatically saved file found")
    else:
        Logging("2. Not show Automatically saved file found")
    time.sleep(1)
  
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["content_editor_copy"])
    driver.switch_to.default_content()
    time.sleep(1)

    ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    time.sleep(1)
    Logging("2. Click  Ctrl + A key successfully")
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    time.sleep(1)
    Logging("3. Click  Ctrl + C key successfully")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_save_task"])
    time.sleep(4)
    Commands.Wait10s_ClickElement(data["editor"]["btn_create_task"])
    Logging("4. Click Create Task successfully")
    time.sleep(2)
    if 'Automatically saved file found' in driver.page_source :
        Commands.Wait10s_ClickElement(data["editor"]["show_noti_task_auto"])
        Logging("1. Click Automatically saved file found")
    else:
        Logging("2. Not show Automatically saved file found")
    time.sleep(1)
   
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["copy_task_new"])
    driver.switch_to.default_content()
    time.sleep(1)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)
    Logging("5. Click Ctrl + V key successfully")
    time.sleep(1)
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(1)
    Commands.Wait10s_InputElement(data["editor"]["txt_name_task"],data["editor"]["name_task_copy"])
    time.sleep(1)
    Logging("6. Input Title Task successfully")
    Commands.Wait10s_ClickElement(data["editor"]["btn_save_task"])
    time.sleep(4)
    if 'Editor Copy' in driver.page_source :
        Logging(Green("1. Copy table in Editor successfully "))
        TestCase_LogResult(**data["testcase_result"]["editor"]["copy_paste"]["pass"])
    else:
        Logging(Red("2. Copy table in Editor Fail"))
        ValidateFailResultAndSystem("<div>[Editor]2 : Copy paste</div>")
        TestCase_LogResult(**data["testcase_result"]["editor"]["copy_paste"]["fail"])
    
    

def editor_format_content(domain_name):    
    Logging("===========  GW-631 : Format content  ============ ")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_create_task"])
    Logging("4. Click Create Task successfully")
    time.sleep(1)
    if 'Automatically saved file found' in driver.page_source :
        Commands.Wait10s_ClickElement(data["editor"]["show_noti_task_auto"])
        Logging("1. Click Automatically saved file found")
    else:
        Logging("2. Not show Automatically saved file found")
    time.sleep(1)
    Commands.Wait10s_InputElement(data["editor"]["txt_name_task"],data["editor"]["title_format_editor"])
    Logging("2. Input Title Task successfully")
    time.sleep(1)
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    Logging("===========  Format [bold/italic/underline]  ============ ")
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["bold_text"])
    Logging("=> Click Icon Bold => Pass")
    Commands.Wait10s_ClickElement(data["editor"]["italic_text"])
    time.sleep(1)
    Logging("=> Click Icon Italic => Pass")
    Commands.Wait10s_ClickElement(data["editor"]["underline_text"])
    Logging("=> Click Icon Underline => Pass")
    time.sleep(1)
   
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["content0_format"])
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["click_tools"])
    Logging("=> Click Tool  => Pass")
    Commands.Wait10s_ClickElement(data["editor"]["click_source_code"])
    Logging("=> Click Source code  => Pass")
    time.sleep(3)
    if 'text-decoration: underline;' in driver.page_source :
        Logging("1. Format Format [bold/italic/underline] =>  PASS ")
    else:
        Logging("2. Format Format [bold/italic/underline] => FAIL ")
    time.sleep(3)
    Commands.Wait10s_ClickElement(data["editor"]["btn_cancel_source"])
    Logging("=> Click button cancel  => Pass")
    time.sleep(1)
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["bold_text"])
    time.sleep(1)
    Logging("=> Click Icon Bold => Pass")
    Commands.Wait10s_ClickElement(data["editor"]["italic_text"])
    Logging("=> Click Icon Italic => Pass")
    Commands.Wait10s_ClickElement(data["editor"]["underline_text"])
    Logging("=> Click Icon Underline => Pass")
    
    Logging("===========  Format Color Text  ============ ")
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["icon_txt_text_corlor"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["select_color_red"])
    Logging("5. Select Corlor => Pass")
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["content1_format"])
    time.sleep(1)
    Logging("=> Click Format Color Text => Pass")
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["click_tools"])
    Logging("=> Click Tool  => Pass")
    Commands.Wait10s_ClickElement(data["editor"]["click_source_code"])
    Logging("=> Click Source code  => Pass")
    time.sleep(1)
    if 'color: #e03e2d;' in driver.page_source :
        Logging(Green("1. Format Color Text =>  PASS "))
    else:
        Logging(Red("2. Format Color Text => FAIL "))

    click_btn_cancel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_cancel_source"]))).click()
    Logging("=> Click button cancel  => Pass")
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["icon_txt_text_corlor"])
    Commands.Wait10s_ClickElement(data["editor"]["select_color_back"])
    Logging("===========  Size Text  ============ ")
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["icon_font_size"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["font_size_text"])
    time.sleep(1)
    if '14pt' in driver.page_source :
        Logging("1. Select Size Text 14pt  successfully ")
    else:
        Logging("2. Select Size Text 14pt Fail ")
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["content2_format"])
    Logging("=> Click Size Text  => Pass")
    
    Logging("===========  Font style  ============ ")
    time.sleep(1)
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["click_icon_font_style"])
    Commands.Wait10s_ClickElement(data["editor"]["select_font_style"])
    time.sleep(1)
    if 'Times New' in driver.page_source :
        Logging(Green("1. Select Font style Times New Roman  successfully "))
    else:
        Logging(Red("2. Select Font style Times New Roman Fail "))
    time.sleep(3)
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["content3_format"])
    time.sleep(1)
    Logging("=> Click Font style  => Pass")

    Logging("===========  Alignment  ============ ")
    driver.switch_to.default_content()
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["click_icon_align"])
    Commands.Wait10s_ClickElement(data["editor"]["select_align_center"])
    Logging("1. Select align Center successfully")
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["content4_format"])
    Logging("2. Input data Content Alignment successfully")
    time.sleep(1)
    Logging("=> Click Alignment  => Pass")
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["click_tools"])
    time.sleep(1)
    Logging("=> Click Tool  => Pass")
    Commands.Wait10s_ClickElement(data["editor"]["click_source_code"])
    Logging("=> Click Source code  => Pass")
    time.sleep(1)
    if 'text-align: center' in driver.page_source :
        Logging(Green("1. Select Alignment Center =>  PASS "))
    else:
        Logging(Red("2. Select Alignment Center => FAIL "))
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_cancel_source"])
    Logging("=> Click button cancel  => Pass")
    time.sleep(1)


    Logging("===========  Line spacing  ============ ")
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["click_icon_align"])
    Commands.Wait10s_ClickElement(data["editor"]["select_align_left"])
    Commands.Wait10s_ClickElement(data["editor"]["icon_line_height"])
    Commands.Wait10s_ClickElement(data["editor"]["select_line_height12"])
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    time.sleep(1)
    content_input.send_keys(data["editor"]["content5_format"])
    content_input.send_keys(Keys.RETURN)
    driver.switch_to.default_content()
    Logging("3. Input Content Editor successfully")
    Logging("=> Click Line spacing  => Pass")
    
    Logging("===========  Background Color Text  ============ ")
    time.sleep(1)
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["icon_backgr_color_text"])
    Logging("1. Click Icon Background Color successfully")
    Commands.Wait10s_ClickElement(data["editor"]["select_color_red"])
    Logging("2. Select Color successfully")

    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["content8_format"])
    driver.switch_to.default_content()
    Logging("3. Input Content Editor successfully")
    Logging("=> Background Color Text  => Pass")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["click_tools"])
    Logging("=> Click Tool  => Pass")
    Commands.Wait10s_ClickElement(data["editor"]["click_source_code"])
    Logging("=> Click Source code  => Pass")
    time.sleep(1)
    if 'background-color: #e03e2d' in driver.page_source :
        Logging("1. Select Background Color Text =>  PASS ")
    else:
        Logging("2. Select Background Color Text => FAIL ")
    
    Commands.Wait10s_ClickElement(data["editor"]["btn_cancel_source"])
    time.sleep(1)
    Logging("=> Click button cancel  => Pass")
    
    Commands.Wait10s_ClickElement(data["editor"]["icon_backgr_color_text"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["select_color_write"])
    time.sleep(1)

    Logging("===========  Check box  ============ ")
    time.sleep(1)
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["icon_insert_checklist"])
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["content6_format"])
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["icon_insert_checklist"])
    Logging("=> Click Check box  => Pass")
    
    Logging("===========  Numbered/Bulletin List  ============ ")
    time.sleep(1)
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["icon_insert_numbered_list"])
    Commands.Wait10s_ClickElement(data["editor"]["select_numbered_list_abc"])
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["content7_format"])
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["icon_uncheck_numbered_list"])
    Logging("=> Click Numbered List  => Pass")
    Logging("=========== Formats Heading  ============ ")
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["btn_format_editor"])
    Logging("1. Click Format in Editor successfully")
    Commands.Wait10s_ClickElement(data["editor"]["select_value_formats"])
    Logging("2. Select Value Formats successfully")
    Commands.Wait10s_ClickElement(data["editor"]["select_value_headings"])
    Logging("3. Select Value Heading successfully")
    Commands.Wait10s_ClickElement(data["editor"]["select_headings_1"])
    Logging("4. Select Value Heading 1 successfully")
    driver.execute_script("window.scrollTo(0, 100)")
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["content9_format"])
    driver.switch_to.default_content()
    Logging("=========== Emoticons  ============ ")
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["select_icon_emoticons"])
    Logging("1. Click icon Emoticons successfully")
    Commands.Wait10s_ClickElement(data["editor"]["select_icon_100"])
    Logging("2. Select value  Emoticons successfully")
    time.sleep(1)
    if '100' in driver.page_source :
        Logging("1. Emoticons successfully ")
    else:
        Logging("2. Emoticons Fail ")
    time.sleep(1)

    Logging("=========== Format-Strikethrough/Superscript/Subscript  ============ ")
    driver.switch_to.default_content()
    Commands.Wait10s_ClickElement(data["editor"]["click_format"])
    Logging("1. Click tab Format successfully")
    Commands.Wait10s_ClickElement(data["editor"]["click_strikethrough"])
    Logging("1. Click Strikethrough successfully")
    driver.execute_script("window.scrollTo(0, 100)")
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    Commands.Wait10s_InputElement_return(data["editor"]["input_editor_tynmce"],data["editor"]["content10_format"])
    driver.switch_to.default_content()
    time.sleep(1)
    Logging("===========  Edit image size and position  ============ ")
    driver.switch_to.default_content()
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["icon_insearch_image_editor"])
    Logging("11. Click icon Insert  successfully")
    Commands.Wait10s_ClickElement(data["editor"]["insert_image_upload"])
    get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["drop_image_editor"])))
    get_file.send_keys(luu_function.file_img)
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_save_insert_image"])
    time.sleep(1)
    Logging("=> Upload  Image successfully")
    driver.execute_script("window.scrollTo(0, 100)")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["icon_insearch_image_editor"])
    Logging("11. Click icon Insert  successfully")
    Commands.Wait10s_clearElement(data["editor"]["txt_width"])
    Commands.Wait10s_InputElement(data["editor"]["txt_width"],data["editor"]["number_width"])
    Logging("=> Input number width successfully")
    Commands.Wait10s_ClickElement(data["editor"]["table_properties_advanced"])
    Logging("7. Click tab Advanced Table Properties successfully")
    Commands.Wait10s_ClickElement(data["editor"]["list_select_border_style"])
    Commands.Wait10s_ClickElement(data["editor"]["select_border_style_soild"])
    Logging("8. Click tab Advanced Table Properties successfully")
    Commands.Wait10s_clearElement(data["editor"]["txt_border_width"])
    Commands.Wait10s_InputElement(data["editor"]["txt_border_width"],data["editor"]["number_border_width_image"])
    Logging("=> Input Border width successfully")
    Commands.Wait10s_ClickElement(data["editor"]["btn_save_insert_image"])
    time.sleep(3)
    Logging("===========  Full Screen  ============ ")
    Commands.Wait10s_ClickElement(data["editor"]["btn_full_screen"])
    Commands.Wait10s_ClickElement(data["editor"]["btn_full_screen"])
    Logging("=> Click Full Screen Editor successfully")
    Commands.Wait10s_ClickElement(data["editor"]["btn_save_task"])
    time.sleep(5)
    if 'Format content Editor' in driver.page_source :
        Logging("=>  Format content successfully ")
        TestCase_LogResult(**data["testcase_result"]["editor"]["format_content"]["pass"])
    else:
        Logging("=>  Format content Fail")
        ValidateFailResultAndSystem("<div>[Editor]2 : Format content</div>")
        TestCase_LogResult(**data["testcase_result"]["editor"]["format_content"]["fail"])
    
    
def editor_upload_office_file(domain_name):
    Logging("===========  GW-633 : Upload office file  ============ ")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_create_task"])
    Logging("4. Click Create Task successfully")
    time.sleep(1)
    if 'Automatically saved file found' in driver.page_source :
        Commands.Wait10s_ClickElement(data["editor"]["show_noti_task_auto"])
        Logging("1. Click Automatically saved file found")
    else:
        Logging("2. Not show Automatically saved file found")
    Commands.Wait10s_InputElement(data["editor"]["txt_name_task"],data["editor"]["title_upload_office_file"])
    time.sleep(1)
    Logging("2. Input Title Task successfully")
    Commands.Wait10s_ClickElement(data["editor"]["btn_view_office_file_html"])
    time.sleep(2)
    select_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["add_form_office"])))
    select_file.send_keys(luu_function.file_editor)
    time.sleep(2)
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    driver.find_element_by_xpath("//body[@id='tinymce']")   
    driver.switch_to.default_content()
    time.sleep(3)
    Commands.Wait10s_ClickElement(data["editor"]["btn_save_task"])
    time.sleep(5)

    if 'Upload office file' in driver.page_source :
        Logging("1. Upload office file successfully ")
        TestCase_LogResult(**data["testcase_result"]["editor"]["upload_office_file"]["pass"])
    else:
        Logging("2. Upload office file Fail ")
        ValidateFailResultAndSystem("<div>[Editor]2 : Upload office file</div>")
        TestCase_LogResult(**data["testcase_result"]["editor"]["upload_office_file"]["fail"])
    time.sleep(1)


def editor_rotate_clockwise_image(domain_name):
    Logging("===========  Rotate clockwise image ============ ")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_create_task"])
    time.sleep(1)
    Logging("4. Click Create Task successfully")
    
    if 'Automatically saved file found' in driver.page_source :
        Commands.Wait10s_ClickElement(data["editor"]["show_noti_task_auto"])
        Logging("1. Click Automatically saved file found")
    else:
        Logging("2. Not show Automatically saved file found")
    Commands.Wait10s_InputElement(data["editor"]["txt_name_task"],data["editor"]["title_image_rotate"])
    Logging("2. Input Title Task successfully")
    Commands.SwitchToFrame_no(data["editor"]["input_editor"])
    driver.find_element_by_xpath("//body[@id='tinymce']")
    driver.switch_to.default_content()
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["icon_insearch_image_editor"])
    Logging("11. Click icon Insert  successfully")
    Commands.Wait10s_ClickElement(data["editor"]["insert_image_upload"])
    time.sleep(1)
    get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["drop_image_editor"])))
    get_file.send_keys(luu_function.file_img)
    time.sleep(2)
    Commands.Wait10s_ClickElement(data["editor"]["btn_save_insert_image"])
    Logging("=> Upload  Image successfully")
    Commands.Wait10s_ClickElement(data["editor"]["icon_rotate_clockwise"])
    Logging("=> Click Icon Rotate clockwise successfully")
    Commands.Wait10s_ClickElement(data["editor"]["btn_save_task"])
    time.sleep(4)

    if 'Editor Rotate clockwise' in driver.page_source :
        Logging(Green("1. Rotate clockwise image successfully "))
        TestCase_LogResult(**data["testcase_result"]["editor"]["rotate_clockwise_image"]["pass"])
    else:
        Logging(Red("2. Rotate clockwise image Fail "))
        TestCase_LogResult(**data["testcase_result"]["editor"]["rotate_clockwise_image"]["fail"])

    Logging("===========  Delete Task Editor  ============ ")
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_back_task"])
    driver.refresh()
    time.sleep(6)
    Commands.Wait10s_ClickElement(data["editor"]["checkbox_all"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_more"])
    time.sleep(1)
    Commands.Wait10s_ClickElement(data["editor"]["btn_delete"])
    time.sleep(1)
    Logging("8. Click button Delete successfully")
    Commands.Wait10s_ClickElement(data["editor"]["btn_ok_delete_task"])
    Logging("9. Delete Task Editor successfully")
    time.sleep(1)

    driver.quit()
    
    
time.sleep(1)

def editor_menu_task(domain_name):
    editor = CheckPresenceOfAdminsubmenu(domain_name)
    
    
    if editor == True:
        try:
            editor_table_task(domain_name)
            Logging("create table successfully")
        except WebDriverException:
            Logging("fail to Editor ")
        
    else:
        Logging("Can not Create Editor")

    if editor == True:
        try:
            editor_copy_paste_task(domain_name)
            Logging("Copy-Paste successfully")
        except WebDriverException:
            Logging("fail to Editor ")
        
    else:
        Logging("Can not Create Editor")
    
    if editor == True:
        try:
            editor_format_content(domain_name)
            Logging("Format Content successfully")
        except WebDriverException:
            Logging("fail to Editor ")
        
    else:
        Logging("Can not Create Editor")

    
    if editor == True:
        try:
            editor_upload_office_file(domain_name)
            Logging("Upload Office file successfully")
        except WebDriverException:
            Logging("fail to Editor ")
        
    else:
        Logging("Can not Create Editor")
    
    if editor == True:
        try:
            editor_rotate_clockwise_image(domain_name)
            Logging("Rotate clockwise image successfully")
        except WebDriverException:
            Logging("fail to Editor ")
        
    else:
        Logging("Can not Create Editor")

    



def is_Displayed(xpath):
    '''
    try:
        driver.find_elements_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
    '''

def so(total):
    num = re.sub(r'\D', "", total)
    return int(num)




    

#editor_menu_task()

