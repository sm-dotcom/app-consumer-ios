import os
from time import sleep
from datetime import date, timedelta
from appium.webdriver.common.appiumby import AppiumBy
from utilities import constants, utils
from utilities.DriverClass import Driver



Driver()
driver = Driver.driver
BLskus = ["188-121-00004"]
BLProducts = ['Fresh Up Spearmint 36s x1']
scriptName = os.path.basename(str(__file__[:-3]))


# def test_startRecording():
#     utils.startRecording(driver)



def test_whitelistedCalculations():
    utils.logout(driver)
    utils.loginConsumer(driver, "3121212122", "89507")
    utils.addProductsToCart(driver)
    utils.cartScreen(driver)
    discountValue = 20
    utils.addCoupon(driver,
                    utils.createWhitelistedCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
                                                  discountValue, ["188-121-00004"]))
    discount = utils.getopAmountsfromCart(driver, "Discounts")
    driver.implicitly_wait(10)
    products = utils.getAllProdAndPrices(driver)
    utils.homeScreen(driver)
    utils.cartScreen(driver)
    utils.removeCoupon(driver)
    if (discountValue / 100) * products['Fresh Up Spearmint 36s x1'] == discount[0]:
        assert True
    else:
        assert False


def test_blacklistedCalculations():
    utils.homeScreen(driver)
    utils.cartScreen(driver)
    utils.cartScreen(driver)
    discountValue = 20
    utils.addCoupon(driver,
                    utils.createBlacklistedCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
                                                  discountValue, BLskus))
    discount = utils.getopAmountsfromCart(driver, "Discounts")
    driver.implicitly_wait(10)
    products = utils.getAllProdAndPrices(driver)
    utils.homeScreen(driver)
    utils.cartScreen(driver)
    utils.removeCoupon(driver)
    total = 0
    for i in products.keys():
        if i in BLProducts:
            continue
        else:
            total = total + products[i]
    if (discountValue / 100) * total == discount[0]:
        assert True
    else:
        assert False


def test_couponCalculations():
    utils.homeScreen(driver)
    utils.cartScreen(driver)
    utils.cartScreen(driver)
    discountValue = 20
    utils.addCoupon(driver,
                    utils.createCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
                                       discountValue))
    discount = utils.getopAmountsfromCart(driver, "Discounts")
    driver.implicitly_wait(10)
    products = utils.getAllProdAndPrices(driver)
    utils.homeScreen(driver)
    utils.cartScreen(driver)
    utils.removeCoupon(driver)
    total = 0
    for i in products.keys():
        total = total + products[i]
    if round((discountValue / 100) * total) == round(discount[0]):
        assert True
    else:
        assert False


# def test_stopRecording():
#     utils.stopRecording(driver, scriptName)




# def test_whitelistedCalculations():
#     utils.logout(driver)
#     utils.loginConsumer(driver, "3121212122", "89507")
#     utils.addProductsToCart(driver)
#     utils.cartScreen(driver)
#     discountValue = 20
#     utils.addCoupon(driver,
#                     utils.createWhitelistedCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
#                                                   discountValue, ["188-121-00004"]))
#     discount = utils.getopAmountsfromCart(driver, "Discounts")
#     driver.implicitly_wait(10)
#     products = utils.getAllProdAndPrices(driver)
#     utils.homeScreen(driver)
#     utils.cartScreen(driver)
#     utils.removeCoupon(driver)
#     if (discountValue / 100) * products['Fresh Up Spearmint 36s x1'] == discount[0]:
#         assert True
#     else:
#         assert False
#
#
# def test_blacklistedCalculations():
#     utils.homeScreen(driver)
#     utils.cartScreen(driver)
#     utils.cartScreen(driver)
#     discountValue = 20
#     utils.addCoupon(driver,
#                     utils.createBlacklistedCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
#                                                   discountValue, BLskus))
#     discount = utils.getopAmountsfromCart(driver, "Discounts")
#     driver.implicitly_wait(10)
#     products = utils.getAllProdAndPrices(driver)
#     utils.homeScreen(driver)
#     utils.cartScreen(driver)
#     utils.removeCoupon(driver)
#     total = 0
#     for i in products.keys():
#         if i in BLProducts:
#             continue
#         else:
#             total = total + products[i]
#     if (discountValue / 100) * total == discount[0]:
#         assert True
#     else:
#         assert False
#
#
# def test_couponCalculations():
#     utils.homeScreen(driver)
#     utils.cartScreen(driver)
#     utils.cartScreen(driver)
#     discountValue = 20
#     utils.addCoupon(driver,
#                     utils.createCoupon(date.today() - timedelta(days=1), date.today() + timedelta(days=10),
#                                        discountValue))
#     discount = utils.getopAmountsfromCart(driver, "Discounts")
#     driver.implicitly_wait(10)
#     products = utils.getAllProdAndPrices(driver)
#     utils.homeScreen(driver)
#     utils.cartScreen(driver)
#     utils.removeCoupon(driver)
#     total = 0
#     for i in products.keys():
#         total = total + products[i]
#     if round((discountValue / 100) * total) == round(discount[0]):
#         assert True
#     else:
#         assert False