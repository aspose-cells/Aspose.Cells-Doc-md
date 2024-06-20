---
title: Lire les étiquettes d axe après avoir calculé le graphique
description: Apprenez à lire les étiquettes d axe dans Aspose.Cells for Java après avoir calculé le graphique. Notre guide vous montrera comment accéder et récupérer les étiquettes d axe, y compris leur mise en forme et leur positionnement.
keywords: Aspose.Cells for Java, graphique, étiquettes d axe, calcul, lecture, accès, récupération, formatage, positionnement.
type: docs
weight: 90
url: /fr/java/read-axis-labels-after-calculating-the-chart/
---

## **Scénarios d'utilisation possibles**

Vous pouvez lire les étiquettes d'axe de votre graphique après avoir calculé ses valeurs en utilisant la méthode [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart/#calculate--). Veuillez utiliser la méthode [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/#getAxisTexts--) à cette fin qui renverra la liste des étiquettes d'axe.

## **Lire les étiquettes des axes après le calcul du graphique**

Veuillez consulter le code d'exemple suivant qui charge le fichier Excel d'exemple (64716829.xlsx) et lit les étiquettes d'axe de catégorie du graphique dans la première feuille de calcul. Ensuite, imprimez les valeurs des étiquettes d'axe sur la console. Veuillez consulter la sortie de la console du code d'exemple ci-dessous pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-ReadAxisLabelsAfterCalculatingTheChart.java" >}}

## **Sortie console**

{{< highlight java >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
