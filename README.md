# Convertisseur MP3 vers MIDI

Une application web qui permet de convertir des fichiers audio MP3 en fichiers MIDI. L'application utilise Python avec Flask pour le backend et essentia-tensorflow pour l'analyse audio.

## Fonctionnalités

- Interface utilisateur simple et intuitive
- Support du glisser-déposer de fichiers
- Conversion en temps réel
- Génération de fichiers MIDI standards
- Barre de progression pour suivre la conversion

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt :
```bash
git clone [URL_DU_REPO]
cd [NOM_DU_DOSSIER]
```

2. Créez un environnement virtuel (recommandé) :
```bash
python -m venv venv
source venv/bin/activate  # Sur macOS/Linux
# ou
.\venv\Scripts\activate  # Sur Windows
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Lancez l'application :
```bash
python app.py
```

2. Ouvrez votre navigateur et accédez à :
```
http://localhost:5000
```

3. Pour convertir un fichier MP3 :
   - Glissez-déposez votre fichier MP3 dans la zone prévue
   - Ou cliquez sur la zone pour sélectionner un fichier
   - Cliquez sur "Convertir en MIDI"
   - Le fichier MIDI sera automatiquement téléchargé

## Structure du projet

```
.
├── app.py              # Application Flask principale
├── requirements.txt    # Dépendances Python
├── templates/          # Templates HTML
│   └── index.html     # Interface utilisateur
└── README.md          # Documentation
```

## Dépendances principales

- Flask : Framework web
- essentia-tensorflow : Analyse audio
- numpy : Calculs numériques
- librosa : Traitement audio
- python-midi : Génération de fichiers MIDI

## Limitations

- La conversion est optimisée pour les fichiers musicaux avec des notes clairement définies
- Les fichiers très complexes peuvent donner des résultats moins précis
- La taille maximale des fichiers est limitée par la configuration de Flask

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Forker le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Support

Si vous rencontrez des problèmes ou avez des questions, n'hésitez pas à ouvrir une issue sur le dépôt GitHub. 