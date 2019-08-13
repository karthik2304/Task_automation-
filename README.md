# Task_automation-
The chat system do's task based on speech recognition  
import os
import random
import webbrowser
import wikipedia
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from random import *
'''import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("speak")
    audio=r.listen(source)
    try:
   text=r.recognize_google(audio)'''
'''path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

'''

def wifi():
    import os
    text=input("wifi on/off")
    if(text=="wifion"):
        os.system('netsh wlan connect name="BSNL_BB"')
        print("successfully wifi on")
    elif (text=="wifioff"):
        os.system("netsh wlan disconnect")
        print("wifi offed")
    



def news():
    news_url="https://news.google.com/news/rss"
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()
    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")
    for news in news_list:
      print(news.title.text)
      print(news.link.text)
      print(news.pubDate.text)
      print("-"*60)
      
def browser():
    text=input("enter something")
    print('you said:{}'.format(text))
    if 'search' in text:
        webbrowser.open('https://www.google.com/search?q='+text)
    elif 'google' in text:
        webbrowser.open("google.com")

    elif 'youtube' in text:
        webbrowser.open("youtube.com")

    elif 'gmail' in text:
        webbrowser.open("https://www.google.com/gmail/")

    elif 'facebook' in text:
        webbrowser.open("facebook.com")

    elif 'wikipedia' in text:
        srch=input()
        print(wikipedia.summary(srch,sentences=3))
    else:
        print("results nt found")
            
def os():
    import os
    mycmd=input('what you want me to open')
            #plays('what you want me to open')
    if 'calculator' in mycmd.lower():
        os.system('start calc.exe')
    elif 'notepad' in mycmd.lower():
        os.system('start notepad.exe')
    elif 'chrome' in mycmd.lower():
        os.system('start chrome.exe')
    elif 'settings' in mycmd.lower():
        os.system('start control.exe')
    elif 'c m d' in mycmd.lower() or 'command' in mycmd.lower():
        os.system('start cmd.exe')
    elif 'word' in mycmd.lower():
        os.system('start winword.exe')
    elif 'powerpoint' in mycmd.lower() or 'ppt' in mycmd.lower():
        os.system('start powerpnt.exe')
    elif 'excel' in mycmd.lower() or 'ppt' in mycmd.lower():
        os.system('start excel.exe')
    elif 'camera' in mycmd.lower() or 'camera' in mycmd.lower():
        os.system('start microsoft.windows.camera:')

def main():
    while(1):
        a=input("enter")
        if a.lower()=='os' or 'os' in a.lower() :
            os()
        elif a.lower()=='browser' or 'browser' in a.lower():
            browser()
        elif a.lower()=='wifi' or 'wifi' in a.lower():
            wifi()
        elif a.lower()=='news' or 'news' in a.lower():
            news()

main()
