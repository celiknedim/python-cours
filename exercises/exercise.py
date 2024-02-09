
# resultat = 12 + 5
# print(resultat)

# first_name = 'nedim'
# print('Bonjour', first_name)

# surname = input('enter your surname = ')
# print('Bonjour', surname)

# date = int(input('your date de naissance = '))
# age = 2024 - date
# print('Bonjour', first_name, surname, 'tu as',age, 'ans')

# number = input('enter your number ')
# print('double of', number, 'is = ', 2*int(number))

# poid = float(input('enter your weight(kg) '))
# taille = float(input('enter your height(cm) '))
# imc = poid/taille
# print(f'your imc is =  {imc:.2f}')

# ========================================================

# exercise 7

# color = '\033[0m'
# color2 = '\033[5;32m\033[44m'
# # print(f"test :  {color}XXXXXXX{color2}...")


# name = input('enter your name ')
# leng = len(name)

# horizontal = '─'
# vertical = '│'
# top_left = '┌'
# top_right = '┐'
# bottom_left = '└'
# bottom_right = '┘'

# msg=f"""
# {color2}{top_left}{horizontal*(leng+2)}{top_right}{color}
# {color2}{vertical} {name} {vertical}{color}
# {color2}{bottom_left}{horizontal*(leng+2)}{bottom_right}{color}
# """

# print(msg)

# print(top_left+horizontal*(leng+2)+top_right)
# print(vertical+' '+name+' '+vertical)
# print(bottom_left+horizontal*(leng+2)+bottom_right)


# ===========================


# exercise 8

# text = 'nedito       hugoto       laurito      nicoto       alexito          morismo'

# # new = text.replace(' ', '/')
# # print(new)

# new2 = '/'.join(text.split())
# print(new2)

# ----------------------

# # exercise 11

# mon = int(input('entrez le montant '))
# per = int(input('entrez le percentage (%) '))

# calc = mon * per / 100
# print(calc)

# --------------------

# # exercise 14

# l1 = float(input('longeur 1? '))
# l2 = float(input('longeur 2? '))

# hypesquare = l1**2 + l2**2
# hype = hypesquare**(0.5)

# # print(hype)
# print(f'hypetenuse =  {hype:.2f}')

# math.sqrt  da olur math class ini import et tabii


# -----------------------------


# # exercise 15

# monht = float(input('entrez le montant '))
# taux = float(input('entrez le taux (%) '))

# ttc = monht + (monht * taux / 100)
# print(ttc)



# -----------------------------

# # exercise 16

# power = int(input("entrez un nombre "))
# nombre = 2**power
# chiffre = len(str(nombre))
# print(chiffre)


# exercise 16/2

# import math
# power = int(input("entrez un nombre "))
# print(math.log10(2) * power)


# ======================================

# exercise 21
 
import re


texte = "Voici une chaîne de caractères avec une adresse e-mail exemple@example.com et une autre adresse test@test.com. rexdmid@fkdslgbdgnj.fr zdifeklgnzrbf koefzgreolmfe,klge,bremtkb;fmb mclaren@campus.fr fkezl,nmegkrzpùek"

pattern_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

resultats = re.findall(pattern_email, texte)

print("Adresses e-mail trouvées :")
for adresse in resultats:
    print(adresse)


