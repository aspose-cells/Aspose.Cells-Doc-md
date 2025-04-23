---  
title: Formatear filas y columnas con Node.js a través de C++  
linktitle: Filas y Columnas  
type: docs  
weight: 100  
url: /es/nodejs-cpp/adjusting-row-height-and-column-width/  
description: Aspose.Cells for Node.js via C++ puede soportar cambiar la altura de filas o el ancho de columnas, así como aplicar formato en filas o columnas.  
keywords: Establecer altura de la fila y ancho de la columna, ajustar la altura de la fila y ancho de la columna, cambiar la altura de la fila o ancho de la columna, dar formato a filas y columnas, cómo establecer la altura de la fila y el ancho de la columna.  
---  

{{% alert color="primary" %}}  
Al trabajar con hojas de cálculo y agregar datos a filas o columnas, puede ser necesario cambiar la altura de las filas o el ancho de las columnas. A veces, aplicar formato en filas o columnas significa que la altura o el ancho actuales deben cambiar para mostrar los datos. Normalmente, los usuarios ajustan la altura de filas y el ancho de columnas en un entorno WYSIWYG usando Microsoft Excel. Pero, con Aspose.Cells, los desarrolladores pueden realizar estas operaciones en tiempo de ejecución.  
{{% /alert %}}  

## **Trabajar con filas**  

### **Cómo ajustar la altura de fila**  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) que representa todas las celdas en la hoja.  

La colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo. Algunos de estos se describen a continuación con más detalle.  

### **Cómo establecer la altura de una fila**  

Es posible establecer la altura de una sola fila llamando al método [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). El método [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) acepta los siguientes parámetros: 

- **Índice de fila**, el índice de la fila a la que le estás cambiando la altura.  
- **Altura de fila**, la altura de fila para aplicar en la fila.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const buffer = Buffer.concat(chunks);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of the second row to 13
worksheet.getCells().setRowHeight(1, 13);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

### **Cómo establecer la altura de todas las filas en una hoja de cálculo**  

Si los desarrolladores necesitan establecer la misma altura de fila para todas las filas en la hoja, pueden hacerlo usando la propiedad [**getStandardHeight()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardHeight--) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

**Ejemplo:**  

```javascript
const fs = require("fs");
const path = require("path");
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

// Setting the height of all rows in the worksheet to 15
worksheet.getCells().setStandardHeight(15);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// (Note: Closing the file stream is unnecessary in this context as it's a 
// synchronous read performed using fs.readFileSync, which does not require
// explicit closure, but if using fs.createReadStream, you would handle it accordingly)
```  

## **Trabajar con columnas**  

### **Cómo establecer el ancho de una columna**  

Establece el ancho de una columna llamando al método [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). El método [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) acepta los siguientes parámetros:  

- **Índice de la columna**, el índice de la columna cuyo ancho se va a cambiar.  
- **Ancho de la columna**, el ancho de columna deseado.  

```javascript
const fs = require("fs");
const path = require("path");
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

// Setting the width of the second column to 17.5
worksheet.getCells().setColumnWidth(1, 17.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream; // Note: No explicit close needed for fs.readFileSync
```  

### **Cómo establecer el ancho de columna en píxeles**  

Establece el ancho de una columna llamando al método [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). El método [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) acepta los siguientes parámetros:  

- **Índice de la columna**, el índice de la columna cuyo ancho se va a cambiar.  
- **Ancho de columna**, el ancho de columna deseado en píxeles.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the width of the column in pixels
worksheet.getCells().setColumnWidthPixel(7, 200);

workbook.save(path.join(outDir, "SetColumnWidthInPixels_Out.xlsx"));
```  

### **Cómo establecer el ancho de todas las columnas en una hoja de cálculo**  

Para establecer el mismo ancho de columna para todas las columnas en la hoja, usa la propiedad [**getStandardWidth()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardWidth--) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of all columns in the worksheet to 20.5
worksheet.getCells().setStandardWidth(20.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// No explicit close needed in Node.js
```  

## **Temas avanzados**  
- [Ajustar automáticamente filas y columnas](/cells/es/nodejs-cpp/autofit-rows-and-columns/)  
- [Convertir Texto en Columnas usando Aspose.Cells](/cells/es/nodejs-cpp/convert-text-to-columns-using-aspose-cells/)  
- [Copiando Filas y Columnas](/cells/es/nodejs-cpp/copying-rows-and-columns/)  
- [Eliminar Filas y Columnas en Blanco en una Hoja de Cálculo](/cells/es/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/)  
- [Agrupar y Desagrupar Filas y Columnas](/cells/es/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/)  
- [Ocultar y Mostrar Filas y Columnas](/cells/es/nodejs-cpp/hiding-and-showing-rows-and-columns/)  
- [Insertar o Eliminar Filas en una Hoja de Cálculo de Excel](/cells/es/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/)  
- [Insertar y Eliminar Filas y Columnas de un archivo de Excel](/cells/es/nodejs-cpp/inserting-and-deleting-rows-and-columns/)  
- [Eliminar filas duplicadas en una hoja de cálculo](/cells/es/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/)  
- [Actualizar referencias en otras hojas de cálculo al eliminar columnas y filas en blanco en una hoja de cálculo](/cells/es/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)  

