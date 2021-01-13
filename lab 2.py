import math

def bounce(n):
    if n==0:        #kollar basläget
        print(0)      #skriver ut 0 vid basläge
    if n>0:     #kollar om n är större än 0
        print(n)        #skriver ut n i nedräkningen
        bounce(n-1)     #kallar på funktionen för n-1
        print(n)        #skriver ut uppräkningen


def bounce2(n):
    m=n         #skapar en till variabel för att hantera räkning/utskrift
    if m==0:        #kollar basläget
        return 0      #returnerar 0 vid basläge
    if m>0:     #kollar om m är större än 0
        print(m)        #skriver ut inmatningen
        while m>0:      #är inmatningen större än 0 körs loopen
            m=m-1       #genomför nedräkningen
            print(m)        #skriver ut nedräkningen
    if m<n:     #kollar om m är mindre än n efter nedräkningen
        while m<n:      #så länge m är mindre än n körs loopen
            m=m+1       #genomför uppräkningen 
            print(m)        #skriver ut uppräkningen


def tvarsumma(n):             
    if n==0:        #kollar basläget
        return 0        #returnerar 0 vid basläge
    if n>0:     #kollar om n är större än 0
        n = (n % 10) + tvarsumma(n // 10 )      #beräknar tvärsumman
        return n        #returnerar tvärsumman
    

def tvarsumma2(n):
    if n==0:        #kollar basläget
        return 0      # returnerar 0 vid basläget
    m=0         #skapar och tilldelar m värdet 0
    while n>0:      #kollar om n är större än 0
        m = m + (n % 10)        #sparar och adderar resten vid division med 10
        n = n // 10         #sparar heltalsdivision med 10
    return m        #skriver ut tvärsumman när loopen är färdig

def f1(x):
    return (x**2 - 1)   #testfunktion 1

def f2(x):
    return (2**x - 1)   #testfunktion 2

def f3(x):
    return (x - math.e**(-x))   #testfunktion 3

def derivative(f, x, h):
     return (1.0 / (2.0*h)) * (f(x+h) - f(x-h)) #returnerar approximation för derivatan
    
    
def solve(f, x0, h):
    xCOMP = x0 + h*2    #tilldelar xCOMP ett värde som aldrig kan vara samma som x0/xVALUE
    xVALUE = x0     #tilldelar xVALUE värdet av variabeln x0
    while(True):    #loopen kör tills något i den bryter den
        if abs(xCOMP - xVALUE) < abs(h):    #kollar om absolutvärdet för xCOMP minus xVALUE
                                            #är mindre är absolutvärdet för variabeln h
           return xVALUE    #om if satsen är sann så returneras xVALUE

        xCOMP = xVALUE      #tilldelar gammalt xVALUE (föregående index) till xCOMP
        xVALUE = xVALUE - (f(xVALUE) / derivative(f, xVALUE, h))
        #beräknar ny approximation och tilldelar den variabeln xVALUE
        #formeln ska innehålla den aktuella mattematiska funktionens
        #derivata så python funktionen från uppgift 5a derivative(f, x, h) kallas i formeln.























