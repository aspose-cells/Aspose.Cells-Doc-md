---
title: Convertir JSON a Excel con Node.js a través de C++
linktitle: Convertir JSON a Excel
type: docs
weight: 300
url: /es/nodejs-cpp/convert-json-to-excel/
description: Aprende cómo convertir JSON a archivo Excel con Aspose.Cells for Node.js via C++.
keywords: Importar JSON sin Office 2013, Office 2016, Office 2019 y Office 365 usando Node.js a través de C++.
---

{{% alert color="primary" %}}

 Aspose.Cells soporta convertir un archivo JSON (JavaScript Object Notation) a un libro de Excel.

{{% /alert %}}

## **Convertir JSON a hoja de cálculo de Excel**
 No necesitas preguntarte cómo convertir JSON a archivo Excel, porque Aspose.Cells for Node.js via C++ ofrece la mejor solución. La API Aspose.Cells proporciona soporte para convertir formato JSON a hojas de cálculo. Puedes usar la clase [**JsonLoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonloadoptions) para especificar configuraciones adicionales para importar JSON a un libro.

El siguiente ejemplo de código muestra la importación de JSON a un Libro de Trabajo de Excel. Por favor, vea el código para convertir el [archivo fuente](sample.json) al archivo xlsx generado por el código para referencia.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");
// create a Workbook object
const wb = new AsposeCells.Workbook(filePath);

// save file to xlsx format
wb.save("sample_out.xlsx");
```

 El siguiente ejemplo de código, que usa la clase JsonLoadOptions para especificar configuraciones adicionales, demuestra cómo importar JSON a un libro de Excel. Consulta el código para convertir el [archivo fuente](sample.json) al archivo xlsx generado por el código como referencia.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");

// Create an options of loading the file.
const options = new AsposeCells.JsonLoadOptions();
options.setMultipleWorksheets(true);

// Loads the workbook from JSON file
const book = new AsposeCells.Workbook(filePath, options);

// Save file to xlsx format
book.save("sample_out.xlsx");
```

 El siguiente ejemplo de código demuestra cómo importar una cadena JSON a un libro de Excel. También puedes especificar la ubicación del diseño al importar JSON. Consulta el código para convertir una cadena JSON al archivo xlsx generado por el código como referencia.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputJson = JSON.stringify([
{ BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
]);
const sheetName = "Sheet1";
const row = 3;
const column = 2;

// create a Workbook object
const book = new AsposeCells.Workbook();
const worksheet = book.getWorksheets().get(sheetName);

// set JsonLayoutOptions to treat Arrays as Table
const jsonLayoutOptions = new AsposeCells.JsonLayoutOptions();
jsonLayoutOptions.setArrayAsTable(true);

AsposeCells.JsonUtility.importData(inputJson, worksheet.getCells(), row, column, jsonLayoutOptions);

// save file to xlsx format
book.save("out.xlsx");
```
