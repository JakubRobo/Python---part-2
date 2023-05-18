from abc import ABC, abstractmethod

class Ksztalt(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def pole(self):
        pass
    
    @abstractmethod
    def obwod(self):
        pass

class Prostokat(Ksztalt):
    def __init__(self, dlugosc, szerokosc):
        super().__init__()
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    
    def pole(self):
        return self.dlugosc * self.szerokosc
    
    def obwod(self):
        return 2 * (self.dlugosc + self.szerokosc)

class Kolo(Ksztalt):
    def __init__(self, promien):
        super().__init__()
        self.promien = promien
    
    def pole(self):
        return 3.14 * self.promien**2
    
    def obwod(self):
        return 2 * 3.14 * self.promien

# Tworzenie obiektów i wywoływanie metod
prostokat = Prostokat(4, 6)
kolo = Kolo(5)

print("Prostokąt:")
print("Pole:", prostokat.pole())
print("Obwód:", prostokat.obwod())

print("Koło:")
print("Pole:", kolo.pole())
print("Obwód:", kolo.obwod())