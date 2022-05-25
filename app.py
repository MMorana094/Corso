from math import *
from typing import Union



print("hello world!")
# nelle stampe multiple python stamperà in ordine riga per riga
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
#Variabili, si usa lo snake style (nome superato da un underscore)
character_age = "70"
character_name = "George"
character_surname = "Rossi"
is_Male = True


print("Hello i'm " + character_name + " " + character_surname + ", i have " + character_age + " years old!")
#lavoriamo con le stringhe

frase = "Gorilla Formaggino"
print(len(frase))                                           #stampo la lunghezza della frase
print(frase[10])                                            #stampo il carattere alla posizione 10 della frase
print(frase.index("o"))                                     #ricerco il valore "o" nella frase
print(frase.replace("Gorilla", "Fantasma"))                 #scambio la parola Gorilla con Fantasma

#lavoriamo con i numeri
print(10%3)
num = -6
print(str(num) + " it's my favorite number")                #casto num a stringa e faccio la stampa concatenata alla stringa
print(abs(num))                                             #restituisce il valore assoluto del numero
print(pow(num, 2))                                          #restituisce la potenza(numero da elevare, potenza)
print(round(4.6584))                                        #arrotondo all'intero più vicino
print(sqrt(36))                                             #ritorna la radice quadrata
print(ceil(36.1))                                           #arrotonda al numero intero maggiore più vicino
#input da tastiera
name = input("enter your name : ")                          #chiedo di inserire un nome
age = input("enter your age : ")                            #chiedo di inserire un età
print("mi chiamo " + name + " ho " + str(age) + " anni!")   #casta l'età in stringa e concateno tutto
