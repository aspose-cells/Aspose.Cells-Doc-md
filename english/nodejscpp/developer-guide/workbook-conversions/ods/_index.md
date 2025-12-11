---
title: Convert Excel workbook to Ods, Sxc and Fods (OpenOffice / LibreOffice Calc) via Node.js
linktitle: Ods
type: docs
weight: 20
url: /nodejs-cpp/convert-excel-to-ods/
description: How to convert Excel to Ods (OpenOffice / LibreOffice Calc) or convert Ods (OpenOffice / LibreOffice Calc) to Excel with Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **About OpenDocument**
The [OpenDocument format (ODF)](https://en.wikipedia.org/wiki/OpenDocument) is a free and open file format for electronic office documents originally developed by Sun for the OpenOffice suite. OpenDocument Spreadsheet (ODS) is the file format for spreadsheet documents. OpenDocument is currently an OASIS and ISO standard.

## **Convert Ods (OpenOffice / LibreOffice Calc) to Excel**
Aspose.Cells for Node.js via C++ supports loading ODS, SXC, and FODS, which are supported by OpenOffice / LibreOffice Calc, and converting [Ods](book1.ods), [Sxc](book1.sxc) and [Fods](book1.fods) to Excel files.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load Excel workbook
const excelFilePath = path.join(__dirname, "book1.xlsx");
let workbook = new AsposeCells.Workbook(excelFilePath);

// Save as ODS file
workbook.save("ods_out.ods");

// Save as SXC file
workbook.save("sxc_out.sxc");

// Save as FODS file
workbook.save("fods_out.fods");
```

## **Convert Excel to Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells for Node.js via C++ supports converting Excel files to ODS, SXC, and FODS files. The code example below shows how to convert the [template](book1.xlsx) to ODS, SXC, and FODS files.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath1 = path.join(dataDir, "book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath1);
// Save as ODS file 
workbook.save("Out.ods");
// Save as SXC file 
workbook.save("Out.sxc");
// Save as FODS file 
workbook.save("Out.fods");
```

## **Advanced topics**
- [Save ODS File in ODF 1.1 and 1.2 Specifications](/cells/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Working with Background in ODS Files](/cells/nodejs-cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="nodejs-cpp" >}}
