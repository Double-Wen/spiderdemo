class URLManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def save_new_url(self, url):
        if url is not None:
            if url not in self.new_urls and url not in self.old_urls and url[0:8] == 'https://':
                print("Save new url{}".format(url))
                self.new_urls.add(url)

    def save_new_urls(self, url_list):
        for url in url_list:
            self.save_new_url(url)

    def get_new_url_num(self):
        return len(self.new_urls)

    def get_old_url_num(self):
        return len(self.old_urls)

    def get_new_url(self):
        if self.get_new_url_num() > 0:
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None
