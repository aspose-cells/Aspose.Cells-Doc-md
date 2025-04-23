---  
title: Arbeitsblatt mit ImageOrPrint Optionen in Node.js über C++ in ein Bild umwandeln  
linktitle: Arbeitsblatt in Bild mithilfe von Bild oder Druckoptionen konvertieren  
type: docs  
weight: 90  
url: /de/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/  
description: Erfahren Sie, wie Sie ein Arbeitsblatt in eine Bilddatei umwandeln und verschiedene Bild und Druckoptionen mit Aspose.Cells for Node.js via C++ anwenden.   
---  

{{% alert color="primary" %}}  
Dieses Dokument ist darauf ausgelegt, ein detailliertes Verständnis dafür zu vermitteln, wie man ein Arbeitsblatt in eine Bilddatei konvertiert und verschiedene Bilddruckoptionen für das Bild anwendet, Optionen wie Auflösung, TIFF-Komprimierung, Bildformat und Seitenqualität.  
{{% /alert %}}  

## **Arbeitsblätter als Bilder speichern - Unterschiedliche Ansätze**  

Manchmal müssen Sie Ihre Arbeitsblätter als bildliche Darstellung präsentieren. Möglicherweise müssen Sie die Arbeitsblattbilder in Ihre Anwendungen oder Webseiten einfügen. Sie müssen möglicherweise die Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Sie möchten einfach ein Arbeitsblatt als Bild gerendert haben, um es anderswo verwenden zu können. Aspose.Cells unterstützt die Konvertierung von Arbeitsblättern in Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells das Festlegen unterschiedlicher Optionen wie Bildformat, Auflösung (sowohl vertikal als auch horizontal), Bildqualität und weitere Bild- und Druckoptionen.  

Sie könnten Office Automation versuchen, aber Office Automation hat seine eigenen Nachteile. Es gibt mehrere Gründe und Probleme: z.B. Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, wobei der wichtigste ist, dass Microsoft selber dringend von Office-Automatisierung von Softwarelösungen abrät.  

Dieser Artikel zeigt, wie man eine Konsolenanwendung in Visual Studio .NET erstellt, die Konvertierung eines Arbeitsblatts in ein Bild mithilfe verschiedener Bild- und Druckoptionen mit wenigen und einfachsten Codezeilen mithilfe der Aspose.Cells-API durchführt.  

Die Klasse [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) repräsentiert ein Arbeitsblatt zur Darstellung von Bildern für das Arbeitsblatt. Sie hat eine überladene [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)-Methode, die ein Arbeitsblatt direkt in Bilddatei(en) mit gewünschten Attributen oder Optionen konvertieren kann. Sie kann ein Objekt zurückgeben, auf das Sie eine Bilddatei auf der Festplatte/Stream speichern können. Es werden mehrere Bildformate unterstützt, z.B. BMP, PNG, GIFF, JPEG, TIFF, EMF und so weiter.  

## **Verwenden von Aspose.Cells zur Konvertierung von Arbeitsblättern in Bilder unter Verwendung von Bild- oder Druckoptionen.**  

### **Erstellen einer Vorlagenarbeitsmappe in Microsoft Excel**  

Ich habe eine neue Arbeitsmappe in MS Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt. Jetzt werde ich das Arbeitsblatt der Vorlagendatei "Sheet1" in eine Bilddatei "SheetImage.tiff" konvertieren und verschiedene Bilddateiloptionen wie horizontale und vertikale Auflösungen, Tiff-Kompression usw. anwenden.  

### **Aspose.Cells herunterladen und installieren**  

Zuerst müssen Sie [herunterladen](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++. Installieren Sie es auf Ihrem Entwicklungskomputer. Alle [Aspose](http://www.aspose.com/) Komponenten funktionieren beim Installieren im Evaluierungsmodus. Der Evaluierungsmodus hat keine Zeitbegrenzung und fügt nur Wasserzeichen in die erstellten Dokumente ein.  

### **Ein Projekt erstellen**  

Starten Sie Ihre bevorzugte Entwicklungsumgebung (z.B. Visual Studio). Erstellen Sie eine neue Konsolenanwendung.  

### **Referenzen hinzufügen**  

Dieses Projekt verwendet Aspose.Cells. Daher müssen Sie in Ihrem Projekt einen Verweis auf die Aspose.Cells-Komponente hinzufügen. Zum Beispiel fügen Sie einen Verweis auf …\Program Files\Aspose\Aspose.Cells for Node.js via C++\Bin\Aspose.Cells.node hinzu.  

### **Arbeitsblatt in eine Bilddatei konvertieren**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Open template
const filePath = path.join(sourceDir, "sampleWorksheetToAnImage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Apply different Image and Print options
const options = new AsposeCells.ImageOrPrintOptions(); // Corrected: Added the instantiation for ImageOrPrintOptions.

// Set Horizontal Resolution
options.setHorizontalResolution(300);

// Set Vertical Resolution
options.setVerticalResolution(300);

// Set TiffCompression
options.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

// Set Image Format
options.setImageType(AsposeCells.ImageType.Tiff);

// Set printing page type
options.setPrintingPage(AsposeCells.PrintingPageType.Default);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, options);

// Render/save the image for the sheet
const pageIndex = 3;
sr.toImage(pageIndex, path.join(outputDir, `outputWorksheetToAnImage_${pageIndex + 1}.tiff`));
```  

## **Konversionsoptionen**  

Es ist möglich, bestimmte Seiten als Bild zu speichern. Der folgende Code konvertiert die ersten und zweiten Arbeitsblätter in einer Arbeitsmappe in JPG-Bilder.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleSpecificPagesToImages.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Specify page index to be rendered
const idxPage = 3;

// Render the third image for the sheet
const bitmap = sr.toImage(idxPage);

// Save the image file
const fs = require("fs");
fs.writeFileSync(path.join(outputDir, `outputSpecificPagesToImage_${idxPage + 1}.jpg`), bitmap);
```  

## **Bildkonvertierung mit WorkbookRender**  

Ein TIFF-Bild kann mehr als einen Frame enthalten. Sie können das gesamte Arbeitsbuch in ein einziges TIFF-Bild mit mehreren Frames oder Seiten speichern:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Tiff);

const workbookRender = new AsposeCells.WorkbookRender(workbook, opts);
workbookRender.toImage(path.join(outputDir, "outputUseWorkbookRenderForImageConversion.tiff"));
```  


