# 🚀 Exercices Python — Navigation Spatiale

> **Thème** : Navigation spatiale, missions interplanétaires et télémétrie
> **Prérequis** : Python 3.x installé
> **Progression** : 🟢 Basique → 🟡 Intermédiaire → 🔴 Avancé
> **Notions ciblées** : Fichiers, modules, `os`, `json`, gestion des exceptions

---

## 📦 Datasets à créer avant de commencer

Avant de démarrer les exercices, créez les fichiers suivants dans un dossier `mission_data/`.

---

### Fichier `mission_data/missions.json`

```json
{
  "missions": [
    {
      "id": "MSN-001",
      "nom": "Artemis IV",
      "destination": "Lune",
      "date_lancement": "2026-09-15",
      "statut": "planifiée",
      "equipage": ["Cmdt. Elena Vasquez", "Dr. Kenji Tanaka", "Ing. Fatou Diallo"],
      "duree_jours": 21,
      "budget_millions_usd": 4200
    },
    {
      "id": "MSN-002",
      "nom": "Ares Genesis",
      "destination": "Mars",
      "date_lancement": "2028-07-20",
      "statut": "en_preparation",
      "equipage": ["Cmdt. Yuri Petrov", "Dr. Amara Osei", "Ing. Lucas Fernandez", "Dr. Mei Chen"],
      "duree_jours": 680,
      "budget_millions_usd": 18500
    },
    {
      "id": "MSN-003",
      "nom": "Europa Probe",
      "destination": "Europe (Jupiter)",
      "date_lancement": "2029-03-10",
      "statut": "conception",
      "equipage": [],
      "duree_jours": 2190,
      "budget_millions_usd": 5600
    },
    {
      "id": "MSN-004",
      "nom": "Titan Explorer",
      "destination": "Titan (Saturne)",
      "date_lancement": "2031-11-05",
      "statut": "conception",
      "equipage": [],
      "duree_jours": 2920,
      "budget_millions_usd": 7800
    },
    {
      "id": "MSN-005",
      "nom": "Helios Station",
      "destination": "Orbite solaire",
      "date_lancement": "2027-01-22",
      "statut": "planifiée",
      "equipage": ["Cmdt. Sofia Lindqvist", "Dr. Rashid Al-Farsi"],
      "duree_jours": 365,
      "budget_millions_usd": 3100
    }
  ]
}
```

---

### Fichier `mission_data/telemetrie.json`

```json
{
  "vaisseau": "Ares Genesis",
  "mission_id": "MSN-002",
  "releves": [
    {
      "timestamp": "2028-07-20T08:00:00Z",
      "phase": "lancement",
      "altitude_km": 0,
      "vitesse_km_s": 0,
      "carburant_pct": 100.0,
      "temperature_cabine_c": 22.1,
      "cap_degres": 90.0,
      "systemes": {"propulsion": "nominal", "support_vie": "nominal", "navigation": "nominal", "communication": "nominal"}
    },
    {
      "timestamp": "2028-07-20T08:05:00Z",
      "phase": "ascension",
      "altitude_km": 85,
      "vitesse_km_s": 2.3,
      "carburant_pct": 94.7,
      "temperature_cabine_c": 23.8,
      "cap_degres": 88.5,
      "systemes": {"propulsion": "nominal", "support_vie": "nominal", "navigation": "nominal", "communication": "nominal"}
    },
    {
      "timestamp": "2028-07-20T08:12:00Z",
      "phase": "orbite_terrestre",
      "altitude_km": 400,
      "vitesse_km_s": 7.66,
      "carburant_pct": 82.3,
      "temperature_cabine_c": 22.5,
      "cap_degres": 45.0,
      "systemes": {"propulsion": "nominal", "support_vie": "nominal", "navigation": "nominal", "communication": "nominal"}
    },
    {
      "timestamp": "2028-07-20T10:30:00Z",
      "phase": "injection_trans_mars",
      "altitude_km": 420,
      "vitesse_km_s": 11.2,
      "carburant_pct": 68.1,
      "temperature_cabine_c": 24.0,
      "cap_degres": 32.7,
      "systemes": {"propulsion": "nominal", "support_vie": "nominal", "navigation": "alerte_mineure", "communication": "nominal"}
    },
    {
      "timestamp": "2028-07-21T00:00:00Z",
      "phase": "croisiere",
      "altitude_km": 52000,
      "vitesse_km_s": 11.1,
      "carburant_pct": 67.8,
      "temperature_cabine_c": 21.9,
      "cap_degres": 31.2,
      "systemes": {"propulsion": "nominal", "support_vie": "nominal", "navigation": "nominal", "communication": "nominal"}
    },
    {
      "timestamp": "2028-08-15T12:00:00Z",
      "phase": "croisiere",
      "altitude_km": 28500000,
      "vitesse_km_s": 10.8,
      "carburant_pct": 65.2,
      "temperature_cabine_c": 22.3,
      "cap_degres": 30.9,
      "systemes": {"propulsion": "nominal", "support_vie": "alerte_mineure", "navigation": "nominal", "communication": "degradee"}
    },
    {
      "timestamp": "2028-12-01T06:00:00Z",
      "phase": "croisiere",
      "altitude_km": 112000000,
      "vitesse_km_s": 10.5,
      "carburant_pct": 61.4,
      "temperature_cabine_c": 19.8,
      "cap_degres": 29.5,
      "systemes": {"propulsion": "nominal", "support_vie": "nominal", "navigation": "nominal", "communication": "nominal"}
    },
    {
      "timestamp": "2029-04-10T18:00:00Z",
      "phase": "approche_mars",
      "altitude_km": 224000000,
      "vitesse_km_s": 5.2,
      "carburant_pct": 42.7,
      "temperature_cabine_c": 21.0,
      "cap_degres": 15.3,
      "systemes": {"propulsion": "alerte_mineure", "support_vie": "nominal", "navigation": "nominal", "communication": "nominal"}
    }
  ]
}
```

---

### Fichier `mission_data/corps_celestes.json`

```json
{
  "corps_celestes": [
    {"nom": "Terre", "type": "planete", "distance_soleil_mkm": 149.6, "rayon_km": 6371, "gravite_m_s2": 9.81, "atmosphere": true, "satellites_principaux": ["Lune"]},
    {"nom": "Lune", "type": "satellite", "distance_soleil_mkm": 149.6, "rayon_km": 1737, "gravite_m_s2": 1.62, "atmosphere": false, "satellites_principaux": []},
    {"nom": "Mars", "type": "planete", "distance_soleil_mkm": 227.9, "rayon_km": 3389, "gravite_m_s2": 3.72, "atmosphere": true, "satellites_principaux": ["Phobos", "Deimos"]},
    {"nom": "Jupiter", "type": "planete", "distance_soleil_mkm": 778.5, "rayon_km": 69911, "gravite_m_s2": 24.79, "atmosphere": true, "satellites_principaux": ["Io", "Europe", "Ganymède", "Callisto"]},
    {"nom": "Europe", "type": "satellite", "distance_soleil_mkm": 778.5, "rayon_km": 1560, "gravite_m_s2": 1.31, "atmosphere": false, "satellites_principaux": []},
    {"nom": "Saturne", "type": "planete", "distance_soleil_mkm": 1434.0, "rayon_km": 58232, "gravite_m_s2": 10.44, "atmosphere": true, "satellites_principaux": ["Titan", "Encelade", "Mimas"]},
    {"nom": "Titan", "type": "satellite", "distance_soleil_mkm": 1434.0, "rayon_km": 2574, "gravite_m_s2": 1.35, "atmosphere": true, "satellites_principaux": []}
  ]
}
```

---

### Fichier `mission_data/journal_bord.txt`

```
[2028-07-20 08:00] LANCEMENT — Décollage nominal. Tous systèmes go.
[2028-07-20 08:05] ASCENSION — Passage Mach 3. Vibrations dans les tolérances.
[2028-07-20 08:12] ORBITE — Insertion orbitale confirmée. Altitude 400 km.
[2028-07-20 10:30] TMS — Injection trans-Mars réussie. Alerte mineure navigation corrigée.
[2028-07-21 00:00] CROISIERE — Mode croisière activé. Équipage au repos.
[2028-08-15 12:00] CROISIERE — Alerte support vie : filtre CO2 secondaire à remplacer. Communication dégradée.
[2028-12-01 06:00] CROISIERE — Mi-parcours. Correction de trajectoire effectuée. Delta-V : 0.3 km/s.
[2029-04-10 18:00] APPROCHE — Mars en visuel. Alerte propulsion mineure : valve pressuriseur.
```

---

## 🟢 Tâche 1 — Lecture de fichiers texte : Le journal de bord

**Notions** : `open()`, `read()`, `readlines()`, `with`, encodage

Écrivez un script qui :

1. Ouvre le fichier `mission_data/journal_bord.txt` en lecture.
2. Affiche le **nombre total de lignes** (entrées du journal).
3. Affiche **uniquement les lignes contenant le mot `"Alerte"` ou `"alerte"`** (insensible à la casse).
4. Écrit ces lignes d'alerte dans un nouveau fichier `mission_data/alertes.txt`.

**Résultat attendu** :
```
Journal de bord : 8 entrées
--- Alertes détectées (2) ---
[2028-08-15 12:00] CROISIERE — Alerte support vie : filtre CO2 secondaire à remplacer. Communication dégradée.
[2029-04-10 18:00] APPROCHE — Mars en visuel. Alerte propulsion mineure : valve pressuriseur.
✅ Fichier alertes.txt créé.
```

---

## 🟢 Tâche 2 — Le module `os` : Exploration du dossier mission

**Notions** : `os.listdir()`, `os.path.exists()`, `os.path.getsize()`, `os.makedirs()`

Écrivez un script qui :

1. Vérifie que le dossier `mission_data/` existe. Si non, affichez une erreur.
2. Liste **tous les fichiers** du dossier avec leur taille en Ko.
3. Crée un sous-dossier `mission_data/rapports/` s'il n'existe pas déjà.
4. Crée un sous-dossier `mission_data/archives/` s'il n'existe pas déjà.
5. Affiche l'arborescence résultante.

**Résultat attendu** :
```
📂 mission_data/
   📄 missions.json          (1.2 Ko)
   📄 telemetrie.json         (2.8 Ko)
   📄 corps_celestes.json     (1.1 Ko)
   📄 journal_bord.txt        (0.7 Ko)
   📁 rapports/               [créé]
   📁 archives/               [créé]
```

---

## 🟢 Tâche 3 — JSON basique : Charger et afficher les missions

**Notions** : `json.load()`, accès aux clés, boucle sur une liste de dicts

Écrivez un script qui :

1. Charge le fichier `missions.json`.
2. Affiche un résumé de chaque mission sous cette forme :
```
[MSN-001] Artemis IV → Lune | 21 jours | Équipage : 3 | Budget : 4 200 M$
[MSN-002] Ares Genesis → Mars | 680 jours | Équipage : 4 | Budget : 18 500 M$
...
```
3. Calcule et affiche le **budget total** de toutes les missions.
4. Identifie la mission la **plus longue** et la **plus courte**.

---

## 🟡 Tâche 4 — Gestion des exceptions : Chargement robuste

**Notions** : `try/except`, `FileNotFoundError`, `json.JSONDecodeError`, `KeyError`, `except` multiple

Écrivez une fonction `charger_json_securise(chemin)` qui :

1. Tente d'ouvrir et charger un fichier JSON.
2. Gère les cas d'erreur suivants avec des messages explicites :
   - Le fichier n'existe pas → `FileNotFoundError`
   - Le fichier est mal formé → `json.JSONDecodeError`
   - Le fichier est vide → cas particulier
3. Retourne `None` en cas d'erreur, les données sinon.

Testez votre fonction avec :
```python
# Cas 1 : fichier normal
data = charger_json_securise("mission_data/missions.json")

# Cas 2 : fichier inexistant
data = charger_json_securise("mission_data/fantome.json")

# Cas 3 : créez un fichier corrompu pour tester
with open("mission_data/corrompu.json", "w") as f:
    f.write("{nom: valeur_sans_guillemets}")
data = charger_json_securise("mission_data/corrompu.json")
```

**Résultat attendu** :
```
✅ missions.json chargé avec succès (5 missions)
❌ Fichier introuvable : mission_data/fantome.json
❌ JSON invalide dans mission_data/corrompu.json : Expecting property name enclosed in double quotes (ligne 1, col 2)
```

---

## 🟡 Tâche 5 — `os` avancé : Commandes système et gestion de fichiers

**Notions** : `os.system()`, `os.rename()`, `os.remove()`, `os.path.join()`, `shutil.copy()`

Écrivez un script qui simule un système d'archivage :

1. Utilisez `os.path.join()` pour construire tous les chemins (portabilité).
2. Copiez `journal_bord.txt` dans `mission_data/archives/` en le renommant avec la date du jour : `journal_bord_2026-02-18.txt` (utilisez le module `datetime`).
3. Créez un fichier `mission_data/rapports/rapport_systeme.txt` contenant :
   - Le résultat de `os.getcwd()`
   - La liste des variables d'environnement liées à Python (`os.environ`) — filtrez celles contenant `"PYTHON"` ou `"PATH"`.
   - L'espace disque si disponible (bonus avec `shutil.disk_usage()`).
4. Affichez un résumé des opérations effectuées.

---

## 🟡 Tâche 6 — JSON en écriture : Ajouter une mission

**Notions** : `json.dump()`, `json.dumps()`, modification de structures, `indent`

Écrivez une fonction `ajouter_mission(chemin_json, nouvelle_mission)` qui :

1. Charge les missions existantes.
2. Vérifie que l'`id` de la nouvelle mission n'existe pas déjà (sinon lève une `ValueError`).
3. Ajoute la mission à la liste.
4. Sauvegarde le fichier JSON avec une indentation propre (`indent=2`).
5. Affiche un message de confirmation.

Testez avec :
```python
nouvelle = {
    "id": "MSN-006",
    "nom": "Proxima Relay",
    "destination": "Alpha Centauri (sonde)",
    "date_lancement": "2035-06-01",
    "statut": "théorique",
    "equipage": [],
    "duree_jours": 29200,
    "budget_millions_usd": 125000
}
ajouter_mission("mission_data/missions.json", nouvelle)
```

Ajoutez aussi une fonction `supprimer_mission(chemin_json, mission_id)` avec confirmation.

---

## 🟡 Tâche 7 — Analyse de télémétrie : Parsing JSON complexe

**Notions** : JSON imbriqué, boucles, conditions, calculs, `datetime`

Chargez `telemetrie.json` et écrivez un script qui :

1. Affiche un tableau résumé de chaque relevé :
```
Phase               | Altitude        | Vitesse   | Carburant | Alertes
--------------------|-----------------|-----------|-----------|--------
lancement           | 0 km            | 0.0 km/s  | 100.0%    | -
ascension           | 85 km           | 2.3 km/s  | 94.7%     | -
orbite_terrestre    | 400 km          | 7.66 km/s | 82.3%     | -
injection_trans_mars| 420 km          | 11.2 km/s | 68.1%     | navigation
croisiere           | 52 000 km       | 11.1 km/s | 67.8%     | -
croisiere           | 28 500 000 km   | 10.8 km/s | 65.2%     | support_vie, comm
croisiere           | 112 000 000 km  | 10.5 km/s | 61.4%     | -
approche_mars       | 224 000 000 km  | 5.2 km/s  | 42.7%     | propulsion
```

2. Calcule la **consommation moyenne de carburant par jour** entre le premier et le dernier relevé.
3. Identifie **tous les relevés contenant au moins une alerte** (systèmes ≠ `"nominal"`).
4. Sauvegardez la liste des alertes dans `mission_data/rapports/alertes_systemes.json`.

---

## 🔴 Tâche 8 — Module personnalisé : `navigation.py`

**Notions** : Créer un module, `import`, `__name__`, fonctions utilitaires

Créez un fichier `navigation.py` qui contient les fonctions suivantes :

```python
# --- navigation.py ---

import json
import math

def distance_interplanetaire(corps1, corps2, donnees_corps):
    """
    Calcule la distance approximative entre deux corps célestes
    basée sur leur distance au Soleil (en millions de km).
    Retourne la valeur absolue de la différence.
    """
    pass

def temps_trajet(distance_mkm, vitesse_km_s):
    """
    Calcule le temps de trajet en jours.
    distance en millions de km, vitesse en km/s.
    """
    pass

def delta_v(gravite_depart, gravite_arrivee, altitude_orbite_km):
    """
    Estimation simplifiée du delta-v nécessaire (en km/s).
    Formule simplifiée : sqrt(2 * g_depart * alt) + sqrt(2 * g_arrivee * alt)
    (les altitudes sont converties en mètres)
    """
    pass

def poids_sur_corps(masse_kg, gravite_m_s2):
    """Calcule le poids (en Newtons) sur un corps céleste."""
    pass

def charger_corps_celestes(chemin="mission_data/corps_celestes.json"):
    """Charge le fichier des corps célestes avec gestion d'erreur."""
    pass
```

Implémentez chaque fonction, puis dans le bloc `if __name__ == "__main__":`, ajoutez des tests :

```python
if __name__ == "__main__":
    corps = charger_corps_celestes()
    
    d = distance_interplanetaire("Terre", "Mars", corps)
    print(f"Distance Terre-Mars : {d} millions km")
    
    t = temps_trajet(d, 11.0)
    print(f"Temps de trajet à 11 km/s : {t:.0f} jours")
    
    print(f"Poids d'un astronaute (80 kg) sur Mars : {poids_sur_corps(80, 3.72):.1f} N")
```

---

## 🔴 Tâche 9 — Exceptions personnalisées et validation de données

**Notions** : Héritage d'exceptions, `raise`, classes d'exception, validation complète

Créez un système de validation pour les données de mission :

```python
# --- exceptions.py ---

class NavigationError(Exception):
    """Classe de base pour les erreurs de navigation spatiale."""
    pass

class MissionDataError(NavigationError):
    """Données de mission invalides ou incomplètes."""
    pass

class TrajectoireError(NavigationError):
    """Paramètres de trajectoire invalides."""
    pass

class CarburantError(NavigationError):
    """Niveau de carburant critique ou invalide."""
    pass
```

Puis écrivez une fonction `valider_mission(mission_dict)` qui vérifie :

1. Tous les champs obligatoires sont présents → sinon `MissionDataError`.
2. La `duree_jours` est positive → sinon `MissionDataError`.
3. Le `budget_millions_usd` est positif → sinon `MissionDataError`.
4. La `date_lancement` est au format valide → sinon `MissionDataError`.
5. Si `destination` est un corps connu, vérifier que la durée est cohérente avec la distance (marge ×10) → sinon `TrajectoireError`.

Écrivez aussi `verifier_carburant(releve)` qui :
- Lève `CarburantError` si `carburant_pct < 10`.
- Affiche un warning si `carburant_pct < 30`.

Testez avec des données valides ET invalides :

```python
from exceptions import *

# Cas valide
try:
    valider_mission({"id": "MSN-001", "nom": "Test", "destination": "Mars",
                     "date_lancement": "2028-01-01", "statut": "planifiée",
                     "equipage": [], "duree_jours": 680, "budget_millions_usd": 5000})
    print("✅ Mission valide")
except NavigationError as e:
    print(f"❌ {type(e).__name__}: {e}")

# Cas invalide : durée négative
try:
    valider_mission({"id": "MSN-999", "nom": "Bad", "destination": "Lune",
                     "date_lancement": "2028-01-01", "statut": "test",
                     "equipage": [], "duree_jours": -5, "budget_millions_usd": 100})
except NavigationError as e:
    print(f"❌ {type(e).__name__}: {e}")

# Cas carburant critique
try:
    verifier_carburant({"carburant_pct": 7.5, "phase": "approche_mars"})
except CarburantError as e:
    print(f"🔴 {e}")
```

---

## 🔴 Tâche 10 — Projet intégrateur : Centre de Contrôle de Mission

**Notions** : Tout ce qui précède + architecture de projet, menu interactif, `os`, `json`, modules, exceptions

Créez un programme `centre_controle.py` qui fonctionne comme un **tableau de bord interactif** en ligne de commande :

```
╔══════════════════════════════════════════════════╗
║       🚀 CENTRE DE CONTRÔLE DE MISSION 🚀       ║
╠══════════════════════════════════════════════════╣
║  1. Afficher toutes les missions                 ║
║  2. Détails d'une mission (par ID)               ║
║  3. Ajouter une nouvelle mission                 ║
║  4. Télémétrie en temps réel (derniers relevés)  ║
║  5. Calculateur de navigation                    ║
║  6. Diagnostic système (alertes)                 ║
║  7. Recherche dans le journal de bord            ║
║  8. Générer un rapport complet (JSON)            ║
║  9. Arborescence des fichiers mission            ║
║  0. Quitter                                      ║
╚══════════════════════════════════════════════════╝
```

Le programme doit :

1. **Option 1** : Charger et afficher `missions.json` (réutiliser Tâche 3).
2. **Option 2** : Demander un ID et afficher tous les détails, incluant le poids d'un astronaute de 80 kg sur la destination (utiliser `navigation.py` et `corps_celestes.json`).
3. **Option 3** : Saisie interactive + validation (réutiliser Tâches 6 et 9).
4. **Option 4** : Afficher le dernier relevé de `telemetrie.json` avec indicateurs colorés :
   - 🟢 Carburant > 50%, 🟡 entre 20-50%, 🔴 < 20%.
5. **Option 5** : Calculateur utilisant `navigation.py` — l'utilisateur choisit départ et arrivée, le programme affiche distance, temps de trajet estimé et delta-v.
6. **Option 6** : Scanner toute la télémétrie et lister les anomalies (réutiliser Tâche 7).
7. **Option 7** : Recherche par mot-clé dans `journal_bord.txt` (réutiliser Tâche 1).
8. **Option 8** : Générer `mission_data/rapports/rapport_complet.json` contenant un résumé de toutes les missions, les alertes, et les statistiques.
9. **Option 9** : Afficher l'arborescence complète de `mission_data/` avec `os` (réutiliser Tâche 2).

**Contraintes techniques** :
- Toute entrée utilisateur doit être protégée par `try/except`.
- Utilisez vos exceptions personnalisées de la Tâche 9.
- Importez `navigation.py` comme module.
- Le programme boucle jusqu'à ce que l'utilisateur choisisse `0`.
- Chaque action doit logger un message horodaté dans `mission_data/rapports/log_controle.txt`.

**Structure de fichiers finale attendue** :
```
projet/
├── centre_controle.py          ← script principal
├── navigation.py               ← module de calculs
├── exceptions.py               ← exceptions personnalisées
└── mission_data/
    ├── missions.json
    ├── telemetrie.json
    ├── corps_celestes.json
    ├── journal_bord.txt
    ├── rapports/
    │   ├── alertes_systemes.json
    │   ├── rapport_complet.json
    │   ├── rapport_systeme.txt
    │   └── log_controle.txt
    └── archives/
        └── journal_bord_2026-02-18.txt
```

---

## 📚 Récapitulatif des notions couvertes

| Tâche | Niveau | Notions Python |
|-------|--------|----------------|
| 1 | 🟢 Basique | `open()`, `read()`, `readlines()`, `with`, écriture fichier |
| 2 | 🟢 Basique | `os.listdir()`, `os.path.exists()`, `os.makedirs()`, `os.path.getsize()` |
| 3 | 🟢 Basique | `json.load()`, accès dict/list, boucles, agrégation |
| 4 | 🟡 Intermédiaire | `try/except`, `FileNotFoundError`, `JSONDecodeError`, multi-except |
| 5 | 🟡 Intermédiaire | `os.system()`, `os.rename()`, `shutil`, `datetime`, `os.environ` |
| 6 | 🟡 Intermédiaire | `json.dump()`, `json.dumps()`, modification de données, `indent` |
| 7 | 🟡 Intermédiaire | JSON imbriqué, parsing complexe, `datetime`, rapports |
| 8 | 🔴 Avancé | Modules, `import`, `__name__`, `math`, fonctions utilitaires |
| 9 | 🔴 Avancé | Exceptions personnalisées, héritage, `raise`, validation |
| 10 | 🔴 Avancé | Architecture projet, menu interactif, intégration complète |

---

> *« Houston, we have no problem. »* 🛰️
> Bon voyage dans le code et dans les étoiles !
