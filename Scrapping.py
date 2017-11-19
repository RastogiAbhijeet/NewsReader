from bs4 import BeautifulSoup
from urllib import request
# from pymongo import
from newspaper import Article
import newspaper
from textblob import TextBlob
from datetime import date
import json
from databaseHandling import InterfaceClass


class ScrapNews(object):
    
    def __init__(self):
        self.listTitleLink = []
        self.obj = InterfaceClass()
        self.listTitleLink = self.obj.validation()
        self.url = request.urlopen("https://news.google.com/news/?ned=us&hl=en")

    def fetchLinks(self):
        soup = BeautifulSoup(self.url,'html.parser')
        for link in soup.find_all("a"):
            x = str(link.get('href'))
            # print(x)
            if x[0] == 'h' or x[0] == '/':
                 if '/section' in x:
                    print(x)

    def fetch_news(self):
        '''
            1. linkAppend : This list is used to avoid the redundancy in fetching the topic links
            2. linkAppendNews : This list is used to avoid the redundancy in fetching the links on individual topic page
        '''

        linkAppend = []
        listAppendNews = []

        soup = BeautifulSoup(self.url,'html.parser')

        # link is an iterable for all the links present on the main Link
        for link in soup.find_all("a"):
            linkLayer_1 = str(link.get('href'))
            if linkLayer_1[0] == 'h':
                # if '/news' in linkLayer_1 and '/topic' in linkLayer_1 and '/section' in linkLayer_1:
                if '/section' in linkLayer_1:
                    linkLayer_1 = 'https://news.google.com/news/' + linkLayer_1
                    if ('topic/BUSINESS' in linkLayer_1 or 'topic/NATION' in linkLayer_1 or 'topic/WORLD' in linkLayer_1 or 'topic/TECHNOLOGY' in linkLayer_1) and linkLayer_1 not in linkAppend:
                        print(linkLayer_1)
                        try:
                            urlLinkLayer_1 = request.urlopen(linkLayer_1)
                            soupLayer_1 = BeautifulSoup(urlLinkLayer_1,'html.parser')
                            count = 0
                            linkAppend.append(linkLayer_1)
                            for targetLink in soupLayer_1.find_all('a'):
                                if count < 20:
                                    tempLink = str(targetLink.get('href'))
                                    # print(tempLink)
                                    if (tempLink[0] == 'h' and ('google' not in tempLink) and ('youtube' not in tempLink) and ('headlines/section/topic/' not in tempLink)) and tempLink not in listAppendNews :
                                        # print("Hello")
                                        print(tempLink)
                                        count+=1
                                        listAppendNews.append(tempLink)
                                        self.process_item(tempLink)
                        except :
                            pass         

    def process_item(self,url_link):
        # obj = InterfaceClass()
        news = Article(url = url_link)
        news.download()
        news.parse()
        x = news.text

        y = news.title
        if y not in self.listTitleLink:
            self.listTitleLink.append(y)
            print("hello")
            sentVal, classValue = self.sentiValue(x)
            jsonObj = {}
            list = []
            list.append(date.today())
            jsonObj['Date'] = str(list[0])
            jsonObj['NewsData'] = x
            jsonObj['NewsTitle'] = y
            jsonObj['Sentiment'] = sentVal
            jsonObj['Classification'] = classValue
            self.obj.insertData(jsonObj)

    def sentiValue(self,x):
        blob = TextBlob(x)
        sentVal  = blob.sentiment.polarity
        classificationValue = None#blob.classify()
        return sentVal, classificationValue

scrapObj = ScrapNews()
scrapObj.fetch_news()


'''
    Program Control

    1. Fetch News()
    2. ProcessItem()
    3. SentiValue()
'''


