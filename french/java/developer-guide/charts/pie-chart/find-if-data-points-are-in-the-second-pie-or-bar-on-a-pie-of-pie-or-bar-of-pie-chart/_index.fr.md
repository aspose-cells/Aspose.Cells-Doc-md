---
title: Trouver si les points de données sont dans le deuxième secteur ou barre d un diagramme de secteur ou barre de diagramme.
type: docs
weight: 910
url: /fr/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Scénarios d'utilisation possibles**
Vous pouvez déterminer si les points de données de la série se trouvent dans le deuxième diagramme circulaire sur un graphique *Diagramme circulaire de cercles* ou dans la barre du *Diagramme à barres de cercles* en utilisant Aspose.Cells. Veuillez utiliser la propriété [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) pour le déterminer.

Veuillez télécharger le [fichier Excel d'exemple](5473373.xlsx) utilisé dans le code d'exemple suivant et voir sa sortie console. Si vous ouvrez le [fichier Excel d'exemple](5473373.xlsx), vous trouverez que tous les points de données inférieurs à 10 se trouvent à l'intérieur de la barre du *Diagramme à barres de cercles*, comme le montre également la sortie de la console.
## **Savoir si les points de données sont dans le deuxième diagramme circulaire ou dans une barre sur un diagramme de deux ou trois cercles ou sur un diagramme à barres de deux ou trois cercles**
Le code d'exemple suivant montre comment savoir si les points de données se trouvent dans le deuxième diagramme circulaire ou la barre sur un *Diagramme de secteurs secondaires* ou *Barre de diagramme circulaire*.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **Sortie console**
Veuillez consulter la sortie de la console suivante générée après l'exécution du code d'exemple ci-dessus avec le [fichier Excel d'exemple](5473373.xlsx). Si [IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) est **false**, le point de données se trouve à l'intérieur du diagramme circulaire, ou s'il est **true**, alors le point de données se trouve à l'intérieur de la barre.

{{< highlight java >}}

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
