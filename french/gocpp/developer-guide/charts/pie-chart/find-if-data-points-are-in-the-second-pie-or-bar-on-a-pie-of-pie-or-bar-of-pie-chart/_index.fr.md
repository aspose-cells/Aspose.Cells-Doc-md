---
title: Vérifiez si les points de données se trouvent dans le deuxième graphique circulaire ou graphique à barres dans un graphique Pie of Pie ou Bar of Pie avec Golang via C++
linktitle: Trouver si les points de données sont dans le deuxième secteur ou barre d un diagramme de secteur ou barre de diagramme.
description: Apprenez comment utiliser Aspose.Cells for C++ pour déterminer si les points de données se trouvent dans la deuxième section ou la barre sur un graphique en secteurs ou en barres de secteur. Notre guide montrera comment identifier et accéder à la seconde section ou barre d’un graphique composite, vous permettant d’analyser et de manipuler efficacement les données.
keywords: Aspose.Cells for C++, Graphique en secteurs, Barres de secteur, Secteur secondaire, Barre secondaire, Analyse de données, Manipulation des données.
type: docs
weight: 180
url: /fr/go-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Scénarios d'utilisation possibles**
Vous pouvez déterminer si les points de données de la série sont dans le deuxième diagramme circulaire sur un graphique *Pie of Pie* ou dans la barre d’un graphique *Bar of Pie* en utilisant Aspose.Cells. Veuillez utiliser la propriété [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/go-cpp/chartpoint/isinsecondaryplot/) pour le vérifier.

Veuillez télécharger le [fichier Excel d'exemple](5115193.xlsx) utilisé dans le code d'exemple suivant et consultez sa sortie console. Si vous ouvrez le [fichier Excel d'exemple](5115193.xlsx), vous constaterez que tous les points de données inférieurs à 10 se trouvent à l'intérieur de la barre du *Barre de diagramme circulaire* comme le montre également la sortie console.

## **Savoir si les points de données sont dans le deuxième diagramme circulaire ou dans une barre sur un diagramme de deux ou trois cercles ou sur un diagramme à barres de deux ou trois cercles**
Le code d'exemple suivant montre comment savoir si les points de données se trouvent dans le deuxième diagramme circulaire ou la barre sur un *Diagramme de secteurs secondaires* ou *Barre de diagramme circulaire*.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfDataPointsAreInTheSecondPieOrBarOnAPieOfPieOrBarOfPieChart.go" >}}
## **Sortie console**
Veuillez voir la sortie console suivante générée après l'exécution du code d'exemple ci-dessus avec le [fichier Excel d'exemple](5115193.xlsx). Si [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) est **faux**, le point de données se trouve dans le secteur ou, s'il est **vrai**, alors le point de données se trouve dans la barre.

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
