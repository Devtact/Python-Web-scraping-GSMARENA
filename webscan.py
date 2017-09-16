import requests
from bs4 import BeautifulSoup


def link_scan(link_url):
    c = 1
    source_code=requests.get(link_url)
    plain_text=source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.find_all('div',{'class':'brandmenu-v2 light l-box clearfix'}):
       for li in link.find_all('li'):
           for anc in li.find_all('a'):
               anc_src = r'http://www.gsmarena.com/' + anc.get('href')
               anc_name = anc.string
               print(c, anc_name,"\n", anc_src, "\n")
               c += 1
               inside_scan(anc_name, anc_src)


def inside_scan(name, hrefs):
    i = 1
    source_code=requests.get(hrefs)
    plain_text=source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.find_all('div',{'class':'makers'}):
       for li in link.find_all('li'):
           for anc in li.find_all('a'):
               anc_src = r'http://www.gsmarena.com/' + anc.get('href')
               for nam in (sp.find('span') for sp in anc.find_all('strong')):
                   modal_name = nam.string
                   #print(name, hrefs, "\n", anc_src, modal_name)
                   print("\t", i, "\t", anc_src, name, modal_name)
                   i += 1

link_scan(r'http://www.gsmarena.com')
