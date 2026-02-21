import re
from pathlib import Path
import os

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#Task 1: Lecture de fichiers texte : Le journal de bord

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


with open("mission_data/journal_bord.txt", "r", encoding="utf-8") as f:

    # 1 & 2: Ouverture du fichier et affichage du nombre total de lignes
    
    print("*  *  *  Journal de bord *  *  *\n\n" + f.read() + "\n\n")
    f.seek(0) #Repositionne le pointeur de lecture mis en fin par read() en position initial comme quand il y à pas encore eu de lecture
   
    total_lines = len(f.readlines())  #Affiche une liste contenant chaque ligne comme item
    print( f"Journal de bord : {total_lines} entrées\n") 
    
    # 3 : Affichage des lignes d'alert
    
    # Remise à zéro du pointeur de lecture
    f.seek(0)

    alert_lines = []          #Va contenir les lignes d'alerte
    total_number_alert_lines = 0   # compteur

    # Parcours ligne par ligne
    for line in f:
        # re.I (ou re.IGNORECASE) rend la recherche insensible à la casse
        if re.search(r"alerte", line, re.I):
            total_number_alert_lines += 1
            alert_lines.append(line.rstrip("\n"))   # on enlève le \n d’affichage et on ajoute à la liste alert_lines

    print(f"\n--- Alertes détectées ({total_number_alert_lines}) ---\n")
    # Affichage des lignes d'alerte
    for alert_line in alert_lines:
     print(alert_line)
     
     
    # 4 : Ecriture des messages d'alert dans un fichier dédié mission_data/alertes.txt
    
    # S'assurer que le fichier (1) existe sinon, le créer (2)
    alert_file = Path("mission_data/alertes.txt") #recupere le path du fichier 
    if not alert_file.exists():
       alert_file.touch(); print("\n ✅ Fichier alertes.txt créé.")  # (1) et (2)
       
       # Enregistrement des messages d'alerte
       with open("mission_data/alertes.txt", "w", encoding="utf-8") as alert_file_content:
           for alert_line in alert_lines:
            alert_file_content.write(alert_line + "\n")
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    
#Task 2 : Exploration du dossier mission

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# 1 : Verification de l'existence du dosssier mission_data/
if not os.path.exists("mission_data/"):
    print("❌ Le dossier mission_data/ n'existe pas !")
else:  # pas demandé maia rajouté
    print("✅ Le dossier mission_data/ existe dans l'arborescence !\n")

# 2 : Liste des fichiers de ce dossier

print("* * * Tous les fichiers * * *\n")
mission_data_files = os.listdir("mission_data/") 


for mission_data_file in mission_data_files:
 """mission_data_files est une liste des fichiers du repertoire mission_data/ cependant plus bas on doit avec
 os.path.gesize() passer le relative path de chaque fichier car le path seul du fichier enfant génère une erreur
 car introuvable
 """
 mission_data_file = os.path.join("mission_data/", mission_data_file) # Recupere le relative path du fichier enfant
 size_mission_data_file = os.path.getsize(mission_data_file) # Recupere la taille du fichier
 print(f"- {mission_data_file} ({size_mission_data_file} ko)")
 
# 3 : En cas d'inexistance du dossier mission_data/rapports/ il doit être crée

if not os.path.exists("mission_data/rapports/"):
    os.makedirs("mission_data/rapports")
    
# 4 : De même en cas d'inexistance du dossier mission_data/archives/ il doit être crée

if not os.path.exists("mission_data/archives/"):
    os.makedirs("mission_data/archives")
   
#  : Affichage de l'arborescence du dossier mission_data 

print("\n Structure du dossier: \n📁 mission_data/")
for mission_data_file in mission_data_files:
 mission_data_file = os.path.join("mission_data/", mission_data_file) # Recupere le relative path du fichier enfant
 print(f"| | {mission_data_file} ({os.path.getsize(mission_data_file)} ko)") 

 