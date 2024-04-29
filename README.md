# Pidec (Python)
Calcul de la n-ième décimale de Pi directement sans calculer les précédentes.

Ce programme permet de calculer la n-ième décimale de pi en utilisant l'algorithme décrit dans l'article "Computation of the n-th decimal digit of π with low memory" (moodle université de rennes : https://foad.univ-rennes.fr/pluginfile.php/2491227/mod_resource/content/1/nthdecimaldigit.pdf)

Cette implémentation est une traduction en python de celle en C++ de Xavier Gourdon, auteur de l'article, disponible à l'adresse http://numbers.computation.free.fr/Constants/Algorithms/pidec.cpp

# Avertissement 
Ce programme s'inscrit dans un cours d'Arithmétique et est un jouet. Il ne devrait **jamais** être utiliser pour le réel calcul de décimales de Pi, d'autant plus qu'il est codé en Python. Python est un langage particulièrement lent (cf : https://sci-hub.3800808.com/10.1038/s41550-020-1208-y), le cout en temps et en énergie d'utiliser ce programme est très élévé. Il serait préférable d'utiliser l'implémentation en C++ de Xavier Gourdon. 