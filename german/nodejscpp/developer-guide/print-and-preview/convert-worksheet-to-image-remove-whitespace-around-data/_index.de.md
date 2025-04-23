---
title: Arbeitsblatt in Bild umwandeln  Entfernen Sie Leerraum um Daten mit Node.js über C++
linktitle: Arbeitsblatt in Bild konvertieren  Leerraum um Daten entfernen
type: docs
weight: 40
url: /de/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Erfahren Sie, wie Sie Microsoft Excel Arbeitsblätter in Bilder umwandeln und Leerraum um die Daten mit Aspose.Cells for Node.js via C++ entfernen. 
---

{{% alert color="primary" %}}

Manchmal müssen Sie Arbeitsblattbilder in Anwendungen oder Webseiten präsentieren. Sie müssen beispielsweise Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder ein anderes Dokument einfügen. Im Grunde genommen möchten Sie ein Arbeitsblatt als Bild rendern, damit es in andere Anwendungen eingefügt werden kann. Aspose.Cells ermöglicht es Ihnen, Microsoft Excel-Arbeitsblätter in Bilder umzuwandeln.

{{% /alert %}}

## **Leerraum um Daten entfernen**

Die [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) API wandelt ein Arbeitsblatt in eine Bilddatei mit beliebigen festgelegten Attributen um, z. B. Imageformat, nach Seiten paginierte Blätter usw. Verschiedene Bildformate werden unterstützt, einschließlich BMP, GIF, JPG, TIFF und EMF.

Wenn Sie die Funktion Blatt-zu-Bild verwenden, hat das Ausgabebild standardmäßig Leerraum, d. h. einen Rand, um es herum. Dies können Sie entfernen, indem Sie die oberen, unteren, linken und rechten Seitenränder für das Ausgangsarbeitsblatt auf 0 setzen und die [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)-Attribute entsprechend festlegen.

Der folgende Codeausschnitt entfernt den Leerraum um die Daten im Ausgabebild.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
const options = new AsposeCells.LoadOptions();
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All));
// Specify your print area if you want
// sheet.getPageSetup().setPrintArea("A1:H8");

// To remove the white border around the image.
sheet.getPageSetup().setLeftMargin(0);
sheet.getPageSetup().setRightMargin(0);
sheet.getPageSetup().setBottomMargin(0);
sheet.getPageSetup().setTopMargin(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Emf);

// Set only one page would be rendered for the image
imgOptions.setOnePagePerSheet(true);
imgOptions.setPrintingPage(AsposeCells.PrintingPageType.IgnoreBlank);

// Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Convert the image
sr.toImage(0, path.join(outputDir, "outputRemoveWhitespaceAroundData.emf"));
```
