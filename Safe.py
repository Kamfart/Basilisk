from pymongo import MongoClient

class Safe(object):
    client = MongoClient('localhost', 27017)
    db = client.basilisk
    collection = None

    def connect(self, user):
        self.collection = self.db[user]
    
    def getTable(self,user,table):
        cursor = self.collection.find({}, {'_id':0})
        # print(cursor)
        documents = []
        for doc in cursor:
            # buff = []
            # buff.append(doc['Title'])
            # buff.append(doc['Username'])
            # buff.append(doc['Passwd'])
            documents.append(doc)
        print(documents)
        return documents