# Projet ARIC Valentin Regnault - Nathan Corneloup - 2024
# Ce programme permet de calculer la n-ième décimale de pi en utilisant l'algorithme décrit dans 
# l'article "Computation of the n-th decimal digit of π with low memory" (moodle université de rennes : https://foad.univ-rennes.fr/pluginfile.php/2491227/mod_resource/content/1/nthdecimaldigit.pdf)

# Cette implémentation est une traduction en python de celle en C++ de Xavier Gourdon, auteur de l'article, disponible à l'adresse http://numbers.computation.free.fr/Constants/Algorithms/pidec.cpp

from math import ceil, comb, gcd, log, e, floor, sqrt, fmod
from random import random


def pgcd_etendu(a, b, d):
    if b == 0:
        return 1, 0, d
    else:
        u, v, d = pgcd_etendu(b, a % b, d)
        return v, u - (a // b) * v, d

def inverse_modulaire(a, m):
    u, v, d = pgcd_etendu(a, m, 1)
    if u < 0:
        u += m
    return u

def facteurs_premiers_inferieur_a(m, k):
    facteurs = set()
    current = m
    p = 2
    while p * p <= current:
        if current % p == 0:
            current //= p
            if p <= k:  
                facteurs.add(p)
        else:
            p += 1

    if current > 1 and current <= k:
        facteurs.add(current)

    return list(facteurs)


def algorithm2(n, k, m):  
    # etape 1  
    # Calcul des facteurs premiers de m inférieurs à k
    facteurs = facteurs_premiers_inferieur_a(m, k)
    l = len(facteurs)

    R = [1] * l

    RDenominateurs = [facteurs[i] for i in range(l)]
    RNumerateurs = [facteurs[i] * (n // facteurs[i]) for i in range(l)]

    # etape 2
    # initialisation des variables
    A, B, C = 1, 1, 1

    # etape 3
    # calcul de S
    for j in range(1, k + 1):
        # a - initialisation des variables
        a = n - j + 1
        b = j

        # b - decomposition de a et b
        for i in range(l):
            p = facteurs[i]
            if RNumerateurs[i] == n - j + 1:
                RNumerateurs[i] -= p
                R[i] *= p
                a /= p
                while a % p == 0:
                    R[i] *= p
                    a //= p

            if RDenominateurs[i] == j:
                RDenominateurs[i] += p
                R[i] //= p
                b /= p
                while b % p == 0:
                    R[i] //= p
                    b //= p
        
        # c - aggregation des résultats
        acc = 1
        if len(R) > 0:
            acc = R[0]
            for i in range(1, l):
                acc = (acc * R[i]) % m


        # d - calcul de A, B et C   
        A = (A * a) % m
        B = (B * b) % m
        C = (C * b + A * acc) % m
        

    # etape 4
    # calcul de S par division de C par B (avec l'inverse modulaire)
    S = C * inverse_modulaire(B, m) % m
    return S

def algorithm1(n):
    # calculs de M et N
    n0 = 15
    logn = log(n)
    M = 2 * floor(3*n / logn**3)  # M is even
    N = 1 + floor((n+n0)*log(10) / (1+log(2*M)))
    N += N % 2  # N should be even

    # calcul de B
    b = 0.0
    for k in range(0, (M +1) * N, 2):
        mod1 = 2*k+1
        mod2 = 2*k+3
        b += (((10**n) % mod1) * 4 % mod1) / mod1 - (((10**n) % (mod2)) * 4 % (mod2)) / mod2
        b -= ceil(b)
    

    # Calcul de C
    c = b
    for k in range(N):
        m = 2 * M * N + 2 * k + 1
        x = algorithm2(N,k,m)
        y = ((5**N % m) * 10**(n - N) * 4 * x) % m
        c += (2 * (k % 2) - 1) * y / m 
        c -= floor(c)
    
    return c


if __name__ == "__main__":
    n = int(input("Quel décimale de pi vous interesse ? Entrer son numéro (fonctionne qu'avec des grandes valeurs) : "))
    x = algorithm1(n)
    y = x * 1e9
    print(f"la {n}ème décimale de pi est : {str(floor(y))[0]}. Les suivantes sont : {str(floor(y))[1:]}")