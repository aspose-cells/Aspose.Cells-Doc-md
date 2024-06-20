---
title: Définir le type de forme des étiquettes de données du graphique
type: docs
weight: 70
url: /fr/java/set-the-shape-type-of-data-labels-of-chart/
---

## **Scénarios d'utilisation possibles**

Vous pouvez changer le type de forme des étiquettes de données du graphique en utilisant la propriété [**DataLabels.ShapeType**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShapeType). Elle prend la valeur de l'énumération [**DataLabelShapeType**](https://reference.aspose.com/cells/java/com.aspose.cells/DataLabelShapeType) et modifie en conséquence le type de forme des étiquettes de données. Certaines de ses valeurs sont

{{< highlight java >}}

DataLabelShapeType.BENT_LINE_CALLOUT

DataLabelShapeType.DOWN_ARROW_CALLOUT

DataLabelShapeType.ELLIPSE

DataLabelShapeType.LINE_CALLOUT

DataLabelShapeType.RECT

etc.

{{< /highlight >}}

## **Définir le type de forme des étiquettes de données du graphique**

Le code d'exemple suivant change le type de forme des étiquettes de données du graphique en [**DataLabelShapeType.WEDGE_ELLIPSE_CALLOUT**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabelshapetype#WEDGE_ELLIPSE_CALLOUT). Veuillez consulter le fichier Excel d'exemple (60489794.xlsx) utilisé dans ce code et le fichier Excel de sortie (60489793.xlsx) généré par celui-ci. La capture d'écran montre l'effet du code sur le fichier Excel d'exemple.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-SetShapeTypeOfDataLabelsOfChart.java" >}}
