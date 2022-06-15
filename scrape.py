#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import re

with open('config.yaml') as f:
    config = yaml.safe_load(f)

class Event:
    def __init__(self, item):
        self.link = "https://www.meetup.com" + item.find(href=True)['href']
        self.title = item.select('.eventCardHead--title')[0].get_text()
        self.date = item.select('.eventTimeDisplay-startDate')[0].get_text()
        self.description = re.sub('Discord.*\n','', item.select('.description-markdown--p')[0].get_text() )
    def readable(self):
        out='----------------------------------------\n'
        string = out + self.link + '\n' + self.title + '\n' + self.date + '\n' + self.description + '\n'
        return string

def scrape():
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    url= config['meetup_url']
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'lxml')
    total=""
    for item in soup.select('.eventCard'):
        try:
            new = Event(item).readable()
            total += new
        except Exception as e:
            #raise e
            print('')
    return total

if __name__ == "__main__":
    print(scrape())
