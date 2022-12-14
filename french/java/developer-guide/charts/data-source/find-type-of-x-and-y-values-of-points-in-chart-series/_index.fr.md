---
title: Trouver le type de valeurs X et Y des points dans la série de graphiques
type: docs
weight: 110
url: /fr/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez connaître le type de valeurs X et Y des points du graphique dans une série. Aspose.Cells fournit[**ChartPoint.XValueTypeChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType)et[**ChartPoint.YValueTypeChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType)propriétés qui peuvent être utilisées à cette fin. Attention, vous devrez téléphoner[**Graphique.calculer()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) avant de pouvoir utiliser efficacement ces propriétés.

## **Trouver le type de valeurs X et Y des points dans la série de graphiques**

L'exemple de code suivant charge le[exemple de fichier Excel](64716920.xlsx)et accède au premier graphique à l'intérieur de la première feuille de calcul. Il appelle ensuite le[**Graphique.calculer()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()et trouve le type des valeurs X et Y du premier point du graphique et les imprime sur la console. Veuillez consulter la sortie de la console ci-dessous pour référence.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Sortie console**

{{< highlight "java" >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
