---  
title: Converti tabella in formato ODS con Node.js tramite C++  
linktitle: Converti Tabella in ODS  
type: docs  
weight: 70  
url: /it/nodejs-cpp/convert-table-to-ods/  
description: Impara come convertire un file Excel con tabella in formato ODS usando Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells supporta la conversione di un file Excel con una tabella in formato ODS. Devi semplicemente salvare il file in formato ODS e il file ODS generato avrà una tabella funzionante.

## Codice di esempio

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

Il file ODS di output generato dal codice di esempio è allegato per il tuo riferimento.

[**Output ODS File**](ConvertTableToOds_out.ods)  

