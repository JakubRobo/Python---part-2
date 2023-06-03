def kalkulator() -> None:
    """Wyświetl menu"""
    print('Kalkulator')
    print('1. dodawanie')
    print('2. odejmowanie')
    print('3. mnożenie')
    print('4. dzielenie')
    print('5. wyjście')
def dodawanie(a: float, b: float) -> None:
    """Wyświetl sumę"""
    print(f"\nSuma wynosi: {a+b}")

def odejmowanie(a: float, b: float) -> None:
    """Wyświetl różnicę"""
    print(f"\nRóżnica wynosi: {a-b}")

def mnozenie(a: float, b: float) -> None:
    """Wyświetl iloczyn"""
    print(f"\nIloczyn wynosi: {a*b}")

def dzielenie(a: float, b: float) -> None:
    """Wyświetl iloraz"""
    if b != 0:
        print(f"\nDzielenie wynosi: {a/b}")      
    else:
        print("\nDzielenie przez 0!!!")


while True:
    kalkulator()
    dzialanie = int(input("Podaj działanie: "))
    if dzialanie == '1':
        dodawanie(int(input("Podaj liczbę a: ")), int(input("Podaj liczbę b: ")))
    elif dzialanie == '2':
        odejmowanie(int(input("Podaj liczbę a: ")), int(input("Podaj liczbę b: ")))
    elif dzialanie == '3':
        mnozenie(int(input("Podaj liczbę a: ")), int(input("Podaj liczbę b: ")))
    elif dzialanie == '4':
        dzielenie(int(input("Podaj liczbę a: ")), int(input("Podaj liczbę b: ")))
    elif dzialanie == '5':
        break 





