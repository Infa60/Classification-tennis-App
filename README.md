# <span style="color:#A02400">ShotPredictionApp</span>

Application des prédictions des coups au Tennis avec une centrale inertielle.<br>

Par <span style="color:#069B23">Anthony PLACÉ</span>, <span style="color:#069B23"> Mathieu BOURGEOIS</span> et <span style="color:#069B23">Victor VATTIER</span>.

<img src="https://zupimages.net/up/23/13/mgzr.png" alt="Alt text" title="Optional title">

## Table des matières :

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribution](#contribution)


# Installation : 

<strong>Voici les étapes d'installation du projet</strong><br>

<span style="color:#99A7FF">1. Cloner le projet à partir du déport github :</span>
```bash
$ git clone https://github.com/VictorVatt/ShotPredictionApp.git
```
<span style="color:#99A7FF">2. Accédez au répertoire du projet :</span>
```bash
$ cd ShotPredictionApp/
```
<span style="color:#99A7FF">3. Créez un environnement virtuel pour le projet :</span>
```bash
$ python3 -m venv venv
```
<span style="color:#99A7FF">4. Activez l'environnement virtuel :</span>
```bash
$ source venv/bin/activate
```
<span style="color:#99A7FF">5. Installez les dépendances nécessaires à l'aide de pip :</span>
```bash
$ pip install -r requirements.txt
```
<span style="color:#99A7FF">6. Exécutez le projet :</span>
```bash
$ python main.py
```

# Utilisation : 

Cette application a été créée pour fonctionner avec les IMU XsensDot et uniquement ceux-ci.
Pour que l'application fonctionne, il faut placer correctement l'IMU au centre du manche de la raquette en respectant l'exemple suivant : 
1. Attendre que le Model soit "OK"
2. Connecter l'IMU XsensDot en appuyant sur "Connexion IMU"
3. Lancer un enregistrement
4. Couper l'enregistrement
5. Voir les résultats

# Contribution : 

Cette application à été réalisé dans le cadre du Master Science du Numérique et Sport DIGISPORT. Les 3 élèves qui ont travaillés sur ce projet sont
Anthony Placé, Mathieu Bourgeois et Victor Vattier.

