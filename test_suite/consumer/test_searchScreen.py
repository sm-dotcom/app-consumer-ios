# import os
# from appium import webdriver
# import pytest
# from utilities import utils, constants
import os
# import allure
# from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from utilities import constants, utils
from time import sleep
from utilities.DriverClass import Driver



# def test_searchScreen():
#     driver.implicitly_wait(20)
#     driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'header-searchbar-input').click()
#     # driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`name == "header-searchbar-input"`]').click()
#     sleep(2)
#     driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
#                         '**/XCUIElementTypeTextField[`name == "header-searchbar-input"`]').send_keys('olpers')
#     driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`label == ""`][3]').click()
#     # driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '** / XCUIElementTypeOther[`label == ""`][1]').click()
#     driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`label == ""`][1]').click()
#     driver.find_element(AppiumBy.ACCESSIBILITY_ID, '')
#     # driver.find_element_by_ios_class_chain('**/XCUIElementTypeTextField[`name == "header-searchbar-input"`]').click()
#     assert True




# def test_searchScreen():
#     driver.implicitly_wait(20)
#     driver.find_element(AppiumBy.ACCESSIBILITY_ID, "search - button").click()
#     driver.find_element(AppiumBy.ACCESSIBILITY_ID, "header - searchbar - input").click()
#     driver.find_element(AppiumBy.ACCESSIBILITY_ID, "header - searchbar - input").send_keys('olpers')
#     assert True

