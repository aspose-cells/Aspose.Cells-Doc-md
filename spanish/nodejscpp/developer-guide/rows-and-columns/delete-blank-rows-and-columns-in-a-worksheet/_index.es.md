---
title: Eliminar filas y columnas en blanco en una hoja de cálculo con Node.js via C++
linktitle: Eliminar Filas y Columnas en Blanco en una Hoja de Cálculo
type: docs
weight: 300
url: /es/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Aprenda cómo eliminar todas las filas y columnas en blanco de una hoja de cálculo usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Es posible eliminar todas las filas y columnas en blanco de una hoja de cálculo. Esto es útil cuando, por ejemplo, se genera un archivo PDF a partir de un archivo de Microsoft Excel y se desea convertir solo filas y columnas que contienen datos u objetos relacionados.

Use los siguientes métodos de Aspose.Cells para eliminar filas y columnas vacías:

1. Para eliminar filas en blanco, utilice el método [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankRows--). Tenga en cuenta que, para las filas en blanco que se eliminarán, no solo es necesario que [**Row.isBlank()**](https://reference.aspose.com/cells/nodejs-cpp/row/#isBlank--) sea verdadero, sino que también no debe haber comentarios visibles definidos para ninguna celda en esas filas, y no debe haber una tabla dinámica cuyo rango se interseque con ellas.
2. Para eliminar columnas en blanco, use el método [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankColumns--).

{{% /alert %}}

## Código Node.js para eliminar filas en blanco

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(filePath);

// Create a Worksheets object with reference to
// The sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Rows from the worksheet
sheet.getCells().deleteBlankRows();

// Save the excel file.
wb.save(path.join(dataDir, "mybook.out.xlsx"));
```

## Código Node.js para eliminar columnas en blanco

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an existing excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleInput.xlsx"));

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = workbook.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Columns from the worksheet
sheet.getCells().deleteBlankColumns();

// Save the excel file.
workbook.save(path.join(dataDir, "mybook.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
