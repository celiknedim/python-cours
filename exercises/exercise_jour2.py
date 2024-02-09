
# nombre = input('entrez un nombre positif ')
# if not nombre.isnumeric():
#     print('entree incorrecte')
#     quit()

# sum = 0

# for i in nombre:
#     sum += int(i)
# print(sum)     


# ==============================================



# for i in range(2, 101, 2):
#     print(i, end=' ')



# ==============================================



# sentence = input('Sentences : ')
# voyelles = 'aeiouàâäéèêëîïôöùûüy'
# sum = 0
# for i in sentence.lower():
#     if i in voyelles:
#         sum += 1
# print(sum)




# ==============================================



# number = input('nombre : ')
# if not number.isnumeric():
#     print('entree incorrecte')
#     quit()

# fact = 1
# if number == 0:
#     print('Factoriel = ', fact)

# for i in range(1, int(number)+1, 1):
#     fact *= i

# print('Factoriel = ',fact)




# ==============================================




# word = input('entrez your word = ')
# for i in range(len(word)):
#     if word[i] != word[-(i+1)]:
#         break
#     else:
#         print(word, 'is palindrome')


# reverse = word[::-1]
# if reverse == word:
#     print('your word is palindrome')





# ==============================================


# import sys, math

# if len (sys.argv) > 1:
#     N = sys.argv[1]
# else:
#     N = input('Chiffre: ')


# if not N.isnumeric():
#     print('entree incorrecte')
#     quit()

# divise = 0
# N = int(N)
# if N==0 or N==1:
#    print(N, ' is not prime number')
# else:
#     for i in range(2, int(math.sqrt(N))):
#         if  N % i == 0:
#             print(N, ' is not prime number')
#             divise = 1
#             break

#     if divise == 0:
#         print(N, ' is a prime number')

    



# ==============================================




# import sys

# if len (sys.argv) > 1:
#     N = sys.argv[1]
# else:
#     N = input('Chiffre: ')


# if not N.isnumeric():
#     print('entree incorrecte')
#     quit()

# n1 = 0
# n2 = 1
# print(n1, n2, end=' ')
# N = int(N)
# for i in range(2,N):    
#     n3 = n2 + n1
#     n1 = n2
#     n2 = n3
#     i+=1
#     print(n2, end=' ')
    
  
    

# ==============================================




# import sys

# if len (sys.argv) > 1:
#     N = sys.argv[1]
# else:
#     N = input('Chiffre: ')


# if not N.isnumeric():
#     print('entree incorrecte')
#     quit()

# sum = 0
# for i in N:
#     i = int(i)
#     sum += pow(i,2)
# print(sum) 




  
    

# ==============================================





# import sys

# if len (sys.argv) > 1:
#     N1 = sys.argv[1]
# else:
#     N1 = input('Chiffre: ')


# if not N1.isnumeric():
#     print('entree incorrecte')
#     quit()

# if len (sys.argv) > 1:
#     N2 = sys.argv[1]
# else:
#     N2 = input('Chiffre: ')


# if not N2.isnumeric():
#     print('entree incorrecte')
#     quit()

# N1 = int(N1)
# N2 = int(N2)

# r = 1
# if N1 > N2:
#     a = N1
# else:
#     a = N2

# if N1 < N2:
#     b = N1
# else:
#     b = N2
# r = b

# while(a % b != 0):
#     r = a % b
#     a = b
#     b = r
# print('pgcd est', r)




  
    

# ==============================================





# import sys

# if len (sys.argv) > 1:
#     N = sys.argv[1]
# else:
#     N = input('Chiffre: ')


# if not N.isnumeric():
#     print('entree incorrecte')
#     quit()


# N = int(N)
# i = 1
# sum = 0
# while(i <= int(N/2)): 
#     if N % i == 0:
#         sum = sum + i
#     i += 1

# if sum == N:
#     print(N, 'is a perfect number')
# else:
#     print(N, 'is not a perfect number')



  
    

# ==============================================



# import sys
# if len(sys.argv)<2:
#     print('il faut 1 chiffre')
#     exit()

# N=int(sys.argv[1])

# result = '1'

# while True:
#     print('chiffre ', N, '(', result, ')')
#     for i in range(2, N):
#         if N % i == 0:
#             print(i, 'divise', N, '->' , N//i)
#             N = N // i
#             result += '*' + str(i)
#             break
#     else:
#         print('pas toruve de diviseur')
#         result += '*'+str(N)
#         break
# print('result', result)



# =================================


# # Définition de la fonction somme_diviseurs_propres
# def somme_diviseurs_propres(nombre):
#     diviseurs_propres = [i for i in range(1, nombre) if nombre % i == 0]
#     return sum(diviseurs_propres)

# # Définition de la fonction recherche_paires_amicaux
# def recherche_paires_amicaux(limite):
#     paires_amicaux = []
    
#     for a in range(2, limite):
#         b = somme_diviseurs_propres(a)
        
#         if a < b < limite and somme_diviseurs_propres(b) == a:
#             paires_amicaux.append((a, b))
    
#     return paires_amicaux

# # Demander à l'utilisateur d'entrer la limite
# limite_utilisateur = int(input("Entrez la limite pour la recherche de paires amicaux : "))

# # Rechercher et afficher les paires amicaux
# resultat = recherche_paires_amicaux(limite_utilisateur)

# # Vérifier si des paires amicaux ont été trouvées
# if resultat:
#     # Afficher les paires amicaux trouvées
#     print("Paires amicaux trouvées :")
#     for paire in resultat:
#         print(paire)
# else:
#     # Afficher un message s'il n'y a aucune paire amicale trouvée
#     print(f"Aucune paire amicale trouvée en dessous de {limite_utilisateur}.")







# ========================================================



