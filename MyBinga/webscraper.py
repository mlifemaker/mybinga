#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib2

def webscraper(site, hdr):
    req=urllib2.Request(site, headers=hdr)
    try:
        page=urllib2.urlopen(req)
        content=page.read()
        return content

    except urllib2.HTTPError,e:
        print e.fp.read()
    
    #soup=BeautifulSoup(html, "lxml")








if __name__=="__main__":
    
    hdr={'Accept':'text/html,application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8'}
    site="http://www.bkam.ma"
    soup=webscraper(site, hdr)
    print(soup)
