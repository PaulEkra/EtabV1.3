from menu import get_whit_no_space,get_user_choice,accueil
from models.Eleve import Eleve
from datetime import date,datetime
from models.ChoixInvalide import ChoixInvalide
from models.Personne import Personne

#Fonctions Menu ELEVES
def menu_eleve():
     print(f"""\t******************************************************\n\n\t\t\tGESTION DES ELEVES\n\n\t******************************************************\n
Menu :
    1: Ajouter un élève\n
    2: Supprimer un élève\n
    3: Modifier les informations de l'élève\n
    4: Lister les élèves\n
    5: Retour\n
    0: Accueil\n
""")
     try:
            choice = get_whit_no_space("Entrez votre choix:")
            if choice == "1":
                enregistrer_eleve()
            elif choice == "2":
                delete_student()
            elif choice == "3":
                edit_eleve()
            elif choice == "4":
                lister_eleve()
            elif choice == "5" or choice == "0":
                accueil()
                
            else:
                raise ChoixInvalide()
     except ChoixInvalide as e:
            print(e)
            menu_eleve()
            

def enregistrer_eleve():
    nom = input("Entrez le nom de l'élève : ")
    prenom = input("Entrez le prénom de l'élève : ")
    while True:
        try:
            dateNaissance_str = get_whit_no_space("Date de Naissance (format JJ-MM-AAAA): ")
            dateNaissance = datetime.strptime(dateNaissance_str, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Erreur : Format de date invalide. Veuillez entrer la date au format JJ-MM-AAAA.")
    ville = input("Entrez la ville : ")
    while True:
        telephone = input("Entrez le numéro de téléphone : ")
        if telephone.isdigit():
            break
        else:
            print("le numéro doit être numérique")
    classe = input("Entrez la classe : ")
    matricule = input("Entrez le matricule : ")
    eleve = Eleve (None, dateNaissance, ville, prenom, nom, telephone, classe,matricule)
    Eleve.ajouter(eleve)
    get_user_choice(
        "1: Ajouter un nouveau élève\n2: Revenir au menu précédent\nEntrez votre choix:",
        enregistrer_eleve,
        menu_eleve
    )

def delete_student():
    while True:
        id= input("Entrez l'id de lélève à supprimer:")
        if id.isdigit():
             break
        else: print("l'id doit être un entier")
    Eleve.supprimer(id)
    get_user_choice("1: Supprimer un autre élève\n2: Revenir au menu précendent\nEntrez votre choix:",delete_student,menu_eleve)
    
    

        
def edit_eleve():
    try:
        id = int(input("Entrez l'id de l'élève à modifier: "))
    except ValueError:
        print("l'id doit être un entier")
        edit_eleve()
    eleve=Eleve.obtenir(id)
    if eleve :
       edit_choice(eleve)
    else:
        menu_eleve()

def edit_choice(eleve):
    try:
            print("1. Modifier le nom\n2. Modifier le prénom\n3. Modifier la date de Naissance\n4. Modifier la ville\n5. Modifier la classe\n6. Modifier le numéro de téléphone\n7. Modifier le matricule\n8. Retour\n0. Accueil")
            choice = get_whit_no_space("Entrez votre choix:")
            if choice == "1":
                nom=input("Entrez le nom: ")
                eleve['personne']['nom'] = nom
                Eleve.modifier(eleve)
            elif choice == "2":
                prenom=input("Entrez le prenom: ")
                eleve['personne']['prenom'] = prenom
                Eleve.modifier(eleve)
            elif choice == "3":
                while True:
                    try:
                        dateNaissance_str = get_whit_no_space("Date de Naissance (format JJ-MM-AAAA): ")
                        dateNaissance = datetime.strptime(dateNaissance_str, "%d-%m-%Y").date()
                        if dateNaissance:
                            eleve['personne']['date_naissance'] = dateNaissance
                            Eleve.modifier(eleve)
                    except ValueError:
                        print("Erreur : Format de date invalide. Veuillez entrer la date au format JJ-MM-AAAA.")
            elif choice == "4":
                ville=input("Entrez la ville: ")
                eleve['personne']['ville'] = ville
                Eleve.modifier(eleve)
            elif choice == "5":
                classe=input("Entrez la classe: ")
                eleve['eleve']['classe'] = classe
                Eleve.modifier(eleve)
            elif choice == "6":
                while True:
                    tel=input("Entrez le nuémro: ")
                    if tel.isdigit():
                        eleve['personne']['telephone'] = tel
                        Eleve.modifier(eleve)
                        break
                    else:
                        print("le numéro doit être numérique")
            elif choice == "7":
                mat=input("Entrez le matricule: ")
                eleve['eleve']['matricule'] = mat
                Eleve.modifier(eleve)
            elif choice == "8":
                menu_eleve()
            elif choice == "0":
                accueil()
                return
            else:
                raise ChoixInvalide()
    except ChoixInvalide as e:
            print(e)
            edit_choice(eleve)
    
def lister_eleve():
    eleves = Eleve.ObtenirEleve() 
    if eleves is not None:
        print("Liste des élèves :")
        for e in eleves:
            print(f"ID: {e[0]}, Nom : {e[1]}, Prénom : {e[2]}, Ville : {e[3]}, Date de Naissance : {e[4]}, "
                  f"Téléphone : {e[5]}, Classe : {e[6]}, Matricule : {e[7]}") 
        menu_eleve()
    else:
        print("Aucun élève trouvé.")