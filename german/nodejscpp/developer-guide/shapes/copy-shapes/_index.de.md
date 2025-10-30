---
title: Zeichnungen zwischen Arbeitsblättern mit Node.js via C++ kopieren
linktitle: Formen kopieren
type: docs
weight: 200
url: /de/nodejs-cpp/copy-shapes-between-worksheets/
description: Erfahren Sie, wie Sie Formen wie Bilder und Diagramme zwischen Arbeitsblättern mit Aspose.Cells for Node.js via C++ kopieren.
---

{{% alert color="primary" %}}

Manchmal müssen Sie Elemente auf einem Arbeitsblatt, z.B. Bilder, Diagramme und andere Zeichenobjekte, zwischen Arbeitsblättern kopieren. Aspose.Cells for Node.js via C++ unterstützt diese Funktion. Diagramme, Bilder und andere Objekte können mit höchster Präzision kopiert werden.

Dieser Artikel vermittelt Ihnen ein umfassendes Verständnis dafür, wie Formen zwischen Arbeitsblättern kopiert werden.

{{% /alert %}}

## **Kopieren eines Bildes von einem Arbeitsblatt auf ein anderes**

Um ein Bild von einem Arbeitsblatt auf ein anderes zu kopieren, verwenden Sie die Methode [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-), wie im folgenden Beispielcode gezeigt.

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

## **Kopieren Sie ein Diagramm von einem Arbeitsblatt auf ein anderes**

Der folgende Code demonstriert die Verwendung der Methode [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addCopy-shape-number-number-number-number-) zum Kopieren eines Diagramms von einem Arbeitsblatt auf ein anderes.

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

## **Kopieren von Steuerelementen und anderen Zeichenobjekten von einem Arbeitsblatt auf ein anderes**

Um Steuerelemente und andere Zeichenobjekte zu kopieren, verwenden Sie die [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addCopy-shape-number-number-number-number-)-Methode wie im untenstehenden Beispiel gezeigt.

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
