---
title: Trouver le type de valeurs X et Y des points dans la série de graphique
type: docs
weight: 110
url: /fr/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez connaître le type de valeurs X et Y des points du graphique dans une série. Aspose.Cells fournit les propriétés [**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType) et [**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType) qui peuvent être utilisées à cette fin. Veuillez noter que vous devrez appeler la méthode [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) avant de pouvoir utiliser ces propriétés de manière efficace.

## **Trouver le type de valeurs X et Y des points dans la série de graphiques**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716920.xlsx) et accède au premier graphique dans la première feuille de calcul. Ensuite, il appelle la méthode [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) et trouve le type de valeurs X et Y du premier point du graphique et les affiche sur la console. Veuillez consulter la sortie de la console ci-dessous pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Sortie console**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
