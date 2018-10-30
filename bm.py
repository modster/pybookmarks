'''
This program cleans up the bookmarks.html file exported from chrome which uses netscape bookmarks format 
Author: Mike Greeff
Dependencies: BeautifulSoup
'''

from bs4 import BeautifulSoup

with open("modster-bookmarks-copy.html") as fp:
    soup = BeautifulSoup(fp , features="html.parser")

a_list = soup.find_all('a')

for each_a in a_list:
    a_date = each_a.attrs['add_date']
    a_str = each_a.string
    a_href = each_a.attrs['href']
    print(a_date, a_str, a_href, sep=",")