---
title: Excel Arbeitsmappe nach Ods, Sxc und Fods (OpenOffice / LibreOffice Calc) via Node.js konvertieren
linktitle: Ods
type: docs
weight: 20
url: /de/nodejs-cpp/convert-excel-to-ods/
description: So konvertieren Sie Excel in Ods (OpenOffice / LibreOffice Calc) oder konvertieren Ods in Excel mit Aspose.Cells for Node.js via C++.
---

## **Über das OpenDocument**
[Das OpenDocument-Format (ODF)](https://en.wikipedia.org/wiki/OpenDocument) ist ein kostenloses und offenes Dateiformat für elektronische Bürodokumente, das ursprünglich von Sun für die Open-Office-Suite entwickelt wurde. OpenDocument Spreadsheet (ODS) ist das Dateiformat für Excel-Dokumente. OpenDocument ist derzeit ein OASIS- und ISO-Standard.

## **Ods (OpenOffice / LibreOffice calc) in Excel konvertieren**
Aspose.Cells for Node.js via C++ unterstützt das Laden von Ods, Sxc und Fods, die von OpenOffice / LibreOffice Calc unterstützt werden, und wandelt [Ods](book1.ods), [Sxc](book1.sxc) und [Fods](book1.fods) in Excel-Dateien um.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load Excel workbook
const excelFilePath = path.join(__dirname, "book1.xlsx");
let workbook = new AsposeCells.Workbook(excelFilePath);

// Save as ods file
workbook.save("ods_out.ods");

// Save as sxc file
workbook.save("sxc_out.sxc");

// Save as fods file
workbook.save("fods_out.fods");
```

## **Excel in Ods (OpenOffice / LibreOffice Calc) konvertieren**
Aspose.Cells for Node.js via C++ unterstützt die Konvertierung von Excel-Dateien in Ods, Sxc und Fods. Das unten stehende Code-Beispiel zeigt, wie die [Vorlage](book1.xlsx) in Ods, Sxc und Fods konvertiert wird.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath1 = path.join(dataDir, "book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath1);
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Erweiterte Themen**
- [ODS-Datei nach ODF 1.1 und 1.2-Spezifikationen speichern](/cells/de/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Arbeiten mit Hintergründen in ODS-Dateien](/cells/de/nodejs-cpp/working-with-background-in-ods-files/)
