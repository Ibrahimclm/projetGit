# Générateur de CV Professionnel - Ibrahim Sy

Ce projet génère un CV professionnel en format PDF pour un consultant en cybersécurité.

## Caractéristiques

- **Design sobre et moderne** : Adapté aux cabinets de conseil en cybersécurité
- **Palette de couleurs professionnelle** : Dominante bleu foncé, gris et noir
- **Structure claire** : Hiérarchie visuelle bien définie
- **Format optimisé** : 1-2 pages maximum
- **Police professionnelle** : Helvetica/Arial pour une lecture optimale
- **Prêt à l'emploi** : Format PDF directement envoyable aux recruteurs

## Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/Ibrahimclm/projetGit.git
cd projetGit
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

Générer le CV en PDF :
```bash
python generate_cv.py
```

Le fichier `CV_Ibrahim_Sy.pdf` sera créé dans le répertoire courant.

## Structure du CV

Le CV comprend les sections suivantes :
- **En-tête** : Informations de contact
- **Profil** : Présentation professionnelle
- **Expérience professionnelle** : Parcours détaillé
- **Compétences** : Gouvernance, GRC, Protection des données, Technique
- **Projets académiques** : Projets significatifs
- **Formation** : Diplômes et formations
- **Certifications** : ISO 27001, ANSSI, CNIL, EBIOS RM
- **Langues** : Français, Anglais, Arabe
- **Informations complémentaires** : RQTH

## Personnalisation

Pour personnaliser le CV, modifiez les fonctions suivantes dans `generate_cv.py` :
- `get_cv_html()` : Pour modifier le contenu
- `get_cv_css()` : Pour ajuster le style et les couleurs

## Technologies utilisées

- **Python 3** : Langage de programmation
- **WeasyPrint** : Conversion HTML/CSS vers PDF
- **HTML5/CSS3** : Structure et mise en forme

## License

Ce projet est destiné à un usage personnel.
