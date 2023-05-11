krotka = (10, -3, 4, 9, 12, -6, 0)

najwieksza = None
najmniejsza = None

for i in krotka:
    if najmniejsza == None or najmniejsza > i:
        najmniejsza = i
    if najwieksza == None or najwieksza < i:
        najwieksza = i

print("Najmniejsza: ",najmniejsza)
print("Największa: ",najwieksza)