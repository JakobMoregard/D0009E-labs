def stringInsert(str_listWrd, str_listDes):     #definerar en funktion för att lägga till i listorna för ord och beskrivning
        word = str(input("Word to insert: "))   #tar in ord som ska sparas
        print()
        
        if word in str_listWrd:     #kollar om ordet finns i stränglistan för ord
            print("error: word is already present")     #om det finns skrivs ett felmeddelande
            print()
            return      #returnerar till funktionen stringList
        
        else:       #finns inte ordet i listan,
            str_listWrd.append(word)    #så läggs det till i listan för ord
            desc = str(input("Description of word: "))  #frågar efter beskrivning åt ordet
            str_listDes.append(desc)    #lägger till beskrivningen i en egen stränglista
            print()
            return      #returnerar till funktionen stringList 
    

def stringLookup(str_listWrd, str_listDes):     #definerar en funktion för att kolla upp ord och beskrivningar ur listorna
    word = str(input("Word to lookup: "))   #tar in ord som ska kollas upp
    print()
        
    if  not(word in str_listWrd):   #kollar om ordet inte finns i listan för ord
        print("error: word is not present") #om det inte finns skrivs ett felmeddelande
        print()
        return      #returnerar till funktionen stringList
    
    else:       #finns ordet i listan,
        i = str_listWrd.index(word)     #så hämtas index för det ordet
        print("Description for " , word , ": " , str_listDes[i])    #skriver ut ordet och beskrivningen som är på samma index som ordet
        print()
        return      #returnerar till funktionen stringList


def stringList():   #definerar en funktion för menyn
    str_listWrd = []    #skapar listan för ord
    str_listDes = []    #skapar listan för beskrivning 

    while True:     #loop som går till programmet avslutar
        print("Menu for string list")   #skriver ut en enkel meny
        print("1: Insert")
        print("2: Lookup")
        print("3: Exit program")
        print()
        n = int(input("Choose alternative: "))  #sparar en integer för det alternativ som valts
        print()
    
        if n == 1:      #är inmatningen 1,
            stringInsert(str_listWrd, str_listDes)  #så kallas funktionen stringInsert

        if n == 2:      #är inmatningen 2,
            stringLookup(str_listWrd, str_listDes)  #så kallas funktionen stringLookup

        if n == 3:      #är inmatningen 3,
            print("Shutting down")
            return      #så bryts loopen och programmet stängs

#------------------------------------------------------------------------------------------


def tupInsert(tup_list):    #definerar en funktion för att spara ord och beskrivning
    word = str(input("Word to insert: "))   #tar in ord som ska sparas
    print()

    found1 = False  #skapar en kontrollflagga
    for key, value in tup_list:     #loop som kollar igenom listan av tupler
        if key == word:     #finns ordet redan som nyckel,
            found1 = True   #ändras kontrollflaggan
            print("error: word is already present") #felmeddelande skrvis
            print()
            return  #returnerar till funktionen tupList
                    
    if found1 == False:     #är kontrollflaggan oförändrad
        desc = str(input("Description of word: "))  #tas beskrivningen in
        tup_list.append((word, desc))   #ordet och beskrivningen läggs till i listan som key och value
        print()
        return  #returnerar till funktionen tupList


def tupLookup(tup_list):    #definerar en funktion för att kolla upp ord och beskrivning
    word = str(input("Word to lookup: "))   #tar in det ord som ska kollas upp
    print()

    found2 = False      #skapar en till kontrollflagga
    for key, value in tup_list:     #loop som kollar igenom listan av tuplar
        if key == word:     #finns ordet redan som nyckel,
            found2 = True   #ändras kontrollflaggan
            print("Description for " , key , ": " , value)  #skriver ut ordet som key med tillhörande value
            print()
            return  #returnerar till funktionen tupList
                    
    if found2 == False:     #är kontrollflaggan oförändrad, 
        print("error: word is not present") #skrivs felmeddelande
        print()
        return  #returnerar till funktionen tupList
    


def tupList():  #definerar en funktion för menyn

    tup_list = []   #skapar listan för tuplerparen
    while True:     #loop som går till programmet avslutar
        print("Menu for tuple list")    #skriver en enkel meny
        print("1: Insert")
        print("2: Lookup")
        print("3: Exit program")
        print()
        n = int(input("Choose alternative: "))  #sparar en integer för det alternativ som valts
        print()
    
        if n == 1:  #är inmatingen 1,
            tupInsert(tup_list) #kallas funktionen tupInsert

        if n == 2:  #är inmatningen 2,
            tupLookup(tup_list) #kallas funktionen tupLookup
   
        if n == 3:  #är inmatningen 3,
            print("Shutting down")
            return  #så bryts loopen och programmet stängs

#------------------------------------------------------------------------------------------          


def dictInsert(dict_cont):  #definerar en funktion för att spara i dictionary
    word = str(input("Word to insert: "))   #tar in ord som ska sparas
    print()
        
    if word in dict_cont:   #finns ordet redan i dictionary
        print("error: word is already present") #skrivs felmeddelande
        print()
        return  #returnerar till funktionen dictionary

    else:   #finns ordet inte
        desc = str(input("Description of word: "))  #tas beskrivningen in
        dict_cont[word] = desc  #ord och beskrivning sparas som key och value i dictionary
        print()
        return  #returnerar till funktionen dictionary

def dictLookup(dict_cont):  #definerar en funktion för att kolla upp i dictionary
    word = str(input("Word to lookup: "))   #tar in ordet som ska kollas upp
    print()
        
    if  not(word in dict_cont): #kollar om ordet inte finns i dictionary
        print("error: word is not present") #skriver felmeddelande
        print()
        return  #returnerar till funktionen dictionary

    else:       #finns ordet i listan,
        print("Description for " , word , ": " , dict_cont[word])   #skrivs ordet som key med tillhörande value
        print()
        return  #returnerar till funktionen dictionary
    
    

def dictionary():   #definerar funktion för menyn
    dict_cont = {}  #skapar ett dictionary
    
    while True:     #loop som går till programmet avslutar
        print("Menu for dictionary")    #skriver en enkel meny
        print("1: Insert")
        print("2: Lookup")
        print("3: Exit program")
        print()
        n = int(input("Choose alternative: "))  #sparar en integer för det alternativ som valts
        print()
    
        if n == 1:  #är inmatningen 1,
           dictInsert(dict_cont)    #kallas funktionen dictInsert

        if n == 2:  #är inmatningen 2,
            dictLookup(dict_cont)   #kallas funktionen dictLookup

        if n == 3:  #är inmatningen 3,
            print("Shutting down")
            return  #så bryts loopen och programmet stängs

#------------------------------------------------------------------------------------------

    
def main_dic(): #deinerar funktion som startar hela programmet
    print("Test:")  #enkel meny med val för vilken typ av lista
    print()
    print("1: String list")
    print("2: Tuple list")
    print("3: Dictionary")
    print()
    s = int(input("Choose alternative: "))  #sparar en integer för det alternativ som valts
    print()

    if s == 1:  #är inmatningen 1,
        stringList()    #kallas funktionen stringList

    if s == 2:  #är inmatningen 2,
        tupList()   #kallas funktionen tupList

    if s == 3:  #är inmatningen 3,
        dictionary()    #kallas funktionen dictionary

