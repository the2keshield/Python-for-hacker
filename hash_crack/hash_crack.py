# Importation du module hashlib pour les fonctions de hachage
# Importation du module sys pour les fonctions système
import hashlib
import sys

# Demande à l'utilisateur de saisir un mot de passe à deviner
# `input()` est utilisé pour recueillir l'entrée de l'utilisateur
mot_de_passe = input("Quel est le mot de passe à deviner :")

# Hachage du mot de passe saisi en utilisant MD5
# `.encode("utf")` convertit la chaîne en bytes, nécessaire pour le hachage
# `hexdigest()` convertit le hash en une chaîne hexadécimale
mot_de_passe_md5 = hashlib.md5(mot_de_passe.encode("utf")).hexdigest()

# Affichage du hash MD5 du mot de passe saisi
print(mot_de_passe_md5)

# Définition d'une fonction pour essayer de casser le hash
def hash_crack():
    try:
        # Ouverture du fichier contenant une liste de mots en français
        # Le chemin est spécifié pour un système Kali Linux
        mot_fr = open("/home/kali/Desktop/liste_francais.txt")

        # Initialisation d'un indicateur pour suivre si le mot de passe a été trouvé
        trouve = False

        # Parcours chaque ligne (mot) dans le fichier
        for mot in mot_fr.readlines():
            # Nettoyage et encodage du mot pour le hachage
            mot = mot.strip("\n").encode("utf8")

            # Création d'un hash MD5 pour le mot courant
            hashmd5 = hashlib.md5(mot).hexdigest()

            # Vérification si le hash correspond au hash du mot de passe entré
            if hashmd5 == mot_de_passe_md5:
                # Si trouvé, afficher le mot et son hash, et mettre l'indicateur à True
                print("Mot de passe trouvé :)....", str(mot), "(", hashmd5, ").")
                trouve = True

        # Si le mot de passe n'a pas été trouvé après la boucle, afficher un message
        if not trouve:
            print("Mot de passe introuvable...")

        # Fermeture du fichier
        mot_fr.close()

    # Gestion des exceptions pour les erreurs de fichier
    except FileExistsError:
        print("Erreur; fichier ou dossier introuvable...")
        sys.exit(1)

    # Gestion des autres exceptions
    except Exception as err:
        print("Erreur :", str(err))
        sys.exit(2)

# Appel de la fonction pour lancer le processus de craquage de mot de passe
hash_crack()