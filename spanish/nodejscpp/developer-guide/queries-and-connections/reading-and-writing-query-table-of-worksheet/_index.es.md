---
title: Leer y escribir la tabla de consulta de la hoja de cálculo con Node.js a través de C++
linktitle: Leer y Escribir Tabla de Consulta de Hoja de Cálculo
type: docs
weight: 40
url: /es/nodejs-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells proporciona la colección Worksheet.QueryTables que devuelve el objeto de tipo QueryTable por índice. Tiene las siguientes dos propiedades

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

Ambos son valores booleanos. Puedes verlos en Microsoft Excel a través de Datos > Conexiones > Propiedades.

{{% /alert %}}

## Lectura y Escritura de Tabla de Consulta de Hoja de Cálculo

El siguiente código de ejemplo lee la primera QueryTable de la primera hoja de cálculo y luego imprime ambas propiedades de la QueryTable. Luego establece QueryTable.preserveFormatting en verdadero.

Puedes descargar el archivo de Excel fuente utilizado en este código y el archivo de Excel de salida generado por el código desde los siguientes enlaces.

- [Archivo de Excel Fuente](5115533.xlsx)
- [Archivo de Excel de Salida](5115537.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first Query Table
const qt = worksheet.getQueryTables().get(0);

// Print Query Table Data
console.log("Adjust Column Width: " + qt.getAdjustColumnWidth());
console.log("Preserve Formatting: " + qt.getPreserveFormatting());

// Now set Preserve Formatting to true
qt.setPreserveFormatting(true);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```

### Salida en Consola

Aquí está la salida de la consola del código de ejemplo anterior

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Recuperar rango de resultados de tabla de consulta

Aspose.Cells proporciona la opción de leer la dirección, es decir, el rango de resultados de celdas para una tabla de consulta. El siguiente código demuestra esta función leyendo la dirección del rango de resultados para una tabla de consulta. El archivo de ejemplo se puede descargar [aquí](72417290.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");

// Create workbook from source excel file
const wb = new AsposeCells.Workbook(filePath);

// Display the address(range) of result range of query table
console.log(wb.getWorksheets().get(0).getQueryTables().get(0).getResultRange().getAddress());
```
