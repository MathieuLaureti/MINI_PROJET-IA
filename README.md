

## Composantes du Rapport de Projet

### 1. Définition de la Tâche


%%
- **Description de la tâche**: Expliquez ce que fait votre système (entrée et sortie).
- **Délimitation**: Assurez-vous que la tâche n'est ni trop large ni trop étroite.
- **Pertinence IA**: Justifiez l'utilisation de l'intelligence artificielle pour cette tâche.
%%
#### **Description de la tâche**: Expliquez ce que fait votre système (entrée et sortie).

Le système qui sera développé devra prendre en entrée une police de caractère ainsi qu'une image textuel ayant cette même police de caractère. Après traitement, Elle retournera une chaîne de caractère correspondant au texte donner en entrée sous forme imagée. Le modèle doit constamment apprendre de nouvelles polices de caractère. Elle doit s'adapter aux nouvelles polices de caractères utilisées et nommer par l'utilisateur.

#### **Délimitation**: Assurez-vous que la tâche n'est ni trop large ni trop étroite.



#### **Pertinence IA**: Justifiez l'utilisation de l'intelligence artificielle pour cette tâche.

 Dans les années précédentes, un programme algorithmique était utilisé pour reconnaître les écritures et les différentes polices de caractère. Cependant, ces programmes manquaient de fiabilité. il était parfois nécessaire d'écrire un nouveau programme et un nouvel algorithme pour des police de caractère plus récente. ces outils informatiques manquait d'adaptabilité. L'utilisation de l'intelligence artificielle basée sur un modèle s'avère une solution efficace, puisqu'elle permet une fonctionnalité d'apprentissage qui lui permet d'intégrer des nouvelles polices de caractère. Ainsi les modèles peuvent être ajusté lorsque de nouvelles police de caractère font leur apparition.


### 2. Brève Revue de la Littérature
%%
- **Synthèse des travaux existants**: Comparez et contrastez votre approche avec les travaux précédents.
- **Citations**: Référez-vous aux articles et publications pertinents.
%%
Dans la littérature, nous pouvons citer deux. Implémentations du OCR :

+ La première consistait à simplifier la documentation des transactions dans le commerce électronique @internationalconferenceonintelligencecomputingandinformationscienceIntelligentComputingInformation2011 . Le OCR servait à numériser les transactions sous format papier. Ainsi, il était plus facile de parcourir l'historique des transactions. Le modèle atteignait un score F1 de 0,7703 lors de ses tests  @internationalconferenceonintelligencecomputingandinformationscienceIntelligentComputingInformation2011 .
+ Le deuxième utilisait le OCR afin de lire des caractères sur des interfaces graphiques comme des boutons, des textes et des champs de texte @zhuOCRRCNNAccurateEfficient2022 . Ce modèle utilise un réseau de neurones dans sa méthode d'apprentissage @zhuOCRRCNNAccurateEfficient2022 . Il a été implémenter sur deux architectures. Soit l'architecture en cascade et l'architecture "bout-en-bout".  Ce modèle a eu un score F1 de 94% @zhuOCRRCNNAccurateEfficient2022 .

### 3. Matériel et Méthodes
%%
- **Infrastructure**: Décrivez les outils et les ressources utilisés (bases de données, logiciels, etc.).
- **Méthodes**: Expliquez les données et/ou algorithmes et techniques employés.
- **Évaluation**: Décrivez comment vous avez mesuré le succès du système (précision, temps de traitement, etc.). 

%%




#### infrastructure
Lors de ce projet, nous utiliserons le langage de programmation Python afin d'entraîner le modèle pour chaque police de caractère entrée par l'utilisateur. Ce langage de programmation est très utilisé pour ce qui est de l'intelligence artificielle de l'analyse de données et du machine Learning. Sa syntaxe est aussi très simpliste et très simple d'utilisation. 

Nous utiliserons aussi un modèle de base conçu pour du OCR. Le modèle TesseracT est un modèle d'OCR qui est facile à agrémenter. Il est ainsi possible d'apprendre au modèle à mieux reconnaître certaines polices d'écriture. Nous utilisons ce modèle afin de comparer les solutions apporter par notre agrémentation. Nous utiliserons aussi des documents produits manuellement afin de tester le modèle de base et le modèle avec agrémentation.

#### méthode

 Afin de parvenir à l'objectif mentionné plutôt, nous utiliserons les entrées de l'utilisateur afin de générer aléatoirement du contenu textuel imagée et structuré dans la police de caractère entrée par l'utilisateur. Les chaînes de caractère utilisées pour générer ces images seront aussi conservés. Pour les images textuelles, il sera utilisé plusieurs types de polices de caractères. Cela a pour objectif de donner une base plus solide sur différentes polices de caractères au modèle. Ensuite, le modèle sera entraîné sur les images de manière supervisé. Les couples (images, chaînes de caractère) formeront dataset utiliser pour entraîner le modèle. Ensuite, le modèle sera testé sur le texte écris manuellement par l'utilisateur. 

De cette manière, nous assurons que le modèle s'entraîne de manière supervisé en requérant un minimum d'interaction avec l'utilisateur.

#### évaluation

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


Pour le bien de ce projet, il a été choisi d'utiliser deux mesures de grandeur : les mots et les caractères. Le score F1 sera calculé pour chaque combinaison entre les grandeur de mesure et les modèles. Les deux modèles étant tesseracT sans agrémentation et la version de tesseracT dans lequel nous y avons ajouté notre agrémentation. C'est-à-dire de l'entraînement supplémentaire. Nous obtiendrons ainsi quatre scores F1 à comparer. Deux scores F1 par modèle sur différentes échelles de mesure. Ainsi, il suffira de comparer, et de trouver le score F1 le plus élevé afin de déterminer le modèle le plus exact par rapport au contenu textuel sous forme de chaîne de caractère. C'est même chaîne de caractère qui nous serviront de valeur de référence pour les tests.




### 4. Résultats



%%
- **Présentation des résultats**: Affichez les résultats obtenus sous forme de tableaux ou graphiques.
- **Analyse**: Interprétez les résultats et discutez de leur signification.
%%



### 5. Conclusion



%%
- **Résumé des résultats**: Faites un résumé des principales découvertes.
- **Perspectives**: Proposez des pistes pour améliorer le système ou pour des travaux futurs.
%%


#### Perspectives et amélioration


%%
Utiliser différents types de Background en arrière des lettres
Utiliser différentes taille de polices d'écriture
Utiliser les caractères français et de d'autres langues
Signe de ponctuation
Caractère spéciaux
%%



Plusieurs mesures peuvent être employés pour améliorer l'exactitude de notre modèle. 

Il pourrait s'avérer nécessaire d'entraîner le modèle sur divers arrière-plan. Dans le cas de ce projet, les images textuelles avec toutes et chacune un arrière-plan complètement blanc. Certaines images textuelles pourrais avoir un arrière-plan d'une couleur différente. Il serait donc pertinent d'entraîner le modèle sur des arrière-plan diversifiées.

Dans les données d'entraînement, l'ensemble des contenus textuel avait une taille de police identique. Dans la réalité d'un utilisateur du modèle, il se pourrait que son contenu textuel imagée soit de tête de police différente. Nous pouvons citer des exemples comme les citations, les notes dans la marge ainsi que les titres dans un texte. Entraîner le modèle sous différentes taille de police serait pertinent.

Encore une fois, dans les données d'entraînement, l'ensemble des caractères proviennent de ceux qui sont permis dans la langue anglaise. cependant l'ensemble des utilisateurs de ce genre de modèle n'ont pas l'anglais comme langue maternelle. nous pouvons citer les langues asiatiques, telles que le japonais ou le mandarin qui possède leur propre ensemble de caractères. nous pouvons énumérer le nombre de caractères japonais au-dessus de 3000, alors que la langue anglaise ne possède que les lettres de l'alphabet. il serait donc pertinent d'entraîner le modèle sur l'ensemble des familles de caractère qui existe dans de multiples cultures et de multiples région du monde.

Outre les caractères, il y a aussi l'ensemble des signes de ponctuation et des caractères spéciaux. La plupart du contenu textuel qui sera analysé par le modèle qui sera utilisé par l'utilisateur oran, une syntaxe nécessitant des signes de ponctuation et des caractères spéciaux. Au sein de nos données d'entraînement, il a été omis, dans son intégralité, l'existence de ces caractères. Pour ces raisons, il serait pertinent d'intégrer ses caractères spéciaux et ses signes de ponctuation à l'intérieur de nos données d'entraînement si le projet était à recommencer ou à poursuivre.



%%
## Directives Générales

- **Originalité**: Chaque projet doit être unique et innovant.
- **Collaboration**: Travaillez en équipe et partagez les tâches de manière équitable.
- **Documentation**: Documentez chaque étape du projet de manière claire et détaillée.

## Évaluation

Les projets seront évalués selon les critères suivants :

- **Définition de la tâche**: Clarté et pertinence.
- **Revue de la littérature**: Pertinence et qualité des références.
- **Méthodes**: Adéquation et justesse des techniques employées.
- **Résultats**: Qualité et analyse des résultats.
- **Conclusion**: Pertinence des conclusions et propositions futures.
- **Présentation orale**: Structure, organisation, cohérence et clarté de la présentation.

%%

















https://tesseract-ocr.github.io/tessdoc/tess4/TrainingTesseract-4.00.html





























































