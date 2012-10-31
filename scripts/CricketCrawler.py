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
        self.crawler_url = "http://www.espncricinfo.com"
        self.target_div = "ciHomeTopHeadlines"
        self.newstitle_div = "NewsTitle"
        self.news_article_div = "stryCntnr"
        self.site_soup = None
        self.news_links = []
    
    def crawl(self):
        '''
            Opens a connection to Cricinfo and gets the HTML source from the homepage
        '''
        # Open the HTTP connection to cricinfo.com
        site_connection = urlopen(self.crawler_url)
        # Read the contents of the homepage
        site_src = site_connection.read()
        # Create a BeautifulSoup based on cricinfo's site contents
        self.site_soup = BeautifulSoup(site_src)
        
        self.getHeadline()
        
        '''for news_item in self.news_links:
            news_item_url = news_item.get('href')
            self.openHeadline(news_item_url)'''
        self.openHeadline(self.news_links[0].get('href'))
        
    
    def openHeadline(self, headline_link):
        '''
            Given a URL to a news headline, open that webpage and read it contents
        '''
        article_connection = urlopen(self.crawler_url + headline_link)
        article_src = article_connection.read()
        article_soup = BeautifulSoup(article_src)
        
        article_div = article_soup.select("[class~=" + self.news_article_div + "]")
        
        print(article_div)

    def getHeadline(self):
        '''
            Given the target div and its class name, the crawler finds all the children under it
        '''
        # Find the headlines div
        headline_div = self.site_soup.select("[class~=" + self.target_div + "]")
        
        if len(headline_div) == 1:
            # Retrive all the children with the anchor tag under the news title div
           self.news_links = self.site_soup.find_all("a", class_=self.newstitle_div)
        
        
        