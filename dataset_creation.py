import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from random import *
import os
import copy

#Transformation d'une image en tableau numpy
#img = mpimg.imread(".\\Données\\dataset1\\images\\9326871.1.jpg")
# plt.imshow(img)
# plt.show()
# print(img)


def premier_point(st): #récupère l'identifiant d'un individu
    if st =='0':
        return('0')
    i=0
    n=len(st)
    while st[i]!='.'and i<n:
        i=i+1
    return st[:i]

def appartenance_individu(photo,liste,G): #teste si l'individu de la photo est présent dans la liste des photos des individus
   #G est la correspondance index-photo, cad gallery
   Individu=premier_point(G[photo])
   for i in range(len(liste)):
       if premier_point(G[liste[i]])==Individu:
           return True
   return False

def dataset_separation(path_vers_images):
    gallery = copy.copy(os.listdir(path_vers_images))
    data_probe_match=[]
    data_probe_not_match=[]
    h=[]
    for i in range(0,200): #récupération de 200 photos aléatoirement
        nb_aleatoire= randint(0,len(gallery)-1)
        while (nb_aleatoire in h) or appartenance_individu(nb_aleatoire,h,gallery):
            nb_aleatoire= randint(0,len(gallery)-1)
        h.append(nb_aleatoire)
    for i in range(100): #parmi les 200 photos sélectionnées, on en tire 100 qui constitueront le dataset probe_match
        nb_aleatoire= choice(h)
        data_probe_match+= [gallery[nb_aleatoire]] #on ajoute la photo tirée aléatoirement dans le probe_match
        h.remove(nb_aleatoire)
        gallery[nb_aleatoire]='0' #on supprime les photos qui serviront pour le dataset_probe_match de la gallery
    for i in range(len(h)):
        data_probe_not_match+=[gallery[h[i]]] #on ajoute le reste des photos tirées aléatoirement dans le jeu de données qui ne devrait pas marcher
        I = premier_point(gallery[h[i]])
        for j in range(len(gallery)):
            p = premier_point(gallery[j])
            if p==I:
                gallery[j]='0'
    while ('0' in gallery):
        gallery.remove('0')
    return (gallery, data_probe_match, data_probe_not_match)

#pour vérifier que les datasets soient bien constitués, on vérifie qu'il n'y a pas de doublons des probe dans gallery
def test_doublon(i,path_vers_images):
   l=sorted(dataset_separation(path_vers_images)[i])
   for i in range(len(l)-1):
       if premier_point(l[i])==premier_point(l[i+1]):
           return True
   return False
