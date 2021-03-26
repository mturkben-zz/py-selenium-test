from selenium import webdriver
import time 
from bs4 import BeautifulSoup

# start Web Browser
browser = webdriver.Firefox()

browser.get('https://www.youtube.com/watch?v=6YzGOq42zLk')

toScroll = 500

while True:
	print('--STARTED--')
	time.sleep(1)
	browser.execute_script("window.scrollTo(0, {});".format(toScroll))

	time.sleep(5)

	html = browser.page_source

	soup = BeautifulSoup(html, 'html.parser')


	getMainYorums = soup.find_all('ytd-comment-thread-renderer')

	for getMainYorum in getMainYorums:
		get_comments = getMainYorum.find(id="content-text").text
		get_channels = getMainYorum.find('span',class_="style-scope ytd-comment-renderer").text
		print("===============================")   
		print('KANAL:::',get_channels)
		print("------------------------")   
		print('YORUM:::',get_comments)
		print("===============================")
		
	toScroll = toScroll + 1000
	print('--ENDED--')

