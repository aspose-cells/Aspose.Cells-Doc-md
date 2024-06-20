---
title: Couleurs personnalisées de tranche ou de secteur dans le diagramme circulaire
type: docs
weight: 30
url: /fr/java/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Cet article explique comment ajouter des couleurs personnalisées aux tranches/secteurs du diagramme circulaire. Par défaut, les diagrammes circulaires utilisent le modèle par défaut de Microsoft Excel. Pour utiliser d'autres couleurs, il est possible de redéfinir les couleurs dans le graphique.

{{% /alert %}}

Pour définir la couleur personnalisée pour les tranches ou secteurs individuels d'un graphique circulaire :

1. Accédez à [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) l'objet [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1. Assignez une couleur de votre choix en utilisant la méthode [**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor).

Cet article explique également comment définir :

- Les données de catégorie d'un graphique.
- Un titre de graphique lié à une cellule.
- Les paramètres de police du titre du graphique.
- La position de la légende.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) n'est pas spécifique aux graphiques circulaires mais peut être utilisé pour tous les types de graphiques.

{{% /alert %}}

**Couleurs de tranches personnalisées dans le diagramme circulaire**

![todo:image_alt_text](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
