import base64
import time
# from dotenv import load_dotenv
import os
from utilities import utils
from utilities.DriverClass import Driver

# load_dotenv()
# Driver()
scriptName = os.path.basename(str(__file__[:-3]))

# try:
#     # driver.implicitly_wait(15)
#     # driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
#     driver.implicitly_wait(5)
#     utils.clickOn(driver, "Allow only while using the app")
#     driver.implicitly_wait(5)
#     utils.clickOn(driver, "")
#     driver.implicitly_wait(5)
#     utils.clickOn(driver, "Confirm")
# except Exception as e:
#     print(e)
#
# try:
#     # driver.implicitly_wait(15)
#     # driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
#     driver.implicitly_wait(5)
#     utils.clickOn(driver, "While using the app")
#     driver.implicitly_wait(5)
#     utils.clickOn(driver, "")
#     driver.implicitly_wait(5)
#     utils.clickOn(driver, "Confirm")
# except Exception as e:
#     print(e)


Driver()
driver = Driver.driver

driver.close_app()
driver.launch_app()
time.sleep(10)


# def test_startRecording():
#     utils.startRecording(driver)


def test_amountUpdate():
    try:
        utils.loginConsumer(driver, "3325845307", "12345")
    except Exception as e:
        print(e)
    utils.addProductsToCart(driver)
    utils.cartScreen(driver)
    sub = utils.getopAmountsfromCart(driver, "Sub Total")
    driver.implicitly_wait(10)
    texts = driver.find_elements_by_android_uiautomator('new UiSelector().className("android.view.ViewGroup").index(2)')
    texts[5].click()
    driver.implicitly_wait(10)
    updatedSub = utils.getopAmountsfromCart(driver, "Sub Total")
    if updatedSub > sub:
        assert True
    else:
        assert False


def test_calculationsCart():
    subTotal = utils.getopAmountsfromCart(driver, "Sub Total")
    prodValues = utils.getAllProdAndPrices(driver)
    if round(sum(prodValues.values())) == round(subTotal[0]):
        assert True
    else:
        assert False


# def test_stopRecording():
#     utils.stopRecording(driver, scriptName)

