def stringList():
    str_listWrd = []
    str_listDes = []

    while True:
        print("Menu for dictionary")
        print("1: Insert")
        print("2: Lookup")
        print("3: Exit program")
        print()
        n = int(input("Choose alternative: "))
        print()
    
        if n == 1:
            word = str(input("Word to insert: "))
            print()
        
            if word in str_listWrd:
               print("error: word is already present")
               print()
            else:
                str_listWrd.append(word)
                desc = str(input("Description of word: "))
                str_listDes.append(desc)
                print()

        if n == 2:
            word = str(input("Word to lookup: "))
            print()
        
            if  not(word in str_listWrd):
                print("error: word is not present")
                print()
            else:
                i = str_listWrd.index(word)
                print("Description for " , word , ": " , str_listDes[i])
                print()

        if n == 3:
            print("Shutting down")
            return



#def tupList():
#    tup_list = []

#    while True:
#        print("Menu for dictionary")
#        print("1: Insert")
#        print("2: Lookup")
#        print("3: Exit program")
#        print()
#        n = int(input("Choose alternative: "))
#        print()
    
#        if n == 1:
            

def dictionary():
    dic_cont = {}
    
    while True:
        print("Menu for dictionary")
        print("1: Insert")
        print("2: Lookup")
        print("3: Exit program")
        print()
        n = int(input("Choose alternative: "))
        print()
    
        if n == 1:
            word = str(input("Word to insert: "))
            print()
        
            if word in dic_cont:
               print("error: word is already present")
               print()
            else:
                desc = str(input("Description of word: "))
                dic_cont[word] = desc
                print()


        if n == 2:
            word = str(input("Word to lookup: "))
            print()
        
            if  not(word in dic_cont):
                print("error: word is not present")
                print()
            else:
                
                print("Description for " , word , ": " , dic_cont[word])
                print()

        if n == 3:
            print("Shutting down")
            return



    
def main_dic():
    #stringList()
    dictionary()
