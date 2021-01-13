class Person:     #klassen för att skapa instanser med personer
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.alias = []

    def addAlias(self, alias): #metod som lägger till alias i instans
        self.alias.append(alias)

    def changeNumber(self, newNumber): #metod som ändrar nummer i instans
        self.number = newNumber

    def IsNumber(self, number):  #metod som kollar om ett nummer redan finns
        return self.number == number

    def IsPerson(self, name):  #metod som agerar flagga för att leta efter personer
        found = False
        if name == self.name:
            found = True
            return found
        for m in self.alias:
            if name == m:
                found = True
                return found
        
    

class Phonebook:   #klassen med telefonboken
    def __init__ (self):
        self.persList = []

    def NumberExist(self, number):  #metod som kollar om ett nummer redan finns
        for n in self.persList:
            if n.IsNumber(number):
                return True
        return False

    def GetIndex(self, name):  #metod som skapar en indexerad lista med hittade personer
        IndexList = []
        for m in enumerate(self.persList):
            if m[1].IsPerson(name):
                IndexList.append(m[0])

        return IndexList
        

    def add(self, n):   #metod för att lägga till person instanser i telefonboken

        if len(n) < 3:
            print("add needs command for name and number")
            return
        
        if len(n) == 3:
            listName = n[1]
            listNumber = n[2]
            pers = Person(listName, listNumber)
            found1 = self.NumberExist(listNumber)
            if found1 == True:
                print("person already present")
                return

            if found1 == False:
                self.persList.append(pers)
                return

        if len(n) > 3:
            print("add only takes name and number commands")
            return
        

    def lookup(self, n):   #metod för att kolla upp person instanser i telefonboken

        if len(n) < 2:
            print("lookup needs command for name")
            return

        if len(n) == 2:
            listName = n[1]
            lookupList = self.GetIndex(listName)
            for x in lookupList:
                print(self.persList[x].number)
                
                
            if len(lookupList) == 0:
                print("name not found")
                return

        if len(n) > 2:
            print("lookup only takes name command")
            return
            

    def alias(self, n):   #metod för att lägga till alias till person instanser

        if len(n) < 3:
            print("alias needs command for name and alias")
            return

        if (len(n) == 3 or len(n) == 4):
            listName = n[1]
            aliasName = n[2]
            IndexList = self.GetIndex(listName)
            if len(IndexList) == 0:
                print("person doesn't exist")
                return

            if len(IndexList) == 1:
                self.persList[IndexList[0]].addAlias(aliasName)
                return

            if len(IndexList) > 1:
                if len(n) < 4:
                    print("multiple persons: type in a number too")
                    return

                listNumber = n[3]
                for x in IndexList:
                    if self.persList[x].IsNumber(listNumber):
                        self.persList[x].addAlias(aliasName)
                        return

                print("no matching number")

        if len(n) > 4:
            print("alias only takes command for name, alias and number")
            return
        
        
    def change(self, n):   #metod för att ändra nummer i person instanser

        if len(n) < 3:
            print("change needs argument for name and new number")
            return

        if (len(n) == 3 or len(n) == 4):
            listName = n[1]
            newNumber = n[2]
            IndexList = self.GetIndex(listName)
            if len(IndexList) == 0:
                print("person doesn't exist")
                return

            if len(IndexList) == 1:
                found3 = self.NumberExist(newNumber)
                if found3 == False:
                    self.persList[IndexList[0]].changeNumber(newNumber)
                    return

                if found3 == True:
                    print("Number already assigned")
                    return

            if len(IndexList) > 1:
                if len(n) < 4:
                    print("multiple persons: type in a number too")
                    return

                listNumber = n[3]
                for x in IndexList:
                    if self.persList[x].IsNumber(listNumber):
                        self.persList[x].changeNumber(newNumber)

        if len(n) > 4:
            print("change only takes commands for name, new number and current number")
            return                    
        

    def remove(self, n):    #metod för att ta bort instanser ur telefonboken

        if len(n) < 2:
            print("remove needs command for name")
            return

        if (len(n) == 2 or len(n) == 3):
            listName = n[1]
            IndexList = self.GetIndex(listName)
            if len(IndexList) == 0:
                print("person doesn't exist")
                return

            if len(IndexList) == 1:
                self.persList.pop(IndexList[0])

            if len(IndexList) > 1:
                if len(n) < 3:
                    print("multiple persons: type in a number too")
                    return

                try:
                    listNumber = n[2]
                    for x in IndexList:
                        if self.persList[x].IsNumber(listNumber):
                            self.persList.pop(x)
                except IndexError:
                    print("nu krånglar jag igen")
                    return

        if len(n) > 3:
            print("remove only takes commands for name and number")
            return


    def save(self, n):  #metod för att spara telefonboken i filen filename

        if len(n) < 2:
            print("save needs command for filename")

        
        if len(n) == 2:
            filename = n[1]
            with open(filename + ".txt", "w") as wf: 
                for m in self.persList:
                    tempName = m.name
                    tempNumber = m.number
                    wf.write(tempNumber + ";" + tempName)
                    for x in m.alias:
                        wf.write(";" + x)
                    wf.write(";" + "\n")

        if len(n) > 2:
            print("save takes no additional command")
            return
                
        
    def load(self, n):  #hämtar tillbaka telefonboken från filen filename

        if len(n) < 2:
            print("load needs command for filename")
            return

        try:
            if len(n) == 2:
                filename = n[1]
                numberfile = open(filename + ".txt")
                self.persList = []
                n = 0
                for line in numberfile.readlines():
                    line_list = line.split(";")
                    line_list.pop()
                    temp = []
                    temp.append("add")
                    temp.append(line_list[1])
                    temp.append(line_list[0])
                    self.add(temp)
                    del line_list[0:2]
                    n += 1
                    for item in line_list:
                        self.persList[n].addAlias(item)
                numberfile.close()
                return
            
        except FileNotFoundError:
            print("could not find file")
        

        if len(n) > 2:
            print("load takes no additional command")
            return


    #def printList(self):
       # string = ""
       # for m in self.persList:    
          #  print(m.name, m.number, end=" ")
           # for x in m.alias:
           #    print(x, end=" ")
           # print()

    
    
def select(): #funktion med menun
    localList = Phonebook()
    while True:
        try:
            n = list(input("telebok >>> ").split())
            if n[0] == "add":   #kallar på metod add
                localList.add(n)

            if n[0] == "lookup":    #kallar på metod lookup
                localList.lookup(n)

            if n[0] == "alias": #kallar på metod alias
                localList.alias(n)

            if n[0] == "change":    #kallar på metod change
                localList.change(n)

            if n[0] == "remove":    #kallar på metod remove
                localList.remove(n)

            if n[0] == "save":  #kallar på metod save
                localList.save(n)

            if n[0] == "load":  #kallar på metod load
                localList.load(n)

            #if n[0] == "check":
               # print(localList.printList())
            
            if n[0] == "quit":  #avslutar programmet
                print(". . .")
                return
                
        except IndexError:
            pass
            

        #localList.printList()
