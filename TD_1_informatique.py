#Problème 16 Project Euler

def solve16(n):
    puissance=2**n
    somme=0
    while puissance!=0:
        somme+=puissance%10
        puissance=puissance//10
    return somme

print(solve16(1000))

assert solve16(1000)==1366


#Problème 22 Project Euler

def valeur_lettre(x):
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    i=0
    while x!=alphabet[i]:
        i=i+1
    return i+1

def valeur(mot,j):
    somme=0
    for i in range(1,len(mot)-1):
        somme+=valeur_lettre(mot[i])     #ord(mot[i])-64
    return somme*j

def solve22():
    fichier=open('p022_names.txt','r')
    a=fichier.read()
    liste=a.split(',')
    tri=sorted(liste,key=str.lower)
    som=0
    for i in range(0,len(tri)):
        som+=valeur(tri[i],i+1)
    return som

print(solve22())

assert solve22()==871198282


#Problème 22 Project Euler

def miroir(x):
    chaine=str(x)
    inverse=""
    for i in chaine:
        inverse=i+inverse
    return int(inverse)

def est_palindrome(x):
    chaine=str(x)
    inverse=""
    for i in chaine:
        inverse=i+inverse
    return chaine==inverse

def est_lychrel(x):
    i=0
    while not i<=50:
        x=x+miroir(x)
        if est_palindrome(
        i=i+1
        