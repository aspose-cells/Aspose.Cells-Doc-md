---
title: Axe X contre. Axe des catégories
description: Apprenez à faire la différence entre l'axe X et l'axe Catégorie au Aspose.Cells for Java. Notre guide vous aidera à comprendre les différences dans leur utilisation et leurs propriétés, et comment les configurer en fonction de vos besoins.
keywords: Aspose.Cells for Java, X axis, Category axis, difference, usage, properties, configuration.
type: docs
weight: 180
url: /fr/java/x-axis-vs-category-axis/
---
##  **Scénarios d'utilisation possibles**
Il existe différents types d'axes X. Alors que l’axe Y est un axe de type Valeur, l’axe X peut être un axe de type Catégorie ou un axe de type Valeur. À l'aide d'un axe Valeur, les données sont traitées comme des données numériques variant continuellement et le marqueur est placé à un point le long de l'axe qui varie en fonction de sa valeur numérique. À l'aide d'un axe Catégorie, les données sont traitées comme une séquence d'étiquettes de texte non numériques et le marqueur est placé en un point le long de l'axe en fonction de sa position dans la séquence. L'exemple ci-dessous illustre la différence entre les axes de valeur et de catégorie.
 Nos exemples de données sont présentés dans le[exemple de fichier de table](sample.png) ci-dessous. La première colonne contient nos données sur l'axe X, qui peuvent être traitées comme des catégories ou comme des valeurs. Notez que les nombres ne sont pas équidistants et n’apparaissent même pas dans l’ordre numérique.

![tâche : image_alt_text](sample.png)
##  **Gérer les axes X et Catégorie comme Microsoft Excel**
Nous afficherons ces données sur deux types de graphiques, le premier graphique est le graphique XY (nuage de points) X comme axe des valeurs, le deuxième graphique est le graphique linéaire X comme axe des catégories.

![tâche : image_alt_text](compare.png)

 L'exemple de code suivant génère le[sortie du fichier Excel](XAxis.xlsx).

##  **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "X-axis-vs-category-axis.java" >}}
