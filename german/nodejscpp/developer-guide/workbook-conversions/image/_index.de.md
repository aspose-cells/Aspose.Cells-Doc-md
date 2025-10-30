---  
title: Bild mit Node.js via C++  
linktitle: Bild  
type: docs  
weight: 300  
url: /de/nodejs-cpp/convert-excel-to-image/  
---  

{{% alert color="primary" %}}  
Aspose.Cells ermöglicht es Ihnen, ein Arbeitsblatt aus der Arbeitsmappe zu exportieren und in verschiedene Formate zu konvertieren. Dieser Artikel erklärt, wie man ein Arbeitsblatt in verschiedene Formate konvertiert.  
{{% /alert %}}  

## Arbeitsmappe in TIFF konvertieren  

Eine Excel-Datei kann mehrere Tabellenblätter mit mehreren Seiten enthalten. [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender) ermöglicht die Konvertierung von Excel nach TIFF mit mehreren Seiten. Außerdem können Sie mehrere Optionen für TIFF steuern, wie [ImageOrPrintOptions.getTiffCompression()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffCompression--), [ImageOrPrintOptions.getTiffColorDepth()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffColorDepth--), Auflösung([ImageOrPrintOptions.getHorizontalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--), [ImageOrPrintOptions.getVerticalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)).  

Der folgende Code zeigt, wie Excel in TIFF mit mehreren Seiten konvertiert wird. Die [Quell-Excel-Datei](workbook-to-tiff-with-mulitiple-pages.xlsx) und das generierte TIFF-Bild (workbook-to-tiff-with-mulitiple-pages.tiff) sind als Referenz angehängt.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "workbook-to-tiff-with-mulitiple-pages.xlsx");

// Load the workbook
const wb = new AsposeCells.Workbook(filePath);

const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Tiff);

// Set resolution to 200
imgOptions.setHorizontalResolution(200);
imgOptions.setVerticalResolution(200);

// Set TIFF compression to LZW
imgOptions.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

const workbookRender = new AsposeCells.WorkbookRender(wb, imgOptions);
workbookRender.toImage("workbook-to-tiff-with-mulitiple-pages.tiff");
```  

## **Arbeitsblatt in Bild konvertieren**  

Arbeitsblätter enthalten Daten, die Sie analysieren möchten. Zum Beispiel kann ein Arbeitsblatt Parameter, Summen, Prozentsätze, Ausnahmen und Berechnungen enthalten.  

Als Entwickler müssen Sie möglicherweise Arbeitsblätter als Bilder präsentieren. Möglicherweise müssen Sie beispielsweise ein Bild eines Arbeitsblatts in einer Anwendung oder auf einer Webseite verwenden. Sie möchten möglicherweise ein Bild in ein Microsoft Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder einen anderen Dokumententyp einfügen. Kurz gesagt, Sie möchten ein Arbeitsblatt als Bild gerendert haben, damit Sie es an anderer Stelle verwenden können.  

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender)

Die [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender)-Klasse repräsentiert ein Arbeitsblatt, das als Bilder gerendert werden soll. Sie hat eine überladene Methode, [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-string-), die ein Arbeitsblatt in Bilddateien mit unterschiedlichen Attributen oder Optionen umwandeln kann. Sie gibt ein Buffer-Objekt zurück und Sie können eine Bilddatei auf der Festplatte speichern oder streamen. Mehrere Bildformate werden unterstützt, zum Beispiel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.  

Der folgende Codeausschnitt zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine Bilddatei konvertiert.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
let path = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
sr.toImage(j, path);
}
```  

{{% alert color="primary" %}}  
Zum jetzigen Zeitpunkt unterstützt die API zur Konvertierung von Arbeitsblättern in Bilder keine 3D-Bubble-Diagramme.  
{{% /alert %}}  

## **Arbeitsblatt in SVG konvertieren**  

SVG steht für Skalierbare Vektorgrafiken. SVG ist eine Spezifikation auf der Grundlage von XML-Standards für zweidimensionale Vektorgrafiken. Es ist ein offener Standard, der vom World Wide Web Consortium (W3C) seit 1999 entwickelt wird.  

Aspose.Cells for Node.js via C++ konnte Arbeitsblätter seit Version 7.1.0 in SVG-Bilder konvertieren. Das folgende Code-Snippet zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei umwandelt.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Put sample text in the first cell of the first worksheet in the newly created workbook
workbook.getWorksheets().get(0).getCells().get("A1").putValue("DEMO TEXT ON SHEET1");

// Add second worksheet in the workbook
workbook.getWorksheets().add(AsposeCells.SheetType.Worksheet);

// Set text in the first cell of the second sheet
workbook.getWorksheets().get(1).getCells().get("A1").putValue("DEMO TEXT ON SHEET2");

// Set currently active sheet index to 1 i.e. Sheet2
workbook.getWorksheets().setActiveSheetIndex(1);

// Save workbook to SVG. It shall render the active sheet only to SVG
workbook.save(path.join(outputDir, "ConvertWorksheetToSVG_out.svg"));
```  

## **Erweiterte Themen**  
- [Konvertieren Sie ein Excel-Diagramm in ein Bild](/cells/de/nodejs-cpp/convert-an-excel-chart-to-image/)  
- [Konvertieren eines Diagramms in ein Bild im SVG-Format](/cells/de/nodejs-cpp/converting-chart-to-image-in-svg-format/)  
- [Diagramm in SVG mit viewBox-Attribut exportieren](/cells/de/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [Konvertierungsvorgang von Excel nach TIFF verfolgen](/cells/de/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
