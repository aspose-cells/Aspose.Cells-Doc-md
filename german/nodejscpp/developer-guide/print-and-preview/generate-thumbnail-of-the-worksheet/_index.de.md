---
title: Thumbnail des Arbeitsblatts mit Node.js via C++ generieren
linktitle: Thumbnail des Arbeitsblatts generieren
type: docs
weight: 110
url: /de/nodejs-cpp/generate-thumbnail-of-the-worksheet/
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ ein Thumbnail Bild eines Arbeitsblatts erstellen. Kleine Bilder für Vorschauen in Dokumenten und Präsentationen.
---

{{% alert color="primary" %}} 

Es kann nützlich sein, Miniaturansichten aus Arbeitsblättern zu generieren. Eine Miniaturansicht ist ein kleines Bild, das in ein Word-Dokument oder eine PowerPoint-Präsentation eingefügt werden kann, um eine Vorschau dessen zu geben, was sich auf dem Arbeitsblatt befindet. Sie kann einer Webseite mit einem Link zum Download des Originaldokuments hinzugefügt werden und hat viele weitere Verwendungsmöglichkeiten.

{{% /alert %}} 

Aspose.Cells for Node.js via C++ ermöglicht das Ausgeben von Arbeitsblättern in Bilddateien, wodurch das Erstellen eines Thumbnails einfach ist. Der folgende Beispielcode zeigt, wie Sie Arbeitsblätter in Bilddateien ausgeben.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate and open an Excel file
const filePath = path.join(sourceDir, "sampleGenerateThumbnailOfWorksheet.xlsx");
const book = new AsposeCells.Workbook(filePath);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Set the vertical and horizontal resolution
imgOptions.setVerticalResolution(200);
imgOptions.setHorizontalResolution(200);

// One page per sheet is enabled
imgOptions.setOnePagePerSheet(true);

// Set desired thumbnail dimensions
imgOptions.setDesiredSize(600, 600, true);

// Get the first worksheet
const sheet = book.getWorksheets().get(0);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the thumbnail directly
sr.toImage(0, path.join(outputDir, "outputGenerateThumbnailOfWorksheet.jpg"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
