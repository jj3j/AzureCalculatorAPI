#!/usr/bin/env python3
import requests
import json
from contextlib import redirect_stdout

url = "https://prices.azure.com/api/retail/prices?$filter=priceType%20eq%20%27Consumption%27%20and%20location%20eq%20%27AP%20Southeast%27&$skip=0"
machine = []

while url:
	print("----")
	print("Requesting", url)

	#Send Requests
	response = requests.get(url)
	data = response.json()

	#Grab New Lists
	machine.extend(data['Items'])

	# Update the URL
	url = data['NextPageLink']

with open('machine.txt', 'a', encoding='utf-8') as f:
	json.dump(machine, f, ensure_ascii=False, indent=4)
