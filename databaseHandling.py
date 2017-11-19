from pymongo import MongoClient

'''
        VARIABLE DECLARATION
        1. NewsData is the name of the database in mongoDb
        2. newTable is the name of the collection in mongoDb

        AIM OF INTERFACE CLASS
        1. To send the newspaper article to the database
        2. To fetch the data from the database where Classification == 'positive'

        STRUCTURE OF THE DATABASE

        {
            'NewsData': <contains article>
            'NewsTitle' : <contains title of the article>
            'Date' : <contains the date, when the article was posted>
            'Sentiment' : <contains the polarity for the article>
            'Classification : <contains the classification for the article>
        }
'''

class InterfaceClass(object):
    def __init__(self):
        self.dbObj = MongoClient('localhost', 27017)
        self.collection = self.dbObj.NewsData
        print("Connected to database")

    def insertData(self, jsObj):
        # print(jsObj)
        try:
            if jsObj['NewsData'] != None and len(jsObj['NewsData'])>40:
                record = self.collection.newsTable.insert(jsObj)
                print("data added")
        except Exception:
            print("Could not insert Data")
    # a method from the gui class will call this function in order the fetch the news from the data with the required sentiment value
    def fetchData(self):
        try:
            # print("hello")
            data = self.collection.newsTable.find()
            return data
        except Exception:
            pass
            
    def validation(self):
        try:
            # print("hello")
            # validTitle = str(jsObj['NewsTitle'])
            # print("Validate title :", validTitle)
            data = self.collection.newsTable.find()
            datalist = []
            list = []
            for document in data:
                datalist.append(document["NewsTitle"])
            return datalist

        except Exception:
            pass

# jsonObj = {}
# jsonObj['Date'] = "21-01-2142"
# jsonObj['NewsData'] = "x"
# jsonObj['NewsTitle'] = "sadfsadf"
# jsonObj['Sentiment'] = "sentVal"
# jsonObj['Classification'] = "positive"
# obj = InterfaceClass()
# obj.insertData(jsonObj)
# obj.fetchData()
# obj.validation()
# dict = obj.fetchData()
# listy = []
# for document in dict:
#     listy.append(document)
#
# print(listy[0]["NewsTitle"])

