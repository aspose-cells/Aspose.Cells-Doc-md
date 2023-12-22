---
title: Rechercher le type de valeurs X et Y des points dans une série de graphiques
description: Apprenez à déterminer le type de valeurs X et Y dans les points de la série de graphiques en utilisant le Aspose.Cells for .NET. Notre guide vous expliquera les différents types de valeurs de données et vous montrera comment y accéder et les utiliser dans vos graphiques.
keywords: Aspose.Cells for .NET, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /fr/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
##  **Scénarios d'utilisation possibles**
Parfois, vous souhaitez connaître le type de valeurs X et Y des points du graphique dans une série. Aspose.Cells fournit les propriétés ChartPoint.XValueType et ChartPoint.YValueType qui peuvent être utilisées à cette fin. Veuillez noter que vous devrez appeler la méthode Chart.Calculate() avant de pouvoir utiliser ces propriétés efficacement.
##  **Rechercher le type de valeurs X et Y des points dans une série de graphiques**
 L'exemple de code suivant charge le[exemple de fichier Excel](64716905.xlsx) et accède au premier graphique à l’intérieur de la première feuille de calcul. Il appelle ensuite la méthode Chart.Calculate() et trouve le type de valeurs X et Y du premier point du graphique et les imprime sur la console. Veuillez consulter la sortie de la console ci-dessous pour référence.
##  **Exemple de code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
##  **Sortie console**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
