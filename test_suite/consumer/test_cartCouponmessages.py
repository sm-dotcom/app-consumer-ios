import time
from datetime import date, timedelta
import os
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from utilities import constants, utils
from utilities.DriverClass import Driver


Driver()
driver = Driver.driver
scriptName = os.path.basename(str(__file__[:-3]))


# Add 7,8 items to cart

# def test_startRecording():
#     utils.startRecording(driver)
#
#
# def test_startTests():
#     try:
#         utils.logout(driver)
#     except Exception as e:
#         print(e)
#     utils.loginConsumer(driver, "3325845307", "12345")


def test_couponApplied():

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(utils.createCoupon(
        date.today() - timedelta(days=1), date.today() + timedelta(days=10),
        20))
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
    sleep(1)
    utils.saveScreenshot(driver, scriptName, "consumer", "test_couponApplied")
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.remove).click()
        assert True
    except Exception as e:
        print(e)
        assert False
    # utils.addProductsToCart(driver)
    # utils.cartScreen(driver)
    # utils.addCoupon(driver, utils.createCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=10), 20))
    # driver.implicitly_wait(10)
    # utils.saveScreenshot(driver, scriptName, "consumer", "test_couponApplied")
    # try:
    #     utils.removeCoupon(driver)
    #     assert True
    # except Exception as e:
    #     print(e)
    #     assert False



def test_invalidCoupon():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys('IAMINVALIDCOUPON')
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
    sleep(1)
    utils.saveScreenshot(driver, scriptName, "consumer", "test_invalidCoupon")
    if driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').is_displayed():
        assert True
    else:
        assert False
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(\"Home\")')
    # utils.cartScreen(driver)
    # utils.addCoupon(driver, "IAMINVALIDCOUPON")
    # driver.implicitly_wait(10)
    # utils.saveScreenshot(driver, scriptName, "consumer", "test_invalidCoupon")
    # if utils.checkIfPresent(driver, constants.promo):
    #     assert True
    # else:
    #     assert False


def test_expiredCoupon():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(utils.createCoupon(
        date.today() - timedelta(days=10), date.today() - timedelta(days=1), 20))
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
    sleep(1)
    utils.saveScreenshot(driver, scriptName, "consumer", "test_expiredCoupon")
    if driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').is_displayed():
        assert True
    else:
        assert False
    # utils.cartScreen(driver)
    # utils.addCoupon(driver, utils.createCoupon(date.today() - timedelta(days=10), date.today() - timedelta(days=1), 20))
    # utils.saveScreenshot(driver, scriptName, "consumer", "test_expiredCoupon")
    # driver.implicitly_wait(10)
    # if utils.checkIfPresent(driver, constants.promo):
    #     assert True
    # else:
    #     assert False



def test_couponNotStarted():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(utils.createCoupon(
        date.today() + timedelta(days=1), date.today() + timedelta(days=10), 20))
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
    sleep(1)
    utils.saveScreenshot(driver, scriptName, "consumer", "test_couponNotStarted")
    if driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').is_displayed():
        assert True
    else:
        assert False
    # utils.cartScreen(driver)
    # utils.addCoupon(driver, utils.createCoupon(date.today() + timedelta(days=1), date.today() + timedelta(days=10), 20))
    # driver.implicitly_wait(10)
    # utils.saveScreenshot(driver, scriptName, "consumer", "test_couponNotStarted")
    # driver.implicitly_wait(10)
    # if utils.checkIfPresent(driver, constants.promo):
    #     assert True
    # else:
    #     assert False


# Need to add products to cart function here
def test_couponMaxUsage():
    coupon = utils.createMaxUsageCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=100), 20)
    print(coupon) #964AHJ
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(coupon)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
    sleep(1)
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`label == "Order Now"`][2]').click()
    # continue shopping click
    # add products to cart
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(coupon)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
    sleep(1)
    utils.saveScreenshot(driver, scriptName, "consumer", "test_couponMaxUsage")
    if driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').is_displayed():
        assert True
    else:
        assert False
    # utils.cartScreen(driver)
    # coupon = utils.createMaxUsageCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=100), 20)
    # utils.addCoupon(driver, coupon)
    # utils.placeOrder(driver)
    # utils.clickOn(driver, "Continue Shopping")
    # utils.addProductsToCart(driver)
    # utils.cartScreen(driver)
    # utils.addCoupon(driver, coupon)
    # driver.implicitly_wait(10)
    # utils.saveScreenshot(driver, scriptName, "consumer", "test_couponMaxUsage")
    # driver.implicitly_wait(10)
    # if utils.checkIfPresent(driver, constants.promo):
    #     assert True
    # else:
    #     utils.saveScreenshot(driver, scriptName, "consumer", "test_couponMaxUsage")
    #     assert False


# def test_stopRecording():
#     utils.stopRecording(driver, scriptName)

