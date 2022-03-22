# import base64
# import time
# import string
# import random
# from utilities import constants
# import requests
# import json
# import os
# import locale
# from utilities import APIs
#
# locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
import json
import locale
import os

import requests


def happyFlow(driver):
    selectL1cat(driver)
    addProductToCart(driver)
    cartScreen(driver)
    addCoupon(driver, 'pizza')
    placeOrder(driver)


def logout(driver):
    try:
        driver.implicitly_wait(10)
        driver.find_element_by_android_uiautomator(f'{constants.account}').click()
        driver.implicitly_wait(10)
        driver.find_element_by_android_uiautomator(f'{constants.logout}').click()
        driver.implicitly_wait(10)
        driver.find_element_by_android_uiautomator(f'{constants.logoutSure}').click()
    except Exception as e:
        print(e)


def loginConsumer(driver, phone, pwd):
    try:
        driver.implicitly_wait(15)
        driver.find_element_by_android_uiautomator(f'{constants.loginUsr}').send_keys(f'{phone}')
        driver.find_element_by_android_uiautomator(f'{constants.loginPwd}').send_keys(f'{pwd}')
        driver.find_element_by_android_uiautomator(f'{constants.loginBtn}').click()
    except Exception as e:
        print(e)


def loginSalesAgent(driver):
    try:
        driver.find_element_by_android_uiautomator(f'{constants.loginUsr}').send_keys(f'{constants.phone[1]}')
        driver.find_element_by_android_uiautomator(f'{constants.loginPwd}').send_keys(f'{constants.pwd}')
        driver.find_element_by_android_uiautomator(f'{constants.loginBtn}').click()
        driver.implicitly_wait(10)
        driver.find_element_by_android_uiautomator(f'{constants.loginUsr}').send_keys(f'{constants.phone[2]}')
        driver.find_element_by_android_uiautomator(f'{constants.confirmSalesAgentLogin}').click()
    except Exception as e:
        print(e)


def loginSalesAgentCustom(driver, consumer):
    try:
        driver.implicitly_wait(20)
        driver.find_element_by_android_uiautomator(f'{constants.loginUsr}').send_keys(f'{constants.phone[1]}')
        driver.find_element_by_android_uiautomator(f'{constants.loginPwd}').send_keys(f'{constants.pwd}')
        driver.find_element_by_android_uiautomator(f'{constants.loginBtn}').click()
        driver.implicitly_wait(10)
        driver.find_element_by_android_uiautomator(f'{constants.loginUsr}').send_keys(f'{consumer}')
        driver.find_element_by_android_uiautomator(f'{constants.confirmSalesAgentLogin}').click()
    except Exception as e:
        print(e)


def selectL1cat(driver, catNumber):
    driver.implicitly_wait(20)
    driver.find_element_by_android_uiautomator(f'new UiSelector().text(\"{APIs.getL1CatNames()[catNumber]}\")').click()


def clickOn(driver, element):
    try:
        driver.implicitly_wait(20)
        driver.find_element_by_android_uiautomator(f"new UiSelector().text(\"{element}\")").click()
        time.sleep(0.5)
    except Exception as e:
        print(e)


def writeText(driver, field, text):
    try:
        driver.implicitly_wait(15)
        driver.find_element_by_android_uiautomator(f"new UiSelector().text(\"{field}\")").send_keys(f'{text}')
    except Exception as e:
        print(e)


def addProductToCart(driver):
    homeScreen(driver)
    selectL1cat(driver, 0)
    driver.implicitly_wait(20)
    driver.swipe(479, 1693, 479, 585, 1000)
    driver.implicitly_wait(5)
    driver.find_element_by_android_uiautomator(constants.product).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(constants.addX).click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(constants.addMore).click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(constants.write).click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(constants.write).clear()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(constants.write).send_keys('11' + "\n")
    driver.implicitly_wait(10)
    # driver.find_element_by_android_uiautomator(constants.confirm).click()
    try:
        driver.find_element_by_android_uiautomator(constants.confirm).click()
        driver.find_element_by_android_uiautomator(constants.confirm).click()
        driver.find_element_by_android_uiautomator(constants.confirm).click()
    except Exception as e:
        print(e)


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


def addCoupon(driver, coupon):
    try:
        removeCoupon(driver)
    except Exception:
        pass
    driver.implicitly_wait(10)
    driver.find_element_by_android_uiautomator(constants.promo).send_keys(coupon)
    driver.implicitly_wait(10)
    driver.find_element_by_android_uiautomator(constants.applyCoupon).click()
    # clickOn(driver, "Apply")


def removeCoupon(driver):
    driver.implicitly_wait(1)
    driver.find_element_by_android_uiautomator(constants.removeCoupon).click()


def cartScreen(driver):
    driver.implicitly_wait(10)
    driver.find_element_by_android_uiautomator('new UiSelector().text(\"Cart\")').click()


def likesScreen(driver):
    driver.implicitly_wait(10)
    driver.find_element_by_android_uiautomator(constants.likes).click()


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


def homeScreen(driver):
    driver.implicitly_wait(5)
    driver.find_element_by_android_uiautomator(constants.home).click()
    driver.find_element_by_android_uiautomator(constants.home).click()


def placeOrder(driver):
    time.sleep(3)
    try:
        driver.implicitly_wait(10)
        clickOn(driver, "Order Now")
    except Exception as e:
        print(e)


def getText(driver, element):
    return driver.find_element_by_android_uiautomator(element).text


def scrollOnePage(driver):
    time.sleep(0.5)
    driver.swipe(536, 1836, 536, 304, 2000)


def checkIfPresent(driver, element):
    driver.implicitly_wait(10)
    if driver.find_element_by_android_uiautomator(element).is_displayed():
        return True
    else:
        return False


def checkIfAllPresent(driver, elements):
    for i in elements:
        driver.implicitly_wait(10)
        if driver.find_element_by_android_uiautomator(f"new UiSelector().text(\"{i}\")").is_displayed():
            pass
        else:
            return False
    return True


def checkIfTextPresent(driver, elementText):
    driver.implicitly_wait(10)
    if driver.find_element_by_android_uiautomator(f"new UiSelector().text(\"{elementText}\")").is_displayed():
        return True
    else:
        return False


def randomString(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def randomNumber(size=2, chars=string.digits):
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


def createCouponLocationSpecific(start, end, value, location_id):
    payload = constants.couponPayload
    payload['name'] = randomString()
    name = payload['name']
    payload['start_date'] = str(start)
    payload['location_id'] = location_id
    payload['user_type'] = "[8,16]"
    payload['end_date'] = str(end)
    payload['discount_value'] = value
    payload1 = json.dumps(payload)
    payload['location_id'] = 210
    # print(payload)
    response = requests.request("POST", os.getenv('createCoupon'), headers=constants.coupon_headers, data=payload1)
    # print(response.text)
    return name


def createDisabledCoupon(start, end, value):
    payload = constants.couponPayload
    payload['name'] = randomString()
    name = payload['name']
    payload['disabled'] = True
    payload['user_type'] = "[8,16]"
    payload['start_date'] = str(start)
    payload['end_date'] = str(end)
    payload['discount_value'] = value
    payload1 = json.dumps(payload)
    # print(payload)
    response = requests.request("POST", os.getenv('createCoupon'), headers=constants.coupon_headers, data=payload1)
    # print(response.text)
    payload['disabled'] = False
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


def createCouponSAPercentLimit(start, end, value, minCoupLim, maxLimit):
    payload = constants.couponPayload
    payload['name'] = randomString()
    name = payload['name']
    payload['user_type'] = "[16]"
    payload['discount_type'] = 1
    payload['min_coupon_limit'] = minCoupLim
    payload['max_discount_value'] = maxLimit
    payload['start_date'] = str(start)
    payload['end_date'] = str(end)
    payload['discount_value'] = value
    payload = json.dumps(payload)
    response = requests.request("POST", os.getenv('createCoupon'), headers=constants.coupon_headers, data=payload)
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


def createCouponSelectedCustomer(start, end, value, custId):
    payload = constants.couponPayload
    payload['name'] = randomString()
    name = payload['name']
    payload['start_date'] = str(start)
    payload['end_date'] = str(end)
    payload['user_type'] = "[8,16]"
    payload['discount_value'] = value
    payload['coupon_customer'] = custId
    payload['coupon_customer_option_id'] = 2
    payload = json.dumps(payload)
    # print(payload)
    response = requests.request("POST", os.getenv('createCoupon'), headers=constants.coupon_headers, data=payload)
    # print(response.text)
    return name


def createWhitelistedCoupon(start, end, value, whitelist):
    payload = constants.couponPayload
    payload['name'] = randomString()
    name = payload['name']
    payload['start_date'] = str(start)
    payload['end_date'] = str(end)
    payload['user_type'] = "[8,16]"
    payload['discount_value'] = value
    payload['products_list_type'] = 1
    payload['coupon_skus'] = whitelist
    payload = json.dumps(payload)
    # print(payload)
    response = requests.request("POST", os.getenv('createCoupon'), headers=constants.coupon_headers, data=payload)
    print(response.text)
    return name


def createBlacklistedCoupon(start, end, value, skus):
    payload = constants.couponPayload
    payload['name'] = randomString()
    name = payload['name']
    payload['start_date'] = str(start)
    payload['end_date'] = str(end)
    payload['discount_value'] = value
    payload['products_list_type'] = 2
    payload['coupon_skus'] = skus
    payload = json.dumps(payload)
    # print(payload)
    response = requests.request("POST", os.getenv('createCoupon'), headers=constants.coupon_headers, data=payload)
    return name


def saveScreenshot(driver, scriptName, user, filename):
    path = f"../../test_results/{user}/screenshots/{scriptName}"
    print(path)
    os.makedirs(path, exist_ok=True)
    time.sleep(1)
    driver.save_screenshot(f"{path}/{filename}.png")


def getopAmountsfromCart(driver, value):
    driver.implicitly_wait(10)
    cartScreen(driver)
    price = []
    driver.implicitly_wait(10)
    texts = driver.find_elements_by_class_name('android.widget.TextView')
    for index, element in enumerate(texts):
        if element.text == value:
            price.append(locale.atof(texts[index + 1].text.strip("PKR ")))
    return price


def navigateToBottomCart(driver):
    driver.implicitly_wait(10)
    itemTotals = [getopAmountsfromCart(driver, "Item Total: ")]
    while True:
        scrollOnePage(driver)
        itemTotals.append(getopAmountsfromCart(driver, "Item Total: "))
        if itemTotals[-1] == itemTotals[-2]:
            break
    return


def getAllProdAndPrices(driver):
    driver.implicitly_wait(10)
    itemTotals = [getopAmountsfromCart(driver, "Item Total: ")]
    products = {}
    getProductsAndPrices(driver, products)
    while True:
        scrollOnePage(driver)
        itemTotals.append(getopAmountsfromCart(driver, "Item Total: "))
        getProductsAndPrices(driver, products)
        if itemTotals[-1] == itemTotals[-2]:
            break
    return products


def getProductsAndPrices(driver, products):
    cartScreen(driver)
    driver.implicitly_wait(10)
    texts = driver.find_elements_by_class_name('android.widget.TextView')
    for index, element in enumerate(texts):
        if element.text == "Item Total: ":
            products[f"{texts[index - 7].text}"] = locale.atof(texts[index + 1].text.strip("PKR "))
    return products


def getTotalItemsFromCart(driver, value):
    items = []
    time.sleep(1)
    driver.implicitly_wait(10)
    texts = driver.find_elements_by_class_name('android.widget.TextView')
    for index, element in enumerate(texts):
        if element.text == value:
            items.append(texts[index + 1])
    return items


def updateMinMax(locationId, min_order_limit, max_order_limit):
    APIs.updateMaxMinForLocation(locationId, min_order_limit, max_order_limit)


def updateProductPrice(productId, price):
    APIs.updateProduct(productId, price, 0, 210)


def getAllTextFromScreen(driver):
    text = []
    textElements = driver.find_elements_by_android_uiautomator(constants.textView)
    for i in textElements:
        text.append(i.text)
    return text


def refreshScreen(driver):
    time.sleep(2)
    driver.swipe(526, 500, 526, 1326, 500)
    # actions = TouchAction(driver)
    # actions.press(x=150, y=350)
    # actions.move_to(x=150, y=800)
    # actions.release()
    # actions.perform()
    # time.sleep(3)


def generatePhonePak():
    # phone_number_pak = PhoneNumber("Pakistan")
    # number = phone_number_pak.get_number(full=False)
    first = str(random.randint(3, 3))
    second = str(random.randint(0, 3))
    third = str(random.randint(0, 7)).zfill(1)
    last = (str(random.randint(1, 9999998)).zfill(7))
    number = first + second + third + last
    # print(number)
    return number


def generateCNIC():
    first = str(random.randint(3, 3))
    second = str(random.randint(1, 99998)).zfill(5)
    last = (str(random.randint(0, 9999998)).zfill(7))
    number = first + second + last
    # print(number)
    return number


def startRecording(driver):
    try:
        driver.start_recording_screen()
    except Exception as e:
        print(e)


def stopRecording(driver, filename):
    try:
        video = driver.stop_recording_screen()
        with open(f"{os.getenv('/home/siraj/Documents/aws/Screenshots')}/{filename}.mp4", "wb") as vd:
            vd.write(base64.b64decode(video))
    except Exception as e:
        print(e)
