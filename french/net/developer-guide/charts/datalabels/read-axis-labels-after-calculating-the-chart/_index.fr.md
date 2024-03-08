---
title: Lire les étiquettes des axes après avoir calculé le graphique
description: Apprenez à lire les étiquettes des axes dans Aspose.Cells for .NET après avoir calculé le graphique. Notre guide vous montrera comment accéder et récupérer les étiquettes des axes, y compris leur formatage et leur positionnement.
keywords: Aspose.Cells for .NET, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning.
type: docs
weight: 90
url: /fr/net/read-axis-labels-after-calculating-the-chart/
---
##  **Scénarios d'utilisation possibles**

Vous pouvez lire les étiquettes des axes de votre graphique après avoir calculé ses valeurs à l'aide de la touche[**Graphique.Calculer()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/)méthode. Veuillez utiliser le[**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/) méthode à cet effet qui renverra la liste des étiquettes d’axe.

##  **Lire les étiquettes des axes après avoir calculé le graphique**

Veuillez consulter l'exemple de code suivant qui charge le[exemple de fichier Excel](ReadAxisLabels.xlsx)et lit les étiquettes de l'axe des catégories du graphique dans la première feuille de calcul. Il imprime ensuite les valeurs des étiquettes des axes sur la console. Veuillez consulter la sortie de la console de l'exemple de code ci-dessous pour référence.

##  **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

##  **Sortie console**

{{< highlight "csharp" >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
