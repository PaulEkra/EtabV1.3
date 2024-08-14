import mysql.connector
from mysql.connector import Error
from datetime import datetime
#Classe Utilisateur
class Utilisateur:
    
    def __init__(self,pseudo,motDePasse,dateCreation):
        self.__id = Utilisateur.next_id
        self.__pseudo = pseudo
        self.__motDePasse = motDePasse
        self.__dateCreation = dateCreation

    def __str__(self) -> str:
        return f"[Identifiant:{self.get_pseudo()} | Mot de passe:{self.get_motDePasse()}]"
    #Getters
    def get_id(self):
        return self.__id
        
    def get_pseudo(self):
        return self.__pseudo
    
    def get_motDePasse(self):
        return self.__motDePasse
    
    def get_dateCreation(self):
        return self.__dateCreation
    
    #Setters
    def set_id(self,id):
        self.__id = id
    
    def set_pseudo(self,pseudo):
        self.__pseudo = pseudo
    
    def set_motDePasse(self, motDePasse):
        self.__motDePasse = motDePasse

    def set_dateCreation(self,dateCreation):
        self.__dateCreation = dateCreation

    #Methodes
    #Méthode authentification
    @staticmethod
    def authentification(identifiant, motDePasse):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT pseudo, mot_de_passe FROM utilisateurs"
                cursor.execute(query)
                utilisateurs = cursor.fetchall()
                
                for user in utilisateurs:
                    pseudo, mot_de_passe = user
                    if identifiant == pseudo and motDePasse == mot_de_passe:
                        return True
                        
                return False

        except Error as e:
            print(f"Error: {e}")
            return False

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    # Méthode ajouter
    @staticmethod
    def ajouterCompte(identifiant, motDePasse,creationDate):
        from Services.Gestions_Utilisateurs import enregistrer_user, menu_utilisateur

        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM utilisateurs WHERE pseudo = %s", (identifiant,))
                if cursor.fetchone():
                    print("Identifiant déjà utilisé.")
                    enregistrer_user()
                    return

                cursor.execute("INSERT INTO utilisateurs (pseudo, mot_de_passe, date_creation) VALUES (%s, %s, %s)",
                            (identifiant, motDePasse, creationDate))
                connection.commit()
                print(f"Utilisateur {identifiant} ajouté avec succès.")

        except Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    
    # Méthode modifier
    @staticmethod
    def modifierMotDePasse(identifiant, motDePasse):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM utilisateurs WHERE pseudo = %s", (identifiant,))
                user = cursor.fetchone()
                
                if user:
                    cursor.execute("UPDATE utilisateurs SET mot_de_passe = %s WHERE pseudo = %s",
                                (motDePasse, identifiant))
                    connection.commit()
                    print("Mot de passe modifié avec succès.")
                else:
                    print("Utilisateur non trouvé.")

        except Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    #Méthode supprimer
    @staticmethod
    def supprimerCompte(identifiant, motDePasse):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM utilisateurs WHERE pseudo = %s AND mot_de_passe = %s",
                            (identifiant, motDePasse))
                user = cursor.fetchone()
                
                if user:
                    cursor.execute("DELETE FROM utilisateurs WHERE pseudo = %s", (identifiant,))
                    connection.commit()
                    print(f"Utilisateur {identifiant} supprimé avec succès.")
                else:
                    print("Identifiant ou mot de passe incorrect.")

        except Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    #Méthode lister
    @staticmethod
    def listerUtilisateur():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT pseudo, mot_de_passe FROM utilisateurs"
                cursor.execute(query)
                utilisateurs = cursor.fetchall()

                if not utilisateurs:
                    return "Il n'y a pas d'utilisateur."
            
            return utilisateurs
                


        except Error as e:
            print(f"Error: {e}")
            return False

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    #Méthode creation d'un user par defaut
    # @staticmethod
    # def initialize_default_user():
    #     default_username = "admin"
    #     default_password = "admin"
    #     default_dateCreation= datetime.now()
    #     Utilisateur(default_username, default_password,default_dateCreation)
    #     print("Utilisateur par défaut créé.")


    @staticmethod
    def initialize_default_user_sql():
        default_username = "admin"
        default_password = "admin"
        default_dateCreation = datetime.now()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM utilisateurs WHERE pseudo = %s", (default_username,))
                if not cursor.fetchone(): 
                    cursor.execute("INSERT INTO utilisateurs (pseudo, mot_de_passe, date_creation) VALUES (%s, %s, %s)",
                                (default_username, default_password, default_dateCreation))
                    connection.commit()
                    print("Utilisateur par défaut créé.")
                else:
                    print("L'utilisateur par défaut existe déjà.")
                    
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



