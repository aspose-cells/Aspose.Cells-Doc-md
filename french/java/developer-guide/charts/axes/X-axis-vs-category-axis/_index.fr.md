---
title: Axe des X Vs. Axe des catégories
description: Apprenez à faire la différence entre l axe X et l axe des catégories dans Aspose.Cells for Java. Notre guide vous aidera à comprendre les différences dans leur utilisation et leurs propriétés, et comment les configurer selon vos besoins.
keywords: Aspose.Cells for Java, axe X, axe des catégories, différence, utilisation, propriétés, configuration.
type: docs
weight: 180
url: /fr/java/x-axis-vs-category-axis/
---

## **Scénarios d'utilisation possibles**
Il existe différents types d'axes des X. Alors que l'axe des Y est un axe de type Valeur, l'axe des X peut être un axe de type Catégorie ou un axe de type Valeur. En utilisant un axe de Valeur, les données sont traitées comme des données numériques continuellement variables, et le marqueur est placé à un point le long de l'axe qui varie en fonction de sa valeur numérique. En utilisant un axe de Catégorie, les données sont traitées comme une séquence d'étiquettes de texte non numériques, et le marqueur est placé à un point le long de l'axe selon sa position dans la séquence. L'exemple ci-dessous illustre la différence entre les axes de Valeur et de Catégorie.
Nos données d'exemple sont présentées dans le [fichier de tableau d'exemple](sample.png) ci-dessous. La première colonne contient nos données d'axe des X, qui peuvent être traitées comme des catégories ou comme des valeurs. Notez que les nombres ne sont pas également espacés, et ils n'apparaissent même pas dans un ordre numérique.

![todo:image_alt_text](sample.png)
## **Manipulez l'axe des X et l'axe des catégories comme Microsoft Excel**
Nous afficherons ces données sur deux types de graphiques, le premier graphique est un graphique XY (dispersion) avec l'axe des X comme axe de valeur, le deuxième graphique est un graphique linéaire avec l'axe des X comme axe de catégorie.

![todo:image_alt_text](compare.png)

Le code d'exemple suivant génère le [fichier Excel de sortie](XAxis.xlsx).

## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "X-axis-vs-category-axis.java" >}}
{{< app/cells/assistant language="java" >}}
