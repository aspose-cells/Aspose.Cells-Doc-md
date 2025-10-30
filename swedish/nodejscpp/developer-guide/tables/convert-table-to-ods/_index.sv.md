---  
title: Konvertera tabell till ODS med Node.js via C++  
linktitle: Konvertera tabell till ODS.  
type: docs  
weight: 70  
url: /sv/nodejs-cpp/convert-table-to-ods/  
description: Lär dig hur du konverterar en Excel fil med tabell till ODS format med Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells stöder konvertering av en Excel-fil med en tabell till ODS-fil. Du behöver bara spara filen i ODS-format och den genererade ODS-filen kommer att ha en fungerande tabell.

## Exempelkod

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTable.xlsx"));

// Save the file
workbook.save(path.join(outputDir, "ConvertTableToOds_out.ods"));
```

Den utdata ODS-fil som genereras av provkoden bifogas för din referens.

[**Output ODS File**](ConvertTableToOds_out.ods)  

{{< app/cells/assistant language="nodejs-cpp" >}}
