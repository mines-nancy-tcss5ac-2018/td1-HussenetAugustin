#Probl�me 16 Projet Euler

def solve16(n):
    #Renvoie la somme des chiffres de 2**n
    puissance=2**n
    somme=0                         #Initialisation de la somme
    while puissance!=0:             #On s'arr�te quand il n'y a plus de chiffres � additionner
        somme+=puissance%10         #Ajout du dernier chiffre en prenant le reste dans la division par 10
        puissance=puissance//10     #On se "s�pare" du chiffre que l'on vient d'ajouter � la somme.
    return somme

print(solve16(1000))

assert solve16(1000)==1366





#Probl�me 22 Projet Euler

def valeur_lettre(x):
    #Renvoie la valeur associer � chaque lettre de l'alphabet
    alphabet=['"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    i=0
    while x!=alphabet[i]:
        i=i+1
    return i                #La position de la lettre dans la liste correspond � son num�ro associ� (position dans l'alphabet)

def valeur(mot,j):
    #Renvoie la valeur du mot donn� comme d�finit dans le probl�me
    somme=0                     #Correspond � la somme des valeurs correspondant � chaque lettre
    for i in range(len(mot)):
        somme+=valeur_lettre(mot[i])     #ord(mot[i])-64
    return somme*j                      #j correspond � la position du mot dans la liste des pr�noms tri�e par ordre alphab�tique

def solve22():
    fichier=open("C:/Users/augus/OneDrive/Documents/p022_names.txt",'r')
    a=fichier.read()                    #on lit le fichier des pr�noms
    liste=a.split(',')                  #on cr�er une liste contenant tous les pr�noms du fichier
    tri=sorted(liste,key=str.lower)     #tri de la liste par ordre alphab�tique
    som=0
    for i in range(0,len(tri)):
        som+=valeur(tri[i],i+1)         #Somme des valeurs des noms de la liste
    return som

print(solve22())

assert solve22()==871198282





#Probl�me 55 Projet Euler

def miroir(x):
    #Renvoie l'inverse de x (le nombre �crit � l'envers)
    chaine=str(x)
    inverse=""
    for i in chaine:
        inverse=i+inverse
    return int(inverse)

def est_palindrome(x):
    #Teste si le nombre x est un palindrome
    return x==miroir(x)

def est_lychrel(x):
    #Teste si le nombre x est un nombre de lychrel
    i=0
    while i<50:                 #On test uniquement les 50 premi�res it�rations (indication donn�e dans le probl�me)
        x=x+miroir(x)
        if est_palindrome(x):
            return False        #Ce n'est pas un nombre de lychrel si on obtient un palindrome avant les 50 premi�res it�rations
        i=i+1
    return True

def solve55():
    #Renvoie le nombre de nombre de lychrel inf�rieur � 10 000
    compteur=0
    for i in range(10000):
        if est_lychrel(i):
            compteur+=1         #Si on obtient un nombre de lychrel, on ajoute 1 au compteur de nombre de lychrel
    return compteur

print(solve55())