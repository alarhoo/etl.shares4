import sharepy
import logging

logging.basicConfig()

class ExtractSharePointFile:
    def __init__(self, site, user, pwd):
        self.site = site
        self.user = user
        self.pwd = pwd

    def connect(self):
        logging.INFO('Connecting to SharePoint: {}'.format(self.site))
        self.sp = sharepy.connect(self.site, self.user, self.pwd)
        return self

    def download_file(self, file_name):
        logging.INFO('Downloading a file: {}'.format(file_name))
        r = self.sp.getfile(file_name, filename='data/Forecast.xlsx')
        print(r)
