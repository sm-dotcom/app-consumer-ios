import os
import time
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from utilities import constants, utils

# from utilities import utils, APIs


scriptName = os.path.basename(str(__file__[:-3]))

desiredCap_ios = {
    "platformName": "iOS",
    "appium:platformVersion": "15.2",
    "appium:deviceName": "iPhone 13 mini",
    "appium:automationName": "XCUITest",
    "appium:udid": "4A111176-6F08-4FD0-BE36-BE6D3C49ED89",
    "appium:bundleId": "co.app.retailerapp"
}

print("Creating session")
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desiredCap_ios)
sleep(5)


account = '**/XCUIElementTypeButton[`label == "  Account"`]'


def test_accountScreen():
    # sleep(2)
    # driver.swipe(1028, 784, 1038, 1390, 1000)
    # driver.scroll()
    driver.implicitly_wait(20)
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "  Account"`]').click()
    sleep(2)
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                        '**/XCUIElementTypeOther[`label == " Help "`][2]').click()
    assert True




def test_navigate_toOrder():
    driver.implicitly_wait(20)
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "  Account"`]').click()
    try:
        sleep(2)
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeOther[`label == "Orders "`][3]').click()
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeStaticText[`label == "Orders"`]').is_displayed()
        # driver.find_element(AppiumBy.NAME, 'back-button').click()
        assert True
    except Exception as e:
        print(e)
        assert False




def test_navigate_toHelp():
    driver.implicitly_wait(20)
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                        '**/XCUIElementTypeButton[`label == "  Account"`]').click()
    try:
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeOther[`label == " Help "`][2]').click()
        # driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'back-button').click()
        assert True
    except Exception as e:
        print(e)
        assert False





def test_expandLanguageselection():
    driver.implicitly_wait(20)
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                        '**/XCUIElementTypeButton[`label == "  Account"`]').click()
    try:
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeOther[`label == "Select Language / اللغة "`][2]').click()
        sleep(3)
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeOther[`label == "Urdu "`][2]').is_displayed()
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeButton[`label == "  Account"`]').click()
        assert True
    except Exception as e:
        print(e)
        assert False




def test_backButton():
    driver.implicitly_wait(20)
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                        '**/XCUIElementTypeButton[`label == "  Account"`]').click()
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'back-button').click()
        sleep(2)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Categories').click()
        assert True
    except Exception as e:
        print(e)
        assert False






# try:
#     driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'list-item-0').click() # Select English
#     # driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`label == "English "`][2]').click()
#     driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'button').click() # Confirm
#     # driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`label == "Confirm"`]').click()
# except Exception as e:
#     print (e)



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




# def test_accountScreen():
#   driver.implicitly_wait(10)
#   driver.find_element(AppiumBy.ACCESSIBILITY_ID, "  Account").click()
#   sleep(4)
#   driver.find_elements_by_ios_uiautomation("new UiSelector().text(\"  Account\")")
#   # driver.find




# try:
# driver.implicitly_wait(15)
# driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
#     driver.implicitly_wait(5)
#     utils.clickOn(Driver.driver, "Allow only while using the app")
#     Driver.driver.implicitly_wait(5)
#     utils.clickOn(Driver.driver, "")
#     Driver.driver.implicitly_wait(5)
#     utils.clickOn(Driver.driver, "Confirm")
# except Exception as e:
#     print(e)





# def test_accountScreen():
#   driver.implicitly_wait(10)
#   driver.find_element(AppiumBy.ACCESSIBILITY_ID, "  Account").click()
#   sleep(4)
#   driver.find_elements_by_ios_uiautomation("new UiSelector().text(\"  Account\")")
#   # driver.find






# def loginConsumerPak(driver, phone, pwd):
#   try:
#     driver.implicitly_wait(25)
#     driver.find_element_by_android_uiautomator(f'{constants.loginUsrp}').send_keys(f'{phone}')
#     driver.find_element_by_android_uiautomator(f'{constants.loginPwd}').send_keys(f'{pwd}')
#     driver.find_element_by_android_uiautomator(f'{constants.sign_in}').click()
#   except Exception as e:
#     print(e)


# def test_signIn():
#       # loginUsr
#       print("Nooria")
#       time.sleep(10)
#       driver.find_element_by_android_uiautomator("new UiSelector().text(\"301 234 5678\")").send_keys("555555123")
#       time.sleep(5)
#       driver.find_element_by_android_uiautomator("new UiSelector().text(\"Please Enter Password.\")").send_keys("79546")
#       time.sleep(5)
#       driver.find_element_by_android_uiautomator("new UiSelector().text(\"Sign in\")").click()
#       assert True
