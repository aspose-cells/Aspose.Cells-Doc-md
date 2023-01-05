---
title: Création d'un graphique à secteurs avec des lignes de repère
linktitle: Diagramme circulaire
type: docs
weight: 45
url: /fr/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

 Cet article explique comment créer un graphique à secteurs avec des lignes de repère à partir de zéro tout en utilisant Aspose.Cells for .NET API. Dans Excel, l'option "Afficher les lignes de repère" est définie par défaut. Ainsi, lorsque vous créez un graphique à secteurs dans Excel, les lignes de repère sont affichées. Cependant, lors de la création d'un graphique similaire avec les API Aspose.Cells, vous devez définir explicitement le[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) la propriété.

{{% /alert %}}

Pour démontrer l'utilisation de Aspose.Cells for .NET API pour créer un graphique à secteurs avec des lignes de repère, nous allons d'abord créer un nouveau[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) et entrez des données qui serviront de source de données de série. Une fois les données en place, nous ajouterons un[**Graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) de type[**GraphiqueType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)à la collection de graphiques et définissez ses différents aspects pour obtenir la vue de graphique souhaitée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Jusqu'à présent, nous avons créé un diagramme circulaire et défini ses différents aspects. Nous allons maintenant activer les lignes de repère du graphique. Veuillez noter que pour afficher les lignes de repère, nous devons déplacer légèrement les étiquettes de données.

Le morceau de code suivant active les lignes de repère, actualise le graphique, puis calcule les positions des étiquettes de données pour les déplacer en conséquence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Enfin, le code suivant enregistre le graphique au format image et le classeur au format XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Graphique à secteurs résultant**|
|:- |
|![tâche : image_autre_texte](creating-pie-chart-with-leader-lines_1.png)|

## **Sujets avancés**
- [Couleurs de tranche ou de secteur personnalisées dans le graphique à secteurs](/cells/fr/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Rechercher si les points de données se trouvent dans le deuxième secteur ou barre sur un secteur de secteur ou une barre de graphique en secteurs](/cells/fr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Articles Liés

- [Création de graphiques](/cells/fr/net/creating-charts/)
- [Personnalisation des graphiques](/cells/fr/net/customizing-charts/)
- [Formatage des données dans les graphiques](/cells/fr/net/data-formatting-in-charts/)
- [Réglage de l'apparence du graphique](/cells/fr/net/setting-chart-appearance/)

