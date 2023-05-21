# Générateur de Lettre de Motivation avec Interface Streamlit

Ce projet est un générateur de lettre de motivation utilisant des techniques de Traitement du Langage Naturel (NLP) en Python. Il utilise un modèle de langage finement ajusté basé sur T5-small, qui a été entraîné sur des exemples de lettres de motivation collectées à partir du site JobHero.

## Description du Modèle

- Nom du Modèle : COVLETGen
- Description du Modèle : Ce modèle est une version fine-tunée de T5-small sur un corpus de lettres de motivation provenant de JobHero.
- Taille du Modèle : T5-small avec 60 millions de paramètres.
- Développé par : Andriamahefa Toky Cedric
- Type de Modèle : Modèle de Langage
- Langue : Anglais

## Paramètres d'Entrée du Modèle

Le modèle prend les paramètres suivants pour générer une lettre de motivation :
- Nom : Le nom du destinataire de la lettre.
- Compétences : Les compétences que vous souhaitez mettre en valeur dans la lettre.
- Expérience : Votre expérience professionnelle pertinente.
- Poste : Le poste pour lequel vous postulez.

## Utilisation

- Utilisation Directe : Le principal cas d'utilisation est de générer un modèle de lettre de motivation.
- Limitations : Le corpus utilisé peut ne pas couvrir toutes les variations possibles de lettres de motivation et de postes.

## Données d'Entraînement

- Pour générer les lettres de motivation, nous avons collecté des échantillons à partir du site https://www.jobhero.com/cover-letter/.
- Nous avons extrait des informations telles que le nom, le poste, les compétences et l'expérience pour entraîner notre modèle pré-entraîné.

## Procédure d'Entraînement

- Nous avons entraîné notre modèle sur Google Colab en utilisant un GPU Tesla T4 avec 16 Go de VRAM.
- Nous avons utilisé un ensemble d'entraînement de 1279 exemples, un ensemble de validation de 160 exemples et un ensemble de test de 160 exemples.
- Nous avons utilisé Adam comme optimiseur avec un taux d'apprentissage de 3e-4 pendant 15 époques.

## Frameworks et Bibliothèques

- transformers
- torch
- torchvision
- datasets
- wandb
- pytorch-lightning

