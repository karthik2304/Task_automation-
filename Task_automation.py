import pyodbc
conn=pyodbc.connect('Driver={SQL Server};''Server=.;''uid=sa;''pwd=1212;')
#from playsound import playsound
import os
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from random import *
import webbrowser
import wikipedia
'''
def plays(a):
    from gtts import gTTS
    import os
    global i
    tts = gTTS(text=a, lang='en',slow=True)
    i+=1
    z="good"+str(i)+".mp3"
    tts.save(z)
    playsound(z)
'''


'''import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("speak")
    audio=r.listen(source)
    try:
   text=r.recognize_google(audio)'''

def plays(a):
    pass
def opening(b):
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

def wifi():
    import os
    text=input("wifi on/off")
    if(text=="wifion"):
        os.system('netsh wlan connect name="BSNL_BB"')
        print("successfully wifi on")
    elif (text=="wifioff"):
        os.system("netsh wlan disconnect")
        print("wifi offed")
    


      
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
def news():
    news_url="https://news.google.com/news/rss"
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()
    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")
    # Print news title, url and publish date
    for news in news_list[0:5]:
      print(news.title.text)
      print(news.link.text)
      print(news.pubDate.text)
      print("-"*60)



def remember(a):
    ne=input('Do you want to see remember list or Want me to remember something or search in list or delete from list')
    if 'remember' in ne:
        n=input('What you want to remember '+a[0])
        conn.execute('insert into remember values(?)',(n))
        conn.commit()
        print('I Remember it',a[0])
    elif 'mylist' in ne:
        n=conn.execute('select name from remember')
        for b in n:
            print(b[0])
    elif 'search' in ne:
        m=input('you can also search from the list')
        n=conn.execute('select name from remember where name like(?)',('%'+m+'%'))
        for b in n:
            print(b[0])
    elif 'delete' in ne:
        n=conn.execute('select * from remember')
        for b in n:
            print(b[0],b[1])
        y=input('enter the list value to be deleted')
        conn.execute('delete from remember where id=?',(y))
        conn.commit()
        print('deleted successfully')

def send(b):
  try:
    a=input('What do you want to send Email or Sms')
    if 'email'in a.lower():
        import smtplib
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("gmail-id", "password")
        SUBJECT=input('what your subject'+b)
        TEXT=input('what your content'+b)
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        server.sendmail("gmail-id",input('To whom you want to send') , message)
        print('Thank you ur Mail has been sent',b)
    elif "mobile" in a.lower() or 'sms' in a.lower():
        from  urllib.request import urlopen
        msg1=input("enter  your msg below 100 words Each word with + not space "+b)
        mobile=input("enter required moblile no "+b)
        url="https://smsapi.engineeringtgr.com/send/?Mobile=9952363956&Password=HARI&Message="+msg1+"&To="+mobile+"&Key=harih3l4YdeRioJxrw5DM07jcgG"
        file=urlopen(url)
        p=file.read()
        if "true" in str(p).lower():
            print("sent success")
  except:
      print('Some error in sending your mail or sms')
        
def main():
    import pyodbc
    conn=pyodbc.connect('Driver={SQL Server};''Server=.;''uid=sa;''pwd=1212;')
    owner=conn.execute("select iif(gender='m','Sir!',iif(gender='f','Madam!','not said yet')),iif(gender='m','Mr. ',iif(martialstatus='s','Miss. ',iif(martialstatus='m','Mrs. ','not set')))+upper(left(name,1))+SUBSTRING(name,2,20),password from owners")
    for b in owner:
        d=(b[0])
        print("hi how can i help you ")
        plays("hi how can i help you ")
        a=input()
        if a.lower()=='configure'.lower() or 'configure' in a:
            print('Would your like to configure',b[0])
            plays('Would your like to configure'+b[0])
            z=input()
            if 'yes' or 'YES' or 's' in z:
                configure(b[2],b[0])
        elif a.lower()=='news'or 'newspaper' in a.lower() or 'todaynews' in a.lower():
            news()
        elif a.lower()=='bye':
            print('Thank you '+b[0]+'bye')
            plays('Thank you '+b[0]+'bye')
        elif  a.lower()=='opening' or 'opening' in a.lower() or 'open' in a.lower() or 'application' in a.lower():
            opening(b)
        elif 'remember' in  a.lower() or 'save' in a.lower():
            remember(b)
        elif 'send' in a.lower() or 'sms' in a.lower():
            send(d)
        elif a.lower()=='browser' or 'browser' in a.lower():
            browser()
        elif a.lower()=='wifi' or 'wifi' in a.lower():
            wifi()
        else:
            import webbrowser
            webbrowser.open('https://www.google.com/search?q=' + a)
    
def myname():
    global i
    plays('myname')
    a=input('myname')
    owner=conn.execute('select name from myname where id =1')
    for y in owner:
        n=y[0]
    if a.lower()==n.lower():
        owner=conn.execute("select iif(gender='m','Sir!',iif(gender='f','Madam!','not said yet')),iif(gender='m','Mr. ',iif(martialstatus='s','Miss. ',iif(martialstatus='m','Mrs. ','not set')))+upper(left(name,1))+SUBSTRING(name,2,20),password from owners")
        for b in owner:
            d=(b[0])
        start(b[1])
        while(1):
            main()            
            a=input('do you want to continue')
            if a.lower()=='yes'or a.lower()=='s' or 'y'==a.lower():
                continue
            elif a.lower()=='no'or a.lower()=='n':
                break
            else:
                print('wrong selection')
                continue

    elif a.lower()=='bye':
        print('bye')
        plays('Thank you '+b[0]+'bye')
        
    else:
        plays('that not my name')
        print('that not my name')
        myname()


i=0
myname()
