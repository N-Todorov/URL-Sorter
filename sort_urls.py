print("""

 _   _ ____  _       ____             _            
| | | |  _ \| |     / ___|  ___  _ __| |_ ___ _ __ 
| | | | |_) | |     \___ \ / _ \| '__| __/ _ \ '__|
| |_| |  _ <| |___   ___) | (_) | |  | ||  __/ |   
 \___/|_| \_\_____| |____/ \___/|_|   \__\___|_|   

    Welcome to ULR Sorter!
    'exit' - exits and saves the progress from the previous url
    'skip' - skips the url
    Once you choose a browser, the program will open the urls one by one
    waiting for you to choose a category for each one.
      
""")



import os
import subprocess
import json
from os.path import exists
from bs4 import BeautifulSoup
import requests

def get_browser():

    if browser == 'chrome':
        try:
            browser_path = 'C:/Program Files (x86)/Google/Chrome/Application/' # change chrome path if needed
            os.chdir(browser_path)
            subprocess.run(["chrome.exe", "--incognito", url])
        except:
            print("Error finding the path to the browser.")



    if browser == 'edge':
        try:
            browser_path = 'C:/Program Files (x86)/Microsoft/Edge/Application' # change edge path if needed
            os.chdir(browser_path)
            subprocess.run(["msedge.exe", "-inprivate", url])
        except:
            print("Error finding the path to the browser.")



    if browser == 'firefox':
        try:
            browser_path = 'C:/Program Files/Mozilla Firefox' # change firefox path if needed
            os.chdir(browser_path)
            subprocess.run(["firefox.exe", "-private-window", url])
        except:
            print("Error finding the path to the browser.")
    

    #    cmd = r'C:\Users\Igor\AppData\Local\Programs\Opera\launcher.exe --private --remote <url>'
    if browser == 'opera':
        try:
            browser_path = 'C:/Program Files/Opera' # change opera path if needed
            os.chdir(browser_path)
            subprocess.run(["Launcher.exe", "--private", url])
        except:
            print("Error finding the path to the browser.")

def save_data():
    os.chdir(os.path.dirname(__file__))
    with open('data.json', 'w') as file:
        json.dump(data, file)                                                                                                  

def clean_data():
  keys = []
  for key in data.keys():
    if data[key] == []:
      print()
      keys.append(key)
  
  for key in keys:
    del data[key]

def print_data():
    with open('sorted.html', 'w') as sorted_html:
        sorted_html.write('''
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<meta http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'none'; img-src data: *; object-src 'none'"></meta>
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>

<DL><p>
''')
        for key in data.keys():
            sorted_html.write(f'    <DT><H3>{key}</H3>\n    <DL><p>\n')
            for value in data[key]:
                site = requests.get(value).content
                soup = BeautifulSoup(site, 'html.parser')
                title = soup.find('title')
                title = title.get_text()
                sorted_html.write(f'        <DT><A HREF="{value}">{title}</A>\n    </DL>\n')
                
        sorted_html.write('</DL><p>')


# get favorites file
files = os.listdir(os.getcwd())

for file in files:
    if file == 'urls.md':
        urls_file = file


#create a data.json
if exists('data.json') == False:
    with open('data.json', 'w') as file:
            json.dump({}, file)

browser = input('Browser (chrome / edge / firefox / opera): ')

with open(urls_file, 'r') as urls_file:
  urls = urls_file.read().splitlines()

data = json.load(open('data.json'))



#get list size to continue from before
data_size = 0 #?
#cant i just len(data.values)?
for value in data.values():
    for item in value:
        data_size += 1

#fix? logic is kinda dumb

if input('Do you want to contrinue? (y/n) ') == 'y':
    if data == {}: 
        print('No data to load')
    else:
        del urls[:data_size]
        #no duplicates
else:
    data = {}
    



#open urls and sort them

for url in urls: 
    get_browser()
    name = input('Category: ')

    if name == 'skip':
        continue

    if name == 'exit':
            #remove last url for duplicates
            data[last_name].pop()
            clean_data()
            save_data()
            print_data()
            break

    if name not in data:
        data[name] = []

    data[name].append(url)
    last_name = name

clean_data()
save_data()



#Loading...
#Loaded!
#while waiting to find browser path

#for value in data.values():
 #   print(data.values)

#how to find firefox.exe or msedge.exe

#should get_browser run in the url for? for now not possible

#invalid escape sequence

#you can later get the data.json and do something with it

#add Notes.md to the urls

#get only specific bookmarks folder

#get urls from urls.md
