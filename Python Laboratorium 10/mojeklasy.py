import random
import math
def testy():
 pass
if __name__ == "__main__":
 testy()
 
class Student():
    def __init__(self,imie,nazwisko,nr_indeksu,kierunek):
        self.imie = imie;
        self.nazwisko = nazwisko;
        self.nr_indeksu = nr_indeksu;
        self.kierunek = kierunek;
    def __str__(self):
        return "Imie: %s Nazwisko: %s indeks: %s Kierunek: %s"%(self.imie,self.nazwisko,self.nr_indeksu,self.kierunek);
    
    
p1 = Student('Mateusz','Dyrdowski','19337','Informatyka')
lancuch = str(p1)
print(lancuch)
