import time
from appium import webdriver
import os


class Driver:
    driver = None
    def __init__(self):

        desiredCap_ios = {
            "platformName": "iOS",
            "appium:platformVersion": "15.2",
            "appium:deviceName": "iPhone 13 mini",
            "appium:automationName": "XCUITest",
            "appium:udid": "4A111176-6F08-4FD0-BE36-BE6D3C49ED89",
            "appium:bundleId": "co.app.retailerapp"
        }

        Driver.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desiredCap_ios)
        time.sleep(5)



# desired_caps = {
#     "avd": os.getenv('AVD'),
#     # "headless": True,
        #     "platformName": "Android",
        #     "platformVersion": "10.0",
        #     "deviceName": "061972516A025250",
        #     "noReset": True,
        #     # "fullReset": False,
        #     "automationName": "uiautomator2",
        #     "systemPort": 8210,
        #     "app": os.getenv('APP'),
        #     "autoGrantPermissions": True
        # }