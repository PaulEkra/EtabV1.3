from models.Personne import Personne
import mysql.connector
from mysql.connector import Error
from Interfaces.ICRUDElve import ICRudeleve
from datetime import datetime

class Eleve(Personne,ICRudeleve):

    def __init__(self, id, dateNaissance, ville, prenom, nom, telephone, classe,matricule):
        super().__init__(id, dateNaissance, ville, prenom, nom, telephone)
        self.__classe = classe
        self.__matricule = matricule

    def __str__(self):
        return f"[ID: {self.get_id},MATRICULE: {self.get_matricule()} NOM: {self.get_nom()}, PRENOMS: {self.get_prenom()}, DATE DE NAISSANCE: {self.get_dateNaissance()}, VILLE: {self.get_ville()}, CLASSE: {self.get_classe()}]"

    # Getter et Setter pour la classe
    
    def get_classe(self):
        return self.__classe
    
    def set_classe(self, classe):
        self.__classe = classe

    def get_matricule(self):
        return self.__matricule
    
    def set_matricule(self, matricule):
        self.__matricule = matricule

    # Méthodes 
    #Methode ajouter
    @staticmethod
    def ajouter(eleve):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
                
                cursor.execute("INSERT INTO personnes (date_naissance, ville, prenom, nom, telephone) VALUES (%s, %s, %s, %s, %s)",
                            (eleve.get_dateNaissance(), eleve.get_ville(), eleve.get_prenom(), eleve.get_nom(), eleve.get_telephone()))
                connection.commit()
                id_personne = cursor.lastrowid

                cursor.execute("INSERT INTO eleves (id_personne, classe, matricule) VALUES (%s, %s, %s)",
                            (id_personne, eleve.get_classe(), eleve.get_matricule()))
                connection.commit()
                print(f"Élève {eleve.get_prenom()} {eleve.get_nom()} ajouté avec succès.")

        except Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    #Methode modifier
    @staticmethod
    def modifier(eleve):
        from Services.Gestions_eleves import edit_choice
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )
            
            if connection.is_connected():
                cursor = connection.cursor()

                update_personne_query = """
                UPDATE personnes 
                SET date_naissance = %s, ville = %s, prenom = %s, nom = %s, telephone = %s 
                WHERE id = %s
                """
                cursor.execute(update_personne_query, 
                        (eleve['personne']['date_naissance'], eleve['personne']['ville'], eleve['personne']['prenom'], eleve['personne']['nom'], eleve['personne']['telephone'], eleve['personne']['id']))                
                update_eleve_query = """
                UPDATE eleves 
                SET classe = %s, matricule = %s 
                WHERE id_personne = %s
                """
                cursor.execute(update_eleve_query, (eleve['eleve']['classe'], eleve['eleve']['matricule'], eleve['eleve']['id']))
                
                connection.commit()

                print(f"Élève {eleve['personne']['prenom']} {eleve['personne']['nom']} modifié avec succès.")
                edit_choice(eleve)
        
        except Error as e:
            print(f"Erreur lors de la modification de l'élève : {e}")
            

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


        
    #Methode lister
    @staticmethod
    def ObtenirEleve():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
                query = " SELECT personnes.id, personnes.nom, personnes.prenom, personnes.ville, personnes.date_naissance, personnes.telephone, eleves.classe, eleves.matricule FROM personnes JOIN eleves ON personnes.id = eleves.id_personne"
                cursor.execute(query)
                eleves = cursor.fetchall()

                if not eleves:
                    return "Il n'y a pas d'élève."
            
            return eleves
        except Error as e:
            print(f"Error: {e}")
            return False

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    #Methode supprimer
    @staticmethod
    def supprimer(id):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
                # Commencez une transaction
                connection.start_transaction()

                # Supprimez d'abord l'élève
                delete_personne_query = "DELETE FROM personnes WHERE id = %s"
                cursor.execute(delete_personne_query, (id,))

                # Supprimez ensuite l'élève associé
                delete_eleve_query = """
                    DELETE FROM eleves 
                    WHERE id_personne = %s
                """
                cursor.execute(delete_eleve_query, (id,))

                # Validez la transaction
                connection.commit()
                print(f"Élève avec ID {id} supprimés.")
        
        except Error as e:
            print(f"Error: {e}")
            
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
  
    #Methode obtenir
    @staticmethod
    def obtenir(identifiant):
        from Services.Gestions_eleves import edit_eleve
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )
            
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                get_personne_query = "SELECT * FROM personnes WHERE id = %s"
                cursor.execute(get_personne_query, (identifiant,))
                personne = cursor.fetchone()

                if personne:
                    get_eleve_query = "SELECT * FROM eleves WHERE id_personne = %s"
                    cursor.execute(get_eleve_query, (identifiant,))
                    eleve = cursor.fetchone()
                    if eleve:
                        result = {
                            'personne': personne,
                            'eleve': eleve
                        }
                        return result
                    else: print("Ce n'est pas un élève")
                else:
                    print(f"Il y a 0 élève avec ID {identifiant}")
                    return edit_eleve()

        except Error as e:
            print(f"Error: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    

    