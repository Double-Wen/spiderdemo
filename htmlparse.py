from lxml import etree
from bs4 import BeautifulSoup
import re
from datasave import DataSave
import requests


class HtmlParse:

    def __init__(self, data=None, aim_url=None):
        if data is None or aim_url is None:
            self.soup = None
            self.page_url = None
        else:
            self.soup = BeautifulSoup(data, 'lxml')
            self.page_url = aim_url

    def parse_data(self, data=None, aim_url=None):
        if data is None or aim_url is None:
            if self.soup is None or self.page_url is None:
                return
            else:
                print("Start analyse data")
                urls = self.get_urls()
                data = self.get_data()
                return urls, data
        self.soup = BeautifulSoup(data, 'lxml')
        self.page_url = aim_url
        print("Start analyse data")
        urls = self.get_urls()
        data = self.get_data()
        return urls, data

    def get_urls(self):
        urls = list()
        links = self.soup.select('a[href*="/science/"]')
        for link in links:
            link_url = link['href']
            urls.append(link_url)
        return urls

    def get_data(self):
        data = {'url': self.page_url}
        title = self.soup.select_one('.cnbeta-article > header > h1')
        data['title'] = title.get_text()
        print("Page url: {}".format(self.page_url))
        print("Data: {}".format(data))
        return data


if __name__ == '__main__':
    url = 'https://www.cnbeta.com/articles/science/967813.htm'
    save = DataSave('./data/hi.txt')
    response = requests.get(url)
    response.encoding = 'utf-8'
    parse = HtmlParse()
    u, d = parse.parse_data(response.text, url)
    save.save(d)
    print(u, d)
