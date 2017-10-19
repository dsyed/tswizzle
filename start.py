#!/usr/bin/env python
import os
import time

from selenium import webdriver

MUTED = False

driver = webdriver.Chrome()
driver.get('https://tickets.taylorswift.com/')

# Agree to TOS (lol)
driver.find_element_by_name('tc_approval').click()
driver.find_element_by_id('tm-signup').click()

# Login to Ticketmaster
driver.switch_to_frame('loginFrame')

username_elem = driver.find_element_by_id('login-input')
username_elem.send_keys(os.environ['TM_EMAIL'])

password_elem = driver.find_element_by_name('password')
password_elem.send_keys(os.environ['TM_PASS'])

driver.find_element_by_id('login-btn').click()


def watch_video(url, length):
    """Auto watch a video on the Taylor Swift Tix page.

    `url`       href value of link to video
    `length`    length of video in seconds
    """
    global MUTED

    # Wait for page to load
    time.sleep(10)

    # Click music video
    driver.find_element_by_css_selector('a[href="{}"]'.format(url)).click()

    # Play & mute the video
    driver.switch_to_frame('watch-video-frame')
    driver.switch_to_frame('frame')

    driver.find_element_by_class_name('html5-video-player').click()

    if not MUTED:
        driver.find_element_by_class_name('ytp-mute-button').click()
        MUTED = True

    # Wait for music video to finish
    time.sleep(length)


    # Reset selection
    driver.switch_to_default_content()

    driver.find_element_by_css_selector('button[data-bdd="modal-close-button"]').click()

for _ in range(10):
    watch_video('entry/activity/watch/music_video', 255)
    watch_video('entry/activity/watch/att_behind_scenes', 30)
    watch_video('entry/activity/watch/lyric_video', 214)
    watch_video('entry/activity/watch/att_tsn', 105)
    watch_video('entry/activity/watch/att_tasty_props', 56)
    watch_video('entry/activity/watch/taylor_mountain', 423)

driver.close()
