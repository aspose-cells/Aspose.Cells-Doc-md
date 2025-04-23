---  
title: Dokument , Arbeitsblatt und Arbeitsmappen Eigenschaften bei Excel zu HTML Konvertierung mit Node.js über C++ exportieren  
linktitle: Dokumentarbeitsmappen und Arbeitsblatteigenschaften beim Konvertieren von Excel in HTML exportieren  
type: docs  
weight: 50  
url: /de/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/  
description: Lernen Sie, wie Sie Dokument , Arbeitsmappen und Arbeitsblatt Eigenschaften bei Excel in HTML mit Aspose.Cells for Node.js via C++ exportieren.  
---  

## **Mögliche Verwendungsszenarien**  

Wenn eine Microsoft Excel-Datei mit Microsoft Excel oder Aspose.Cells for Node.js via C++ in HTML exportiert wird, werden verschiedene Arten von Dokument-, Arbeitsmappen- und Arbeitsblatt-Eigenschaften exportiert, wie im folgenden Screenshot gezeigt. Um diese Eigenschaften beim Export zu vermeiden, setzen Sie [**HtmlSaveOptions.getExportDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportDocumentProperties--), [**HtmlSaveOptions.getExportWorkbookProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorkbookProperties--) und [**HtmlSaveOptions.getExportWorksheetProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetProperties--) auf **false**. Der Standardwert dieser Eigenschaften ist **true**. Das folgende Bild zeigt, wie diese Eigenschaften im exportierten HTML aussehen.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Dokument-, Arbeitsmappen- und Arbeitsblatteigenschaften beim Konvertieren von Excel in HTML exportieren**  

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767776.xlsx) und konvertiert sie in HTML, ohne die Dokument-, Arbeitsmappen- und Arbeitsblatt-Eigenschaften im [Ausgabe-HTML](61767779.zip) zu exportieren.  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// We do not want to export document, workbook and worksheet properties
options.setExportDocumentProperties(false);
options.setExportWorkbookProperties(false);
options.setExportWorksheetProperties(false);

// Export the Excel file to Html with Html Save Options
workbook.save("outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html", options);
```  

