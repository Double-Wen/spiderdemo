from datasave import DataSave
from htmldownloader import HtmlDownloader
from htmlparse import HtmlParse
from urlmanager import URLManager


class Scheduler:
    def __init__(self, path, base_url, count):
        self.url_manager = URLManager()
        self.data_save = DataSave(path)
        self.html_parser = HtmlParse()
        self.downloader = HtmlDownloader()
        self.root_url = base_url
        self.count = count

    def run_spider(self):
        self.url_manager.save_new_url(self.root_url)
        while self.url_manager.get_new_url_num() and self.url_manager.get_old_url_num() < self.count:
            try:
                url = self.url_manager.get_new_url()
                response = self.downloader.download(url)
                new_urls, data = self.html_parser.parse_data(response, url)
                self.url_manager.save_new_urls(new_urls)
                self.data_save.save(data)
                print("Already spider {} pages".format(len(self.url_manager.old_urls)))
            except Exception as e:
                print("Error", e)


if __name__ == '__main__':
    root_url = "https://www.cnbeta.com/articles/science/967813.htm"
    save_path = './data/hi.txt'
    Spider = Scheduler(save_path, root_url, 50)
    Spider.run_spider()
