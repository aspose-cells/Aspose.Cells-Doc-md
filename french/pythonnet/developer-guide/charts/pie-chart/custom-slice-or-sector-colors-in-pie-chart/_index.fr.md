---
title: Couleurs personnalisées de tranche ou de secteur dans le diagramme circulaire
description: Apprenez comment utiliser Aspose.Cells pour Python via .NET pour personnaliser les couleurs de tranche et de secteur dans un graphique en secteurs (pie chart). Notre guide montrera comment attribuer des couleurs uniques à chaque tranche, secteur ou légion pour une meilleure attraction visuelle et une meilleure représentation des données.
keywords: Aspose.Cells pour Python via .NET, Graphique en secteurs, Couleurs de tranches personnalisées, Couleurs de secteurs personnalisés, Attrait visuel, Représentation des données.
type: docs
weight: 60
url: /fr/python-net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Cet article explique comment ajouter des couleurs personnalisées aux tranches/secteurs d'un diagramme circulaire. Par défaut, les diagrammes circulaires utilisent le modèle par défaut de Microsoft Excel. Pour utiliser d'autres couleurs, redéfinissez les couleurs dans le diagramme.

{{% /alert %}}

Pour définir une couleur personnalisée pour les tranches ou secteurs individuels d'un diagramme circulaire :

1. Accédez à [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) l'objet [**ChartPoint**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint).
1. Attribuez la couleur de votre choix en utilisant la propriété [**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color).

Cet article explique également comment :

- Les données de catégorie d'un graphique.
- Un titre de graphique lié à une cellule.
- Les paramètres de police du titre du graphique.
- La position de la légende.

{{% alert color="primary" %}}

[**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color) n'est pas spécifique aux diagrammes circulaires mais peut être utilisé pour tous les types de diagrammes.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CustomSliceSectorColorsPieChart-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
