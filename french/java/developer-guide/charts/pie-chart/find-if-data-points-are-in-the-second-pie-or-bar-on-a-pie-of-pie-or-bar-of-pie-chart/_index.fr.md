---
title: Rechercher si les points de données se trouvent dans le deuxième secteur ou barre sur un secteur de secteur ou une barre de graphique en secteurs
type: docs
weight: 910
url: /fr/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
## **Scénarios d'utilisation possibles**
 Vous pouvez trouver si les points de données de la série sont dans le deuxième secteur sur*tarte de tarte* graphique ou dans la barre de*Barre de tarte* graphique en utilisant Aspose.Cells. Veuillez utiliser le[ChartPoint.IsInSecondaryPlotChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot)propriété pour le déterminer.

 Veuillez télécharger le[exemple de fichier excel](5473373.xlsx) utilisé dans l'exemple de code suivant et consultez sa sortie de console. Si vous ouvrez le[exemple de fichier excel](5473373.xlsx), vous trouverez, tous les points de données qui sont inférieurs à 10 sont à l'intérieur de la barre de*Barre de tarte*graphique comme indiqué également par la sortie de la console.
## **Rechercher si les points de données se trouvent dans le deuxième secteur ou barre sur un secteur de secteur ou une barre de graphique en secteurs**
 L'exemple de code suivant montre comment déterminer si des points de données se trouvent dans le deuxième secteur ou barre d'un*tarte de tarte* ou alors*Barre de tarte*graphique.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **Sortie console**
 Veuillez consulter la sortie de console suivante générée après l'exécution de l'exemple de code ci-dessus avec le[exemple de fichier excel](5473373.xlsx) . Si[IsInSecondaryPlotIsInSecondaryPlotIsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) est**faux** , le point de données est à l'intérieur du secteur ou s'il est**vrai**, alors le point de données est à l'intérieur de la barre.

{{< highlight "java" >}}

 Value: 15

IsInSecondaryPlot: false

Value: 9

IsInSecondaryPlot: true

Value: 2

IsInSecondaryPlot: true

Value: 40

IsInSecondaryPlot: false

Value: 5

IsInSecondaryPlot: true

Value: 4

IsInSecondaryPlot: true

Value: 25

IsInSecondaryPlot: false

{{< /highlight >}}
