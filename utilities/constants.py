# Constants to locates

import os
import requests
# from dotenv import load_dotenv
from utilities import APIs

# load_dotenv()
from utilities import APIs


# Desired_Capabilities = {
#     "avd": "Pixel_4_API_29",
#     # "headless": True,
#     "platformName": "Android",
#     "platformVersion": "10.0",
#     "deviceName": "Android_SDK",
#     "udid": "emulator-5556",
#     "noReset": True,
#     # "fullReset": False,
#     "automationName" : "uiautomator2",
#     "app" : "C:\\Users\\USER\\Downloads\\app-universal-release_4.apk",
#     "appPackage": "com.app.retailerapp",
#     "appActivity": "com.app.retailerapp.MainActivity",
#     "autoGrantPermissions": "true",
#     "appWaitForLaunch": "false",
#     "unicodeKeyboard": "true"
#     # "autoDissmissAlerts": "true"  # to dismiss all alerts
# }



# PHONE_NO_3 = os.getenv('PHONE_NO_3')
# ACCCOUNT_PASSWORD = os.getenv('ACCCOUNT_PASSWORD')
# PHONE_NO_1 = os.getenv('PHONE_NO_1')
# PHONE_NO_2 = os.getenv('PHONE_NO_2')
# PASSWORD = os.getenv('PASSWORD')
# INVALID_PASSWORD = os.getenv('INVALID_PASSWORD')
# INVALID_PHONE_NO = os.getenv('INVALID_PHONE_NO')
# INVALID_PHONE_NO_PAK = os.getenv('INVALID_PHONE_NO_PAK')
# INVALID_PHONE_NO_SAU = os.getenv('INVALID_PHONE_NO_SAU')
# VALID_UNREGISTERED_PHONE = os.getenv('VALID_UNREGISTERED_PHONE')
# SALES_AGENT_PHONE = os.getenv('SALES_AGENT_PHONE')
# SALES_AGENT_PWD = os.getenv('SALES_AGENT_PWD')
# SPHONE = os.getenv('SPHONE')
# LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')
# LOGIN_PHONE  = os.getenv('LOGIN_PHONE')
#
#
#
#
#
# account_user = PHONE_NO_3
# account_pwd = ACCCOUNT_PASSWORD
# allowLoc = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]'
# loginUsrp = "new UiSelector().text(\"301 234 5678\")"
# loginUsrs = "new UiSelector().text(\"51 234 5678\")"
# loginPwd = "new UiSelector().text(\"Please Enter Password.\")"
# loginBtn = "new UiSelector().className(\"android.view.ViewGroup\").index(5)"
# invalidPhone_msg = "new UiSelector().className(\"android.widget.TextView\").text(\"Please Enter Mobile No.\")"
# enter_password_msg = "new UiSelector().className(\"android.widget.TextView\").text(\"Please Enter Password.\")"
# confirmSalesAgentLogin = "new UiSelector().className(\"android.view.ViewGroup\").index(4)"
# phone = [PHONE_NO_1, PHONE_NO_2]
# sphone = SPHONE
# valid_unregistered_phone = VALID_UNREGISTERED_PHONE
# invalidPhoneNo = [INVALID_PHONE_NO, INVALID_PHONE_NO_PAK , INVALID_PHONE_NO_SAU]
# pwd = PASSWORD
# invalidpwd = INVALID_PASSWORD
# sales_agent_phone = SALES_AGENT_PHONE
# sales_agent_pwd = SALES_AGENT_PWD
# # random_phoneno = []
#
#
# login_phone = LOGIN_PHONE
# login_pwd = LOGIN_PASSWORD

# login_phone = LOGIN_PHONE   3339711642
# login_pwd = LOGIN_PASSWORD  49571






# Account Screen
account = '**/XCUIElementTypeButton[`label == "  Account"`]'
order = '**/XCUIElementTypeOther[`label == "Orders "`][3]'
title_orders = '**/XCUIElementTypeStaticText[`label == "Orders"`]'
help = '**/XCUIElementTypeOther[`label == " Help "`][2]'
title_help = '**/XCUIElementTypeStaticText[`label == "Help"`]'
cart = '**/XCUIElementTypeButton[`label == "  Cart"`]'
whatsapp_button = 'whatsapp-button'
like = '  Likes'


# Cart Screen
apply = 'Apply'
remove = 'Remove'
orderNow = '**/XCUIElementTypeOther[`label == "Order Now"`][2]'
pkr0SA = '(//XCUIElementTypeStaticText[@name="text"])[12]'
pkr0 = '(//XCUIElementTypeStaticText[@name="text"])[6]'
incrementBtn = '(//XCUIElementTypeOther[@name="plus-image"])[1]'
pkrSt = '(//XCUIElementTypeStaticText[@name="text"])[4]'
discounts = '(//XCUIElementTypeStaticText[@name="text"])[6]'
pkrOt = '(//XCUIElementTypeStaticText[@name="text"])[8]'


# create coupons
couponPayload = {"name": "testautomation", "start_date": "2021-11-16", "end_date": "2021-11-25", "coupon_customer": [],
           "discount_value": 10, "disabled": False, "discount_type": 1, "location_id": "210", "business_unit_id": "233",
           "company_id": 4, "coupon_customer_option_id": 1, "products_list_type": 0, "min_coupon_limit": "100",
           "max_discount_value": 0, "max_usage_per_customer": 0, "user_type": "[8]", 'name': "hello"}
coupon_headers = {
    'authorization': os.getenv('HYPR_AUTH'),
    'Content-Type': 'application/json',
    'Cookie': os.getenv('HYPR_COOKIE')
}
