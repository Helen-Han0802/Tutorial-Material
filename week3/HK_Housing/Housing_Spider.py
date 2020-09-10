# coding=utf-8
import requests
import json
import csv

url = "https://data.28hse.com/en/webservice"

for page in range(1,2):
	start = (page-1)*10
	payload = {
		'draw':str(page),
		'columns[0][data]':'date',
		"columns[0][name]":"",
		'columns[0][searchable]':'true',
		'columns[0][orderable]':'false',
		'columns[0][search][value]':'',
		'columns[0][search][regex]':'false',
		'columns[1][data]':'catfathername',
		'columns[1][name]':'',
		'columns[1][searchable]':'true',
		'columns[1][orderable]':'false',
		'columns[1][search][value]':'',
		'columns[1][search][regex]':'false',
		'columns[2][data]':'catname',
		'columns[2][name]':'',
		'columns[2][searchable]':'true',
		'columns[2][orderable]':'false',
		'columns[2][search][value]':'',
		'columns[2][search][regex]':'false',
		'columns[3][data]':'price',
		'columns[3][name]':'',
		'columns[3][searchable]':'true',
		'columns[3][orderable]':'false',
		'columns[3][search][value]':'',
		'columns[3][search][regex]':'false',
		'columns[4][data]':'winloss',
		'columns[4][name]':'',
		'columns[4][searchable]':'true',
		'columns[4][orderable]':'false',
		'columns[4][search][value]':'',
		'columns[4][search][regex]':'false',
		'columns[5][data]':'area',
		'columns[5][name]':'',
		'columns[5][searchable]':'true',
		'columns[5][orderable]':'false',
		'columns[5][search][value]':'',
		'columns[5][search][regex]':'false',
		'columns[6][data]':'sq_price',
		'columns[6][name]':'',
		'columns[6][searchable]':'true',
		'columns[6][orderable]':'false',
		'columns[6][search][value]':'',
		'columns[6][search][regex]':'false',
		'columns[7][data]':'addr',
		'columns[7][name]':'',
		'columns[7][searchable]':'true',
		'columns[7][orderable]':'false',
		'columns[7][search][value]':'',
		'columns[7][search][regex]':'false',
		'columns[8][data]':'contract',
		'columns[8][name]':'',
		'columns[8][searchable]':'true',
		'columns[8][orderable]':'false',
		'columns[8][search][value]':'',
		'columns[8][search][regex]':'false',
		'columns[9][data]':'addr',
		'columns[9][name]':'',
		'columns[9][searchable]':'true',
		'columns[9][orderable]':'false',
		'columns[9][search][value]':'',
		'columns[9][search][regex]':'false',
		'start':str(start),
		'length':'10',
		'search[value]':'',
		'search[regex]':'false',
		'cmd':'area_deals',
		'area_id':'3' # New Te
	}

	wb_data = requests.post(url, data= payload)
	print('--------------')
	print(str(page))
	data= wb_data.text
	print(data)