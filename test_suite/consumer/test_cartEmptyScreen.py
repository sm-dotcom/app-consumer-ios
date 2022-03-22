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


Driver()
driver = Driver.driver
# scriptName = os.path.basename(str(__file__[:-3]))




# def test_startRecording():
#     utils.startRecording(driver)

def test_emptyScreenTitle():
    try:
        driver.implicitly_wait(10)
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeButton[`label == "  Cart"`]').click()
        sleep(2)
        var = driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                  '**/XCUIElementTypeStaticText[`label == " Cart is empty!"`]').text
        if var == "Cart is empty!":
            assert True
    except Exception as e:
        print(e)
        assert False




def test_emptyScreenContent():
    try:
        driver.implicitly_wait(10)
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeButton[`label == "  Cart"`]').click()
        var = driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeStaticText[`label == "Looks like you have no items in your shopping cart. Go back to the home page to add items."`]').text
        if var == "Looks like you have no items in your shopping cart. Go back to the home page to add items.":
            assert True
    except Exception as e:
        print(e)
        assert False




def test_backToHomeBtn():
    try:
        driver.implicitly_wait(10)
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeButton[`label == "  Cart"`]').click()
        sleep(1)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'back-button').click()
        assert True
    except Exception as e:
        print(e)
        assert False



def test_backToHomeVisibility():
    try:
        driver.implicitly_wait(10)
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeButton[`label == "  Cart"`]').click()
        sleep(1)
        if driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'back-button').is_displayed():
            assert True
    except Exception as e:
        print(e)
        assert False





# def test_emptyTheCart():
#     try:
#         driver.implicitly_wait(20)
#         utils.logout(driver)
#     except Exception as e:
#         print(e)
#     try:
#         utils.loginConsumer(driver, "3325845307", "12345")
#         utils.cartScreen(driver)
#         utils.placeOrder(driver)
#         utils.clickOn(driver, "Continue Shopping")
#     except Exception as e:
#         print(e)


# def test_emptyScreenTitle():
#     utils.cartScreen(driver)
#     text = " Cart is empty!"
#     if utils.checkIfTextPresent(driver, text):
#         assert True
#     else:
#         assert False


# def test_emptyScreenContent():
#     utils.cartScreen(driver)
#     content = utils.getText(driver, constants.emptyCartMsg2)
#     text = "Looks like you have no items in your shopping cart. Go back to the home page to add items."
#     print()
#     assert content in text
#
#
# def test_backToHomeVisibility():
#     utils.cartScreen(driver)
#     driver.implicitly_wait(10)
#     if driver.find_element_by_android_uiautomator(constants.backToHome).is_displayed():
#         assert True
#     else:
#         assert False
#
#
# def test_backToHomeBtn():
#     utils.cartScreen(driver)
#     driver.implicitly_wait(10)
#     try:
#         driver.find_element_by_android_uiautomator(constants.backToHome).click()
#         assert True
#     except Exception as e:
#         print(e)
#         assert False
#
#
# def test_stopRecording():
#     utils.stopRecording(driver, scriptName)
#
#
#
#
# driver = Driver.driver



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



# def test_accountScreen():
#     # sleep(2)
#     # driver.swipe(1028, 784, 1038, 1390, 1000)
#     # driver.scroll()
#     driver.implicitly_wait(20)
#     driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "  Account"`]').click()
#     sleep(2)
#     driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`label == " Help "`][2]').click()
#     assert True
