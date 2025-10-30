---  
title: Arbeitsblatt oder Diagramm in ein Bild mit gewünschter Breite und Höhe exportieren via Node.js  
linktitle: Arbeitsblatt oder Diagramm in ein Bild mit gewünschter Breite und Höhe exportieren  
type: docs  
weight: 290  
url: /de/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/  
description: Erfahren Sie, wie Sie ein Arbeitsblatt oder Diagramm mit Aspose.Cells for Node.js via C++ in ein Bild mit festgelegter Breite und Höhe exportieren.  
---  

{{% alert color="primary" %}}  
Sie können Aspose.Cells for Node.js via C++ verwenden, um Ihr Arbeitsblatt oder Diagramm in ein Bild mit gewünschter Breite und Höhe zu exportieren. Es bietet die [**ImageOrPrintOptions.setDesiredSize(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#setDesiredSize-number-number-boolean-)-Methode, um die gewünschte Breite und Höhe des exportierten Bildes festzulegen. Die Breite und Höhe sind in Pixeln angegeben.  
{{% /alert %}}  

Der folgende Code exportiert das Arbeitsblatt in ein Bild mit der Größe 400x400.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const filePath = path.join(sourceDir, "sampleWorksheetToImageDesiredSize.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set image or print options we want one page per sheet. The image format is in png and desired dimensions are 400x400
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);
opts.setDesiredSize(400, 400, false);

// Render sheet into image
const sr = new AsposeCells.SheetRender(worksheet, opts);
sr.toImage(0, path.join(outputDir, "outputWorksheetToImageDesiredSize.png"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
