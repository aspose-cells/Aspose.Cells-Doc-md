---
title: Agrupación y desagrupación de filas y columnas con Node.js vía C++
linktitle: Agrupando y Desagrupando Filas y Columnas
type: docs
weight: 50
url: /es/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/
description: Descubra cómo agrupar y desagrupar filas y columnas en Excel usando Aspose.Cells for Node.js via C++.
--- 

## **Introducción**

En un archivo de Microsoft Excel, puedes crear un esquema para los datos que te permita mostrar y ocultar niveles de detalle con un solo clic de ratón.

Haz clic en los **Símbolos de Esquema**, 1,2,3, + y - para mostrar rápidamente solo las filas o columnas que proporcionen resúmenes o encabezados para secciones en una hoja de cálculo, o puedes usar los símbolos para ver detalles bajo un resumen o encabezado individual como se muestra a continuación en la figura:

|**Agrupar Filas y Columnas.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestión de Agrupación de Filas y Columnas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) que permite acceder a cada hoja en el archivo de Excel. Una hoja se representa mediante la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) que representa todas las celdas en la hoja.

La colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) proporciona varios métodos para gestionar filas o columnas en una hoja, algunos de estos se discuten a continuación en más detalle.

### **Agrupar Filas y Columnas**

Es posible agrupar filas o columnas llamando a los métodos [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupRows-number-number-boolean-) y [**groupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupColumns-number-number-) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Ambos métodos toman los siguientes parámetros:

- Índice de la primera fila/columna, la primera fila o columna del grupo.
- Índice de la última fila/columna, la última fila o columna del grupo.
- Está oculto, un parámetro booleano que especifica si ocultar o no filas/columnas después de agrupar.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileContent = fs.readFileSync(filePath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileContent);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows (from 0 to 5) and making them hidden by passing true
worksheet.getCells().groupRows(0, 5, true);

// Grouping first three columns (from 0 to 2) and making them hidden by passing true
worksheet.getCells().groupColumns(0, 2, true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Configuración de Grupo**

Microsoft Excel te permite configurar la configuración de grupo para mostrar:

- Filas resumen debajo del detalle.
- Columnas de resumen a la derecha del detalle.

Los desarrolladores pueden configurar estas opciones de agrupación usando la propiedad [**getOutline()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getOutline--) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

### **Filas de Resumen Debajo del Detalle**

Es posible controlar si las filas de resumen se muestran debajo del detalle configurando la propiedad [**getSummaryRowBelow()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryRowBelow--) de la clase [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) a **true** o **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

// Setting SummaryRowBelow property to false
worksheet.getOutline().setSummaryRowBelow(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Columnas Resumen a la Derecha del Detalle**

Los desarrolladores también pueden controlar la visualización de columnas de resumen a la derecha del detalle configurando la propiedad [**getSummaryColumnRight()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryColumnRight--) de la clase [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) a **true** o **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

worksheet.getOutline().setSummaryColumnRight(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Desagrupando Filas y Columnas**

Para desagrupar filas o columnas agrupadas, llame a los métodos [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) y [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupColumns-number-number-) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Ambos métodos toman dos parámetros:

- Índice de la primera fila o columna, la primera fila/columna a desagrupar.
- Índice de la última fila o columna, la última fila/columna a desagrupar.

[**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) tiene una sobrecarga que toma un tercer parámetro booleano. Configurarlo a **true** elimina toda la información agrupada. De lo contrario, solo se elimina la agrupación exterior.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading Excel file into buffer
const buffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file content
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Ungrouping first six rows (from 0 to 5)
worksheet.getCells().ungroupRows(0, 5);

// Ungrouping first three columns (from 0 to 2)
worksheet.getCells().ungroupColumns(0, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
