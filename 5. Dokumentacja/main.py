from typing import Union

def kalkulator() -> None:
    while True:
        print('Kalkulator')
        print('1. dodawanie')
        print('2. odejmowanie')
        print('3. mnożenie')
        print('4. dzielenie')
        print('5. wyjście')

        dzialanie = input("Podaj działanie: ")
        if dzialanie == '1':
            a = int(input('Podaj pierwszą liczbę: '))
            b = int(input('Podaj drugą liczbę: '))
            wynik = dodawanie(a, b)
        elif dzialanie == '2':
            a = int(input('Podaj pierwszą liczbę: '))
            b = int(input('Podaj drugą liczbę: '))
            wynik = odejmowanie(a, b)
        elif dzialanie == '3':
            a = int(input('Podaj pierwszą liczbę: '))
            b = int(input('Podaj drugą liczbę: '))
            wynik = mnozenie(a, b)
        elif dzialanie == '4':
            a = int(input('Podaj pierwszą liczbę: '))
            b = int(input('Podaj drugą liczbę: '))
            wynik = dzielenie(a, b)
        elif dzialanie == '5':
            break  
        else:
            wynik = 'Nie ma takiego działania'

        print("Wynik:", wynik)
        print() 


def dodawanie(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


def odejmowanie(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a - b

def mnozenie(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b

def dzielenie(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if b != 0:
        return a / b
    else:
        return 'Dzielenie przez zero!'


kalkulator()
