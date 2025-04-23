---
title: Lire les étiquettes d axe après avoir calculé le graphique
description: Apprenez comment lire les étiquettes d axe dans Aspose.Cells pour Python via .NET après le calcul du graphique. Notre guide vous montrera comment accéder et récupérer les étiquettes d axe, y compris leur mise en forme et leur positionnement.
keywords: Aspose.Cells pour Python via .NET, graphique, étiquettes d axe, calcul, lecture, accès, récupération, mise en forme, positionnement.
type: docs
weight: 90
url: /fr/python-net/read-axis-labels-after-calculating-the-chart/
---

## **Scénarios d'utilisation possibles**

Vous pouvez lire les étiquettes d'axe de votre graphique après avoir calculé ses valeurs en utilisant la méthode [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/). Veuillez utiliser la méthode [**Axis.get_axis_texts()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis/get_axis_texts) à cette fin qui renverra la liste des étiquettes d'axe.

## **Lire les étiquettes des axes après le calcul du graphique**

Veuillez consulter le code d'exemple suivant qui charge le fichier Excel d'exemple et lit les étiquettes d'axe de catégorie du graphique dans la première feuille de calcul. Il imprime ensuite les valeurs des étiquettes d'axe sur la console. Veuillez consulter la sortie de la console du code d'exemple ci-dessous pour une référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ReadAxisLabelsAfterCalculatingTheChart.py" >}}

## **Sortie console**

{{< highlight csharp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
