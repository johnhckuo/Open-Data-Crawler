#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
import sys
import timeit
import msvcrt
from selenium.webdriver.common.by import By
import urllib
import urllib2
import xml.etree.ElementTree as ET
import json
import datetime
import re
import csv

year = ['104', '105']
month = '5'

def __getElement__(code, type):
	if type=="id":
		return driver.find_element_by_css_selector("#"+code);
	else:
		return driver.find_element_by_css_selector("."+code);
		
def inputDate(year, startMonth, endMonth, cityCode):

	el = __getElement__("goodsCodeType","id");
	for option in el.find_elements_by_tag_name('option'):
		if option.text == u"6碼":
			option.click() # select() in earlier versions of webdriver
			break

	driver.find_element_by_id('goodsCodeValue').clear()
	el = driver.find_element_by_css_selector("#goodsCodeValue");
	el.send_keys(cityCode)
	
	el = __getElement__("START_YEAR","id");
	for option in el.find_elements_by_tag_name('option'):
		if option.text == year:
			option.click() # select() in earlier versions of webdriver
			break
			
	el = __getElement__("START_MONTH","id");
	for option in el.find_elements_by_tag_name('option'):
		if option.text == startMonth:
			option.click() # select() in earlier versions of webdriver
			break
			
	el = __getElement__("END_MONTH","id");
	for option in el.find_elements_by_tag_name('option'):
		if option.text == endMonth:
			
			option.click() # select() in earlier versions of webdriver
			break
			
	el = driver.find_elements_by_xpath("//*[contains(text(), '國家檢索')]")[0]
	el.click()
	
	time.sleep(3);
	
	el = __getElement__("areaList","id");
	for option in el.find_elements_by_tag_name('option'):
		if option.text == u"全部國家":
			option.click() # select() in earlier versions of webdriver
			break
			
	el = __getElement__("from_select_by_Continent","id");
	for option in el.find_elements_by_tag_name('option'):
		if option.text == u"全部國家合計":
			option.click() # select() in earlier versions of webdriver
			break
	
	el = driver.find_elements_by_xpath("//*[contains(text(), '全部增加')]")[0]
	el.click()
	
	el = driver.find_elements_by_xpath("//*[contains(text(), '選取完成')]")[0]
	el.click()
	
	el = __getElement__("ExportTotal", "id")
	el.click()
	
	
	el = __getElement__("ctl00_ContentPlaceHolder1_rbMoney2", "id")
	el.click()
	
	el = __getElement__("SEARCH", "id")
	el.click()
	

	#str = str.encode('Big5','ignore')
	el = driver.find_elements_by_xpath("//*[@value='匯出至csv']")[0]
	el.click()
	driver.back()

	


if __name__ == "__main__":
	

	csvArr ='';
	
	print "initialize file reading session"
	file = open('C:/Users/Johnhckuo/Downloads/good.csv', 'r')
	content = file.read()
	csvArr = content.split(",")
	print csvArr
	start = timeit.default_timer()
	print "done"
	print "Initializing Page Loading/Login Sequence"
	driver = webdriver.Chrome(executable_path=r"C:\Users\Johnhckuo\Desktop\chromedriver_win32\chromedriver.exe") # 啟動 chromedriver
	driver.get('https://portal.sw.nat.gov.tw/APGA/GA03'); # 首頁
	print "done"
	print "selenium part started"
	for i in range(len(csvArr)):
		for j in range(len(year)):
			inputDate(year[j], '1', month, csvArr[i])
	
	
# prints the first base:OBS_VALUE it finds

#	writer=csv.writer(f, lineterminator='\n')
#	f.write(dateList[i].encode("Big5", 'ignore')+ ',' + audienceList[i].encode("Big5", 'ignore')+ ',' + contentList[i].encode("Big5", 'ignore')) # python will convert \n to os.linesep
#	writer.writerow('')
#root.write("filename.xml")
#search_box3 = driver.find_elements_by_class_name("uiTextareaAutogrow _552m");
#search_box3.send_keys('哈囉');
#search_box3.submit();
#http://stackoverflow.com/questions/11289496/how-to-deal-with-not-well-formed-character-in-xml-file-with-elementtree-in-pytho
#http://stackoverflow.com/questions/3064247/cant-parse-xml-effectively-using-python
#http://stackoverflow.com/questions/13046240/parseerror-not-well-formed-invalid-token-using-celementtree/20204635#20204635
#http://lxml.de/index.html
#https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=etree+nonetype+