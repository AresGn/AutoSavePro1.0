# AutoSavePro (Version Simplifiée)

## Description
AutoSavePro est une application de bureau simple mais puissante conçue pour automatiser la sauvegarde de vos travaux dans des applications spécifiques. En simulant la combinaison de touches Ctrl+S à intervalles réguliers, AutoSavePro aide à prévenir la perte de données due aux oublis de sauvegarde ou aux plantages inattendus.

## Fonctionnalités
- Sélection d'une application spécifique à surveiller
- Configuration de l'intervalle de sauvegarde automatique
- Simulation de la combinaison de touches Ctrl+S pour sauvegarder
- Interface utilisateur graphique intuitive
- Journalisation des activités de sauvegarde

## Prérequis
- Python 3.7+
- Bibliothèques listées dans `requirements.txt`

## Installation
1. Clonez ce dépôt ou téléchargez les fichiers source.
2. Naviguez vers le dossier du projet dans votre terminal.
3. Installez les dépendances requises :
   ```
   pip install -r requirements.txt
   ```

## Utilisation
1. Exécutez `main.py` pour lancer l'application :
   ```
   python main.py
   ```
2. Dans l'interface :
   - Entrez l'intervalle de sauvegarde souhaité en minutes.
   - Cliquez sur "Démarrer" pour commencer la surveillance.
3. L'application simulera Ctrl+S à l'intervalle spécifié dans l'applicatio active sur votre espace de travail par exemple Bloc Notes.
4. Les logs d'activité s'afficheront dans la zone de texte de l'interface.

## Structure du Projet
```
AutoSavePro/
├── autosave/
│   ├── __init__.py
│   ├── saver.py
│   └── gui.py
├── main.py
└── requirements.txt
```
