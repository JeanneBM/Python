# Ten program używa pętli do wyświetlenia
# tabeli liczb i ich kwadratów.

# Pobranie wartości maksymalnej sekwencji liczb.
print('Ten program wyświetla listę liczb')
print('(począwszy od 1) i ich kwadraty.')
end = int(input('Podaj wartość maksymalną: '))

# Wyświetlenie nagłówków tabeli.
print()
print('Liczba\tKwadrat')
print('--------------')

# Wyświetlenie liczb i ich kwadratów.
for number in range(1, end + 1):
    square = number**2
    print(number, '\t', square)


