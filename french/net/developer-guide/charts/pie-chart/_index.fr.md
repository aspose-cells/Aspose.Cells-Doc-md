---
title: Création d'un diagramme circulaire avec des lignes de repère
description: Découvrez comment utiliser Aspose.Cells for .NET pour créer un diagramme circulaire avec des lignes de repère dans Microsoft Excel. Notre guide vous montrera comment ajouter des lignes de repère qui relient les points de données à la légende et améliorent la clarté globale de votre graphique.
keywords: Aspose.Cells for .NET, Pie Chart, Leader Lines, Microsoft Excel, Data Visualization, Chart Customization.
linktitle: Diagramme circulaire
type: docs
weight: 45
url: /fr/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

Cet article explique comment créer un diagramme circulaire avec des lignes de repère à partir de zéro en utilisant Aspose.Cells for .NET API. Dans Excel, l'option « Afficher les lignes de repère » est définie par défaut. Ainsi, lorsque vous créez un diagramme circulaire dans Excel, les lignes de repère sont affichées. Cependant, lors de la création d'un graphique similaire avec les API Aspose.Cells, vous devez définir explicitement le[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) propriété.

{{% /alert %}}

 Pour démontrer l'utilisation de Aspose.Cells for .NET API pour créer un diagramme circulaire avec des lignes de repère, nous allons d'abord créer un nouveau[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) et saisissez des données qui serviront de source de données de série. Une fois les données en place, nous ajouterons un[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) de type[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)à la collection de graphiques et définissez ses différents aspects pour obtenir la vue graphique souhaitée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Jusqu'à présent, nous avons créé un diagramme circulaire et défini ses différents aspects. Nous allons maintenant activer les lignes de repère du graphique. Veuillez noter que pour afficher les lignes de repère, nous devons déplacer un peu les étiquettes de données.

Le morceau de code suivant active les lignes de repère, actualise le graphique, puis calcule les positions des étiquettes de données pour les déplacer en conséquence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Enfin, le code suivant enregistre le graphique au format image et le classeur au format XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Graphique circulaire résultant**|
| :- |
|![tâche : image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

##  **Sujets avancés**
- [Couleurs de tranche ou de secteur personnalisées dans un graphique à secteurs](/cells/fr/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Déterminez si les points de données se trouvent dans le deuxième secteur ou la deuxième barre d'un secteur ou d'une barre de diagramme circulaire](/cells/fr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

##  Articles Liés

- [Création de graphiques](/cells/fr/net/creating-charts/)
- [Personnalisation des graphiques](/cells/fr/net/customizing-charts/)
- [Formatage des données dans les graphiques](/cells/fr/net/data-formatting-in-charts/)
- [Définition de l'apparence du graphique](/cells/fr/net/setting-chart-appearance/)

