import datetime
heure = datetime.datetime.now().strftime("%H:%M")



# Fontion message de bienvenue
def print_welcome_message():
    print(f"\t ****************************************************** \n\n\t\tBIENVENU DANS L’APPLICATION ETAB v1.2\n\n\t ******************************************************\n")

# def connexion():
#     print_welcome_message()
#     identifiant=input("Identifiant : ")
#     motDePasse=input("Mot de passe : ")

    

#Fonctions Menu Principal
def print_menu():
    print(f"""MENU:\n
      1: Gestion des élèves\n
      2: Gestion des professeurs\n
      3: Gestion des utilisateurs\n
      0: Quitter\n
 Date système :{heure}\n""")

def accueil():
    print_welcome_message()
    print_menu()

    

     
def get_whit_no_space(prompt):
    choix = input(prompt)
    return "".join(choix.split())

def erreur(prompt):
    print(prompt)


def get_user_choice(text,function1,function2):
    while True:
        # try:
            choix = get_whit_no_space(text)
            
            if choix == "1":
                function1()
                break 
            elif choix == "2":
                function2()
                break  
            else:
                erreur("Choix invalide. Veuillez entrer '1' ou '2'.")