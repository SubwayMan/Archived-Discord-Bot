#database for more user interaction
import pymongo
import env_variables
from pymongo import MongoClient

#load databases
cluster = MongoClient(env_variables.Database_log)
db = cluster['Discordbot']
collection = db['UserData']

#other data for ease of use
dataholes = [] #for if a member leaves, his/her id is freed up
#DELETES ALL DATABASE CONTENTS
def nuke():
    restInPeace = collection.delete_many({})

#returns if a certain name is in the database
def isInside(username):
    x = collection.find({})
    for i in x:
        if i['name'] == username:
            return True
    return False

#adds new field - make sure fieldname is not the name of an already existing field!
def addNewField(fieldName, value = 0):
    base = collection.find({})
    for i in range(totalPosts()):
        collection.update_one(
            {'_id': i},
            {'$set': {fieldName: value}}
        )

#returns whether user has collected daily
def HasCollected(tag):
    usr = collection.find_one({'_id': tag})
    return usr['HasCollected']

#return the total number of posts
def totalPosts():
    x = collection.find({})
    output = 0
    for i in x:
        output += 1
    return output

#adds user to database
def postsAdd(username, givid):
    post = {'_id': givid, 'name': str(username), 'score': 0, 'swearjar': 0, 'messagecount': 0}
    collection.insert_one(post)

#removes user to database
def postRemove(username):
    term = collection.find_one({'name': username})
    dataholes.append(term['_id'])
    bye = collection.delete_one({'name': username})

#updates swearjar
def swearJar(userid):
    collection.update_one(
        {'_id':userid},
        {'$inc': {'swearjar': 1}})

#upon given name, returns id
def getID(name):
    usr = collection.find_one({'name': name})
    return usr['_id']

#updates total message count
def count(tag):
    collection.update_one(
        {'_id': tag},
        {'$inc': {'messagecount': 1}}
    )

#increases a user's score
def Scoring(tag, amount):
    collection.update_one(
        {'_id': tag},
        {'$inc': {'score': amount}}
    )

#returns swearjar count
def returnSwears(tag):
    usr = collection.find_one({'_id': tag})
    return usr['swearjar']

#returns message count
def returnmsg(tag):
    usr = collection.find_one({'_id': tag})
    return usr['messagecount']

def returnValue(tag, xfield):
    usr = collection.find_one({'_id': tag})
    return usr[xfield]
print(totalPosts())
