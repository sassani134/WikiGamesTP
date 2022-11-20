from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import sys

def scrap():

    randomWiki = "https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard"
    soup = BeautifulSoup(urlopen(randomWiki), 'html.parser')
    goal = BeautifulSoup(urlopen(randomWiki), 'html.parser').title.string

    print ("**********The wiki game begin**********")
    print ("The goal is to reach the page : " + goal)
    print (soup.a)
    print (soup.p)
    #Test
    #print (soup.prettify())
    print (BeautifulSoup(urlopen(randomWiki), 'html.parser').h1.string)
    print (soup.title.string)
    for link in soup.find_all('a'):
    #     print(link)
        print(link.get('href'))
        

scrap() 

"""
mw-parser-output
    for link in soup.find_all('a'):
        print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie
"""