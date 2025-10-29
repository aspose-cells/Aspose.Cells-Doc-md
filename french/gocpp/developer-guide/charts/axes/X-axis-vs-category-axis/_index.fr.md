---
title: Axe X vs. Axe de catégorie avec Golang via C++
linktitle: Axe des X Vs. Axe des catégories
description: Apprenez à différencier l axe X et l axe de catégorie dans Aspose.Cells for C++. Notre guide vous aidera à comprendre leurs différences d utilisation et de propriétés, ainsi que comment les configurer selon vos besoins.
keywords: Aspose.Cells for C++, axe X, axe de catégorie, différence, utilisation, propriétés, configuration.
type: docs
weight: 180
url: /fr/go-cpp/X-axis-vs-category-axis/
---

## **Scénarios d'utilisation possibles**
Il existe différents types d'axes des X. Alors que l'axe des Y est un axe de type Valeur, l'axe des X peut être un axe de type Catégorie ou un axe de type Valeur. En utilisant un axe de Valeur, les données sont traitées comme des données numériques continuellement variables, et le marqueur est placé à un point le long de l'axe qui varie en fonction de sa valeur numérique. En utilisant un axe de Catégorie, les données sont traitées comme une séquence d'étiquettes de texte non numériques, et le marqueur est placé à un point le long de l'axe selon sa position dans la séquence. L'exemple ci-dessous illustre la différence entre les axes de Valeur et de Catégorie.
Nos données d'exemple sont présentées dans le [fichier de tableau d'exemple](sample.png) ci-dessous. La première colonne contient nos données d'axe des X, qui peuvent être traitées comme des catégories ou comme des valeurs. Notez que les nombres ne sont pas également espacés, et ils n'apparaissent même pas dans un ordre numérique.

![todo:image_alt_text](sample.png)

## **Manipulez l'axe des X et l'axe des catégories comme Microsoft Excel**
Nous afficherons ces données sur deux types de graphiques, le premier est un graphique XY (Dispersion) avec l'axe X en tant qu'axe de valeur, le second est un graphique en ligne avec l'axe X en tant qu'axe de catégorie.

![todo:image_alt_text](compare.png)

## **Code d'exemple**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-XAxisVsCategoryAxis.go" >}}
