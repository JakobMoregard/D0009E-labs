def recept(Antal):
    egg = Antal*3//4
    print (egg , "st ägg")
    sugar =(3/4)* Antal
    print (sugar , "dl socker")
    VanillaSugar = (2/4)* Antal
    print (VanillaSugar , "tsk vaniljsocker")
    BakeSoda = (2/4)* Antal
    print (BakeSoda , "tsk bakpulver")
    flour = (3/4)* Antal
    print (flour , "dl mjöl")
    butter = (75/4)* Antal
    print (butter , "g smör")
    water = (1/4)* Antal
    print (water , "dl vatten")
    print ()


def tidblanda(Antal):
    return (10+(1*Antal))
    

def tidgradda(Antal):
    return (30+(3*Antal))

   
def sockerkaka(Antal):
    recept(Antal)
    print ("Och det kommer att ta" , tidblanda(Antal)+tidgradda(Antal) ,
           "minuter att baka sockerkakan")
    print()
    

#Antal = int(input("Hur många ska ha kaka: "))
sockerkaka(4)
sockerkaka(7)
