# IPA TRANSLATE

import fileinput
import dictio
from dictio import fullDict     

index = 0

while True:
    try:
        srcTxt = input("Input word you want to look up: ")
        print(dictio.fullDict[index][srcTxt])
    except:        
        try:
            queryInput = input('What does '+srcTxt+' mean?: ')
            newDictEntry = "        "+"'"+srcTxt+"'"+":"+"'"+queryInput+"'"+","+"\n"
            f = open("C:\\Users\\otaco\\Desktop\\DevProjects\\IPA translate\\dictio.py", "r")
            contents = f.readlines()
            f.close()

            # contents.insert(2, newDictEntry)

            # f = open("C:\\Users\\otaco\\Desktop\\DevProjects\\IPA translate\\dictio.py", "w")
            # contents = "".join(contents)
            # f.write(contents)
            # f.close()
            
        except:
                    print("error has occured.")

# fullDict = [
    # {
        # 'arbre':'tree',
        # 'arc-en-ciel':'rainbow',
        # 'bierre':'beer',
        # 'belle':'beautiful'
    # }
# ]
