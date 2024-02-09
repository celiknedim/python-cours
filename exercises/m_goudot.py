# '''
# Exercice :
# Écrivez un programme qui demande à l'utilisateur un 
# nombre entier positif et calcule la somme de ses 
# chiffres. 
# Ex: 1234 → 10 car 1 + 2 + 3 + 4 = 10
# '''

# N=input('Chiffre: ')

# if not N.isnumeric():
#     print('Votre entrée est incorrecte...')
#     quit()

# S=0 # Accumulateur

# # Boucle sur les characteres dans N
# for x in N:
#     #~ print('x:',x)
#     S += int(x)

# print("Somme=", S)


# =================================



# '''
# Exercice :
# Écrivez un programme qui affiche tous les nombres pairs de 1 à 100 en 
# utilisant une boucle.
# '''

# for i in range(2, 101, 2): 
#     print(i, end=' ') # sans retour à la ligne

# print() # avec un retour à la ligne



# =================================

# '''
# Exercice :
# Écrivez un programme qui demande à l'utilisateur 
# de saisir une phrase, puis compte et affiche le 
# nombre de voyelles (a, e, i, o, u) dans la phrase.
# '''

# phrase = input('Phrase: ')

# voyelles = "aeiouàâäéèêëîïôöùûüy"

# S=0

# # Pour tous les char de lower(phrase)
# for c in phrase.lower(): 
#     if c in voyelles: 
#         S += 1
    
# print('résultat:', S)



# =================================



# '''
# Exercice :
# Écrivez un programme qui demande à l'utilisateur un 
# nombre entier positif et calcule sa factorielle. La 
# factorielle de n (notée n!) est le produit de tous 
# les entiers de 1 à n. Par exemple, 5! = 5 × 4 × 3 × 
# 2 × 1 = 120.
# '''
# import sys
# # Boucle infinie pour récupérer un entier
# while True:
#     N=input('Chiffre: ')
#     if N.isnumeric():
#         break
    
# '''
# if len(sys.argv)>1:
#     N=sys.argv[1]
# else:
#     N=input('Chiffre: ')

# if not N.isnumeric():
#     print('Votre entrée est incorrecte...')
#     quit()
# '''

# P=1
# # Calcul de N!
# for n in range(1, int(N)+1):
#     P *= n

# print(N, '!=', P)



# =================================




# '''
# Exercice :
# Écrivez un programme qui vérifie si un mot est un 
# palindrome. Un palindrome est un mot qui se lit de 
# la même manière de gauche à droite et de droite à 
# gauche. Par exemple, "radar" est un palindrome.
# '''
# import sys

# # Utilise le premier parametre de la ligne de commande
# # ou demande le mot
# if len(sys.argv)>1:
#     line=sys.argv[1]
# else:
#     line=input('Mot: ')

# line = line.lower()

# for i in range(len(line)):
#     print(i, line[i], line[-i-1])
#     if line[i] != line[-i-1]:
#         break
# else:
#     print("C'est un palindrome !")



# =================================



# '''
# Exercice :
# Écrivez un programme qui génère les n premiers termes de la suite de 
# Fibonacci. La suite de Fibonacci commence par 0 et 1, puis chaque terme 
# suivant est la somme des deux termes précédents. 
# Par exemple, si l'utilisateur entre n = 5, le programme doit 
# afficher la suite : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# '''

# # f contien les 2 derniers chiffres de la suite
# f=[0, 1]
# print('F 0 = 0')
# print('F 1 = 1')

# # Calcul des nombres suivants, on l'ajoute dans la liste à chaque fois
# for i in range(2,40):
#     f.append(f[-1] + f[-2])

# print(f)

# '''
#     s = f[0] + f[1] # Calcul du terme suivant
#     print('F', i, "=", s)
#     f = [f[1], s] # MaJ de la liste des 2 dernier

#     '''



# =================================




# '''
# Exercice :
# Écrivez un programme qui calcule la somme des carrés des chiffres d'un 
# nombre entier positif donné par l'utilisateur. Par exemple, si 
# l'utilisateur entre 123, le programme doit calculer 1^2 + 2^2 + 3^2 = 14.
# '''

# import sys
# if len(sys.argv)>1:
#     N=sys.argv[1]
# else:
#     N=input('Chiffre: ')

# if not N.isnumeric():
#     print('Votre entrée est incorrecte...')
#     quit()

# S=0 # Accumulateur

# for i in N:
#     # On ajoute le carré du chiffre à chaque fois
#     carre = int(i)**2
#     print(i, carre)
#     S += carre

# print('somme des carré des chiffres:', S)




## =================================




# '''
# Exercice :
# Écrivez un programme qui recherche et affiche tous les nombres parfaits 
# inférieurs à un nombre donné par l'utilisateur. Un nombre parfait est égal 
# à la somme de ses diviseurs propres (les diviseurs autres que lui-même). 
# Par exemple, 28 est un nombre parfait car 1 + 2 + 4 + 7 + 14 = 28.
# '''
# import math

# N=1
# while True:
#     # On va tester si N est parfait...
#     # Quels sont les diviseurs de N???
#     S=0
#     for i in range(1,N):
#         if N % i==0:
#             S+=i
#             #~ print(' ',i)
#     if N==S:
#         print(N, 'est parfait !')
#     N+=1



# =================================


# '''
# Exercice :
# Écrivez un programme qui factorise un nombre donné par l'utilisateur en 
# utilisant la méthode de la division successive par les nombres premiers. 
# Par exemple, si l'utilisateur entre 56, le programme doit afficher la 
# factorisation : 2^3 * 7.
# '''

# import sys
# if len(sys.argv)<2:
#     print('il faut 1 chiffre')
#     exit()

# N=int(sys.argv[1])

# result="1" # Va contenir les diviseurs

# # Recherche d'un nombre diviseur
# while True:
#     print('recherche chiffre:', N, '(', result, ')')
#     # On teste les entiers inférieur à N
#     for i in range(2, N):
#         if N % i == 0: # i divise N
#             print(i, 'divise', N, '->', N//i)
#             # On divise N par i, on ajoute dans result, puis break
#             N = N // i
#             result+="*"+str(i)
#             break # boucle interne
            
#     else: # Si pas de break ci-dessus
#         print('pas trouvé de diviseur...')
#         result+="*"+str(N)
#         break # boucle externe

# print('result', result[2:])



