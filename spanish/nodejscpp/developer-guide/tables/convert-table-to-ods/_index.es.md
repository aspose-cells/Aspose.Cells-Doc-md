---  
title: Convertir Tabla a ODS con Node.js a través de C++  
linktitle: Convertir Tabla a ODS  
type: docs  
weight: 70  
url: /es/nodejs-cpp/convert-table-to-ods/  
description: Aprenda cómo convertir un archivo Excel con una tabla a formato ODS usando Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells admite convertir un archivo Excel con una tabla a archivo ODS. Solo necesita guardar el archivo en formato ODS y el archivo ODS generado tendrá una tabla funcional.

## Código de Muestra

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

El archivo ODS de salida generado por el código de ejemplo se adjunta para su referencia.

[**Output ODS File**](ConvertTableToOds_out.ods)  

