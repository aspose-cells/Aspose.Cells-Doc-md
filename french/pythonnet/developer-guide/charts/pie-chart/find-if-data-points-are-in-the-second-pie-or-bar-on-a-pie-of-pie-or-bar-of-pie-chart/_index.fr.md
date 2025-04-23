---
title: Trouver si les points de données sont dans le deuxième secteur ou barre d un diagramme de secteur ou barre de diagramme.
description: Apprenez comment utiliser Aspose.Cells pour Python via .NET pour déterminer si des points de données se trouvent dans le deuxième diagramme en secteurs ou dans la barre d’un graphique en secteurs de secteurs ou de barres. Notre guide montrera comment identifier et accéder au secteur ou à la barre secondaire dans un graphique composite, vous permettant d analyser et de manipuler efficacement les données.
keywords: Aspose.Cells pour Python via .NET, Graphique en secteurs de secteur, Graphique en secteurs de barre, Secteur secondaire, Barre secondaire, Analyse de données, Manipulation des données.
type: docs
weight: 180
url: /fr/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Scénarios d'utilisation possibles**
Vous pouvez déterminer si les points de données d'une série se trouvent dans le deuxième secteur d’un graphique *Pie of Pie* ou dans la barre d’un graphique *Bar of Pie* en utilisant Aspose.Cells pour Python via .NET. Veuillez utiliser la propriété [ChartPoint.is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot) pour le déterminer.

Veuillez télécharger le [fichier Excel d'exemple](5115193.xlsx) utilisé dans le code d'exemple suivant et consultez sa sortie console. Si vous ouvrez le [fichier Excel d'exemple](5115193.xlsx), vous constaterez que tous les points de données inférieurs à 10 se trouvent à l'intérieur de la barre du *Barre de diagramme circulaire* comme le montre également la sortie console.

## **Savoir si les points de données sont dans le deuxième diagramme circulaire ou dans une barre sur un diagramme de deux ou trois cercles ou sur un diagramme à barres de deux ou trois cercles**
Le code d'exemple suivant montre comment savoir si les points de données se trouvent dans le deuxième diagramme circulaire ou la barre sur un *Diagramme de secteurs secondaires* ou *Barre de diagramme circulaire*.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindDataPointsInPieBar.py" >}}
## **Sortie console**
Veuillez consulter la sortie console suivante générée après l'exécution du code d'exemple ci-dessus avec le [fichier Excel exemple](5115193.xlsx). Si [is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot/) est **faux**, le point de données est à l'intérieur du secteur, sinon il est dans la barre.



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
