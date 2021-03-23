import requests
from bs4 import BeautifulSoup
from threading import Thread

mas=['?znak=sagittarius','?znak=aries','?znak=taurus','?znak=gemini','?znak=cancer','?znak=leo']
r='https://1001goroskop.ru/'

class Tred(Thread):
    def __init__(self,r):
        Thread.__init__(self)

        self.r=r
        self.start()


    def run(self):
         print(ness(htmlhochy(self.r))+"\n")



def htmlhochy(r):

    return requests.get(r).text



def ness(html):
    he= BeautifulSoup(html)
    t=he.find('div', itemprop="description").text
    return t

for i in range (6):
    tyt=r+mas[i]
    Tred(tyt)
