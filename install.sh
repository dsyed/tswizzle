#!/bin/bash

# Install Chrome webdriver for OS X
curl -O https://chromedriver.storage.googleapis.com/2.32/chromedriver_mac64.zip
unzip chromedriver_mac64.zip
chmod +x chromedriver
mv chromedriver /usr/local/bin
rm chromedriver chromedriver_mac64.zip

# Install python requirements
pip install -r requirements.txt
