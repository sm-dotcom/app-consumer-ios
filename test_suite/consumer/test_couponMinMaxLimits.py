import os
from time import sleep
from datetime import date, timedelta
from appium.webdriver.common.appiumby import AppiumBy
from utilities import constants, utils
from utilities.DriverClass import Driver

Driver()
driver = Driver.driver
scriptName = os.path.basename(str(__file__[:-3]))


# def test_startRecording():
#     utils.startRecording(driver)


def test_couponMaxUsed():
    # driver.implicitly_wait(10)
    coupon = utils.createMaxUsageCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=100), 20)
    print(coupon)  # 964AHJ
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



def test_couponFixedMinLimitNegative():
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(3)
    # Get subtotal value and
    var = driver.find_element(AppiumBy.XPATH, constants.pkrSt).text.strip('PKR ')
    comma = var.replace(',', '')
    var1 = str(comma).strip('')
    print(var1)
    cartAmount = int(var1) + 1
    str(cartAmount)
    sleep(2)
    utils.addCoupon(driver, utils.createCouponFixedLimit(
        date.today() - timedelta(days=1), date.today() + timedelta(days=10), 100, cartAmount))
    sleep(1)
    if driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').is_displayed():
        utils.saveScreenshot(driver, scriptName, "consumer", "test_couponFixedMinLimitNegative")
        assert True
    else:
        assert False



def test_couponFixedMinLimitPositive():
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(3)
    # Get subtotal value and
    var = driver.find_element(AppiumBy.XPATH, constants.pkrSt).text.strip('PKR ')
    comma = var.replace(',', '')
    var1 = str(comma).strip('')
    print(var1)
    cartAmount = int(var1)
    str(cartAmount)
    sleep(2)
    utils.addCoupon(driver, utils.createCouponFixedLimit(
        date.today() - timedelta(days=1), date.today() + timedelta(days=10), 100, cartAmount))
    sleep(1)
    discount = driver.find_element(AppiumBy.XPATH, constants.discounts).text.strip('PKR ')
    discountValue = int(discount)
    print(discountValue)
    if discountValue > 0:
        utils.removeCoupon(driver)
        assert True
    else:
        utils.saveScreenshot(driver, scriptName, "consumer", "test_couponFixedMinLimitPositive")




def test_couponPercentMinLimitNegative():
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(3)
    # Get subtotal value and
    var = driver.find_element(AppiumBy.XPATH, constants.pkrSt).text.strip('PKR ')
    comma = var.replace(',', '')
    var1 = str(comma).strip('')
    print(var1)
    cartAmount = int(var1) + 1
    str(cartAmount)
    sleep(2)
    utils.addCoupon(driver,
                    utils.createCouponPercentLimit(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
                                                   10, cartAmount, 100))
    sleep(1)
    if driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').is_displayed():
        utils.saveScreenshot(driver, scriptName, "consumer", "test_couponPercentMinLimitNegative")
        assert True
    else:
        assert False



def test_couponPercentMinLimitPositive():
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(3)
    # Get subtotal value and
    var = driver.find_element(AppiumBy.XPATH, constants.pkrSt).text.strip('PKR ')
    comma = var.replace(',', '')
    var1 = str(comma).strip('')
    print(var1)
    cartAmount = int(var1)
    str(cartAmount)
    sleep(2)
    utils.addCoupon(driver,
                    utils.createCouponPercentLimit(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
                                                   30, cartAmount, round((cartAmount * 0.3) / 2)))
    sleep(1)
    discount = driver.find_element(AppiumBy.XPATH, constants.discounts).text.strip('PKR ')
    discountValue = int(discount)
    print(discountValue)
    if discountValue > 0:
        utils.removeCoupon(driver)
        assert True
    else:
        utils.saveScreenshot(driver, scriptName, "consumer", "test_couponPercentMinLimitPositive")
        assert False




def test_couponPercentMaxLimit():
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(3)
    # Get subtotal value and
    var = driver.find_element(AppiumBy.XPATH, constants.pkrSt).text.strip('PKR ')
    comma = var.replace(',', '')
    var1 = str(comma).strip('')
    print(var1)
    cartAmount = int(var1)
    str(cartAmount)
    sleep(2)
    maxLimit = round((cartAmount * 0.5) / 2)
    print(maxLimit)
    utils.addCoupon(driver,
                    utils.createCouponPercentLimit(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
                                                   50, cartAmount, maxLimit))
    sleep(1)
    discount = driver.find_element(AppiumBy.XPATH, constants.discounts).text.strip('PKR ')
    discountValue = int(discount)
    print(discountValue)
    if discountValue <= maxLimit:
        utils.removeCoupon(driver)
        assert True
    else:
        utils.saveScreenshot(driver, scriptName, "consumer", "test_couponPercentMaxLimit")
        assert False



# def test_stopRecording():
#     utils.stopRecording(driver, scriptName)








# def test_couponFixedMinLimitPositive():
#     utils.cartScreen(driver)
#     cartAmount = utils.getopAmountsfromCart(driver, "Sub Total")[0]
#     utils.addCoupon(driver,
#                     utils.createCouponFixedLimit(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
#                                                  100, cartAmount))
#     # print(utils.checkIfPresent(driver, constants.promo))
#     if utils.getopAmountsfromCart(driver, "Discounts")[0] > 0:
#         utils.removeCoupon(driver)
#         assert True
#     else:
#         utils.saveScreenshot(driver, scriptName, "consumer", "test_couponFixedMinLimitPositive")
#
#
# def test_couponPercentMinLimitNegative():
#     utils.cartScreen(driver)
#     cartAmount = utils.getopAmountsfromCart(driver, "Sub Total")[0]
#     utils.addCoupon(driver,
#                     utils.createCouponPercentLimit(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
#                                                    10, cartAmount + 1, 100))
#     if utils.checkIfPresent(driver, constants.promo):
#         utils.saveScreenshot(driver, scriptName, "consumer", "test_couponPercentMinLimitNegative")
#         assert True
#     else:
#         assert False
#
#
# def test_couponPercentMinLimitPositive():
#     utils.cartScreen(driver)
#     cartAmount = utils.getopAmountsfromCart(driver, "Sub Total")[0]
#     utils.addCoupon(driver,
#                     utils.createCouponPercentLimit(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
#                                                    30, cartAmount, round((cartAmount*0.3)/2)))
#     # print(utils.checkIfPresent(driver, constants.promo))
#     if utils.getopAmountsfromCart(driver, "Discounts")[0] > 0:
#         utils.removeCoupon(driver)
#         assert True
#     else:
#         utils.saveScreenshot(driver, scriptName, "consumer", "test_couponPercentMinLimitPositive")
#
#
# def test_couponPercentMaxLimit():
#     utils.cartScreen(driver)
#     cartAmount = utils.getopAmountsfromCart(driver, "Sub Total")[0]
#     maxLimit = round((cartAmount*0.5)/2)
#     utils.addCoupon(driver,
#                     utils.createCouponPercentLimit(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
#                                                    50, cartAmount, maxLimit))
#     # print(utils.checkIfPresent(driver, constants.promo))
#     if utils.getopAmountsfromCart(driver, "Discounts")[0] <= maxLimit:
#         utils.removeCoupon(driver)
#         assert True
#     else:
#         utils.saveScreenshot(driver, scriptName, "consumer", "test_couponPercentMaxLimit")
#         assert False
#
#
# def test_stopRecording():
#     utils.stopRecording(driver, scriptName)
