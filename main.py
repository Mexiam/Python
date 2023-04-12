# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print("-----------------------------------------Ex 1-----------------------------------------")
def celcius_farenheit(celcius):
    F = (celcius*9/5)+32
    return F

temperature_celcius = 22
print(celcius_farenheit(temperature_celcius))

print("-----------------------------------------Ex 2-----------------------------------------")

def mention(note):
    if note < 10:
        return "insuffisant"
    if 10 <= note < 12:
        return "passable"
    if 12 <= note < 14:
        return "assez bien"
    if 14 <= note < 16:
        return "passable"
    if 16 <= note <= 20:
        return "très bien"

print(mention(13))

print("-----------------------------------------Ex 3-----------------------------------------")

def nombre_pairs(n):
    array = []
    for i in range(n+1):
        if i % 2 == 0:
            ar=[i]
            array.extend(ar)
    return array

print( nombre_pairs(10) )

print("-----------------------------------------Ex 4-----------------------------------------")

def remplacer(texte, caractere, nouveau_caractere):
    str = ""
    for char in texte:
        if char == caractere:
            str += nouveau_caractere
        else:
            str += char
    return str

print( remplacer("toto", "o" , "i") )
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("-----------------------------------------Ex 5-----------------------------------------")

def est_palindrome(mot) :
    return mot == mot[::-1]

print( est_palindrome("ressasser") ) # affiche : True
print( est_palindrome("palindrome") ) # affiche : False


print("-----------------------------------------Ex 6-----------------------------------------")

def triplets_pythagoriciens(n) :
    tab = []
    for a in range(n+1):
        for b in range(a+1,n+1):
            for c in range(b+1,n+1):
                if c**2 == a**2 + b**2:
                     tab.append((a,b,c))
    return tab

print( triplets_pythagoriciens(20) )

print("-----------------------------------------Ex 7-----------------------------------------")
def diviseurs(n) :
    tab = []
    for i in range(1,n+1):
        if n % i == 0:
            tab.append(i)
    return tab

print( diviseurs(60) )

print("-----------------------------------------Ex 8-----------------------------------------")
def est_parfait(n) :
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum == n


print( est_parfait(6) ) # affiche : True
print( est_parfait(42) ) # affiche : False
print( est_parfait(8128) ) # affiche : True
print("-----------------------------------------Ex 9-----------------------------------------")

def occurrences_lettres(mot) :
    dic = {
    }
    for lettre in mot:
        if lettre in dic:
            dic[lettre] += 1
        else:
            dic[lettre]=1
    return dic

print( occurrences_lettres("ANTICONSTITUTIONNELLEMENT") )
print("-----------------------------------------Ex 10-----------------------------------------")
points_lettres = {
        1: ["E", "A", "I", "N", "O", "R", "S", "T", "U", "L"],
        2: ["D", "M", "G"],
        3: ["B", "C", "P"],
        4: ["F", "H", "V"],
        8: ["J", "Q"],
        10: ["K", "W", "X", "Y", "Z"]
    }
def calculer_score(mot, points_lettres) :
    sum = 0
    for lettre in mot:
        for points, lettres in points_lettres.items():
                if lettre in lettres:
                    sum += points
    return sum

print( calculer_score("POMME", points_lettres) ) # affiche : 9
print( calculer_score("JUKEBOX", points_lettres) ) # affiche : 34
