import re
from pathlib import Path

#Task 1: Lecture de fichiers texte : Le journal de bord

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
    alert_file = Path("mission_data/alertes.txt")
    if not alert_file.exists(): # (1)
       alert_file.touch() #(2)
       print("\n ✅ Fichier alertes.txt créé.")
       # Enregistrement des messages d'alerte
    
       with open("mission_data/alertes.txt", "w", encoding="utf-8") as alert_file_content:
           for alert_line in alert_lines:
            alert_file_content.write(alert_line + "\n")
    