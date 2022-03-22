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


def test_invalidCouponReset():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    utils.addCoupon(driver, "coupon88")
    if driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').is_displayed():
        assert True
    else:
        assert False




def test_couponResetManual():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    utils.addCoupon(driver, utils.createCoupon
    (date.today() - timedelta(days=1), date.today() + timedelta(days=10), 20))
    try:
        utils.removeCoupon(driver)
        assert True
    except Exception as e:
        print(e)
        assert False



def test_discountOnSubtotal():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
    sleep(2)
    discountPercent = 20
    utils.addCoupon(driver, utils.createCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
                                               discountPercent))
    subtotal = utils.subTotalValue(driver)  #driver.find_element(AppiumBy.XPATH, constants.pkrSt).text.strip('PKR ')
    discount = utils.discountValue(driver)  #driver.find_element(AppiumBy.XPATH, constants.discounts).text.strip('PKR ')
    ordertotal = utils.orderTotalValue(driver)  #driver.find_element(AppiumBy.XPATH, constants.orderTotal).text.strip('PKR ')
    # print(subtotal, type(subtotal))
    # print(discount, type(discount))
    # print(discount, type(ordertotal))
    # print(round(discount))
    # print(round((discountPercent / 100) * subtotal))
    if round(subtotal - ordertotal) == round(discount) == round((discountPercent / 100) * subtotal):
        utils.removeCoupon(driver)
        assert True
    else:
        utils.removeCoupon(driver)
        assert False


    # utils.cartScreen(driver)
    # discountPercent = 20
    # utils.addCoupon(driver, utils.createCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=10), discountPercent))
    # subtotal = utils.getopAmountsfromCart(driver, "Sub Total")[0]
    # discount = utils.getopAmountsfromCart(driver, "Discounts")[0]
    # ordertotal = utils.getopAmountsfromCart(driver, "Order Total")[0]
    # if round(subtotal-ordertotal) == round(discount) == round((discountPercent/100)*subtotal):
    #     utils.removeCoupon(driver)
    #     assert True
    # else:
    #     utils.removeCoupon(driver)
    #     assert False


# def test_stopRecording():
#     utils.stopRecording(driver, scriptName)


# def test_invalidCouponReset():
#     driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7  7  Cart').click()
#     sleep(2)
#     utils.addCoupon(driver, "coupon88")
#
#     utils.cartScreen(driver)
#     utils.addCoupon(driver, "coupon88")
#     if utils.checkIfPresent(driver, constants.promo):
#         assert True
#     else:
#         assert False
#
#
# def test_couponResetManual():
#     utils.cartScreen(driver)
#     utils.addCoupon(driver, utils.createCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=10), 20))
#     try:
#         utils.removeCoupon(driver)
#         assert True
#     except Exception as e:
#         print(e)
#         assert False
#
#
# def test_discountOnSubtotal():
#     utils.cartScreen(driver)
#     discountPercent = 20
#     utils.addCoupon(driver, utils.createCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
#                                                discountPercent))
#     subtotal = utils.getopAmountsfromCart(driver, "Sub Total")[0]
#     discount = utils.getopAmountsfromCart(driver, "Discounts")[0]
#     ordertotal = utils.getopAmountsfromCart(driver, "Order Total")[0]
#     if round(subtotal - ordertotal) == round(discount) == round((discountPercent / 100) * subtotal):
#         utils.removeCoupon(driver)
#         assert True
#     else:
#         utils.removeCoupon(driver)
#         assert False

