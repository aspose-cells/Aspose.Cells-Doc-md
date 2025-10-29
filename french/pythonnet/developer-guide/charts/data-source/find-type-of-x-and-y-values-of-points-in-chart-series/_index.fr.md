---
title: Trouver le type de valeurs X et Y des points dans la série de graphique
description: Apprenez à déterminer le type de valeurs X et Y dans les points de séries de graphiques en utilisant Aspose.Cells pour Python via .NET. Notre guide expliquera les différents types de valeurs de données et vous montrera comment y accéder et travailler avec elles dans vos graphiques.
keywords: Aspose.Cells pour Python via .NET, création de graphiques, valeurs X, valeurs Y, types de données, accès, travaillez avec, séries de graphiques.
type: docs
weight: 150
url: /fr/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez connaître le type des valeurs X et Y des points du graphique dans une série. Aspose.Cells pour Python via .NET fournit [**ChartPoint.x_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/x_value_type/) et [**ChartPoint.y_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/y_value_type/) propriétés qui peuvent être utilisées à cet effet. Veuillez noter que vous devrez appeler la méthode [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) avant de pouvoir utiliser efficacement ces propriétés.

## **Trouver le type de valeurs X et Y des points dans la série de graphiques**
Le code d'exemple suivant charge le [fichier Excel d'exemple](64716905.xlsx) et accède au premier graphique dans la première feuille de calcul. Il appelle ensuite la méthode [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) et détermine le type des valeurs X et Y du premier point du graphique, puis les affiche dans la console. Veuillez consulter la sortie de la console ci-dessous pour référence.

## **Code d'exemple**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.py" >}}

## **Sortie console**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
