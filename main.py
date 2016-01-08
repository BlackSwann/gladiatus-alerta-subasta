__author__ = 'BlackSwan'


from lxml import html
from lxml import etree
import requests
import browsercookie
import winsound
import easygui
import time

import sys


while(True):
    cj = browsercookie.firefox()
    page = requests.get(sys.argv[1], cookies=cj)

    tree = html.fromstring(page.content)

    counter = 0



    status = tree.xpath('//*[@id="content"]/p[2]/span[2]/b')

    if status[0].text == "corto":
        if counter == 0 :
            easygui.msgbox("CORTO")
        break
    if status[0].text == "muy corto":
        winsound.Beep(300,2000)
        easygui.msgbox("MUY CORTO")
        break
    else :
        print status[0].text


    time.sleep(60)

