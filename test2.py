from selenium import webdriver
import time 
from bs4 import BeautifulSoup
from datetime import datetime
# start Web Browser
browser = webdriver.Firefox()

browser.get('https://www.youtube.com/watch?v=6YzGOq42zLk')

toScroll = 500
s_number = 1

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

while True:
	print('--STARTED--TO_SCROOL:{}--SCROLL:{}--'.format(toScroll,s_number))
	time.sleep(1)
	browser.execute_script("window.scrollTo(0, {});".format(toScroll))
	time.sleep(5)
	html = browser.page_source
	soup = BeautifulSoup(html, 'html.parser')

	getMainYorums = soup.find_all('ytd-comment-thread-renderer')

	for getMainYorum in getMainYorums:
		get_comments = getMainYorum.find(id="content-text").text
		get_channels = getMainYorum.find('span',class_="style-scope ytd-comment-renderer").text
		print(get_comments);
		print('----------------------------------------------------------------------\n');
		print(get_channels);
		
	toScroll = toScroll + (s_number * 750)
	s_number = s_number + 1
	print('--ENDED--')



now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
