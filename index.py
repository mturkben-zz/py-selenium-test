from selenium import webdriver
import time 
from bs4 import BeautifulSoup
import os
import sys
arg = sys.argv

arg_list = []
_arg = 0

for args in arg:
    arg_list.append(args)

    if _arg == 0:
        arg_list.remove(arg[_arg])
    _arg = _arg + 1

print(arg_list)

argument_list = []
controller_list = []

for catcher in arg_list:
    if catcher[0] == '-':
        controller_list.append(catcher)
    else:
        argument_list.append(catcher)

print(controller_list)
print(argument_list)

def main():
    print('Enter Post Link:')
    getPostLink = input()
    _browser(getPostLink)


def _browser(postLink):
    
    browser = webdriver.Firefox()
    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(3)
    browser.find_element_by_name("//input[@username").send_keys("mturkben721@gmail.com")
    browser.find_element_by_name("//input[@name='password']").send_keys("ryzer346mmt.M")
    browser.find_element_by_xpath("//*[class='dCJp8']").click()
    time.sleep(3)

    browser.get(postLink)

    time.sleep(2)
    html = browser.page_source

    time.sleep(2)
    soup = BeautifulSoup(html, 'html.parser')
    allYorums = soup.find_all('ul', class_="Mr508")

    for yorum in allYorums:
        toTop = yorum.find('div', class_='C4VMK')
        toTopIns = toTop.find_all('span')
        index = 0
        for toTop in toTopIns:
            if (index % 2 == 0):
                print('name::',toTop.text)
            else:
                print('comment',toTop.text)
            index = index + 1
    time.sleep(2)
    browser.close()

main()