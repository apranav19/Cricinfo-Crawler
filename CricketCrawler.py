'''
Created on Oct 31, 2012

@author: PranavAngara19
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

class CricketCrawler(object):
    '''
    This class represents a cricket crawler. It is a simple web crawler that goes to cricinfo.com
    and finds the latest headlines
    '''

    def __init__(self):
        '''
        Initialize the url to cricinfo.com and set the target class name (div)
        '''
        self.crawler_url = "http://www.cricinfo.com"
        self.target_div = "ciHomeTopHeadlines"
    
    def crawl(self):
        # Open the HTTP connection to cricinfo.com
        site_connection = urlopen(self.crawler_url)
        # Read the contents of the homepage
        site_src = site_connection.read()
        print(site_src.decode("utf-8"))