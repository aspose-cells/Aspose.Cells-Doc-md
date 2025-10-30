---
title: Insertar y Eliminar Filas y Columnas de un archivo de Excel
linktitle: Inserción y Eliminación de Filas y Columnas
type: docs
weight: 70
url: /es/nodejs-cpp/inserting-and-deleting-rows-and-columns/
description: Este artículo muestra cómo insertar y eliminar filas y columnas mediante la API Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js vía C++ gestionar filas y columnas, insertar filas y columnas, eliminar filas y columnas
---

## **Introducción**

Ya sea creando una nueva hoja de cálculo desde cero o trabajando en una hoja de cálculo existente, puede ser necesario agregar filas o columnas adicionales para acomodar más datos. Inversamente, también puede ser necesario eliminar filas o columnas de posiciones específicas en la hoja de cálculo. 
Para cumplir con estos requisitos, Aspose.Cells for Node.js via C++ proporciona un conjunto muy simple de clases y métodos, discutidos a continuación.

### **Gestionar Filas y Columnas**

Aspose.Cells for Node.js via C++ proporciona una clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) que permite acceder a cada hoja de cálculo en un archivo Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) que representa todas las celdas en la hoja de cálculo.

La colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) proporciona varios métodos para gestionar filas y columnas en una hoja de cálculo. Algunos de estos se discuten a continuación.

{{% alert color="primary" %}}

Cuando se añaden filas o columnas, el contenido en la hoja de cálculo se desplaza hacia abajo o hacia la derecha, y si se eliminan filas o columnas, el contenido se desplaza hacia arriba o hacia la izquierda.

{{% /alert %}}


## **Insertar Filas y Columnas**

### **Cómo insertar una fila**

Inserte una fila en la hoja de cálculo en cualquier ubicación llamando al método [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) de la colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). El método [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) toma el índice de la fila donde se insertará la nueva fila.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRow(2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Cómo insertar múltiples filas**

Para insertar múltiples filas en una hoja de cálculo, llame al método [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) de la colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). El método [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) toma dos parámetros:

- Índice de la fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, el número total de filas que se deben insertar.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileData = fs.readFileSync(filePath);
const workbook = new AsposeCells.Workbook(fileData);

const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().insertRows(2, 10);

workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Cómo insertar una fila con formato**

Para insertar una fila con opciones de formato, use la sobrecarga [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) que toma [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) como parámetro. Establezca la propiedad [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) de la clase [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) con la enumeración [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/). La enumeración [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) tiene tres miembros que se enumeran a continuación.

- SameAsAbove: Formatea la fila igual que la fila superior.
- SameAsBelow: Formatea la fila igual que la fila inferior.
- Clear: Borra el formato.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting Formatting options
const insertOptions = new AsposeCells.InsertOptions();
insertOptions.setCopyFormatType(AsposeCells.CopyFormatType.SameAsAbove);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2, 1, insertOptions);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "InsertingARowWithFormatting.out.xls"));
```

### **Cómo Insertar una Columna**

Los desarrolladores también pueden insertar una columna en la hoja de cálculo en cualquier ubicación llamando al método [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) de la colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). El método [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) toma el índice de la columna donde se insertará la nueva columna.

```javascript
const fs = require('fs');
const path = require('path');
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fileStream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fileStream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a column into the worksheet at 2nd position
worksheet.getCells().insertColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Eliminar Filas y Columnas**

### **Cómo borrar múltiples filas**

Para eliminar múltiples filas de una hoja de cálculo, llama al método [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) de la colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). El método [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, el número total de filas que deben ser eliminadas.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Read file contents as Uint8Array
const fileContent = fs.readFileSync(filePath);
const fileBuffer = new Uint8Array(fileContent);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting 10 rows from the worksheet starting from 3rd row
worksheet.getCells().deleteRows(2, 10);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```


### **Cómo eliminar una columna**

Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llama al método [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) de la colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). El método [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) toma el índice de la columna a eliminar.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting a column from the worksheet at 5th position
worksheet.getCells().deleteColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));

// Closing resources is handled automatically by Node.js, no specific close needed.
```
{{< app/cells/assistant language="nodejs-cpp" >}}
