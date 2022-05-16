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
from luu_function import local, data, Logging, ValidateFailResultAndSystem,TestCase_LogResult
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
    click_btn_create_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_create_task"])))
    click_btn_create_task.click()
    time.sleep(1)
    Logging("1. Click Create Task successfully")
    time.sleep(1)
    if 'Automatically saved file found' in driver.page_source :
        click_btn_delete_auto_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["show_noti_task_auto"])))
        click_btn_delete_auto_task.click()
        Logging("1. Click Automatically saved file found")
    else:
        Logging("2. Not show Automatically saved file found")

    time.sleep(1)
    txt_title_name_task = driver.find_element_by_xpath(data["editor"]["txt_name_task"])
    txt_title_name_task.send_keys(data["editor"]["name_task"])
    time.sleep(1)
    Logging("2. Input Title Task successfully")
    time.sleep(1)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    content_input.send_keys(data["editor"]["content_editor_task"])
    content_input.send_keys(Keys.RETURN)
    driver.switch_to.default_content()
    time.sleep(2)
    Logging("3. Input Content Editor successfully")
    
    click_table_editor = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_table"])))
    click_table_editor.click()
    time.sleep(1)
    click_value_table = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_table_2"])))
    click_value_table.click()
    click_column_row = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_column"])))
    click_column_row.click()
    Logging("4. Create Table In Editor successfully")
    time.sleep(1)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    count_line = int(len(driver.find_elements_by_xpath(data["editor"]["line_count"])))
    Logging("Total Row in Table:" + str(count_line))
    time.sleep(1)
    Logging("=========== Text Color -  Border width - Border style - Text format: bold/italic/underline ============ ")
    time.sleep(1)
    content1_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column1_row1"])))
    content1_input.send_keys(data["editor"]["name_content_column1_row1"])
    Logging("5. Input Content Column 1- Row 1 In Editor successfully")
    content2_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column2_row1"])))
    content2_input.click()
    
    driver.switch_to.default_content()
    icon_color_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_txt_text_corlor"])))
    icon_color_text.click()
    time.sleep(1)
    select_color_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_color_red"])))
    select_color_text.click()
    Logging("5. Select Corlor => Pass")

    time.sleep(1)
    driver.switch_to.default_content()
    icon_color_bold = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["bold_text"])))
    icon_color_bold.click()
   
    Logging("Click Icon Bold => Pass")
    time.sleep(1)
    icon_color_italic = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["italic_text"])))
    icon_color_italic.click()
    time.sleep(1)
    Logging("Click Icon Italic => Pass")
    time.sleep(1)
    icon_color_underline = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["underline_text"])))
    icon_color_underline.click()
    time.sleep(1)
    Logging("Click Icon Underline => Pass")
    

    click_table_editor = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_table"])))
    click_table_editor.click()
    time.sleep(1)
    click_table_properties = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["table_properties"])))
    click_table_properties.click()
    txt_border_width = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["txt_border_width_task"])))
    txt_border_width.clear()
    txt_border_width.send_keys(data["editor"]["number_border_width"])
    Logging("6. Input Border Width In Editor successfully")
    click_tab_advanced_table = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["table_properties_advanced"])))
    click_tab_advanced_table.click()
    Logging("7. Click tab Advanced Table Properties successfully")
    click_border_style_list = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["list_select_border_style"])))
    click_border_style_list.click()
    select_border_style_list = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_border_style_soild"])))
    select_border_style_list.click()
    Logging("8. Click tab Advanced Table Properties successfully")
    btn_save_table_prroperties = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_btn_save_table_properties"])))
    btn_save_table_prroperties.click()
    Logging("9. Set Table Properties successfully")
    click_align_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_icon_align"])))
    click_align_text.click()
    select_align_center = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_align_center"])))
    select_align_center.click()
    Logging("10. Select align Center successfully")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content2a_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column2_row1"])))
    content2a_input.send_keys(data["editor"]["name_content_column2_row1"])
    time.sleep(1)
    Logging("6. Input Content Column 2- Row 1 In Editor successfully")

    Logging("===========  Insert Image  ============ ")

    content3_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column3_row1"])))
    content3_input.click()
    driver.switch_to.default_content()
    time.sleep(1)
    click_align_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_icon_align"])))
    click_align_text.click()
    select_align_center = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_align_center"])))
    select_align_center.click()
    Logging("10. Select align Center successfully")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content3_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column3_row1"])))
    content3_input.send_keys(data["editor"]["name_content_column3_row1"])
    time.sleep(1)
    Logging("7. Input Content Column 3- Row 1 In Editor successfully")
    content3_tr2_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column3_row2"])))
    content3_tr2_input.click()
    driver.switch_to.default_content()
    time.sleep(1)
    icon_insert_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_insearch_image_editor"])))
    icon_insert_image.click()
    Logging("11. Click icon Insert  successfully")
    time.sleep(1)
    icon_fd_upload_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["insert_image_upload"])))
    icon_fd_upload_image.click()
    time.sleep(1)
    get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["drop_image_editor"])))
    get_file.send_keys(luu_function.file_img)
    time.sleep(1)
    btn_save_upload_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_save_insert_image"])))
    btn_save_upload_image.click()
    time.sleep(1)
    Logging("=> Upload  Image successfully")
    Logging("8. Input Content Column 3- Row 2 In Editor successfully")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    time.sleep(1)
    content4_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column4_row1"])))
    content4_input.click()
    driver.switch_to.default_content()
    time.sleep(1)
    click_align_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_icon_align"])))
    click_align_text.click()
    select_align_center = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_align_center"])))
    select_align_center.click()
    Logging("10. Select align Center successfully")
    driver.switch_to.default_content()
    time.sleep(1)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content4_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column4_row1"])))
    content4_input.send_keys(data["editor"]["name_content_column4_row1"])
    Logging("9. Input Content Column 4- Row 1 In Editor successfully")
    Logging("===========  Insert Link  ============ ")
    content4_tr2_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column4_row2"])))
    content4_tr2_input.click()
    driver.switch_to.default_content()
    time.sleep(1)
    click_icon_link = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_link_edit"])))
    click_icon_link.click()
    Logging("10. Click Icon Link successfully")
    txt_input_url = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["txt_url_edit_table"])))
    txt_input_url.send_keys(data["editor"]["name_url"])
    Logging("=> Input URL successfully")
    time.sleep(2)
    txt_url_display = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["txt_to_display"])))
    txt_url_display.send_keys(data["editor"]["name_text_to_display"])
    Logging("=> Input URL successfully")
    btn_save_ensert_link = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_save_insert_link_table"])))
    btn_save_ensert_link.click()
    Logging("=> Click button save Insert Link successfully")
    Logging("10. Input Content Column 4- Row 2 In Editor successfully")
    Logging("===========  Insert Row After  ============ ")
    driver.execute_script("window.scrollTo(0, 100)")
    time.sleep(1)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content4_col4_tr3 = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column4_row3"])))
    content4_col4_tr3.click()
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)
    click_table_editor = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_table"])))
    click_table_editor.click()
    click_table_row = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["table_row"])))
    click_table_row.click()
    Logging("11. Click value row successfully")
    click_insert_row_after = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["insert_row_after"])))
    click_insert_row_after.click()
    Logging("11. Click Insert Row After successfully")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    count_line_insert = int(len(driver.find_elements_by_xpath(data["editor"]["line_count"])))
    Logging("Total Insert Row After:" + str(count_line_insert))
    time.sleep(1)

    if count_line_insert== count_line +1 :
        Logging(" ***  Total Insert Row After correctly")
    else:
        Logging(" Total Insert Row After => Fail ")

    
    #driver.switch_to.default_content()
    time.sleep(1)

    Logging("=========== Row Properties: Background color - Border Color - Border style ============ ")

    column1_row4_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column1_row4"])))
    column1_row4_input.click()
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    column1_row4_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column1_row4"])))
    column1_row4_input.send_keys(data["editor"]["name_content_column1_row4"])
    Logging("1. Input Content Column 4- Row 1 In Editor successfully")
    tr4_td_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column1_row4"])))
    tr4_td_5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column5_row4"])))
    webdriver.ActionChains(driver).click_and_hold(tr4_td_1).move_to_element(tr4_td_5).perform()
    webdriver.ActionChains(driver).release().perform()
    Logging("2. Highlight lines successfully")
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)
    click_table_editor = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_table"])))
    click_table_editor.click()
    click_table_row = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["table_row"])))
    click_table_row.click()
    Logging("3. Click value row successfully")
    click_row_properties = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["row_properties"])))
    click_row_properties.click()
    Logging("4. Click Row properties successfully")
    click_tab_advanced_table = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["table_properties_advanced"])))
    click_tab_advanced_table.click()
    Logging("5. Click tab Advanced Table Properties successfully")
    click_icon_background_color = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_background_color"])))
    click_icon_background_color.click()
    Logging("6. Click icon Background Color successfully")
    select_background_color = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_color_light_blue_background"])))
    select_background_color.click()
    Logging("7. Select Corlor => Pass")
    click_border_style_list = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["list_select_border_style"])))
    click_border_style_list.click()
    select_border_style_list = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_border_style_soild"])))
    select_border_style_list.click()
    Logging("8. Select Border style successfully")
    click_border_color = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_border_color"])))
    click_border_color.click()
    select_border_color = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_color_light_red_border"])))
    select_border_color.click()
    Logging("9. Select Corlor => Pass")
    btn_save_row_prroperties = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_btn_save_table_properties"])))
    btn_save_row_prroperties.click()
    Logging("10. Click button Save Row Properties successfully")
    Logging("===========  Merge / Split cells  ============ ")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    column5_row2_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column5_row2"])))
    column5_row2_input.click()
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)
    Logging("1. Click  Column 5- Row 2 In Editor successfully")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    tr2_td_5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column5_row2"])))
    tr3_td_5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["content_column5_row3"])))
    webdriver.ActionChains(driver).click_and_hold(tr2_td_5).move_to_element(tr3_td_5).perform()
    webdriver.ActionChains(driver).release().perform()
    Logging("2. Highlight lines successfully")
    driver.switch_to.default_content()
    time.sleep(1)
    click_table_editor = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_table"])))
    click_table_editor.click()
    click_table_cells = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["table_cell"])))
    click_table_cells.click()
    Logging("3. Click Table - Cells successfully")
    click_merge_cells = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["merge_cells"])))
    click_merge_cells.click()
    Logging("4. Click Merge cells successfully")
    Logging("=>  Merge cells successfully")
    driver.switch_to.default_content()
    click_btn_save_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_save_task"])))
    click_btn_save_task.click()
    time.sleep(4)
    if 'Content Editor' in driver.page_source :
        Logging("1. Create table in Editor successfully ")
        TestCase_LogResult(**data["testcase_result"]["editor"]["create_table"]["pass"])
    else:
        Logging("2. Create table in Editor successfully")
        ValidateFailResultAndSystem("<div>[Editor]1 : Table Performance</div>")
        TestCase_LogResult(**data["testcase_result"]["editor"]["create_table"]["fail"])
    


def editor_copy_paste_task(domain_name):
    Logging("===========  GW-630 : Copy paste  ============ ")
    time.sleep(1)
    click_btn_more = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_more"])))
    click_btn_more.click()
    time.sleep(1)
    click_btn_edit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_modify"])))
    click_btn_edit.click()
    Logging("1. Click button Modify successfully")
    time.sleep(1)
    if 'Automatically saved file found' in driver.page_source :
        click_btn_delete_auto_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["show_noti_task_auto"])))
        click_btn_delete_auto_task.click()
        Logging("1. Click Automatically saved file found")
    else:
        Logging("2. Not show Automatically saved file found")
    time.sleep(1)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    content_input.send_keys(data["editor"]["content_editor_copy"])
    content_input.send_keys(Keys.RETURN)
    driver.switch_to.default_content()
    time.sleep(1)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    time.sleep(1)
    Logging("2. Click  Ctrl + A key successfully")
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    time.sleep(1)
    Logging("3. Click  Ctrl + C key successfully")
    time.sleep(1)
    click_btn_save_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_save_task"])))
    click_btn_save_task.click()
    time.sleep(4)
    click_btn_create_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_create_task"])))
    click_btn_create_task.click()
    Logging("4. Click Create Task successfully")
    time.sleep(2)
    if 'Automatically saved file found' in driver.page_source :
        click_btn_delete_auto_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["show_noti_task_auto"])))
        click_btn_delete_auto_task.click()
        Logging("1. Click Automatically saved file found")
    else:
        Logging("2. Not show Automatically saved file found")
    time.sleep(1)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    content_input.send_keys(data["editor"]["copy_task_new"])
    content_input.send_keys(Keys.RETURN)
    driver.switch_to.default_content()
    time.sleep(1)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)
    Logging("5. Click Ctrl + V key successfully")
    time.sleep(1)
    driver.execute_script("window.scrollTo(100, 0)")
    time.sleep(1)
    txt_title_name_task = driver.find_element_by_xpath(data["editor"]["txt_name_task"])
    txt_title_name_task.send_keys(data["editor"]["name_task_copy"])
    time.sleep(1)
    Logging("6. Input Title Task successfully")
    click_btn_save_task = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_save_task"])))
    click_btn_save_task.click()
    time.sleep(4)
    if 'Editor Copy' in driver.page_source :
        Logging("1. Copy table in Editor successfully ")
        TestCase_LogResult(**data["testcase_result"]["editor"]["copy_paste"]["pass"])
    else:
        Logging("2. Copy table in Editor successfully")
        ValidateFailResultAndSystem("<div>[Editor]2 : Copy paste</div>")
        TestCase_LogResult(**data["testcase_result"]["editor"]["copy_paste"]["fail"])
    
    

def editor_format_content(domain_name):    
    Logging("===========  GW-631 : Format content  ============ ")
    time.sleep(1)
    click_btn_create_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_create_task"])))
    click_btn_create_task.click()
    
    Logging("4. Click Create Task successfully")
    time.sleep(1)
    if 'Automatically saved file found' in driver.page_source :
        click_btn_delete_auto_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["show_noti_task_auto"])))
        click_btn_delete_auto_task.click()
        Logging("1. Click Automatically saved file found")
    else:
        Logging("2. Not show Automatically saved file found")
    time.sleep(1)
    txt_title_name_task = driver.find_element_by_xpath(data["editor"]["txt_name_task"])
    txt_title_name_task.send_keys(data["editor"]["title_format_editor"])
    Logging("2. Input Title Task successfully")
    time.sleep(1)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    Logging("===========  Format [bold/italic/underline]  ============ ")
    driver.switch_to.default_content()
    icon_color_bold = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["bold_text"])))
    icon_color_bold.click()
    Logging("=> Click Icon Bold => Pass")
    icon_color_italic = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["italic_text"])))
    icon_color_italic.click()
    time.sleep(1)
    Logging("=> Click Icon Italic => Pass")
    icon_color_underline = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["underline_text"])))
    icon_color_underline.click()
    Logging("=> Click Icon Underline => Pass")
    time.sleep(1)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    content_input.send_keys(data["editor"]["content0_format"])
    content_input.send_keys(Keys.RETURN)
    driver.switch_to.default_content()
    click_tools = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_tools"])))
    click_tools.click()
    Logging("=> Click Tool  => Pass")
    click_source_code = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_source_code"])))
    click_source_code.click()
    Logging("=> Click Source code  => Pass")
    time.sleep(3)
    if 'text-decoration: underline;' in driver.page_source :
        Logging("1. Format Format [bold/italic/underline] =>  PASS ")
    else:
        Logging("2. Format Format [bold/italic/underline] => FAIL ")
    time.sleep(3)
    click_btn_cancel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_cancel_source"])))
    click_btn_cancel.click()
    Logging("=> Click button cancel  => Pass")
    time.sleep(1)
    driver.switch_to.default_content()
    icon_color_bold = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["bold_text"])))
    icon_color_bold.click()
    time.sleep(1)
    Logging("=> Click Icon Bold => Pass")
    icon_color_italic = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["italic_text"])))
    icon_color_italic.click()
    Logging("=> Click Icon Italic => Pass")
    icon_color_underline = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["underline_text"])))
    icon_color_underline.click()
    Logging("=> Click Icon Underline => Pass")
    
    Logging("===========  Format Color Text  ============ ")
    driver.switch_to.default_content()
    icon_color_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_txt_text_corlor"])))
    icon_color_text.click()
    time.sleep(1)
    select_color_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_color_red"])))
    select_color_text.click() 
    Logging("5. Select Corlor => Pass")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    content_input.send_keys(data["editor"]["content1_format"])
    content_input.send_keys(Keys.RETURN)
    time.sleep(1)
    Logging("=> Click Format Color Text => Pass")
    driver.switch_to.default_content()
    click_tools = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_tools"])))
    click_tools.click()
    Logging("=> Click Tool  => Pass")
    click_source_code = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_source_code"])))
    click_source_code.click()
    Logging("=> Click Source code  => Pass")
    time.sleep(1)
    if 'color: #e03e2d;' in driver.page_source :
        Logging("1. Format Color Text =>  PASS ")
    else:
        Logging("2. Format Color Text => FAIL ")
    click_btn_cancel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_cancel_source"]))).click()
    Logging("=> Click button cancel  => Pass")
    driver.switch_to.default_content()
    icon_color_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_txt_text_corlor"])))
    icon_color_text.click()
    select_color_text_black = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_color_back"])))
    select_color_text_black.click()
    Logging("===========  Size Text  ============ ")
    driver.switch_to.default_content()
    icon_font_size_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_font_size"])))
    icon_font_size_text.click()
    time.sleep(1)
    select_font_size_text= WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["font_size_text"])))
    select_font_size_text.click()
    time.sleep(1)
    if '14pt' in driver.page_source :
        Logging("1. Select Size Text 14pt  successfully ")
    else:
        Logging("2. Select Size Text 14pt Fail ")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    content_input.send_keys(data["editor"]["content2_format"])
    content_input.send_keys(Keys.RETURN)
    Logging("=> Click Size Text  => Pass")
    

    Logging("===========  Font style  ============ ")
    time.sleep(1)
    driver.switch_to.default_content()
    icon_font_style = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_icon_font_style"])))
    icon_font_style.click()
    select_font_style= WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_font_style"])))
    select_font_style.click()
    time.sleep(1)
    if 'Times New' in driver.page_source :
        Logging("1. Select Font style Times New Roman  successfully ")
    else:
        Logging("2. Select Font style Times New Roman Fail ")
    time.sleep(3)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    content_input.send_keys(data["editor"]["content3_format"])
    content_input.send_keys(Keys.RETURN)
    time.sleep(1)
    Logging("=> Click Font style  => Pass")

    Logging("===========  Alignment  ============ ")
    driver.switch_to.default_content()
    time.sleep(1)
    click_align_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_icon_align"])))
    click_align_text.click()
    select_align_center = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_align_center"])))
    select_align_center.click()
    Logging("1. Select align Center successfully")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    time.sleep(1)
    content_input.send_keys(data["editor"]["content4_format"])
    content_input.send_keys(Keys.RETURN)
    Logging("2. Input data Content Alignment successfully")
    time.sleep(1)
    Logging("=> Click Alignment  => Pass")
    driver.switch_to.default_content()
    click_tools = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_tools"])))
    click_tools.click()
    time.sleep(1)
    Logging("=> Click Tool  => Pass")
    click_source_code = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_source_code"])))
    click_source_code.click()
    Logging("=> Click Source code  => Pass")
    time.sleep(1)
    if 'text-align: center' in driver.page_source :
        Logging("1. Select Alignment Center =>  PASS ")
    else:
        Logging("2. Select Alignment Center => FAIL ")
    time.sleep(1)
    click_btn_cancel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_cancel_source"]))).click()
    Logging("=> Click button cancel  => Pass")
    time.sleep(1)


    Logging("===========  Line spacing  ============ ")
    driver.switch_to.default_content()
    click_align_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_icon_align"])))
    click_align_text.click()
    select_align_left = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_align_left"])))
    select_align_left.click()
    click_line_height_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_line_height"])))
    click_line_height_text.click()
    select_line_height = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_line_height12"])))
    select_line_height.click()
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
    click_icon_backgr_color_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_backgr_color_text"])))
    click_icon_backgr_color_text.click()
    Logging("1. Click Icon Background Color successfully")
    select_color_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_color_red"])))
    select_color_text.click()
    Logging("2. Select Color successfully")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    time.sleep(1)
    content_input.send_keys(data["editor"]["content8_format"])
    content_input.send_keys(Keys.RETURN)
    driver.switch_to.default_content()
    Logging("3. Input Content Editor successfully")
    Logging("=> Background Color Text  => Pass")
    time.sleep(1)

    click_tools = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_tools"])))
    click_tools.click()
    Logging("=> Click Tool  => Pass")
    click_source_code = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_source_code"])))
    click_source_code.click()
    Logging("=> Click Source code  => Pass")
    time.sleep(1)
    if 'background-color: #e03e2d' in driver.page_source :
        Logging("1. Select Background Color Text =>  PASS ")
    else:
        Logging("2. Select Background Color Text => FAIL ")
    
    click_btn_cancel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_cancel_source"]))).click()
    time.sleep(1)
    Logging("=> Click button cancel  => Pass")
    
    
    click_icon_backgr_color_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_backgr_color_text"])))
    click_icon_backgr_color_text.click()
    time.sleep(1)
    select_color_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_color_write"])))
    select_color_text.click()
    time.sleep(1)

    Logging("===========  Check box  ============ ")
    time.sleep(1)
    driver.switch_to.default_content()
    click_checkbox = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_insert_checklist"])))
    click_checkbox.click()
    
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    time.sleep(1)
    content_input.send_keys(data["editor"]["content6_format"])
    content_input.send_keys(Keys.RETURN)
    driver.switch_to.default_content()
    click_checkbox = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_insert_checklist"])))
    click_checkbox.click()
    Logging("=> Click Check box  => Pass")
    


    Logging("===========  Numbered/Bulletin List  ============ ")
    time.sleep(1)
    driver.switch_to.default_content()
    click_numbered_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_insert_numbered_list"])))
    click_numbered_list.click()
   
    select_numbered_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_numbered_list_abc"])))
    select_numbered_list.click()
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    content_input.send_keys(data["editor"]["content7_format"])
    content_input.send_keys(Keys.RETURN)
    driver.switch_to.default_content()
    unclick_numbered_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_uncheck_numbered_list"])))
    unclick_numbered_list.click()
    Logging("=> Click Numbered List  => Pass")
    

    
    Logging("=========== Formats Heading  ============ ")
    driver.switch_to.default_content()
    click_tab_format = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_format_editor"])))
    click_tab_format.click()
    Logging("1. Click Format in Editor successfully")
    click_tab_format = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_value_formats"])))
    click_tab_format.click()
    Logging("2. Select Value Formats successfully")
    select_value_headings = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_value_headings"])))
    select_value_headings.click()
    Logging("3. Select Value Heading successfully")
    select_value_headings_1 = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_headings_1"])))
    select_value_headings_1.click()
    Logging("4. Select Value Heading 1 successfully")
    driver.execute_script("window.scrollTo(0, 100)")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    time.sleep(1)
    content_input.send_keys(data["editor"]["content9_format"])
    content_input.send_keys(Keys.RETURN)
    driver.switch_to.default_content()
   

    Logging("=========== Emoticons  ============ ")
    
    driver.switch_to.default_content()
    click_icon_emoticons = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_icon_emoticons"])))
    click_icon_emoticons.click()
    Logging("1. Click icon Emoticons successfully")
    select_value_icon_emoticons = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_icon_100"])))
    select_value_icon_emoticons.click()
    Logging("2. Select value  Emoticons successfully")
    time.sleep(1)
    if '100' in driver.page_source :
        Logging("1. Emoticons successfully ")
    else:
        Logging("2. Emoticons Fail ")
    time.sleep(1)

    Logging("=========== Format-Strikethrough/Superscript/Subscript  ============ ")
    driver.switch_to.default_content()
    click_tab_format = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_format"])))
    click_tab_format.click()
    
    Logging("1. Click tab Format successfully")
    click_strikethrough_format = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["click_strikethrough"])))
    click_strikethrough_format.click()
    Logging("1. Click Strikethrough successfully")
    driver.execute_script("window.scrollTo(0, 100)")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    content_input = driver.find_element_by_xpath("//body[@id='tinymce']")
    time.sleep(1)
    content_input.send_keys(data["editor"]["content10_format"])
    content_input.send_keys(Keys.RETURN)
    driver.switch_to.default_content()
    time.sleep(1)
    

    Logging("===========  Edit image size and position  ============ ")
    driver.switch_to.default_content()
    time.sleep(1)
    icon_insert_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_insearch_image_editor"])))
    icon_insert_image.click()
    Logging("11. Click icon Insert  successfully")
    icon_fd_upload_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["insert_image_upload"])))
    icon_fd_upload_image.click()
    get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["drop_image_editor"])))
    get_file.send_keys(luu_function.file_img)
    time.sleep(1)
    btn_save_upload_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_save_insert_image"])))
    btn_save_upload_image.click()
    time.sleep(1)
    Logging("=> Upload  Image successfully")
    driver.execute_script("window.scrollTo(0, 100)")
    time.sleep(1)
    icon_insert_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_insearch_image_editor"])))
    icon_insert_image.click()
    Logging("11. Click icon Insert  successfully")
    txt_width_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["txt_width"])))
    txt_width_image.clear()
    txt_width_image = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["txt_width"])))
    txt_width_image.send_keys(data["editor"]["number_width"])
    Logging("=> Input number width successfully")
    click_tab_advanced_table = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["table_properties_advanced"])))
    click_tab_advanced_table.click()
    Logging("7. Click tab Advanced Table Properties successfully")
    click_border_style_list = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["list_select_border_style"])))
    click_border_style_list.click()
    select_border_style_list = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["select_border_style_soild"])))
    select_border_style_list.click()
    Logging("8. Click tab Advanced Table Properties successfully")
    txt_border_width_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["txt_border_width"])))
    txt_border_width_image.clear()
    txt_border_width_image = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["txt_border_width"])))
    txt_border_width_image.send_keys(data["editor"]["number_border_width_image"])
    Logging("=> Input Border width successfully")
    btn_save_upload_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_save_insert_image"])))
    btn_save_upload_image.click()
    time.sleep(3)
    Logging("===========  Full Screen  ============ ")
    click_icon_full_screen = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_full_screen"])))
    click_icon_full_screen.click()
    click_icon_full_screen = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_full_screen"])))
    click_icon_full_screen.click()
    Logging("=> Click Full Screen Editor successfully")
    click_btn_save_task = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_save_task"])))
    click_btn_save_task.click()
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
    click_btn_create_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_create_task"])))
    click_btn_create_task.click()
    Logging("4. Click Create Task successfully")
    time.sleep(1)
    if 'Automatically saved file found' in driver.page_source :
        click_btn_delete_auto_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["show_noti_task_auto"])))
        click_btn_delete_auto_task.click()
        Logging("1. Click Automatically saved file found")
    else:
        Logging("2. Not show Automatically saved file found")
    
    txt_title_name_task = driver.find_element_by_xpath(data["editor"]["txt_name_task"])
    txt_title_name_task.send_keys(data["editor"]["title_upload_office_file"])
    time.sleep(1)
    Logging("2. Input Title Task successfully")
    click_btn_view_office_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_view_office_file_html"])))
    click_btn_view_office_file.click()
    time.sleep(2)
    select_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["add_form_office"])))
    select_file.send_keys(luu_function.file_editor)
    time.sleep(2)
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    driver.find_element_by_xpath("//body[@id='tinymce']")
    driver.switch_to.default_content()
    time.sleep(3)
    click_btn_save_task = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_save_task"])))
    click_btn_save_task.click()
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
    click_btn_create_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_create_task"])))
    click_btn_create_task.click()
    time.sleep(1)
    Logging("4. Click Create Task successfully")
    
    if 'Automatically saved file found' in driver.page_source :
        click_btn_delete_auto_task = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["show_noti_task_auto"])))
        click_btn_delete_auto_task.click()
        Logging("1. Click Automatically saved file found")
    else:
        Logging("2. Not show Automatically saved file found")
    
    txt_title_name_task = driver.find_element_by_xpath(data["editor"]["txt_name_task"])
    txt_title_name_task.send_keys(data["editor"]["title_image_rotate"])
    Logging("2. Input Title Task successfully")
    editor_frame = driver.find_element_by_class_name("tox-edit-area__iframe")
    driver.switch_to.frame(editor_frame)
    driver.find_element_by_xpath("//body[@id='tinymce']")
    driver.switch_to.default_content()
    time.sleep(1)
    icon_insert_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_insearch_image_editor"])))
    icon_insert_image.click()
    Logging("11. Click icon Insert  successfully")
    
    icon_fd_upload_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["insert_image_upload"])))
    icon_fd_upload_image.click()
    time.sleep(1)
    get_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["drop_image_editor"])))
    get_file.send_keys(luu_function.file_img)
    time.sleep(2)
    btn_save_upload_image = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_save_insert_image"])))
    btn_save_upload_image.click()
    Logging("=> Upload  Image successfully")
    click_icon_rotate_clockwise = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, data["editor"]["icon_rotate_clockwise"])))
    click_icon_rotate_clockwise.click()
    Logging("=> Click Icon Rotate clockwise successfully")
    click_btn_save_task = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_save_task"])))
    click_btn_save_task.click()
    time.sleep(4)

    if 'Editor Rotate clockwise' in driver.page_source :
        Logging("1. Rotate clockwise image successfully ")
        TestCase_LogResult(**data["testcase_result"]["editor"]["rotate_clockwise_image"]["pass"])
    else:
        Logging("2. Rotate clockwise image Fail ")
        TestCase_LogResult(**data["testcase_result"]["editor"]["rotate_clockwise_image"]["fail"])

    Logging("===========  Delete Task Editor  ============ ")
    time.sleep(1)
    click_btn_back = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_back_task"])))
    click_btn_back.click()
    driver.refresh()
    time.sleep(6)
    time.sleep(2)
    #txt_search_name_task = driver.find_element_by_xpath(data["editor"]["txt_search_name_task"])
    #txt_search_name_task.send_keys(data["editor"]["name_task_search_delete"])
    #txt_search_name_task.send_keys(Keys.RETURN)
    #time.sleep(1)
    #Logging("7. Search Title Task successfully")
    click_checkbox_all = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["checkbox_all"])))
    click_checkbox_all.click()
    time.sleep(1)
    click_btn_more = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_more"])))
    click_btn_more.click()
    time.sleep(1)
    click_btn_delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_delete"])))
    click_btn_delete.click()
    time.sleep(1)
    Logging("8. Click button Delete successfully")
    click_btn_ok = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["editor"]["btn_ok_delete_task"])))
    click_btn_ok.click()
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

