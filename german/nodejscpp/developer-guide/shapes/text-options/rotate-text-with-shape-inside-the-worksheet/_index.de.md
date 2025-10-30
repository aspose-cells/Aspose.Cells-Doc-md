---
title: Text mit Shape innerhalb des Arbeitsblatts mit Node.js über C++ drehen
linktitle: Text mit Shape innerhalb des Arbeitsblatts drehen
type: docs
weight: 1300
url: /de/nodejs-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Lernen Sie, wie man Text mit Shape innerhalb eines Excel Arbeitsblatts mit Aspose.Cells for Node.js via C++ dreht.
---

## **Mögliche Verwendungsszenarien**

Sie können Text in jede Form mit Microsoft Excel einfügen. Wenn Sie eine Form mit sehr altem Microsoft Excel 2003 hinzufügen, wird der Text nicht mit der Form rotieren. Wenn Sie jedoch eine Form mit neueren Versionen von Microsoft Excel hinzufügen, z.B. 2007, 2010, 2013 oder 2016, dreht sich der Text mit der Form. Sie können steuern, ob der Text mit der Form rotieren soll oder nicht, indem Sie die [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--)-Eigenschaft verwenden. Der Standardwert davon ist **true**, was bedeutet, dass sich der Text mit der Form dreht. Wenn Sie es auf **false** setzen, dreht sich der Text nicht mit der Form.

## **Text mit Form im Arbeitsblatt drehen**

Das folgende Beispiel lädt die [Beispieldatei Excel](64716896.xlsx), die eine Dreiecksform enthält, und deren Text sich mit der Form dreht. Wenn Sie die Beispiel-Excel-Datei in Microsoft Excel öffnen und die Dreiecksform drehen, wird sich auch der Text mitdrehen. Der Code setzt dann die [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--)-Eigenschaft auf **false** und speichert die Datei als [Ausgabe-Excel](64716897.xlsx). Wenn Sie jetzt die Ausgabedatei in Microsoft Excel öffnen und die Dreiecksform drehen, dreht sich der Text nicht mehr mit. Bitte sehen Sie sich den folgenden Screenshot an, der die Wirkung des Codes auf die Beispiel-Excel-Datei zeigt.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleRotateTextWithShapeInsideWorksheet.xlsx");

// Load sample Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access cell B4 and add message inside it.
const cellB4 = worksheet.getCells().get("B4");
cellB4.putValue("Text is not rotating with shape because RotateTextWithShape is false.");

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Access shape text alignment.
const shapeTextAlignment = shape.getTextBody().getTextAlignment();

// Do not rotate text with shape by setting RotateTextWithShape as false.
shapeTextAlignment.setRotateTextWithShape(false);

// Save the output Excel file.
const outputFilePath = path.join(dataDir, "outputRotateTextWithShapeInsideWorksheet.xlsx");
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
