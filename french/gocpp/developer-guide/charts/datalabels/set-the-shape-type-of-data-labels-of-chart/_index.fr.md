---
title: Définir le type de forme des étiquettes de données du graphique avec Golang via C++
linktitle: Définir le type de forme des étiquettes de données du graphique
description: Apprenez comment définir le type de forme des étiquettes de données dans les graphiques en utilisant Aspose.Cells for C++. Notre guide expliquera les différents types de formes disponibles et vous montrera comment choisir la forme appropriée pour vos étiquettes de données afin d améliorer la présentation et la convivialité de vos graphiques.
keywords: Aspose.Cells for C++, création de graphiques, étiquettes de données, types de formes, présentation, convivialité.
type: docs
weight: 110
url: /fr/go-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Scénarios d'utilisation possibles**
Vous pouvez changer le type de forme des étiquettes de données du graphique en utilisant la propriété `DataLabels.ShapeType`. Elle prend la valeur de l’énumération `DataLabelShapeType` et modifie le type de forme des étiquettes de données en conséquence. Certaines de ses valeurs sont :

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **Définir le type de forme des étiquettes de données du graphique**
Le code d'exemple suivant change le type de forme des étiquettes de données du graphique en `DataLabelShapeType.WedgeEllipseCallout`. Consultez le fichier Excel d'exemple ([fichier.xlsx](60489778.xlsx)) utilisé dans ce code et le fichier Excel de sortie ([fichier.xlsx](60489779.xlsx)) généré par celui-ci. La capture d'écran montre l'effet du code sur le fichier Excel d'exemple. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Code d'exemple**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetTheShapeTypeOfDataLabelsOfChart.go" >}}
