---
title: Konvertera Excel arbetsbok till Ods, Sxc och Fods (OpenOffice / LibreOffice calc) via Node.js
linktitle: Ods
type: docs
weight: 20
url: /sv/nodejs-cpp/convert-excel-to-ods/
description: Hur konverterar man Excel till Ods (OpenOffice / LibreOffice Calc) eller konverterar Ods (OpenOffice / LibreOffice Calc) till Excel med Aspose.Cells for Node.js via C++.
---

## **Om OpenDocument**
[OpenDocument-formatet (ODF)](https://en.wikipedia.org/wiki/OpenDocument) är ett gratis och öppet filformat för elektroniska dokument för kontorsändamål, ursprungligen utvecklat av Sun för Open Office-suite. OpenDocument Spreadsheet (ODS) är filformatet för Excel-dokument. OpenDocument är för närvarande en OASIS och ISO-standard.

## **Konvertera Ods (OpenOffice / LibreOffice calc) till Excel**
Aspose.Cells for Node.js via C++ stöder att ladda Ods, Sxc och Fods som stöds av OpenOffice / LibreOffice Calc, och konverterar [Ods](book1.ods), [Sxc](book1.sxc) och [Fods](book1.fods) till Excelfiler.

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

## **Konvertera Excel till Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells for Node.js via C++ stödjer konvertering av Excel-filer till Ods, Sxc och Fods-filer. Exempel på kod nedan visar hur man konverterar [mallen](book1.xlsx) till Ods, Sxc och Fods-fil.

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

## **Fortsatta ämnen**
- [Spara ODS-fil enligt ODF 1.1 och 1.2-specifikationer](/cells/sv/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Arbeta med bakgrund i ODS-filer](/cells/sv/nodejs-cpp/working-with-background-in-ods-files/)
