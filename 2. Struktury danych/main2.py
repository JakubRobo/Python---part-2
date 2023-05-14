word = input("Podaj słowo: ")

palindrom = word[::-1]

if word == palindrom:
    print("słowo jest palindromem")
else:
    print("nie jest palindromem")