import os
from datetime import date, timedelta
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from utilities import constants, utils
from utilities.DriverClass import Driver


Driver()
driver = Driver.driver
scriptName = os.path.basename(str(__file__[:-3]))

# def test_startRecording():
#     utils.startRecording(driver)


# def test_startTests():
#     try:
#         utils.logout(driver)
#     except Exception as e:
#         print(e)
#     utils.loginConsumer(driver, "3325845307", "12345")




def test_consumerCouponPositive():
    # utils.addProductsToCart(driver)
    # utils.cartScreen(driver)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(utils.createCoupon(
        date.today() - timedelta(days=1), date.today() + timedelta(days=10),
        20))
    var = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Discounts PKR 0').text
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
    sleep(1)
    if var == 'Discounts PKR 0':
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.remove).click()
        assert True
    else:
        utils.saveScreenshot(driver, scriptName, "consumer", "test_consumerCouponPositive")
        assert False




def test_SalesCouponNegative():
    # utils.logout(driver)
    # utils.loginConsumer(driver, "3325845307", "12345")
    # utils.addProductsToCart(driver)
    # utils.cartScreen(driver)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(
            utils.createCouponSA(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
                                 20))
        var = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Discounts PKR 0').text
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
        sleep(1)
        var2 = driver.find_element(AppiumBy.XPATH, constants.pkr0).text
        print(var2)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.remove).click()
        utils.saveScreenshot(driver, scriptName, "consumer", "test_SalesCouponPositive")
        assert 'PKR 0' not in var2
    except Exception as e:
        assert False
        # utils.addCoupon(driver, utils.createCouponSA(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
    #                                              20))
    # if utils.checkIfPresent(driver, constants.promo):
    #     assert True
    # else:
    #     utils.saveScreenshot(driver, scriptName, "consumer", "test_SalesCouponNegative")
    #     assert False




def test_BothCouponConsumer():
    # utils.logout(driver)
    # utils.loginConsumer(driver, "3325845307", "12345")
    # utils.cartScreen(driver)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(
            utils.createCouponBoth(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
                                   20))
        var = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Discounts PKR 0').text
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
        sleep(1)
        var2 = driver.find_element(AppiumBy.XPATH, constants.pkr0).text
        print(var2)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.remove).click()
        utils.saveScreenshot(driver, scriptName, "consumer", "BothCouponSA")
        assert 'PKR 0' not in var2
    except Exception as e:
        assert False

    # utils.addCoupon(driver, utils.createCouponBoth(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
    #                                                20))
    # if utils.getopAmountsfromCart(driver, "Discounts")[0] > 0:
    #     utils.removeCoupon(driver)
    #     assert True
    # else:
    #     utils.saveScreenshot(driver, scriptName, "consumer", "BothCouponSA")
    #     assert False




def test_consumerCouponNegative():
    # utils.logout(driver)
    # utils.loginSalesAgentCustom(driver, "3325845307")
    # utils.addProductsToCart(driver)
    # utils.cartScreen(driver)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(utils.createCoupon(
        date.today() - timedelta(days=1), date.today() + timedelta(days=10),
        20))
    var = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Discounts PKR 0').text
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
    sleep(1)
    if var == 'Discounts PKR 0':
        assert True
    # utils.addCoupon(driver, utils.createCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
    #                                            20))
    # if utils.checkIfPresent(driver, constants.promo):
    #     assert True
    else:
        utils.saveScreenshot(driver, scriptName, "consumer", "test_consumerCouponNegative")
        assert False




def test_SalesCouponPositive():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(
            utils.createCouponSA(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
                                                     20))
        var = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Discounts PKR 0').text
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
        sleep(1)
        var2 = driver.find_element(AppiumBy.XPATH, constants.pkr0SA).text
        print(var2)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.remove).click()
        utils.saveScreenshot(driver, scriptName, "consumer", "test_SalesCouponPositive")
        assert 'PKR 0' not in var2
    except Exception as e:
        assert False
    # if var2 == 'Discounts PKR 0':
        # assert True
    # utils.cartScreen(driver)
    # utils.addCoupon(driver, utils.createCouponSA(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
    #                                              20))
    # if utils.getopAmountsfromCart(driver, "Discounts")[0] > 0:
    #     utils.removeCoupon(driver)
    #     assert True
    # else:
    #     utils.saveScreenshot(driver, scriptName, "consumer", "test_SalesCouponPositive")
    #     assert False






def test_BothCouponSA():
    # utils.logout(driver)
    # utils.loginSalesAgentCustom(driver, "3325845307")
    # utils.addProductsToCart(driver)
    # utils.cartScreen(driver)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(
            utils.createCouponBoth(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
                                   20))
        var = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Discounts PKR 0').text
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
        sleep(1)
        var2 = driver.find_element(AppiumBy.XPATH, constants.pkr0SA).text
        print(var2)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.remove).click()
        utils.saveScreenshot(driver, scriptName, "consumer", "BothCouponSA")
        assert 'PKR 0' not in var2
    except Exception as e:
        assert False



    # utils.addCoupon(driver, utils.createCouponBoth(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
    #                                                20))
    # if utils.getopAmountsfromCart(driver, "Discounts")[0] > 0:
    #     utils.removeCoupon(driver)
    #     assert True
    # else:
    #     utils.saveScreenshot(driver, scriptName, "consumer", "BothCouponSA")
    #     assert False





# def test_stopRecording():
#     utils.stopRecording(driver, scriptName)

