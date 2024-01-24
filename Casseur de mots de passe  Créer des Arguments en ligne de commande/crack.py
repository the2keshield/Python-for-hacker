# Importation des modules nécessaires
import sys
import hashlib
import argparse

# Configuration de l'analyseur d'arguments pour interpréter les options de ligne de commande
parser = argparse.ArgumentParser(description="Crackeur de mot de passe")

# Ajout d'options pour le fichier de dictionnaire, la génération de hash MD5, et le hash MD5 à craquer
parser.add_argument("-f", "--file", dest="file", help="Lien du dictionnaire dans Explorer", required=False)
parser.add_argument("-g", "--gen", dest="gen", help="Generer MD5 hash of password", required=False)
parser.add_argument("-md5", dest="md5", help="Hashed password MD5", required=False)

# Parsing des arguments de la ligne de commande
args = parser.parse_args()

# Définition d'une fonction pour tenter de craquer un hash MD5 en utilisant un fichier de dictionnaire
def crack_dict(md5, file):
    try:
        # Indicateur pour savoir si le mot de passe a été trouvé
        trouve = False

        # Ouverture du fichier de dictionnaire
        ofile = open(file, "r")
        for mot in ofile.readlines():
            # Nettoyage et encodage du mot du dictionnaire
            mot = mot.strip("\n").encode("utf8")

            # Hachage du mot en MD5
            hashmd5 = hashlib.md5(mot).hexdigest()

            # Vérification si le hash correspond au hash fourni
            if hashmd5 == md5:
                print("Mot de passe trouvé : " + str(mot) + " (" + hashmd5 + ")")
                trouve = True

        # Si le mot de passe n'est pas trouvé, afficher un message
        if not trouve:
            print("Mot de passe non trouvé")

        # Fermeture du fichier de dictionnaire
        ofile.close()

    # Gestion des exceptions pour les erreurs de fichier
    except FileNotFoundError:
        print("Erreur ; nom de dossier ou fichier introuvable !")
        sys.exit(1)
    except Exception as err:
        print("Erreur : " + str(err))
        sys.exit(2)

# Vérification si un hash MD5 est fourni et lancement du processus de craquage
if args.md5:
    print("[CRACKING HASH " + args.md5 + "]")
    if args.file:
        print("[USING DICTIONARY FILE " + args.file + "]")
        crack_dict(args.md5, args.file)
else:
    print("MD5 HASH NOT PROVIDED")

# Si l'option de génération de hash est utilisée, générer et afficher le hash MD5 du mot de passe fourni
if args.gen:
    print("[MD5 HASH OF " + args.gen + " : " + hashlib.md5(args.gen.encode("utf8")).hexdigest())
