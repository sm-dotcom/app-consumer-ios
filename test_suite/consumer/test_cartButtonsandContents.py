import os
# import allure
# from allure_commons.types import AttachmentType
from datetime import timedelta, date
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


def test_whatsappBtn():
    try:
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                            constants.cart).click()
        sleep(2)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                            constants.whatsapp_button).click()
        assert True
    except Exception as e:
        assert False



# def test_addItemsToCart():
#     try:
#         driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
#                             constants.like).click()
#         driver.find_element(AppiumBy.)



def test_cartItemsCount():
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                            '3  3  Cart').click()
        sleep(2)
        items = driver.find_elements(AppiumBy.XPATH,
                                '(//XCUIElementTypeImage[@name="product-rectangle-image"])')
        for i in items:
            # print(items)
            total_items = len(items)
            str(total_items)
            print(total_items)
            var = driver.find_element(AppiumBy.IOS_PREDICATE, 'label == "3 Items"').text
            print(var)
            assert total_items in var
    except Exception as e:
        assert False




# def test_emptyTheCart():
#     try:
#         driver.find_element(AppiumBy.ACCESSIBILITY_ID,
#                             '3  3  Cart').click()
#         sleep(2)
#         driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'button').click()
#         sleep(1)
#         driver.find_element(AppiumBy.ID, '1D010000-0000-0000-D47D-000000000000').click()
#         # driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.cart).click()
#     except Exception as e:
#         print(e)



def test_ApplyBtn():
    sleep(5)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                         '3  3  Cart').click()
    sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(utils.createCoupon(
        date.today() - timedelta(days=1), date.today() + timedelta(days=10),
        20))
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()
        sleep(1)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.remove).click()
        assert True
    except Exception as e:
        assert False


# Add atleast 7 items in cart



def test_OrderNowScrollVisibility():
    sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                        '7  7  Cart').click()
    sleep(2)
    try:
        driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`label == "Order Now"`][2]').is_displayed()
        sleep(3)
        utils.scrollOnePage(driver)
        # # driver.scroll()
        # driver.swipe(479, 1793, 479, 585, 1000)
        sleep(2)
        if not driver.find_element(AppiumBy.IOS_PREDICATE, 'label == "Order Total"').is_displayed():
            assert True
    except Exception as e:
        assert False




def test_IncrementBtn():
    # driver.implicity_wait(10)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                        '7  7  Cart').click()
    sleep(2)
    try:
        driver.find_element(AppiumBy.XPATH, constants.incrementBtn).click()
    # incrementBtn = driver.find_elements(AppiumBy.XPATH, '(//XCUIElementTypeOther[@name="plus-image"])')
    # try:
    #     for i in incrementBtn:
    #         incrementBtn.click()
    #         assert True
    except Exception as e:
        assert False




    # utils.cartScreen(driver)
    # check = [utils.getopAmountsfromCart(driver, "Item Total: ")]
    # a = True
    # while a:
    #     utils.scrollOnePage(driver)
    #     check.append(utils.getopAmountsfromCart(driver, "Item Total: "))
    #     try:
    #         utils.checkIfPresent(driver, constants.orderNow)
    #     except Exception as e:
    #         a = False
    #     if check[-1] == check[-2]:
    #         break
    # if a:
    #     assert True
    # else:
    #     assert False




# def test_cartItemsCount():
#     driver.launch_app()
#     utils.cartScreen(driver)
#     items = utils.getTotalItemsFromCart(driver, "Cart Items ")
#     assert " Items" in items[0].text


# def test_whatsappBtn():
#     utils.homeScreen(driver)
#     try:
#         driver.find_element_by_android_uiautomator(constants.whatsappIcon).click()
#         assert True
#     except Exception as e:
#         assert False




# def test_ApplyBtn():
#     driver.launch_app()
#     utils.cartScreen(driver)
#     driver.find_element_by_android_uiautomator(constants.promo).send_keys(utils.createCoupon(
#         date.today() - timedelta(days=1), date.today() + timedelta(days=10),
#         20))
#     try:
#         utils.clickOn(driver, "Apply")
#         utils.clickOn(driver, "Remove")
#         assert True
#     except Exception as e:
#         utils.saveScreenshot(driver, scriptName, "consumer", "test_ApplyBtn")
#         assert False



# def test_OrderNowScrollVisibility():
#     utils.cartScreen(driver)
#     check = [utils.getopAmountsfromCart(driver, "Item Total: ")]
#     a = True
#     while a:
#         utils.scrollOnePage(driver)
#         check.append(utils.getopAmountsfromCart(driver, "Item Total: "))
#         try:
#             utils.checkIfPresent(driver, constants.orderNow)
#         except Exception as e:
#             a = False
#         if check[-1] == check[-2]:
#             break
#     if a:
#         assert True
#     else:
#         assert False




# def test_IncrementBtn():
#     utils.cartScreen(driver)
#     driver.implicitly_wait(10)
#     incrementBtn = driver.find_element_by_android_uiautomator('new UiSelector().text(\"\")')
#     try:
#         incrementBtn.click()
#         assert True
#     except Exception as e:
#         assert False


# def test_stopRecording():
#     utils.stopRecording(driver, scriptName)
