---  
title: Rendern einer PDF Seite pro Excel Arbeitsblatt  Excel zu PDF Konvertierung mit Node.js via C++  
linktitle: Ein PDF Seite pro Excel Arbeitsblatt rendern  Konvertierung von Excel in PDF  
type: docs  
weight: 100  
url: /de/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/  
---  

{{% alert color="primary" %}}  

Wenn Sie mit großen Microsoft Excel-Dateien arbeiten (zum Beispiel einer Arbeitsmappe mit vielen Blättern, jeweils mit 50 Spalten und 300 oder mehr Zeilen Daten), möchten Sie vielleicht, dass die PDF-Ausgabe eine Seite pro Arbeitsblatt zeigt, unabhängig von der Größe des Arbeitsblatts. Das bedeutet, dass jede Seite wahrscheinlich eine völlig andere Seitengröße hat. Dies kann durch Verwendung von Aspose.Cells for Node.js via C++ erreicht werden.  

{{% /alert %}}  

Bitte sehen Sie sich den folgenden Beispielcode an, der eine Excel-Datei mit mehreren Arbeitsblättern in PDF konvertiert.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Implement one page per worksheet option
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setOnePagePerSheet(true);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile.out.pdf"), pdfSaveOptions);
```  

{{% alert color="primary" %}}  

Wenn die Option {0} (https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) auf **wahr** gesetzt ist, wird der gesamte Inhalt des Blatts auf eine PDF-Seite gerendert.  

{{% /alert %}} {{% alert color="primary" %}}  

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) kurz vor der Konvertierung der Tabelle in PDF aufzurufen. Dies stellt sicher, dass die formelabhängigen Werte neu berechnet werden und die korrekten Werte im PDF angezeigt werden.  

{{% /alert %}}  

