#this script gets all of the urls from a bookmarks.html file and a clean urls file
#it writes them to the parent direcory

import os
from pathlib import Path
from bs4 import BeautifulSoup
from os.path import exists

options = input('''What do you want to get?
            1.Bookmarks
            2.Urls
            3.Both
          ''')

def get_bookmarks():

    for link in soup.find_all('a'):
        url = link.get('href')
        if url.endswith('/'):
            url = url[:-1]
        urls.append(url)
        create_urls_file.write(url + '\n')


def get_urls():
    
    for link in links:
        if link.endswith('/'):
            link = link[:-1]
        create_urls_file.write(link + '\n')

urls = []
files = os.listdir(os.getcwd())

#get bookmarks file
for file in files:
    if file == 'bookmarks.html':
        bookmarks_path = file

for file in files:
    if file == 'links.md':
        urls_file = file

if exists('bookmarks.html'):
    with open(bookmarks_path, 'r', encoding='utf-8') as bookmarks:
        html_content = bookmarks.read()

soup = BeautifulSoup(html_content, 'lxml')

created_file = 'urls.md'
save_path = os.path.join(os.getcwd(), created_file)

if exists('links.md'):
    with open(urls_file, 'r') as urls_file:
        links = urls_file.read().splitlines()
  
with open(save_path, 'w') as create_urls_file:

    if options == '1':
        get_bookmarks()
    if options == '2':
        get_urls()
    if options == '3':
        get_bookmarks()
        get_urls()


