---
title: Convert Excel workbook to Ods,Sxc and Fods (OpenOffice / LibreOffice calc) via Node.js
linktitle: Ods
type: docs
weight: 20
url: /nodejs-cpp/convert-excel-to-ods/
description: How to convert Excel to Ods (OpenOffice / LibreOffice Calc) or convert Ods (OpenOffice / LibreOffice Calc) to Excel with Aspose.Cells for Node.js via C++.
---

## **About OpenDocument**
The [OpenDocument format (ODF)](https://en.wikipedia.org/wiki/OpenDocument) is a free and open file format for electronic office documents originally developed by Sun for the Open Office suite. OpenDocument Spreadsheet (ODS) is the file format for Excel documents. OpenDocument is currently an OASIS and ISO standard.

## **Convert Ods (OpenOffice / LibreOffice calc) to Excel**
Aspose.Cells for Node.js via C++ supports loading Ods, Sxc and Fods which are supported by OpenOffice / LibreOffice Calc, and convert [Ods](book1.ods), [Sxc](book1.sxc) and [Fods](book1.fods) to Excel files.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load your source ods file
const odsFilePath = path.join(__dirname, "book1.ods");
let workbook = new AsposeCells.Workbook(odsFilePath);

// Save as xlsx file
workbook.save("ods_out.xlsx");

// Load your source sxc file
const sxcFilePath = path.join(__dirname, "book1.sxc");
workbook = new AsposeCells.Workbook(sxcFilePath);

// Save as xls file
workbook.save("sxc_out.xls");

// Load your source fods file
const fodsFilePath = path.join(__dirname, "book1.fods");
workbook = new AsposeCells.Workbook(fodsFilePath);

// Save as xlsb file
workbook.save("fods_out.xlsb");
```

## **Convert Excel to Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells for Node.js via C++ supports converting Excel files to Ods, Sxc and Fods files. The code example below shows how to convert the [template](book1.xlsx) to Ods, Sxc and Fods file.

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

## **Advance topics**
- [Save ODS File in ODF 1.1 and 1.2 Specifications](/cells/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Working with Background in ODS Files](/cells/nodejs-cpp/working-with-background-in-ods-files/)
