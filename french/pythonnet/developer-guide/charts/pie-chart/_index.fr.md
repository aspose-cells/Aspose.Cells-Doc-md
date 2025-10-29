---
title: Créer un graphique circulaire avec lignes de repère
description: Apprenez à utiliser Aspose.Cells pour Python via .NET pour créer un graphique en secteurs avec des lignes de leader dans Microsoft Excel. Notre guide montrera comment ajouter des lignes de leader reliant les points de données à la légende et améliorer la clarté globale de votre graphique.
keywords: Aspose.Cells pour Python via .NET, Graphique en secteurs, Lignes de leader, Microsoft Excel, Visualisation de données, Personnalisation du graphique.
linktitle: Graphique circulaire
type: docs
weight: 45
url: /fr/python-net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Cet article explique comment créer un graphique en secteurs avec des lignes de leader à partir de zéro en utilisant l'API Aspose.Cells pour Python via .NET. Dans Excel, l'option 'Afficher les lignes de leader' est activée par défaut, donc lorsque vous créez un graphique en secteurs dans Excel, les lignes de leader sont affichées. Cependant, lors de la création d'un graphique similaire avec l'API Aspose.Cells pour Python via .NET, vous devez explicitement définir la propriété [**Series.has_leader_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/has_leader_lines).

{{% /alert %}}

Pour démontrer l'utilisation de l'API Aspose.Cells pour Python via .NET pour créer un graphique en secteurs avec des lignes de leader, nous allons d'abord créer un nouveau [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) et y insérer quelques données qui serviront de source de données de la série. Une fois les données en place, nous ajouterons un [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) de type [**ChartType.PIE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) à la collection de graphiques et réglerons ses différents aspects pour obtenir la vue souhaitée du graphique.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateWorkbook.py" >}}

Jusqu'à présent, nous avons créé un graphique circulaire et réglé ses différents aspects. Maintenant, nous allons activer les lignes de repère pour le graphique. Veuillez noter que pour afficher les lignes de repère, nous devons déplacer légèrement les étiquettes de données.

Le code suivant active les lignes de repère, actualise le graphique, puis calcule les positions des étiquettes de données pour les déplacer en conséquence.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TurnOnLeaderLines.py" >}}

Enfin, le code suivant sauvegarde le graphique au format image et le classeur au format XLSX.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SaveChartInImageAndWorkbookInXLSX.py" >}}

|**Diagramme circulaire résultant**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Sujets avancés**
- [Couleurs de tranche personnalisées dans le diagramme circulaire](/cells/fr/python-net/custom-slice-or-sector-colors-in-pie-chart/)
- [Savoir si les points de données sont dans le deuxième diagramme circulaire ou dans une barre sur un diagramme de deux ou trois cercles ou sur un diagramme à barres de deux ou trois cercles](/cells/fr/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Articles Connexes

- [Création de graphiques](/cells/fr/python-net/creating-charts/)
- [Personnalisation des graphiques](/cells/fr/python-net/customizing-charts/)
- [Mise en forme des données dans les graphiques](/cells/fr/python-net/data-formatting-in-charts/)
- [Réglage de l’apparence du graphique](/cells/fr/python-net/setting-chart-appearance/)

{{< app/cells/assistant language="python-net" >}}
