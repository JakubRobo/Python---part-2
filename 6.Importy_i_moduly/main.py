import mod
mod.dodawanie
mod.odejmowanie
mod.dzielenie
mod.mnozenie


print("Wybierz działanie.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnozenie")
print("4.Dzielenie")

while True:
    choice = input("Wybierz liczbę (1/2/3/4): ")

    num1 = float(input("Wpisz pierwszą liczbę: "))
    num2 = float(input("Wpisz drugą liczbę: "))

    if choice == '1':
            print(num1, "+", num2, "=", mod.dodawanie(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", mod.odejmowanie(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", mod.mnozenie(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", mod.dzielenie(num1, num2))
        
    dalej = input("Liczymy dalej? (tak/nie): ")
    if dalej == "nie":
        break
    else:
        print("Błąd")