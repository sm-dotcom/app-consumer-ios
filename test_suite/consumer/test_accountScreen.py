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


# scriptName = os.path.basename(str(__file__[:-3]))



# desiredCap_ios = {
#   "platformName": "iOS",
#   "appium:platformVersion": "15.2",
#   "appium:deviceName": "iPhone 12",
#   "appium:automationName": "XCUITest",
#   "appium:udid": "9F58C20B-8D2E-43DB-8E6A-9207A88F101F",
#   "appium:bundleId": "co.app.retailerapp"
# }

# print("Creating session")
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desiredCap_ios)

Driver()
driver = Driver.driver



# def test_start():
#     try:
#         utils.logout(driver)
#     except Exception as e:
#         print(e)
#     utils.loginConsumerPak(driver, "3215555555", "81509")
#     sleep(3)



# scriptName = os.path.basename(str(__file__[:-3]))
# driver = AppiumDriver.Remote("http://127.0.0.1:4723/wd/hub", constants.Desired_Capabilities)
# driver.implicitly_wait(10)
# actions = TouchAction(driver)



def test_accountScreen():
    # sleep(2)
    # driver.swipe(1028, 784, 1038, 1390, 1000)
    # driver.scroll()
    driver.implicitly_wait(20)
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "  Account"`]').click()
    sleep(2)
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`label == " Help "`][2]').click()
    assert True




# @allure.severity(allure.severity_level.NORMAL)
def test_navigate_toOrder():
    driver.implicitly_wait(20)
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, constants.account).click()
    try:
        sleep(2)
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN, constants.order).click()
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN, constants.title_orders).is_displayed()
        # a = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Orders"`]').getText()
        # print (a)
        assert True
    except Exception as e:
        print(e)
        assert False




# @allure.severity(allure.severity_level.NORMAL)
# def test_navigate_toNotifications():
#     utils.clickOn(driver, "Account")
#     try:
#         utils.clickOn(driver, "Notifications")
#         assert True
#     except Exception as e:
#         print(e)
#         assert False




# @allure.severity(allure.severity_level.NORMAL)
def test_navigate_toHelp():
    utils.clickOnIOSChain(driver, constants.account)
    try:
        utils.clickOnIOSChain(driver, constants.help)
        sleep(1)
        utils.checkIfPresentIOSChain(driver, constants.title_help)
        assert True
    except Exception as e:
        print(e)
        assert False





# @allure.severity(allure.severity_level.NORMAL)
def test_expandLanguageselection():
    utils.clickOn(driver, "Account")
    try:
        utils.clickOn(driver, "Select Language / اللغة")
        sleep(3)
        utils.checkIfTextPresent(driver, "Urdu")
        assert True
    except Exception as e:
        print(e)
        assert False




# @allure.severity(allure.severity_level.NORMAL)
def test_backButton():
    utils.clickOn(driver, "Account")
    try:
        utils.clickOn(driver, "")
        sleep(3)
        utils.checkIfTextPresent(driver, "Categories")
        assert True
    except Exception as e:
        print(e)
        assert False




# @allure.severity(allure.severity_level.NORMAL)
def test_Logout():
    utils.logout(driver)
