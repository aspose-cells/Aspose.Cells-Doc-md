---
title: Copier des formes entre feuilles avec Node.js via C++
linktitle: Copier les formes
type: docs
weight: 200
url: /fr/nodejs-cpp/copy-shapes-between-worksheets/
description: Apprenez comment copier des formes telles que des images et des graphiques entre feuilles en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Parfois, vous devez copier des éléments sur une feuille de calcul, comme des images, des graphiques et d'autres objets de dessin, entre feuilles. Aspose.Cells for Node.js via C++ prend en charge cette fonction. Les graphiques, images et autres objets peuvent être copiés avec la plus haute précision.

Cet article vous donne une compréhension détaillée de comment copier des formes entre les feuilles de calcul.

{{% /alert %}}

## **Copier une image d'une feuille de calcul à une autre**

Pour copier une image d'une feuille de calcul à une autre, utilisez la méthode [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) comme indiqué dans le code exemple ci-dessous.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_picture.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the Picture from the "Picture" worksheet.
const picturesource = workbook.getWorksheets().get("Picture").getPictures().get(0);

// Save Picture to Memory Stream
const ms = picturesource.getData();

// Copy the picture to the Result Worksheet
workbook.getWorksheets().get("Result").getPictures().add(picturesource.getUpperLeftRow(), picturesource.getUpperLeftColumn(), ms, picturesource.getWidthScale(), picturesource.getHeightScale());

// Save the Worksheet
workbook.save(path.join(dataDir, "PictureCopied_out.xlsx"));
```

## **Copier un graphique d'une feuille de calcul à une autre**

Le code suivant démontre l'utilisation de la méthode [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addCopy-shape-number-number-number-number-) pour copier un graphique d'une feuille de calcul à une autre.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_chart.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the Chart from the "Chart" worksheet.
const chartsource = workbook.getWorksheets().get("Chart").getCharts().get(0);
const cshape = chartsource.getChartObject();

// Copy the Chart to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(cshape, 20, 0, 2, 0);

// Save the Worksheet
workbook.save(path.join(dataDir, "ChartCopied_out.xlsx"));
```

## **Copier les contrôles et autres objets de dessin d'une feuille de calcul à une autre**

Pour copier les contrôles et autres objets de dessin, utilisez la méthode [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addCopy-shape-number-number-number-number-) comme indiqué dans l'exemple ci-dessous.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_control.xlsx");
// Open the template file
const workbook = new AsposeCells.Workbook(filePath);

// Get the Shapes from the "Control" worksheet.
const shape = workbook.getWorksheets().get("Control").getShapes();

// Copy the Textbox to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(shape.get(0), 5, 0, 2, 0);

// Copy the Oval Shape to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(shape.get(1), 10, 0, 2, 0);

// Save the Worksheet
workbook.save(path.join(dataDir, "ControlsCopied_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
