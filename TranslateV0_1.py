import fileinput
import dictio
import json
from dictio import fullDict  
import sys

index = 0

# VERSION 0.1
# while True:
    # try:
        # srcTxt = input("Input word you want to look up: ")
        # firstLetter = srcTxt[0]
        # print(dictio.fullDict3[firstLetter][srcTxt])
    # except: 
        # try:
                # queryInput = input('What does '+srcTxt+' mean?: ')                                 
                # with open('C:\\Users\\otaco\\Desktop\\DevProjects\\IPA translate\\dictio2.json','r+') as f:
                    # dictio.fullDict3[firstLetter].update({srcTxt:queryInput})
                    # dic = json.load(f)
                    # dic.update(fullDict3[firstLetter])
                    # json.dump(dic, f)
        # except:
                    # print("error has occured.")
                    # print(fullDict3[firstLetter])

# VERSION 0.1.2
# while True:
    # try:
        # srcTxt = input("Input word you want to look up: ")
        # firstLetter = srcTxt[0]
        # print(dictio.fullDict3[firstLetter][srcTxt])
    # except: 
        # try:
            # queryInput = input('What does '+srcTxt+' mean?: ')
            # with open('C:\\Users\\otaco\\Desktop\\DevProjects\\IPA translate\\dictio.py', 'r') as f:
                # fullDict3[firstLetter].update({srcTxt:queryInput})
                # print(fullDict3[firstLetter])
                # jd = json.dumps(fullDict3)
            # with open('C:\\Users\\otaco\\Desktop\\DevProjects\\IPA translate\\dictio.py', 'w') as z:
                # z.write(jd)
                # z.close()
        # except:
            # print("error has occured.")
            
# VERSION 0.1.2.1
while True:
    try:
        inputSrc = input("Input word you want to look up: ")
        ISfirstLetter = inputSrc[0]
        if inputSrc == "ESC":
            break
        print(dictio.fullDict[ISfirstLetter][inputSrc])
    except: 
        try:
            queryInput = input('What does '+inputSrc+' mean?: ')
            with open('C:\\Users\\otaco\\Desktop\\DevProjects\\IPA translate\\dictio.py', 'r') as f:
                fullDict[ISfirstLetter].update({inputSrc:queryInput})
                newDict = "fullDict = "+json.dumps(fullDict)
            with open('C:\\Users\\otaco\\Desktop\\DevProjects\\IPA translate\\dictio.py', 'w') as f:
                f.write(newDict)
                f.close()
        except:
            print("error has occured.")