---
title: Couleurs de tranche ou de secteur personnalisées dans le graphique à secteurs
type: docs
weight: 30
url: /fr/java/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

Cet article explique comment ajouter des couleurs personnalisées aux tranches/secteurs du graphique à secteurs. Par défaut, les graphiques à secteurs utilisent le modèle Excel par défaut Microsoft. Pour utiliser d'autres couleurs, il est possible de redéfinir les couleurs dans le nuancier.

{{% /alert %}}

Pour définir la couleur personnalisée des tranches ou secteurs individuels d'un graphique à secteurs :

1.  Accéder au[**Série**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) objets[**Point de graphique**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1.  Attribuez une couleur de votre choix à l'aide des[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)méthode.

Cet article explique également comment définir :

- Données de catégorie d'un graphique.
- Un titre de graphique lié à une cellule.
- Les paramètres de police du titre du graphique.
- La position de la légende.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) n'est pas spécifique aux camemberts mais peut être utilisé pour tous les types de graphiques.

{{% /alert %}}

**Couleurs de tranche personnalisées dans le graphique à secteurs**

![tâche : image_autre_texte](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
