---
title: Trouver le type de valeurs X et Y des points dans la série de graphiques
type: docs
weight: 150
url: /fr/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez connaître le type de valeurs X et Y des points du graphique dans une série. Aspose.Cells fournit les propriétés ChartPoint.XValueType et ChartPoint.YValueType qui peuvent être utilisées à cette fin. Veuillez noter que vous devrez appeler la méthode Chart.Calculate() avant de pouvoir utiliser ces propriétés efficacement.
## **Trouver le type de valeurs X et Y des points dans la série de graphiques**
 L'exemple de code suivant charge le[exemple de fichier Excel](64716905.xlsx) et accède au premier graphique à l'intérieur de la première feuille de calcul. Il appelle ensuite la méthode Chart.Calculate() et trouve le type des valeurs X et Y du premier point du graphique et les imprime sur la console. Veuillez consulter la sortie de la console ci-dessous pour référence.
## **Exemple de code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
## **Sortie console**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
