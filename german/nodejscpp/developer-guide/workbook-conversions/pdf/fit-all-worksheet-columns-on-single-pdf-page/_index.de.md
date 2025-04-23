---
title: Alle Spalten eines Arbeitsblatts auf einer einzelnen PDF Seite anzeigen mit Node.js via C++
linktitle: Alle Arbeitsblattsäulen auf eine einzelne PDF Seite passen
type: docs
weight: 160
url: /de/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Manchmal möchten Sie eine PDF-Datei generieren, die alle Spalten eines Arbeitsblatts auf einer Seite passt. Die [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--)-Eigenschaft bietet diese Funktion auf sehr benutzerfreundliche Weise. Komplexe Berechnungen wie die Höhe und Breite der Ausgabe-PDF werden intern behandelt und basieren auf den Daten im Arbeitsblatt.

{{% /alert %}}

## **Arbeitsblattsäulen auf eine einzelne PDF-Seite anpassen**

[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) stellt sicher, dass alle Spalten in einem Arbeitsblatt auf einer einzigen PDF-Seite dargestellt werden, auch wenn Zeilen je nach Dateninhalt auf mehrere Seiten erweitert werden können.

Der folgende Beispielcode zeigt, wie die [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--)-Eigenschaft verwendet wird, um ein großes Arbeitsblatt mit 100 Spalten zu rendern.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create and initialize an instance of Workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Create and initialize an instance of PdfSaveOptions
const saveOptions = new AsposeCells.PdfSaveOptions();
// Set AllColumnsInOnePagePerSheet to true
saveOptions.setAllColumnsInOnePagePerSheet(true);
// Save Workbook to PDF format by passing the object of PdfSaveOptions
const outputFilePath = path.join(dataDir, "output.out.pdf");
workbook.save(outputFilePath, saveOptions);
```

{{% alert color="primary" %}}

Wenn ein bestimmtes Arbeitsblatt viele Spalten hat, kann die gerenderte PDF-Datei den Inhalt in sehr kleiner Größe anzeigen. Es ist immer noch lesbar, wenn es in einer Anzeige-Anwendung wie Acrobat Reader skaliert wird.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
