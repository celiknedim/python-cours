# Exercice 5 : Liste des Carrés
# Créez une liste contenant les 
# carrés des nombres entre 1 et 10 (inclus).

# x = []
# y = []

# for i in range(11):
#     x.append(i*i)

# print(x)

# y = [i*i for i in range(11) if i%2==0]

# print(y)



################################

mots = '''
Exercice 6 : Filtrage par Longueur de Mot
Étant donné une liste de mots, écrivez une fonction
qui retourne une nouvelle liste contenant uniquement
les mots ayant plus de 4 caractères.
''' 
# mot = []
# for i in mots.split():
#     if len(i) > 3:
#         mot.append(i)
# print(mot)



################################


'''Exercice 8 : Comptage d'Occurrences
Écrivez une fonction qui compte le nombre d'occurrences
de chaque élément dans une liste et retourne un dictionnaire
avec ces comptages.'''

# print(set(mots))

def count_element_dict(malist):
    my_dict = {}
    for i in set(mots):
        countAll = mots.count(i)
        my_dict[i] = countAll
    return my_dict
my_dict = count_element_dict(mots)
print(my_dict)