import fileinput
import dictio
from dictio import fullDict
import json
import pprint
from sortedcontainers import SortedDict
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

'''
Store player data as indexes in the playerDatabase.json that gets translated from the 
player class lists (i.e.[0][1]=Blood DK). 
'''
class player:

    def __init__(self, name, spec):
        '''Return a new Player object'''  
        self.name = name
        # self.cls = cls
        self.spec = spec
        # self.race = race 
    
    # def 
    
    # name(self, name)
    # cls = ('Death Knight','Druid','Hunter','Mage','Monk','Paladin','Priest','Rogue','Shaman','Warlock','Warrior')
    # clsIndex = self.name.index
    def spec(c,s):
        specLists = (
        ['Blood','Frost','Unholy'],                  #0  DK     [0][0],[0][1],[0][2]
        ['Balance','Feral','Guardian','Resto'],      #1  Druid  [1][0],[1][1],[1][2],[1][3]
        ['Beast Master','Marksmanship','Surival'],   #2  Hunter [2][0],[2][1],[2][2]
        ['Arcane','Fire','Frost'],                   #3  Mage   [3][0],[3][1],[3][2]
        ['Brewmaster','Mistwalker','Windwalker'],    #4  Monk   [4][0],[4][1],[4][2]
        ['Holy','Protection','Retribution'],         #5  Paladin[5][0],[5][1],[5][2]
        ['Disciple','Holy','Shadow'],                #6  Priest [6][0],[6][1],[6][2]
        ['Assassination','Outlaw','Subtlety'],       #7  Rogue  [7][0],[7][1],[7][2]
        ['Elemental','Enhancement','Restoration'],   #8  Shaman [8][0],[8][1],[8][2]
        ['Affliction','Demonology','Destruction'],   #9  Warlock[9][0],[9][1],[9][2]
        ['Arms','Fury','Protection'])                #10 Warrior[10][0],[10][1],[10][2] 
        return specLists[c][s]
# print(player.spec(0,2))
    # race = ('Blood Elf','Draenei','Dwarf','Gnome','Goblin','Human','Night Elf','Orc','Pandaren','Tauren','Troll','Undead','Worgen')

    # def playerInfo(inputSearch):
        # print('Name: ',inputSearch.name+'\n'+'Class: ',inputSearch.cls+'\n'+'Spec: ',inputSearch.spec+'\n'+'Race: ',inputSearch.race+'\n\n')
        # name = player.name
        # cls = player.cls
        # spec = player.spec
        # race = player.race
        # print('Name: ',name+'\n'+'Class: ',cls+'\n'+'Spec: ',spec+'\n'+'Race: ',race+'\n\n')
        # print('Name: ',Kepryx.name+'\n'+'Class: ',Kepryx.cls+'\n'+'Spec: ',Kepryx.spec+'\n'+'Race: ',Kepryx.race+'\n\n')
        # return "Hello!"
        
Jaike = player('Jaike',player.spec(2,1))
print(Jaike)
# Kepryx = player('Kepryx',player.cls[0],player.spec(0,0),player.race[0])
''' Format of instantiated playerInfo.'''
print('Name: ',Jaike.name+'\n'+'Spec: ',Jaike.spec+'\n\n')
# print('Name: ',Kepryx.name+'\n'+'Class: ',Kepryx.cls+'\n'+'Spec: ',Kepryx.spec+'\n\n')
## Unique ID -- Create ID serialization for each new player.
## Look up database and if doesn't exist, offer to create ID. Every player has unique ID.
## Create return from main function that generates all vars to give feed into the print.

# def playerToIndex():
'''passes Player name to retrieve all the indexes of its description (i.e. Race, Class,
Spec) to that can be used to call the player class.'''


# inputSearch = input("Write something: ")    
# while True:
    # try:
        # inputSearch = input("Write something: ")
        # inputSearchQuery = player.playerInfo(inputSearch)
        # print(player.playerInfo(inputSearch))
    # except:
        # print("Nothing here")

####===== dict search   
# while True:
    # try:
        # srcTxt = input("Input word you want to look up: ")
        # firstLetter = srcTxt[0]
        # if srcTxt == "ESC":
            # break
        # print(dictio.fullDict[firstLetter][srcTxt])
    # except: 
        # try:
            # queryInput = input('What does '+srcTxt+' mean?: ')
            # with open('C:\\Users\\otaco\\Desktop\\DevProjects\\IPA translate\\dictio.py', 'r') as f:
                # fullDict[firstLetter].update({srcTxt:queryInput})
                # newDict = "fullDict = "+json.dumps(fullDict)
            # with open('C:\\Users\\otaco\\Desktop\\DevProjects\\IPA translate\\dictio.py', 'w') as f:
                # f.write(newDict)
                # f.close()
        # except:
            # print("error has occured.")
# print('Out of MAIN loop')

''' SPEC FOR TRANS DICT
Take in sentence, delimit whitespace&apostrophes, take [0] of each word,
search fullDict for individual keys and return their values by delimiting
new struc back to whitespace; return translated sentence.

VERSION2
Take in sentence: delimit whitespace with split. Take [0] of each word, using comma as delimiter with range
up to "]" OR for w in list. Then taking the actual words with same delimiter as key for dict search.
Return key's values with whitespace for translated sentence. 
'''

####===== Attempt at split then print 1st letter
# while True:
    # try:
        # srcTxt = input("Input sentence you want to look up: ")
        # snT = str.split(srcTxt)
        # snTf = str.split(srcTxt)[0][0]
        # print(snT)
        # for w in snT[0][0]:
            # print(w)
        ## for w in snTf:  
            ## print(snTf)
        ## firstLetter = snT[0][0]+snT[1][0]+snT[2][0]
        ## Arbre Bierre Chat
        
        ## print(firstLetter)
        ## print(dictio.fullDict[snT][])
    # except:
        # print("error...BUT")
     

        # print(snT)
        
####===== Using stackoverflow version of 1st leter
## SPEC: take letter, find value, add whitespace, then take next letter, repeat, until no more.

# data = input('Enter a phrase: ')
# data = [i[0] for i in data.split(' ')]
# lenSentence = (len(data))
# print(lenSentence)


'''
##===== SOF full sentence solution
def translate(translation_map):
    # use raw input and split the sentence into a list of words
    input_list = raw_input('Enter a phrase: ').split()
    output_list = []

    # iterate the input words and append translation
    # (or word if no translation) to the output
    for word in input_list:
        translation = translation_map.get(word)
        output_list.append(translation if translation else word)

    # convert output list back to string
    return ' '.join(output_list)
'''



# for w in data


# print(dictio.fullDict[data])

# print(''.join(data))     
        
        
# with open('C:\\Users\\otaco\\Desktop\\DevProjects\\IPA translate\\dictio.py', 'r') as f:

# k = "uid"
# v = "sa"
# "%s=%s" % (k, v) 1
# 'uid=sa
# fullDict3 = {
   
    # 'a':{
        # 'aziz':'azrs',
        # 'arbre':'tree',
        # 'arc-en-ciel':'rainbow'
    # }
# }       

# sorted(fullDict3)
# pprint(fullDict3)
        
# for key in sorted(fullDict3.keys()):
    # print("%s: %s") % (key, fullDict3[key])     

# fullDict4 = SortedDict(fullDict3)
# sorted_list = list(fullDict4.keys())   

# print(fullDict4)

# pp.pprint(fullDict['a'])
  
#PRINT B OF ARRAY
# print(dictio.fullDict3['a'])


# class Robot:
    # population = 0
    # def __init__(self, name):
        # self.name = name
        # print("(Initializing {0})".format(self.name))
        # Robot.population += 1
        
    # def die(self):
        # print("{0} is being destroyed!".format(self.name))
        # Robot.population -= 1
        
        # if Robot.population == 0:
            # print("{0} was the last one.".format(self.name))
        # else:
            # print("there are still {:d} robots working.".format(Robot.population))
            
    # def say_hi(self):
        # print("Greetings, my masters call me {0}.".format(self.name))
        
    # @classmethod
    # def how_many(cls):
        # print("We have {:d} robots.".format(cls.population))
        
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# Robot.how_many()

# droid2 = Robot("C-3P0")
# droid2.say_hi()
# Robot.how_many()

# print("\nRobots can do some work here.\n")
# print("Robots have finished their work. So let's destroy them.")
# droid1.die()
# droid2.die()
# Robot.how_many()




