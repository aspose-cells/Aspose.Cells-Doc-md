---
title: Déterminez si les points de données se trouvent dans le deuxième secteur ou la deuxième barre d'un secteur ou d'une barre de diagramme circulaire
description: Découvrez comment utiliser Aspose.Cells for .NET pour déterminer si les points de données se trouvent dans le deuxième secteur ou la deuxième barre d'un secteur ou d'une barre d'un diagramme circulaire. Notre guide vous montrera comment identifier et accéder au secteur ou à la barre secondaire sur un graphique composite, vous permettant d'analyser et de manipuler efficacement les données.
keywords: Aspose.Cells for .NET, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.
type: docs
weight: 180
url: /fr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
##  **Scénarios d'utilisation possibles**
 Vous pouvez savoir si les points de données des séries se trouvent dans le deuxième secteur sur*Tarte à la tarte* graphique ou dans la barre de*Barre de tarte* graphique en utilisant le Aspose.Cells. Veuillez utiliser le[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)propriété pour la déterminer.

 Veuillez télécharger le[exemple de fichier Excel](5115193.xlsx)utilisé dans l’exemple de code suivant et consultez sa sortie de console. Si vous ouvrez le[exemple de fichier Excel](5115193.xlsx) , vous constaterez que tous les points de données inférieurs à 10 sont à l'intérieur de la barre de*Barre de tarte*graphique comme le montre également la sortie de la console.
##  **Déterminez si les points de données se trouvent dans le deuxième secteur ou la deuxième barre d'un secteur ou d'une barre de diagramme circulaire**
 L'exemple de code suivant montre comment déterminer si les points de données se trouvent dans le deuxième secteur ou barre d'un*Tarte à la tarte* ou*Barre de tarte*graphique.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
##  **Sortie console**
 Veuillez consulter la sortie de console suivante générée après l'exécution de l'exemple de code ci-dessus avec le[exemple de fichier Excel](5115193.xlsx) . Si[IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)est *faux**, le point de données est à l'intérieur du secteur ou s'il est *vrai**, alors le point de données est à l'intérieur de la barre.



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
