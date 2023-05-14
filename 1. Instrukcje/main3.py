import random

liczba = random.randint(0,100)
odp = print(input("Podaj liczbę!: "))
odp = int(odp)
proba = 0
if liczba == odp:
    print("Gratulacje! Trafiłeś liczbę!")
    print("Liczba prób: "+ proba)
    pass
if liczba > odp:
    print("Liczba za duża! Próbuj dalej!")
    proba += 1
    print("Próba: " + proba)
    pass
else:
    print("Liczba za mała! Próbuj dalej!")
    proba += 1
    print("Próba: " + proba)
