import time
from menu import accueil,get_whit_no_space,erreur
from Services.Gestions_eleves import menu_eleve
from Services.Gestions_professeurs import menu_professeur
from Services.Gestions_Utilisateurs import connexion,menu_utilisateur
from models.Utilisateur import Utilisateur as u
# Lancement de l'application
start_time = time.time()
u.initialize_default_user_sql()
connexion()
accueil()

# Boucle principale
while True:
    choice = get_whit_no_space("Entrez votre choix: ")
    if choice == "1":
        menu_eleve()
    elif choice == "2":
        menu_professeur()
    elif choice == "3":
        menu_utilisateur()
    elif choice == "0":
        end_time = time.time()
        duration = end_time - start_time
        print(f"Merci d'avoir utilisé l'application ETAB. Au revoir!\n Temps de session:  {duration:.1f} s")
        break
    else:
        erreur("Choix invalide, veuillez réessayer.")
        accueil()