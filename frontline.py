# IPA TRANSLATE

fulldict = [
    {
        'arbre':'tree',
        'arc-en-ciel':'rainbow',
        'bierre':'beer',
        'belle':'beautiful'
    }
]

while True:
    try:
        srcTxt = input("Input word you want to look up: ")
        print(fulldict[0][srcTxt])
    except:        
        print("--")
        try:
            queryAdding = input('What does '+srcTxt+' mean?: ')
            fulldict[0][srcTxt] = queryAdding;
        except:
            print("error has occured.")
        



# while True:
    # try:
        # x = int(raw_input("Please enter a number: "))
        # break
    # except ValueError:
        # print("Oops!  That was no valid number.  Try again...")