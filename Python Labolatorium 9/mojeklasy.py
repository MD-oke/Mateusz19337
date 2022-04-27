import random
import math
def testy():
 pass
if __name__ == "__main__":
 testy()

class Punkt2D:
    x = random.randrange(1,10)
    y = random.randrange(1,10)
    
    def Drukuj(self):
        print("----------------------------------")
        print("Punkt 2D x=",self.x,"Punkt 2D y=",self.y)
    def Zeruj(self):
        self.x=0
        self.y=0
        
class Punkt3D(Punkt2D):
    z = random.randrange(1,10)
    def Drukuj(self):
        print("----------------------------------")
        print("Punkt 3D x=",self.x,"Punkt 3D y=",self.y,"Punkt 3D z=",self.z)
    def Zeruj(self):
        self.z=0

class Odcinek(Punkt2D):
    def Drukuj():
        l1=Punkt2D();
        l2=Punkt2D();
        dzialanie=math.sqrt(math.pow((l1.y-l1.x),2)+math.pow((l2.y-l2.x),2))
        print("----------------------------------")
        print("odcinek =",dzialanie)   
        
l1= Punkt2D()
print(l1.x,l1.y)
l1.Drukuj()
l1.Zeruj()
l1.Drukuj()

l2= Punkt3D()
print(l1.x,l1.y)
l2.Drukuj()
l2.Zeruj()
l2.Drukuj()

wynik=Odcinek()
Odcinek.Drukuj()