import requests


class HtmlDownloader:

    def __init__(self, base_encoding='utf-8'):
        self.encoding = base_encoding

    def download(self, aim_url):
        if aim_url is None:
            return None
        print("Start downloading data, url: {}".format(aim_url))
        response = requests.get(aim_url)
        if response.status_code == 200:
            print("Successfully downloaded")
            response.encoding = self.encoding
            return response.text


if __name__ == '__main__':
    url = 'https://www.bing.com'
    d = HtmlDownloader(url)
    bing_html = d.download(url)
    print(bing_html)
