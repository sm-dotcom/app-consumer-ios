import json
import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

payload = {}

login_headers = {
    'Content-Type': 'application/json',
    'App-Type': 'CONSUMER',
    'language': 'EN',
    'Cookie': os.getenv('COOKIE')
}


login_payload = json.dumps({
    "username": "92" + os.getenv('PHONE_NO_1'),
    "password": os.getenv('PASSWORD')
})


def LoginToken():
    response = requests.request("POST", os.getenv('login'), headers=login_headers, data=login_payload)
    return response.json()['data']['token']


consumer_header = {
    'Authorization': LoginToken(),
    'language': 'EN',
    'Cookie': os.getenv('COOKIE')
}

admin_Header = {
    'authority': 'stageapi.retailo.me',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'text/plain',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkX2F0IjoiMjAyMC0wOC0zMVQwNzowMDo1Ny4wMDBaIiwidXBkYXRlZF9hdCI6IjIwMjAtMDgtMzFUMDc6MDA6NTcuMDAwWiIsImRlbGV0ZWRfYXQiOm51bGwsImlkIjoxNjAsIm5hbWUiOiJoYXNoX2EiLCJ1c2VybmFtZSI6Imhhc2hfYSIsImRpc2FibGVkIjpmYWxzZSwicGhvbmUiOiIwOTAwNzg2MDEiLCJjbmljX3BpY3R1cmUiOiIiLCJjbmljIjoiMTIzMTIzMTIzIiwiYWRkcmVzcyI6IjEyMzIzIiwiZW1haWwiOiJtdWhhbW1hZC5zaXJhakByZXRhaWxvLmNvIiwiZGVsZXRlZF9ieSI6bnVsbCwicm9sZSI6eyJjcmVhdGVkX2F0IjpudWxsLCJ1cGRhdGVkX2F0IjpudWxsLCJkZWxldGVkX2F0IjpudWxsLCJpZCI6OSwibmFtZSI6IkNPTVBBTlkgT1dORVIifSwiYWNjZXNzSGllcmFyY2h5Ijp7ImNvbXBhbmllcyI6WzRdLCJidXNpbmVzc191bml0cyI6WzQsMjYsMjcsMjIyLDIyMywyMjUsMjI4LDIyOSwyMzAsMjMxLDIzMiwyMzMsMjM0XSwibG9jYXRpb25zIjpbNyw4LDksMTAsMTMsNzgsODEsOTMsMTAxLDE0OCwxOTEsMTk0LDE5NSwxOTYsMjAxLDIwMiwyMDMsMjA0LDIwNSwyMDYsMjA3LDIwOCwyMDksMjEwLDIxMSwyMTJdfSwic2Vzc2lvbl91dWlkIjoiMDYzNzM4NGYtZDFkNi00ZjhlLWFkMTMtYWJlNDllZTRlNjhhIiwiaWF0IjoxNjQwNzg1MjAwLCJhdWQiOiJoeXByLnBrIiwiaXNzIjoiaHlwci5wayJ9.aZLmEivFBZ3v4sbqnI2T7zTBYfKlg2t4OKyHSdTorHA',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'sec-ch-ua-platform': '"Linux"',
    'origin': 'https://stageadmin.retailo.me',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://stageadmin.retailo.me/',
    'accept-language': 'en-US,en;q=0.9',
    'Cookie': 'sails.sid=s%3AzOu9CUFGfiKDHmwEY0G8BYsJGkQgB774.w0e5Kj9kW3bI3RGjWKwwVrmJV1oMrsoqUKX6dI0JK9A'
}


def getL1CatNames():
    cat = []
    response = requests.request("GET", os.getenv('getCatsByLoc'), headers=consumer_header, data={})
    # print(response.json())
    for i in response.json()['data']['categories']:
        cat.append(i['name'])
    return cat


def getL2CatNames():
    cat = []
    response = requests.request("GET", os.getenv('getCatsByL1'), headers=consumer_header, data={})
    for i in response.json()['data']['categories']:
        cat.append(i['name'])
    return cat



def updateMaxMinForLocation(locationId, min_order_limit, max_order_limit):
    import requests
    url = f"https://stageapi.retailo.me/location/{locationId}"
    locationPayload = f'{{"priority": 1,"disabled": false,"company_id": 4,"image_url": "","service_charge_type": "FLAT","service_charge_value": 0,"delivery_charge_type": "FLAT","delivery_charge_value": 0,"min_order_limit": {min_order_limit},"max_order_limit": {max_order_limit},"is_day_wise_time": false,"delivery_time": "12:00:00","operating_days": [{{"created_at": "2021-01-25T05:45:31.000Z","updated_at": "2021-11-24T15:51:31.000Z","deleted_at": null,"id": 1115,"start_time": "00:00:00","end_time": "23:59:00","disabled": false,"day_id": 1,"location_id": {locationId},"day_name": "Sunday"}},{{"created_at": "2021-01-25T05:45:31.000Z","updated_at": "2021-11-24T15:51:31.000Z","deleted_at": null,"id": 1116,"start_time": "00:00:00","end_time": "23:59:00","disabled": false,"day_id": 2,"location_id": {locationId},"day_name": "Monday"}},{{"created_at": "2021-01-25T05:45:31.000Z","updated_at": "2021-11-24T15:51:31.000Z","deleted_at": null,"id": 1117,"start_time": "00:00:00","end_time": "23:59:00","disabled": false,"day_id": 3,"location_id": {locationId},"day_name": "Tuesday"}},{{"created_at": "2021-01-25T05:45:31.000Z","updated_at": "2021-11-24T15:51:31.000Z","deleted_at": null,"id": 1114,"start_time": "00:00:00","end_time": "23:59:00","disabled": false,"day_id": 4,"location_id": {locationId},"day_name": "Wednesday"}},{{"created_at": "2021-01-25T05:45:31.000Z","updated_at": "2021-11-24T15:51:31.000Z","deleted_at": null,"id": 1118,"start_time": "00:00:00","end_time": "23:59:00","disabled": false,"day_id": 5,"location_id": {locationId},"day_name": "Thrusday"}},{{"created_at": "2021-01-25T05:45:31.000Z","updated_at": "2021-11-24T15:51:31.000Z","deleted_at": null,"id": 1119,"start_time": "00:00:00","end_time": "23:59:00","disabled": false,"day_id": 6,"location_id": {locationId},"day_name": "Friday"}},{{"created_at": "2021-01-25T05:45:31.000Z","updated_at": "2021-11-24T15:51:31.000Z","deleted_at": null,"id": 1120,"start_time": "00:00:00","end_time": "23:59:00","disabled": false,"day_id": 7,"location_id": {locationId},"day_name": "Saturday"}}],"events": []}}'
    response = requests.request("PUT", url, headers=admin_Header, data=locationPayload)
    # pprint(response.json())


def updateProduct(productId, price, disable, locationId):
    url = f"https://stageapi.retailo.me/product/updateProduct?location_id={locationId}"
    payloadProduct = json.dumps({
        "id": productId,
        "price": price,
        "disabled": disable,
        "multilingual": []
    })
    headersProduct = {
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkX2F0IjoiMjAyMC0wOC0zMVQwNzowMDo1Ny4wMDBaIiwidXBkYXRlZF9hdCI6IjIwMjAtMDgtMzFUMDc6MDA6NTcuMDAwWiIsImRlbGV0ZWRfYXQiOm51bGwsImlkIjoxNjAsIm5hbWUiOiJoYXNoX2EiLCJ1c2VybmFtZSI6Imhhc2hfYSIsImRpc2FibGVkIjpmYWxzZSwicGhvbmUiOiIwOTAwNzg2MDEiLCJjbmljX3BpY3R1cmUiOiIiLCJjbmljIjoiMTIzMTIzMTIzIiwiYWRkcmVzcyI6IjEyMzIzIiwiZW1haWwiOiJtdWhhbW1hZC5zaXJhakByZXRhaWxvLmNvIiwiZGVsZXRlZF9ieSI6bnVsbCwicm9sZSI6eyJjcmVhdGVkX2F0IjpudWxsLCJ1cGRhdGVkX2F0IjpudWxsLCJkZWxldGVkX2F0IjpudWxsLCJpZCI6OSwibmFtZSI6IkNPTVBBTlkgT1dORVIifSwiYWNjZXNzSGllcmFyY2h5Ijp7ImNvbXBhbmllcyI6WzRdLCJidXNpbmVzc191bml0cyI6WzQsMjYsMjcsMjIyLDIyMywyMjUsMjI4LDIyOSwyMzAsMjMxLDIzMiwyMzMsMjM0XSwibG9jYXRpb25zIjpbNyw4LDksMTAsMTMsNzgsODEsOTMsMTAxLDE0OCwxOTEsMTk0LDE5NSwxOTYsMjAxLDIwMiwyMDMsMjA0LDIwNSwyMDYsMjA3LDIwOCwyMDksMjEwLDIxMV19LCJzZXNzaW9uX3V1aWQiOiI1NTQyMTk2YS00MGM3LTQzNTAtODU2OC0wODljNGI1MzFjZWMiLCJpYXQiOjE2NDAyNjk1NzUsImF1ZCI6Imh5cHIucGsiLCJpc3MiOiJoeXByLnBrIn0.3DpN1eizw0eMOyJpE2uKZ34ljJYQ9_nwYHDCctAMePA',
        'Content-Type': 'application/json',
        'Cookie': 'sails.sid=s%3Atn6VpwcXa3pvdQh2K3uIss4GCSb6iAK9.SU4LQwN1aD6A6l5vgo3RkkdC2xERCCwgS4QsCDrCies'
    }
    response = requests.request("POST", url, headers=headersProduct, data=payloadProduct)
