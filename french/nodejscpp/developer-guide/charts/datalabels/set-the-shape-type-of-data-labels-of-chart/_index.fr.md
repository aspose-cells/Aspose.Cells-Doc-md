---
title: Définir le type de forme des étiquettes de données du graphique avec Node.js via C++
linktitle: Définir le type de forme des étiquettes de données du graphique
description: Apprenez comment définir le type de forme des étiquettes de données dans les graphiques en utilisant Aspose.Cells for Node.js via C++. Ce guide expliquera les différents types de formes disponibles et vous montrera comment choisir la forme appropriée pour vos étiquettes de données afin d améliorer la présentation et l utilisabilité.
keywords: Aspose.Cells for Node.js via C++, programmation de graphiques, étiquettes de données, types de formes, présentation, utilisabilité.
type: docs
weight: 110
url: /fr/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Scénarios d'utilisation possibles**
Vous pouvez changer le type de forme des étiquettes de données du graphique en utilisant la propriété `DataLabels.shapeType`. Elle accepte la valeur de l'énumération `DataLabelShapeType` et modifie le type de forme des étiquettes de données en conséquence. Certains de ses valeurs sont

{{< highlight javascript >}}
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
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetShapeTypeOfDataLabelsOfChart.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Access first series
const series = chart.getNSeries().get(0);

// Set the shape type of data labels i.e. Speech Bubble Oval
series.getDataLabels().setShapeType(AsposeCells.DataLabelShapeType.WedgeEllipseCallout);

// Save the output Excel file
workbook.save(path.join(dataDir, "outputSetShapeTypeOfDataLabelsOfChart.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
