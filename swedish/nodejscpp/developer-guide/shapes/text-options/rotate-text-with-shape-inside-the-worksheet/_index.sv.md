---
title: Rotera Text med Form inuti Arket med Node.js via C++
linktitle: Rotera text med Shape i kalkylbladet
type: docs
weight: 1300
url: /sv/nodejs-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Lär dig hur man roterar text med form inuti ett Excel ark med Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**

Du kan lägga till text inuti vilken form som helst med Microsoft Excel. Om du lägger till en form med den mycket gamla Microsoft Excel 2003 kommer texten inte att rotera med formen. Men om du lägger till en form med nyare versioner av Microsoft Excel t.ex. 2007, 2010, 2013 eller 2016, etc. så roterar texten med formen. Du kan styra om texten ska rotera med formen eller inte med hjälp av [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) egenskapen. Värdet för standard är **true** vilket innebär att texten roterar med formen, men om du sätter det till **false**, roterar inte texten med formen.

## **Rotera text med Shape i kalkylbladet**

Följande exempel laddar den [exempel-Excelfilen](64716896.xlsx) som har en triangel och dess text roterar med formen. Om du öppnar exempel-Excelfilen i Microsoft Excel och roterar triangelns form, kommer texten också att rotera med den. Koden sätter sedan [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) egenskapen till **false** och sparar det som [utdata Excel-fil](64716897.xlsx). Om du nu öppnar den utgångna Excel-filen i Microsoft Excel och roterar triangelns form, roterar inte texten längre med den. Se skärmbilden nedan för att visa kodens effekt på exempel-Excelfilen som referens.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Exempelkod**

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
