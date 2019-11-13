import pymongo
import env_variables
from pymongo import MongoClient
cluster = MongoClient(env_variables.Database_log)
db = cluster['Discordbot']
collection = db['ongoingames']

mtrix = [[] for i in range(7)]
tokens = {
    'e': 0,
    'x': 1,
    'y': 2
}
#nuke
def nuke():
    restInPeace = collection.delete_many({})

#returns nomber of ongoing ongoingames
def gameAmount():
    x = 0
    for i in collection.find({}):
        x += 1
    return x

#returns whether a player is already in a game
def isAlreadyPlaying(player1, player2):
    for i in collection.find({}):
        if i['player1'] == player1 or i['player1'] == player2 or i['player2'] == player1 or i['player2'] == player2:
            return True
    return False
#adds a game to the database
def newGame(player1, player2):
    if isAlreadyPlaying(player1, player2):
        print(f'game request denied between {player1} and {player2}')

    #add post
    game = {'_id':gameAmount(), 'player1': player1, 'player2': player2,
        'gamestring': 'eeeeee eeeeee eeeeee eeeeee eeeeee eeeeee eeeeee'
        }
    collection.insert_one(game)

#deletes a game after it finishes
def removal(player1, player2):
    collection.delete_one({'player1': player1})
    print(f'game between {player1} and {player2} succesfully terminated.')

#returns gamestring
def ReturnAndSetBoard(player1, player2):
    select = collection.find_one({'player1': player1, 'player2': player2})
    if select == None:
        print('no board found')
        return None
    x = 0
    for i in select['gamestring']:
        if i == ' ':
            x += 1
            continue
        mtrix[x].append(tokens[i])
    return select['gamestring']

#update game board
def updateBoard(player1, player2, newboard):
    collection.update_one(
        {'player1': player1, 'player2': player2},
        {'$set':{'gamestring': newboard}}
    )


def printState():
    print('1       2       3       4       5       6       7\n--------------------------------------------------')
    for i in range(len(mtrix[0])):
        for row in mtrix:
            print(row[i], end = '       ')
        print('\n')

print(ReturnAndSetBoard('fuckmehard', 'fuckmeharder'))
printState()
