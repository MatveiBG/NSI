import random

def slot_partie(mise): #fonction prenant en argument lamise sur laquelle l'utlisateur va jouer
    gains_slot=0 #création de la variable gains_slot qui définit combien ont été gagné sur cette session

    symboles=['7','cloche','bar3','bar2','bar1','lemon','scatter'] #liste des symboles tirables

    #définition des symboles tirés
    p1=random.randint(0,6)
    p2=random.randint(0,6)
    p3=random.randint(0,6)
    p4=random.randint(0,6)
    p5=random.randint(0,6)
    p6=random.randint(0,6)
    p7=random.randint(0,6)
    p8=random.randint(0,6)
    p9=random.randint(0,6)

    tirage=[p1,p2,p3,p4,p5,p6,p7,p8,p9] #création d'une liste des valeurs utiliées pour définir les gains

    #vérification des tirages des 7
    if tirage.count(0)==3:
        gains_slot=gains_slot+(mise*2)
        print("Vous avez tirer 3 syboles '7', vous gagnez: ",mise*2)
    elif tirage.count(0)==4:
        gains_slot=gains_slot+(mise*5)
        print("Vous avez tirer 4 syboles '7', vous gagnez: ",mise*5)
    elif tirage.count(0)==5:
        gains_slot=gains_slot+(mise*20)
        print("Vous avez tirer 5 syboles '7', vous gagnez: ",mise*20)
    elif tirage.count(0)==6:
        gains_slot=gains_slot+(mise*50)
        print("Vous avez tirer 6 syboles '7', vous gagnez: ",mise*50)
    elif tirage.count(0)==7:
        gains_slot=gains_slot+(mise*200)
        print("Vous avez tirer 7 syboles '7', vous gagnez: ",mise*200)
    elif tirage.count(0)==8:
        gains_slot=gains_slot+(mise*1000)
        print("Vous avez tirer 8 syboles '7', vous gagnez: ",mise*1000)
    elif tirage.count(0)==9:
        gains_slot=gains_slot+(mise*9000)
        print("Vous avez tirer 9 syboles '7', vous gagnez: ",mise*9000)

    #vérification des tirages des scatters
    dice1=0
    dice2=0
    if tirage.count(6)==3 or tirage.count(6)>3:
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print("Vous venez de faire un triple scatter!!")
        if dice1==dice2:
            gains_slot=gains_slot+mise*10
            print("Vous avez tiré un double au dés et avez donc gagner 10 fois votre mise soit:", mise*10)
        else:
            gains_slot=gains_slot+mise*2
            print("Vous n'avez pas tiré un double au dés et avez donc gagner 2 fois votre mise soit:", mise*2)

    #vérification de toutes les autres combinaisons
    def multi(pos): #définition d'une fonction à laquelle faire appel pour les mutiplicateurs
        gains_temp=0
        if pos==1:
            gains_temp=gains_temp+mise*8
        elif pos==2:
            gains_temp=gains_temp+mise*6
        elif pos==3:
            gains_temp=gains_temp+mise*4
        elif pos==4:
            gains_temp=gains_temp+mise*3
        elif pos==5:
            gains_temp=gains_temp+mise*1
        return gains_temp

    #p1-p2-p3 (horizontale haut)
    if p1==p2 and p1==p3 and p1!=0 and p1!=6:
        gains_slot=gains_slot+multi(p1)
        print('bravo vous gagnez:',multi(p1))

    #p1-p5-p9 (diagonale haut-gauche to bas-droite)
    if p1==p5 and p1==p9 and p1!=0 and p1!=6:
        gains_slot=gains_slot+multi(p1)
        print('bravo vous gagnez:',multi(p1))

    #p1-p4-p7 (verticale gauche)
    if p1==p2 and p1==p3 and p1!=0 and p1!=6:
        gains_slot=gains_slot+multi(p1)
        print('bravo vous gagnez:',multi(p1))

    #p2-p5-p8 (verticale milieu)
    if p2==p5 and p2==p8 and p2!=0 and p2!=6:
        gains_slot=gains_slot+multi(p2)
        print('bravo vous gagnez:',multi(p2))

    #p3-p6-p9 (verticale droite)
    if p3==p6 and p3==p9 and p3!=0 and p3!=6:
        gains_slot=gains_slot+multi(p3)
        print('bravo vous gagnez:',multi(p3))

    #p3-p5-p7 (diagonale haut-droite to bas-gauche)
    if p3==p5 and p3==p7 and p3!=0 and p3!=6:
        gains_slot=gains_slot+multi(p3)
        print('bravo vous gagnez:',multi(p3))

    #p4-p5-p6 (horizontale milieu)
    if p4==p5 and p4==p6 and p4!=0 and p4!=6:
        gains_slot=gains_slot+multi(p4)
        print('bravo vous gagnez:',multi(p4))

    #p7-p8-p9 (horizontale bas)
    if p7==p8 and p7==p9 and p7!=0 and p7!=6:
        gains_slot=gains_slot+multi(p7)
        print('bravo vous gagnez:',multi(p7))

    return gains_slot, tirage
slot_partie(13)





import sys, time, pygame
from tkinter import *
from sqlite3 import *
from pygame.locals import *
#from Casino_Matvei.test import slot_partie

pygame.init()

screen = pygame.display.set_mode((1600, 900))

#image fond machine

fond_slot= pygame.image.load("images/fond_slot_machine.png")


screen.blit(fond_slot, (0, 0))


#importation de toutes les images

bar= pygame.image.load("images/bar.png")
bar_2= pygame.image.load("images/bar_2.png")
bar_3= pygame.image.load("images/bar_3.png")
symb_7= pygame.image.load("images/symb_7.png")
bar= pygame.image.load("images/bar.png")
cherry= pygame.image.load("images/cherry.png")
cloche=pygame.image.load("images/cloche.png")

pos_1=(495, 95)
pos_2=(700, 95)
pos_3=(905, 95)
pos_4=(495, 300)
pos_5=(700, 300)
pos_6=(905, 300)
pos_7=(495, 505)
pos_8=(700, 505)
pos_9=(905, 505)
list_pos=[pos_1,pos_2,pos_3,pos_4,pos_5,pos_6,pos_7,pos_8,pos_9]

symboles=['7','cloche','bar3','bar2','bar1','lemon','scatter']

list_symbole = [1,2,1,1,2,1,1,2,1]


for i in range (9):
    if list_symbole[i-1]==0:
        screen.blit(symb_7,list_pos[i-1])
    elif list_symbole[i-1]==1:
        screen.blit(cloche,list_pos[i-1])
    elif list_symbole[i-1]==2:
        screen.blit(bar_3,list_pos[i-1])
    elif list_symbole[i-1]==3:
        screen.blit(bar_2,list_pos[i-1])
    elif list_symbole[i-1]==4:
        screen.blit(bar,list_pos[i-1])
    elif list_symbole[i-1]==5:
        screen.blit(lemon,list_pos[i-1])
    elif list_symbole[i-1]==6:
        screen.blit(scatter,list_pos[i-1])
pygame.display.flip()
