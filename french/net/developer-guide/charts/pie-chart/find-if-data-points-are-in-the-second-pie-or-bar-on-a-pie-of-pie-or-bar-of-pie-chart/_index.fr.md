---
title: Trouver si les points de données sont dans le deuxième secteur ou barre d un diagramme de secteur ou barre de diagramme.
description: Apprenez comment utiliser Aspose.Cells for .NET pour savoir si les points de données se trouvent dans le deuxième diagramme circulaire ou la deuxième barre sur un diagramme de secteur ou barre de diagramme. Notre guide vous démontrera comment identifier et accéder au diagramme circulaire ou à la barre secondaire sur un graphique composite, vous permettant d analyser et de manipuler efficacement les données.
keywords: Aspose.Cells for .NET, Diagramme de secteurs secondaires, Barre de diagramme circulaire, Diagramme circulaire secondaire, Barre secondaire, Analyse des données, Manipulation des données.
type: docs
weight: 180
url: /fr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Scénarios d'utilisation possibles**
Vous pouvez savoir si les points de données d'une série se trouvent dans le deuxième diagramme circulaire sur un *Diagramme de secteurs secondaires* ou dans la barre du *Barre de diagramme circulaire* en utilisant Aspose.Cells. Veuillez utiliser la propriété [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) pour le déterminer.

Veuillez télécharger le [fichier Excel d'exemple](5115193.xlsx) utilisé dans le code d'exemple suivant et consultez sa sortie console. Si vous ouvrez le [fichier Excel d'exemple](5115193.xlsx), vous constaterez que tous les points de données inférieurs à 10 se trouvent à l'intérieur de la barre du *Barre de diagramme circulaire* comme le montre également la sortie console.
## **Savoir si les points de données sont dans le deuxième diagramme circulaire ou dans une barre sur un diagramme de deux ou trois cercles ou sur un diagramme à barres de deux ou trois cercles**
Le code d'exemple suivant montre comment savoir si les points de données se trouvent dans le deuxième diagramme circulaire ou la barre sur un *Diagramme de secteurs secondaires* ou *Barre de diagramme circulaire*.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **Sortie console**
Veuillez consulter la sortie de la console suivante générée après l'exécution du code d'exemple ci-dessus avec le [fichier Excel d'exemple](5115193.xlsx). Si [IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) est **false**, le point de données est à l'intérieur du secteur ou s'il est **true**, alors le point de données est à l'intérieur de la barre.



{{< highlight java >}}

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
