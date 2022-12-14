---
title: Axe X vs. Axe des catégories
type: docs
weight: 180
url: /fr/net/X-axis-vs-category-axis/
---
## **Scénarios d'utilisation possibles**
Il existe différents types d'axes X. Alors que l'axe Y est un axe de type Valeur, l'axe X peut être un axe de type Catégorie ou un axe de type Valeur. À l'aide d'un axe des valeurs, les données sont traitées comme des données numériques à variation continue et le marqueur est placé à un point le long de l'axe qui varie en fonction de sa valeur numérique. À l'aide d'un axe Catégorie, les données sont traitées comme une séquence d'étiquettes de texte non numériques et le marqueur est placé à un point le long de l'axe en fonction de sa position dans la séquence. L'exemple ci-dessous illustre la différence entre les axes de valeur et de catégorie.
 Nos exemples de données sont présentés dans le[exemple de fichier de table](sample.png) dessous. La première colonne contient nos données d'axe X, qui peuvent être traitées comme des catégories ou comme des valeurs. Notez que les nombres ne sont pas espacés de manière égale et qu'ils n'apparaissent même pas dans l'ordre numérique.

![tâche : image_autre_texte](sample.png)
## **Gérer les axes X et Catégorie comme Microsoft Excel**
Nous afficherons ces données sur deux types de graphique, le premier graphique est le graphique XY (nuage) X comme axe des valeurs, le deuxième graphique est le graphique linéaire X comme axe des catégories.

![tâche : image_autre_texte](compare.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "X-axis-vs-category-axis.cs" >}}
