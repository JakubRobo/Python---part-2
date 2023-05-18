while True:
    print('Kalkulator')
    print('1. Dodawanie')
    print('2. Odejmowanie')
    print('3. Mnożenie')
    print('4. Dzielenie')
    print('5. Wyjście')
    dzialanie = input("Podaj działanie: ")

    if dzialanie == '1':
        try:
            a = int(input('Podaj pierwszą liczbę: '))
            b = int(input('Podaj drugą liczbę: '))
            wynik = a + b
        except ValueError:
            print("Wprowadzono nieprawidłowe dane. Podaj liczby całkowite.")
            continue
    elif dzialanie == '2':
        try:
            a = int(input('Podaj pierwszą liczbę: '))
            b = int(input('Podaj drugą liczbę: '))
            wynik = a - b
        except ValueError:
            print("Wprowadzono nieprawidłowe dane. Podaj liczby całkowite.")
            continue
    elif dzialanie == '3':
        try:
            a = int(input('Podaj pierwszą liczbę: '))
            b = int(input('Podaj drugą liczbę: '))
            wynik = a * b
        except ValueError:
            print("Wprowadzono nieprawidłowe dane. Podaj liczby całkowite.")
            continue
    elif dzialanie == '4':
        try:
            a = int(input('Podaj pierwszą liczbę: '))
            b = int(input('Podaj drugą liczbę: '))
            try:
                wynik = a / b
            except ZeroDivisionError:
                print("Nie można dzielić przez zero!")
                continue
        except ValueError:
            print("Wprowadzono nieprawidłowe dane. Podaj liczby całkowite.")
            continue
    elif dzialanie == '5':
        break
    else:
        wynik = 'Nie ma takiego działania'
    
    print("Wynik:", wynik)
    print()
