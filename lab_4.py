class Personer:
    def __init__(self, name = "", number = "", newname = ""):
        self.name = name
        self.number = number
        self.newname = newname


def add():
    n = list(input("telebok> ").split())
    if n[0] == "add":
        name = n[1]
        number = n[2]
        print(name + " ; " + number)
    else:
         print("fel")
        
def alias():
    n = list(input("telebok> ").split())
    if n[0] == "alias":
        
