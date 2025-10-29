---
title: Lire les étiquettes d axe après avoir calculé le graphique avec Golang via C++
linktitle: Lire les étiquettes d axe après avoir calculé le graphique
description: Apprenez comment lire les étiquettes d axe dans Aspose.Cells for C++ après avoir calculé le graphique. Notre guide vous montrera comment accéder et récupérer les étiquettes d axe, y compris leur mise en forme et leur positionnement.
keywords: Aspose.Cells for C++, graphique, étiquettes d axe, calcul, lecture, accès, récupération, mise en forme, positionnement.
type: docs
weight: 90
url: /fr/go-cpp/read-axis-labels-after-calculating-the-chart/
---

## **Scénarios d'utilisation possibles**

Vous pouvez lire les étiquettes d'axe de votre graphique après avoir calculé ses valeurs en utilisant la méthode [**Chart.Calculate()**](https://reference.aspose.com/cells/go-cpp/chart/calculate/). Veuillez utiliser la méthode [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/) à cette fin qui renverra la liste des étiquettes d'axe.

## **Lire les étiquettes des axes après le calcul du graphique**

Veuillez consulter le code d'exemple suivant qui charge le fichier Excel d'exemple et lit les étiquettes d'axe de catégorie du graphique dans la première feuille de calcul. Il imprime ensuite les valeurs des étiquettes d'axe sur la console. Veuillez consulter la sortie de la console du code d'exemple ci-dessous pour une référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadAxisLabelsAfterCalculatingTheChart.go" >}}
## **Sortie console**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
