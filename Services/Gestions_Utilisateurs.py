import datetime
from menu import print_welcome_message,print_menu,erreur,get_user_choice,get_whit_no_space,accueil
from Classes.Utilisateur import Utilisateur as user

from Classes.ChoixInvalide import ChoixInvalide
# Lancement de l'application
def connexion():
    while True:
        print_welcome_message()
        identifiant=input("Identifiant : ")
        motDePasse=input("Mot de passe : ")
        user.authentification(identifiant, motDePasse)
        if user.authentification(identifiant, motDePasse):
            print_menu()
            break
    
        else:
            erreur("Connexion echouée.\nVeuillez réessayer\n\n")

def menu_utilisateur():
    print(f"""\t******************************************************\n\n\t\t\tGESTION DES Utilisateurs\n\n\t******************************************************\n
Menu :
    1: Ajouter un utilisateur\n
    2: Supprimer un utilisateur\n
    3: Modifier les informations de l'utilisateur\n
    4: Lister les utilisateurs\n
    5: Retour\n
    0: Accueil\n
""")
    try:
        choice = get_whit_no_space("Entrez votre choix:")
        if choice == "1":
            enregistrer_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            edit_user()
        elif choice == "4":
             lister_utilisateurs()
        elif choice == "5" or choice == "0":
            accueil()
            
        else:
                raise ChoixInvalide()
    except ChoixInvalide as e:
            print(e)
            menu_utilisateur()
        

def enregistrer_user():
            
            print("Entrez les informations sur l'utilisateur\n")
            identifiant = input("Entrez l'identifiant : ")
            motDePasse = input("Entrez le mot de passe : ")
            dateCreation = datetime.datetime.now()
            user.ajouterCompte(identifiant, motDePasse,dateCreation)
            get_user_choice("1: Ajouter un nouveau utilisateur\n2: Revenir au menu précendent\nEntrez votre choix:",enregistrer_user,menu_utilisateur)

def edit_user():
    identifiant = input("Entrez l'identifiant pour modifier le mot de passe : ")
    nouveauMotDePasse = input("Entrez le nouveau mot de passe : ")
    user.modifierMotDePasse(identifiant, nouveauMotDePasse)
    get_user_choice("1: Modifier un autre utilisateur\n2: Revenir au menu précendent\nEntrez votre choix:",edit_user,menu_utilisateur)


def delete_user():
    identifiant = input("Entrez l'identifiant à supprimer : ")
    motDePasse = input("Entrez le mot de passe : ")
    user.supprimerCompte(identifiant, motDePasse)
    get_user_choice("1: Supprimer un autre utilisateur\n2: Revenir au menu précendent\nEntrez votre choix:",delete_user,menu_utilisateur)

def lister_utilisateurs():
    utilisateurs = user.listerUtilisateur() 
    if utilisateurs:
        print("Liste des utilisateurs :")
        for u in utilisateurs:
            print(f"Identifiant : {u[0]}, Mot de passe : {u[1]}") 
            
        menu_utilisateur()
    else:
        print("Aucun utilisateur trouvé.")
    
