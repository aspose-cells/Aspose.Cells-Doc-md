---
title: Trouver le type de valeurs X et Y des points dans la série de graphique
description: Apprenez à déterminer le type de valeurs X et Y dans les points de la série de graphique en utilisant Aspose.Cells for .NET. Notre guide expliquera les différents types de valeurs de données et vous montrera comment y accéder et les manipuler dans vos graphiques.
keywords: Aspose.Cells for .NET, création de graphiques, valeurs X, valeurs Y, types de données, accès, manipulation, série de graphique.
type: docs
weight: 150
url: /fr/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Scénarios d'utilisation possibles**
Parfois, vous voulez connaître le type de valeurs X et Y des points de graphique dans une série. Aspose.Cells fournit les propriétés ChartPoint.XValueType et ChartPoint.YValueType qui peuvent être utilisées à cette fin. Veuillez noter que vous devrez appeler la méthode Chart.Calculate() avant de pouvoir utiliser ces propriétés de manière efficace.
## **Trouver le type de valeurs X et Y des points dans la série de graphiques**
Le code d'exemple suivant charge le [fichier Excel d'exemple](64716905.xlsx) et accède au premier graphique dans la première feuille de calcul. Ensuite, il appelle la méthode Chart.Calculate() et trouve le type de valeurs X et Y du premier point du graphique, puis les imprime sur la console. Veuillez consulter la sortie de la console ci-dessous à titre de référence.

## **Code d'exemple**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}

## **Sortie console**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
