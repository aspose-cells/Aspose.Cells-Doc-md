---
title: Créer un graphique circulaire avec lignes de repère
description: Apprenez à utiliser Aspose.Cells for .NET pour créer un graphique circulaire avec des lignes de repère dans Microsoft Excel. Notre guide montrera comment ajouter des lignes de repère qui relient les points de données à la légende et améliorent la clarté globale de votre graphique.
keywords: Aspose.Cells for .NET, Graphique circulaire, Lignes de repère, Microsoft Excel, Visualisation des données, Personnalisation du graphique.
linktitle: Graphique circulaire
type: docs
weight: 45
url: /fr/net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Cet article explique comment créer un graphique circulaire avec des lignes de repère à partir de zéro en utilisant l'API Aspose.Cells for .NET. Dans Excel, l'option 'Afficher les lignes de repère' est définie par défaut, donc lorsque vous créez un graphique circulaire dans Excel, les lignes de repère sont affichées. Cependant, lors de la création d'un graphique similaire avec les API Aspose.Cells, vous devez définir explicitement la propriété [**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines).

{{% /alert %}}

Pour illustrer l'utilisation de l'API Aspose.Cells for .NET pour créer un graphique circulaire avec des lignes de repère, nous allons d'abord créer un nouveau [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) et saisir des données qui serviront de source de données de série. Une fois les données en place, nous ajouterons un [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) de type [**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) à la collection de graphiques et en réglerons les différents aspects pour obtenir la vue de graphique souhaitée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Jusqu'à présent, nous avons créé un graphique circulaire et réglé ses différents aspects. Maintenant, nous allons activer les lignes de repère pour le graphique. Veuillez noter que pour afficher les lignes de repère, nous devons déplacer légèrement les étiquettes de données.

Le code suivant active les lignes de repère, actualise le graphique, puis calcule les positions des étiquettes de données pour les déplacer en conséquence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Enfin, le code suivant sauvegarde le graphique au format image et le classeur au format XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Diagramme circulaire résultant**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Sujets avancés**
- [Couleurs de tranche personnalisées dans le diagramme circulaire](/cells/fr/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Savoir si les points de données sont dans le deuxième diagramme circulaire ou dans une barre sur un diagramme de deux ou trois cercles ou sur un diagramme à barres de deux ou trois cercles](/cells/fr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Articles Connexes

- [Création de graphiques](/cells/fr/net/creating-charts/)
- [Personnalisation des graphiques](/cells/fr/net/customizing-charts/)
- [Mise en forme des données dans les graphiques](/cells/fr/net/data-formatting-in-charts/)
- [Réglage de l’apparence du graphique](/cells/fr/net/setting-chart-appearance/)

{{< app/cells/assistant language="csharp" >}}
