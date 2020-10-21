# -*- coding: utf8 -*-
import useful_tolls

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 10, 12],
]
for row in number_grid:
    print(row)
    for digits in row:
        print(digits)


# Tłumacz

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + 'g'

            else:
                translation = translation + 'g'
                print(letter)

        else:
            translation = translation + letter
            print(letter)
    return translation


print(translate(input('podaj wyraz: ')))
try:
    value = 10 / 0
    number = int(input('Podaj liczbe: '))
    print(number)
# Kursy try except
except ZeroDivisionError as error:
    print(error)
    print('Division Error')
except ValueError:
    print('Value Error')
pracownicy_plik = open('index.html', 'a')
# otwiera plik
# w - pisze
# a - dodaje
# r -czyta
'open write read append file '''
pracownicy_plik.write('\n<p>This is HTML</p>')
# pracownicy_plik.readlines()  # czyta linijki
# pracownicy_plik.readable()  # wartość BOOL czy do odczytu czy nie
# pracownicy_plik.read()  # czyta wszystko bez pętli for ... in
# pracownicy_plik.readline()  # czyta jedną linie
# pracownicy_plik.close()

print(useful_tolls.get_file_ext('index.html'))
