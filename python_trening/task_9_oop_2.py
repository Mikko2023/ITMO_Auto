class Page:

        def __init__(self, url):
            self.url = url

        def __get__(self):
            print(self.url)
home = page ('https://sait.com')
home.get()