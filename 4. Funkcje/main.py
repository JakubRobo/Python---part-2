print('Kalkulator')
print('1. dodawanie')
print('2. odejmowanie')
print('3. mnożenie')
print('4. dzielenie')

a = int(input('Podaj pierwszą liczbę '))
b = int(input('Podaj drugą liczbę '))

dzialanie = input('Wybierz działanie ')
if dzialanie == '1':
      wynik = a+b
elif dzialanie == '2':
      wynik = a-b
elif dzialanie == '3':
      wynik = a*b
elif dzialanie == '4':
      wynik = a/b
else:
      wynik = 'nie ma takiego dzialania'
print(wynik)