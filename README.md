

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

Il est important de générer des chaînes de caractère qui forment des phrases dans une certaine langue. Les programmes aussi sont normalement spécialisés dans une seule langue à la fois. C'est pour cela que chaque police de caractère sous forme de chaîne textuelle et d'image ont été écrit en anglais par souci de généralité. Ce sont toujours les mêmes chaînes de caractère qui sont transformées pour chaque police de caractère. Il a été aussi écrit une jeune de caractère comportant toutes les caractères permis afin de pouvoir entraîner le modèle sur chacun d'eux. Il se pourrait par exemple que le modèle ne soit jamais entraîné sur la lettre "X" puisque cette lettre est rare en anglais.

Des fichiers "ttf" permettent aussi de faire référence à différentes polices de caractères, afin de créer les images sous forme textuelles. Ce sont ces fichiers qui définissent les polices de caractère

Après la création de chaîne, de caractère sous forme d'image et sous forme textuelle, certains fichiers de référence pour la création du modèle ont été créé. notamment des fichiers de mapping, afin d'indiquer au modèle l'emplacement de chaque caractère. Des fichiers "traineddata" ont aussi été créé afin de pouvoir entraîner le modèle. 



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


// Mathieu, lis attentivement ces deux paragraphes puisse qu'il concernent quelque chose que tu as lu et cherché

Cependant, au milieu du projet, il a été constaté que le score F1 ne serait pas le meilleur outil pour évaluer ce modèle.

Effectivement, cette méthode est utilisée pour des modèles complets. Cette manière d'évaluer un modèle OCR est limité. Notamment parce qu'elle ne prend pas en compte la structure de la phrase, les mots manquants et l'image textuelle. Elle ne prend pas en compte les mots qui se ressemblent, elle calcule l'erreur par rapport à la chaîne des caractères en elle-même. S'il ne manque qu'un seul caractère, tous les suivants sont considérés comme étant mauvais, et donc une erreur. Cela augmente le taux d'erreur de manière artificielle. 

Dans le cadre de ce projet, nous utiliserons une autre méthode d'évaluation. Nous utiliserons la méthode WER, CER et MER. Ces méthodes consiste simplement à mesurer le nombre de substituions qu'il faut effectuer sur une chaîne de caractère pour obtenir une chaîne de caractère de référence. Plus il faut faire de substitution, plus la chaîne de caractère est différente de celle de référence. Le taux d'erreur en est donc augmenté. Les différentes mesures respectivement ce taux de substitution sur les mot, les caractères et la chaîne de caractère en tant que tel. 

Cette méthode d'évaluation est plus adaptée puisqu'elle tient en compte de la structure de la phrase. Elle ne divise pas la phrase au moment où il y a la première erreur. Ce qui rend le taux d'erreur plus pertinent pour un modèle de OCR. 


### 4. Résultats



%%
- **Présentation des résultats**: Affichez les résultats obtenus sous forme de tableaux ou graphiques.
- **Analyse**: Interprétez les résultats et discutez de leur signification.
%%


Ce graphique présente le CER en fonction du nombre itération de l'entraînement du modèle. on peut voir ici qu'il y a un coude qui se forme pour chacune des polices de caractère. Ainsi presque tous les modèles ont un niveau de précision CER acceptable. Seuls les modèles Bradley_Hand_ITC et Stencil ne semble pas avoir un coude acceptable. 

![[Graphique.png]]
La raison pour laquelle certaines polices d'écriture n'ont pas un coude acceptable est simplement le fait que ce sont des polices d'écriture qui sont très peu utilisées et moins lisible. Les caractères ont notamment des formes assez inhabituelle. Ce sont des police de caractère qui se rapproche beaucoup plus des lettres attachées que de véritables caractères écrit par un ordinateur.

Cependant puisque les autres polices de caractère sont des polices qui sont beaucoup plus semblables à des polices de caractère écrites par un ordinateur et que les caractères sont bien définis et séparés les uns des autres, le modèle a tendance à beaucoup mieux les reconnaître.

L'objectif est en quelque sorte accomplie, puisque le modèle sera utilisé pour reconnaître des polices de caractères écrites à l'ordinateur et non de façon manuscrite par un être humain. 

L'utilisation de ce modèle aussi pourra être utilisé dans l'industrie si plus développé.

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


// ici, tu peux parler des situations que tu as rencontrées durant le développement Mathieu





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








EASY OCR : https://github.com/JaidedAI/EasyOCR
TESSERACT : https://github.com/tesseract-ocr/tesseract
Google Vision API : https://cloud.google.com/vision?hl=fr
ABBYY : https://www.abbyy.com/ocr-sdk/

https://github.com/kennethleungty/OCR-Metrics-CER-WER?utm_source=chatgpt.com


https://github.com/kennethleungty/OCR-Metrics-CER-WER?utm_source=chatgpt.com


https://tesseract-ocr.github.io/tessdoc/tess4/TrainingTesseract-4.00.html


https://tesseract-ocr.github.io/tessdoc/tess4/TrainingTesseract-4.00.html

https://docs.kolena.com/metrics/wer-cer-mer/


https://github.com/tesseract-ocr/tesstrain






Sens de lecture
Radical_stroke.txt : mapper symboles asiatiques caractère spéciaux



























































