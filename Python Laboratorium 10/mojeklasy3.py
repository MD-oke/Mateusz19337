import random
import math
def testy():
 pass
if __name__ == "__main__":
 testy()
 
class Student():
    __licznik =0
    def __init__(self,imie,nazwisko,nr_indeksu,kierunek):
        Student.__licznik += 1
        self.imie = imie;
        self.nazwisko = nazwisko;
        self.nr_indeksu = nr_indeksu;
        self.kierunek = kierunek;
    def __str__(self):
        return "Imie: %s Nazwisko: %s indeks: %s Kierunek: %s"%(self.imie,self.nazwisko,self.nr_indeksu,self.kierunek);
    def __eq__(self,other):
        return self.imie == other.imie;
    def __it__(self,other):
        return self.imie < other.imie;
    def getlicznik(self):
        return Student.licznik
p1 = Student('Mateusz','Dyrdowski','19337','Informatyka')
p2 = Student('Jan','Kowalski','11111','Informatyka')
lancuch = str(p1)
print(lancuch)
lancuch = str(p2)
print(lancuch)

print(p1.nazwisko == p2.nazwisko)
print(p1.nr_indeksu < p2.nr_indeksu)
