#!/usr/bin/env python
# coding=utf-8

"""
@purpose: collect the number of patents within each search
@author: wenwei peng
@contact: wpengad@ust.hk
@file: Patent_num_by_city_year
@time: 2019-04-04
"""
import urllib
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
from multiprocessing import Pool
import re

def gen_query():
	query = []
	for st in ['CN','KR','JP','DE','TW','HK','SG']:
		for year in range(1976,2019):
			query.append('ISD/{0} AND ABST/(method or process) AND ACN/{1}'.format(year,st))
	return query


def gen_query_all():

	lists = pd.read_csv("CityBoundaries.txt")
	#print(lists['Name'],lists['St'])
	query = []
	for st in lists['St']:
		for year in range(1976,2019):
			query.append('ISD/1/1/{0} AND AS/{1}'.format(year,st))
	return query


def get_num(query):
		
	headers = {

		'ccept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
		'Connection': 'keep-alive',
		'Host': 'patft.uspto.gov',
		'Referer': 'http://patft.uspto.gov/netahtml/PTO/search-adv.htm',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
	}

	param_list= {

		'Sect1': 'PTO2',
		'Sect2': 'HITOFF',
		'u': '/netahtml/PTO/search-adv.htm',
		'r': '0',
		'p': '1',
		'f': 'S',
		'l': '50',
		'Query': query,
		'd': 'PTXT'
	}

	url = 'http://patft.uspto.gov/netacgi/nph-Parser?' + urllib.parse.urlencode(param_list)
	try:
		web_data = requests.get(url, headers = headers)
		if web_data.status_code != 200:
			f = open('Badlist.txt','a',encoding='utf-8',errors='ignore') 
			f.write("\n" + 'query:{0}'.format(query))
			f.close()
			pass

		else:
			if 'No patents have matched your query'in web_data.text:
				out = 0
			elif 'Single Document' in web_data.text:
				out = 1
			else:
				out = re.findall('''<strong>(.*?)</strong>''',web_data.text.lower().strip().replace("\n",""))

			print(query,"=>>>",out)
			f = open('./Output/Num_Q4_2019_05_30.txt','a',encoding='utf-8',errors='ignore') 
			f.write("\n" + 'query:{0}; num:{1};'.format(query,out))
			f.close()
			
	except Exception as e:
		print(e)
		f = open('Badlist.txt','a',encoding='utf-8',errors='ignore') 
		f.write("\n" + 'query:{0}'.format(query))
		f.close()
		pass

if __name__ == '__main__':

	query_list = gen_query()
	for query in query_list:
		get_num(query)

	


