

https://github.com/MathieuLaureti/MINI_PROJET-IA


Noms : Nicolas Tessier, Mathieu Laureti


## Composantes du Rapport de Projet

### 1. Définition de la Tâche




#### **Description de la tâche**: Expliquez ce que fait votre système (entrée et sortie).

Le but de ce projet est d’entraîner le modèle OCR Tesseract sur des polices d’écriture peu conventionnelles, comme des cursives ou des manuscrites, afin d’explorer les limites du modèle. L’objectif est de développer un système capable de générer automatiquement un modèle personnalisé pour une police précise, en l’agrémentant de la version anglaise officielle de Tesseract. Cinq polices de différentes complexitées seront utilisées pour tester ce système.
#### **Délimitation**: Assurez-vous que la tâche n'est ni trop large ni trop étroite.

#### **Pertinence IA**: Justifiez l'utilisation de l'intelligence artificielle pour cette tâche.

 Dans les années précédentes, un programme algorithmique était utilisé pour reconnaître les écritures et les différentes polices de caractère. Cependant, ces programmes manquaient de fiabilité. il était parfois nécessaire d'écrire un nouveau programme et un nouvel algorithme pour des police de caractère plus récente. ces outils informatiques manquait d'adaptabilité. L'utilisation de l'intelligence artificielle basée sur un modèle s'avère une solution efficace, puisqu'elle permet une fonctionnalité d'apprentissage qui lui permet d'intégrer des nouvelles polices de caractère. Ainsi les modèles peuvent être ajusté lorsque de nouvelles police de caractère font leur apparition.


### 2. Brève Revue de la Littérature

- **OCRopus** : Un projet modulaire également basé sur LSTM. Bien qu’il soit moins maintenu aujourd’hui, il a inspiré les versions récentes de Tesseract. Il est utile pour ceux qui veulent concevoir des pipelines OCR personnalisés, mais demande plus de configuration.
    
- **Kraken** : Basé sur OCRopus, Kraken est orienté vers la reconnaissance de documents historiques ou manuscrits. Il prend en charge des scripts complexes et offre une interface d'entraînement conviviale. C’est un bon choix pour les projets nécessitant la reconnaissance de textes anciens ou dans des alphabets non latins.
    
- **EasyOCR** : Basé sur PyTorch, ce moteur se distingue par sa simplicité d’utilisation et sa prise en charge de plus de 80 langues. Il est moins flexible que Tesseract pour l'entraînement personnalisé, mais il offre de bons résultats rapidement sur des textes imprimés standards.
    
- **Calamari OCR** : Un moteur OCR moderne utilisant TensorFlow et compatible avec les fichiers d'OCRopus. Il permet l'entraînement multi-polices et multi-langues et propose des outils puissants de fusion de modèles (voting). Il est particulièrement adapté aux scénarios où plusieurs modèles OCR doivent être combinés.

Dans la littérature, nous pouvons citer deux. Implémentations du OCR :

+ La première consistait à simplifier la documentation des transactions dans le commerce électronique . Le OCR servait à numériser les transactions sous format papier. Ainsi, il était plus facile de parcourir l'historique des transactions. Le modèle atteignait un score F1 de 0,7703 lors de ses tests  
+ Le deuxième utilisait le OCR afin de lire des caractères sur des interfaces graphiques comme des boutons, des textes et des champs de texte. Ce modèle utilise un réseau de neurones dans sa méthode d'apprentissage. Il a été implémenter sur deux architectures. Soit l'architecture en cascade et l'architecture "bout-en-bout".  Ce modèle a eu un score F1 de 94% 



### 3. Matériel et Méthodes

#### Infrastructure
Lors de ce projet, nous utiliserons le langage de programmation Python afin d'entraîner le modèle pour chaque police de caractère entrée par l'utilisateur. Ce langage de programmation est très utilisé pour ce qui est de l'intelligence artificielle de l'analyse de données et du machine Learning. Sa syntaxe est aussi très simpliste et très simple d'utilisation. 

Nous utiliserons aussi un modèle de base conçu pour du OCR. Le modèle Tesseract est un modèle d'OCR qui est facile à agrémenter grâce aux nombreux outils disponible comme cntraining, combine_tessdata, lstmtraining, text2image, etc. Il est ainsi possible d'apprendre au modèle à reconnaître plus efficacement et avec plus de précision certaines polices d'écriture.

De plus, nous avons également utilisé la librairie TESSTRAIN qui implémentes les différents outils d'entrainement du modèle Tesseract en un outil simple qui ne demande que des images et des fichiers avec le texte sur l'image.

#### Méthode

 Pour entrainer un modèle sur une police précise nous avons tout d'abord créer un script python utilisant l'outil Text2image de Tesseract afin de créer des images ainsi que des textes pour l'entrainement. Le contenu de ce texte est important, il est essentiels que tous les charactères soit présent, mais aussi que le contenu soit structurer en phrases afin que le modèle s'entraine sur des données qui correspondent à la réalité. Ce script prend de nombreux paramètres en compte comme le nombre d'image, les phrases utilisées, la police, la taille de la police dans les image et la résolution. Ce script coupler à la libraire TESSTRAIN permet de créer un modèle basé sur le modèle anglais de Tesseract entrainé additionnellement pour détecter une police donné.

#### Évaluation

Le but de ce projet est de comparer le modèle avec notre agrémentation avec le modèle de base. Ainsi, il sera possible de mesurer le gain ou la perte de précision du modèle. Nous comparons ainsi les scores F1, du modèle de base et du modèle avec notre agrémentation. Un modèle avec un score F1 moins élevé et moins précis et vice-versa. Il suffit donc de trouver le modèle avec le score F1 le plus élevé.

Pour l'évaluation, il sera donc nécessaire d'écrire un programme Python simple qui mesurera la précision et le rappel, dépendant eux-mêmes de quatre données

+ faux positif (TP)
+ faut négatif (FN)
+ vrai positif (TP)
+ vrai négatif (TN)

Nous avons le choix de calculer ces données parmi différentes grandeurs textuel. Nous pouvons les calculer à partir :

+ Des caractères correctement reconnus
+ Des mots correctement reconnus
+ Des lignes correctement reconnues
+ Des phrases correctement reconnues










































































