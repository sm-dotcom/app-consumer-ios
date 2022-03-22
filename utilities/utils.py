import os
import time
import string
import random
from utilities import constants, APIs
import requests
import json
from time import sleep
# import locale
# from utilities import APIs
# from phone_gen import PhoneNumber
# locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
from appium.webdriver.common.appiumby import AppiumBy




def randomString(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def createCoupon(start, end, value):
    payload = constants.couponPayload
    payload['name'] = randomString()
    name = payload['name']
    payload['start_date'] = str(start)
    payload['end_date'] = str(end)
    payload['user_type'] = "[8]"
    payload['discount_value'] = value
    payload = json.dumps(payload)
    # print(payload)
    response = requests.request("POST", os.getenv('createCoupon'), headers=constants.coupon_headers, data=payload)
    print(response.text)
    return name



def saveScreenshot(driver, scriptName, user, filename):
    path = f"../../test_results/{user}/screenshots/{scriptName}"
    print(path)
    os.makedirs(path, exist_ok=True)
    time.sleep(1)
    driver.save_screenshot(f"{path}/{filename}.png")



def createCouponSA(start, end, value):
    payload = constants.couponPayload
    payload['name'] = randomString()
    name = payload['name']
    payload['user_type'] = "[16]"
    payload['start_date'] = str(start)
    payload['end_date'] = str(end)
    payload['discount_value'] = value
    payload = json.dumps(payload)
    # print(payload)
    response = requests.request("POST", os.getenv('createCoupon'), headers=constants.coupon_headers, data=payload)
    # print(response.text)
    return name



def createCouponBoth(start, end, value):
    payload = constants.couponPayload
    payload['name'] = randomString()
    name = payload['name']
    payload['user_type'] = "[8,16]"
    payload['start_date'] = str(start)
    payload['end_date'] = str(end)
    payload['discount_value'] = value
    payload = json.dumps(payload)
    # print(payload)
    response = requests.request("POST", os.getenv('createCoupon'), headers=constants.coupon_headers, data=payload)
    # print(response.text)
    return name



def createMaxUsageCoupon(start, end, value):
    payload = constants.couponPayload
    payload['name'] = randomString()
    name = payload['name']
    payload['max_usage_per_customer'] = 1
    payload['start_date'] = str(start)
    payload['end_date'] = str(end)
    payload['discount_value'] = value
    payload = json.dumps(payload)
    # print(payload)
    response = requests.request("POST", os.getenv('createCoupon'), headers=constants.coupon_headers, data=payload)
    # print(response.text)
    return name



def createCouponFixedLimit(start, end, value, minCoupLim):
    payload = constants.couponPayload
    payload['name'] = randomString()
    name = payload['name']
    payload['discount_type'] = 2
    payload['min_coupon_limit'] = minCoupLim
    payload['start_date'] = str(start)
    payload['end_date'] = str(end)
    payload['discount_value'] = value
    payload = json.dumps(payload)
    response = requests.request("POST", os.getenv('createCoupon'), headers=constants.coupon_headers, data=payload)
    return name



def createCouponPercentLimit(start, end, value, minCoupLim, maxLimit):
    payload = constants.couponPayload
    payload['name'] = randomString()
    name = payload['name']
    payload['discount_type'] = 1
    payload['min_coupon_limit'] = minCoupLim
    payload['max_discount_value'] = maxLimit
    payload['start_date'] = str(start)
    payload['end_date'] = str(end)
    payload['discount_value'] = value
    payload = json.dumps(payload)
    response = requests.request("POST", os.getenv('createCoupon'), headers=constants.coupon_headers, data=payload)
    return name




def addCoupon(driver, coupon):
    try:
        removeCoupon(driver)
    except Exception:
        pass
    driver.implicitly_wait(10)
    # sleep(1)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'text-input').send_keys(coupon)
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.apply).click()


def removeCoupon(driver):
    sleep(1)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, constants.remove).click()



def subTotalValue(driver):
    var = driver.find_element(AppiumBy.XPATH, constants.pkrSt).text.strip('PKR ')
    comma = var.replace(',', '')
    var1 = str(comma).strip('')
    # print(var1)
    subTotal = int(var1)
    str(subTotal)
    return subTotal



def discountValue(driver):
    discount = driver.find_element(AppiumBy.XPATH, constants.discounts).text.strip('PKR ')
    discountValue = float(discount)
    print(discountValue)
    str(discountValue)
    return discountValue


def orderTotalValue(driver):
    var = driver.find_element(AppiumBy.XPATH, constants.pkrOt).text.strip('PKR ')
    comma = var.replace(',', '')
    var1 = str(comma).strip('')
    # print(var1)
    orderTotal = float(var1)
    str(orderTotal)
    return orderTotal



def scrollOnePage(driver):
    time.sleep(1)
    driver.swipe(536, 1836, 536, 304, 2000)



def clickOnID(driver, element):
    driver.implicitly_wait(20)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, element).click()
    # driver.find_element_by_android_uiautomator(f"new UiSelector().text(\"{element}\")").click()


def clickOnIOSChain(driver, element):
    driver.implicitly_wait(20)
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, element).click()
    # driver.find_element_by_android_uiautomator(f"new UiSelector().text(\"{element}\")").click()



def checkIfPresentID(driver, element):
    driver.implicitly_wait(10)
    if driver.find_element(AppiumBy.ACCESSIBILITY_ID, element).is_displayed():
    # if driver.find_element_by_android_uiautomator(element).is_displayed():
        return True
    else:
        return False



def checkIfPresentIOSChain(driver, element):
    driver.implicitly_wait(10)
    if driver.find_element(AppiumBy.IOS_CLASS_CHAIN, element).is_displayed():
    # if driver.find_element_by_android_uiautomator(f"new UiSelector().text(\"{elementText}\")").is_displayed():
        return True
    else:
        return False



def checkIfTextPresentIOSChain(driver, elementText):
    driver.implicitly_wait(10)
    if driver.find_element(AppiumBy.ACCESSIBILITY_ID, elementText).is_displayed():
    # if driver.find_element_by_android_uiautomator(f"new UiSelector().text(\"{elementText}\")").is_displayed():
        return True
    else:
        return False




# def addProductToCart(driver):
#     homeScreen(driver)
#     selectL1cat(driver, 0)
#     driver.implicitly_wait(20)
#     driver.swipe(479, 1693, 479, 585, 1000)
#     driver.implicitly_wait(5)
#     driver.find_element_by_android_uiautomator(constants.product).click()
#     driver.implicitly_wait(5)
#     driver.find_element_by_xpath(constants.addX).click()
#     driver.implicitly_wait(10)
#     driver.find_element_by_xpath(constants.addMore).click()
#     driver.implicitly_wait(10)
#     driver.find_element_by_xpath(constants.write).click()
#     driver.implicitly_wait(10)
#     driver.find_element_by_xpath(constants.write).clear()
#     driver.implicitly_wait(10)
#     driver.find_element_by_xpath(constants.write).send_keys('11' + "\n")
#     driver.implicitly_wait(10)
#     # driver.find_element_by_android_uiautomator(constants.confirm).click()
#     try:
#         driver.find_element_by_android_uiautomator(constants.confirm).click()
#         driver.find_element_by_android_uiautomator(constants.confirm).click()
#         driver.find_element_by_android_uiautomator(constants.confirm).click()
#     except Exception as e:
#         print(e)



def removeProductsFromCart(driver, untilSubTotal):
    cartScreen(driver)
    subTotal = getopAmountsfromCart(driver, "Sub Total")
    while subTotal[0] > untilSubTotal:
        cartScreen(driver)
        texts = driver.find_elements_by_android_uiautomator(
            'new UiSelector().className("android.view.ViewGroup").index(2)')
        texts[6].click()
        driver.find_element_by_android_uiautomator(constants.confirm).click()
        subTotal = getopAmountsfromCart(driver, "Sub Total")


def updateProductQtyFromCart(driver, productNumber, updatedQty):
    quantityWidget = driver.find_elements_by_class_name('android.widget.EditText')
    productQuantity = quantityWidget[productNumber]
    productQuantity.click()
    productQuantity.clear()
    productQuantity.send_keys(f'{updatedQty}')
    driver.keyevent(66)
    time.sleep(2)


def cartScreen(driver):
    driver.implicitly_wait(10)
    driver.find_element_by_android_uiautomator('new UiSelector().text(\"Cart\")').click()



def addProductsToCart(driver):
    try:
        likesScreen(driver)
    except Exception as e:
        print(e)
    products = driver.find_elements_by_android_uiautomator('new UiSelector().text(\"\")')
    for i in products:
        i.click()


def homeScreen(driver):
    driver.implicitly_wait(10)
    driver.find_element_by_android_uiautomator(constants.home).click()

