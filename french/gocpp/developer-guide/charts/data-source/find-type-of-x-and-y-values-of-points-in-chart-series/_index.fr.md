---
title: Trouver le type de valeurs X et Y des points dans la série de graphiques avec Golang via C++
linktitle: Trouver le type de valeurs X et Y des points dans la série de graphique
description: Apprenez comment déterminer le type de valeurs X et Y dans les points de la série de graphiques en utilisant Aspose.Cells for C++. Notre guide expliquera les différents types de valeurs de données et vous montrera comment y accéder et les manipuler dans vos graphiques.
keywords: Aspose.Cells for C++, diagramme, valeurs X, valeurs Y, types de données, accès, manipulation, série de graphiques.
type: docs
weight: 150
url: /fr/go-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez connaître le type des valeurs X et Y des points dans une série de graphiques. Aspose.Cells fournit les méthodes `ChartPoint::get_XValueType` et `ChartPoint::get_YValueType` qui peuvent être utilisées à cette fin. Veuillez noter que vous devrez appeler la méthode `Chart::Calculate()` avant de pouvoir utiliser efficacement ces propriétés.

## **Trouver le type de valeurs X et Y des points dans la série de graphiques**
Le code d'exemple suivant charge le [fichier Excel d'exemple](64716905.xlsx) et accède au premier graphique dans la première feuille de calcul. Ensuite, il appelle la méthode `Chart::Calculate()` et détermine le type des valeurs X et Y du premier point de graphique, puis les affiche dans la console. Veuillez voir la sortie console ci-dessous pour référence.

## **Code d'exemple**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindTypeOfXAndYValuesOfPointsInChartSeries.go" >}}
## **Sortie console**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
