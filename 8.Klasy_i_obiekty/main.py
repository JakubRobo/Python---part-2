class Czytelnik:
    def __init__(self, imie, nazwisko, nr_karty):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_karty = nr_karty
    def info(self):
        print(f"Czytelnik: {self.imie} {self.nazwisko}, nr karty: {self.nr_karty}")


czytelnik1 = Czytelnik("Jan", "Kowalski", 12345)
czytelnik2 = Czytelnik("Anna", "Nowak", 67890)
czytelnik3 = Czytelnik("Mariusz", "Pudzianowski", 42069)
czytelnik4 = Czytelnik("Robert", "Nowak", 21370)

czytelnik1.info()
czytelnik2.info()
czytelnik3.info()
czytelnik4.info()
