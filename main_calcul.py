import random, time
  
print("Bonjour, dans ce jeu de calcul mental, il vous faudra trouver le résultat d'une multiplication dans le temps que vous aurez choisi !")
print("Donc bonne chance !")

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!!')
  
def multiplication(a,b):
    global resultat
    resultat=int(a)*int(b)
    return resultat

def answers(reponse):
    while int(reponse)!=int(resultat):
        reponse=input("Rentre la réponse: ")
        while reponse.isdigit()!=True:
            reponse=input("Rentre la réponse !!! ")
    
    if int(reponse)==int(resultat):
        print("Vous avez gagné !")
        print(f"Le résultat était bien {resultat} !")    
    else:
        print("Il y a un problème !")    
            
def request():
    global a,b
    a=input("Rentre le premier nombre: ")
    while a.isdigit()!=True:
        a=input("Rentre le premier nombre: ")


    b=input("Rentre le deuxième nombre: ")
    while b.isdigit()!=True:
        b=input("Rentre le deuxième nombre: ")

t = input("Entre le temps en secondes: ")
while t.isdigit()!=True:
    t = input("Entre le temps en secondes: ")

(request(), multiplication(a, b)) 


reponse=input("Rentre la réponse: ")
while reponse.isdigit()!=True:
    reponse=input("Rentre la réponse: ")


(answers(reponse), countdown(int(t)))

