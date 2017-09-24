#!/usr/bin/env python
import os
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://tickets.taylorswift.com/')

driver.find_element_by_name('tc_approval').click()
driver.find_element_by_id('tm-signup').click()

driver.switch_to_frame('loginFrame')

username_elem = driver.find_element_by_id('login-input')
username_elem.send_keys(os.environ['TM_EMAIL'])

password_elem = driver.find_element_by_name('password')
password_elem.send_keys(os.environ['TM_PASS'])

driver.find_element_by_id('login-btn').click()

for _ in range(10):
    # Wait for page to load
    time.sleep(3)

    # Click music video
    driver.find_element_by_css_selector('a[href="entry/activity/watch/music_video"]').click()

    driver.switch_to_frame('watch-video-frame')
    driver.switch_to_frame('frame')

    driver.find_element_by_class_name('html5-video-player').click()
    driver.find_element_by_class_name('ytp-mute-button').click()

    # Wait for music video to finish
    time.sleep(255)

    driver.switch_to_default_content()


# driver.close()
