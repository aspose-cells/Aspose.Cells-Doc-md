---
title: Rechercher si les points de données se trouvent dans le deuxième secteur ou barre sur un secteur de secteur ou une barre de graphique en secteur
type: docs
weight: 180
url: /fr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
## **Scénarios d'utilisation possibles**
 Vous pouvez trouver si les points de données de la série sont dans le deuxième secteur sur*tarte de tarte* graphique ou dans la barre de*Barre de tarte* graphique en utilisant Aspose.Cells. Veuillez utiliser le[ChartPoint.IsInSecondaryPlotChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)propriété pour le déterminer.

 Veuillez télécharger le[exemple de fichier excel](5115193.xlsx) utilisé dans l'exemple de code suivant et consultez sa sortie de console. Si vous ouvrez le[exemple de fichier excel](5115193.xlsx) , vous trouverez, tous les points de données qui sont inférieurs à 10 sont à l'intérieur de la barre de*Barre de tarte*graphique comme indiqué également par la sortie de la console.
## **Rechercher si les points de données se trouvent dans le deuxième secteur ou barre sur un secteur de secteur ou une barre de graphique en secteur**
 L'exemple de code suivant montre comment déterminer si des points de données se trouvent dans le deuxième secteur ou barre d'un*tarte de tarte* ou*Barre de tarte*graphique.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **Sortie console**
 Veuillez consulter la sortie de console suivante générée après l'exécution de l'exemple de code ci-dessus avec le[exemple de fichier excel](5115193.xlsx) . Si[IsInSecondaryPlotIsInSecondaryPlotIsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) est**faux** , le point de données est à l'intérieur du secteur ou s'il est**vrai**, alors le point de données est à l'intérieur de la barre.



{{< highlight "java" >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
