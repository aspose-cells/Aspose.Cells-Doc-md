---
title: Créer un graphique circulaire avec lignes de repère
linktitle: Graphique circulaire
type: docs
weight: 170
url: /fr/java/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Cet article explique comment créer un graphique en secteurs avec des lignes de leader à partir de zéro tout en utilisant l'API Aspose.Cells for Java. Dans Excel, l'option 'Afficher les lignes de leader' est activée par défaut, donc lorsque vous créez un graphique en secteurs dans Excel, les lignes de leader sont affichées. Cependant, lors de la création d'un graphique similaire avec les API Aspose.Cells, vous devez définir explicitement la propriété [**Series.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#HasLeaderLines).

{{% /alert %}}

## **Créer un graphique circulaire avec des lignes de repère**

Afin de démontrer l'utilisation de l'API Aspose.Cells for Java pour créer un graphique en secteurs avec des lignes de leader, nous allons tout d'abord créer une nouvelle [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) et saisir des données qui serviront de source de données pour les séries. Une fois les données en place, nous ajouterons un [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) de type [**Pie**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE) à la collection de graphiques et définirons ses différents aspects pour obtenir la vue de graphique souhaitée.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**Graphique en Secteurs Résultant**

![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)

## Articles Connexes

- [Création et Personnalisation des Graphiques](/cells/fr/java/creating-and-customizing-charts/)
- [Formatage des Graphiques](/cells/fr/java/chart-formatting/)
