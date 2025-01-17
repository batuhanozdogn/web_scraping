# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MhJ9rKORkBLyBRgF8jl8bWNEsEQNQiyL
"""

import requests
import json
import pandas as pd

url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    try:
        data = response.json()
        df = pd.DataFrame(data)
        print(df.head())
    except json.JSONDecodeError:
        print("Error decoding JSON response")
else:
    print(f"Failed to retrieve data: {response.status_code}")

response_text=response.text
print(response_text)

response_text = response.text

json_object = json.loads(response_text)

with open("OC.json", "w") as outfile:
    json.dump(json_object, outfile, indent=4)
data = json_object["records"]["data"]
print(type(data))

print(type(json_object))
print(json_object.keys())
print(json_object["records"])
json_object['records'].keys()

print(type(json_object['records']['data']))
e_date=json_object['records']['expiryDates']
print(e_date)

oc_data = {}
for ed in e_date:
    oc_data[ed] = {"CE": [], "PE": []}
    for di in range(len(data)):
        if data[di]['expiryDate'] == ed:
            if 'CE' in data[di]:
                oc_data[ed]["CE"].append(data[di]['CE'])
            else:
                oc_data[ed]["CE"].append('_')

            if 'PE' in data[di] and data[di]['PE']['expiryDate'] == ed:
                oc_data[ed]["PE"].append(data[di]['PE'])
            else:
                oc_data[ed]["PE"].append('_')

oc_data.keys()