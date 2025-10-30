---  
title: Insertar o eliminar filas en una hoja de Excel con Node.js mediante C++  
linktitle: Insertar o Eliminar Filas en una Hoja de Cálculo de Excel  
type: docs  
weight: 20  
url: /es/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/  
description: Este artículo proporciona código de Node.js usando C++ para insertar y eliminar filas en una hoja de Excel.  
keywords: Node.js para insertar o eliminar filas en hoja de Excel, Node.js para insertar o eliminar filas en Excel, Node.js para insertar filas en Excel, Node.js para eliminar filas en Excel, insertar o eliminar filas en hoja de Excel con Node.js, insertar o eliminar filas en Excel con Node.js, insertar filas en Excel con Node.js, eliminar filas en Excel con Node.js  
---  

{{% alert color="primary" %}}  

Al crear una nueva hoja o trabajar con una hoja existente, puede que necesite agregar filas o columnas adicionales para acomodar los datos. En otras ocasiones, puede que necesite eliminar filas o columnas de posiciones específicas en la hoja.  

{{% /alert %}}  

Aspose.Cells for Node.js via C++ ofrece dos métodos para insertar y eliminar filas: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) y [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-). Estos métodos están optimizados para rendimiento y realizan el trabajo muy rápidamente.  

Para insertar o eliminar varias filas, le recomendamos que siempre use los métodos [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) y [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) en lugar de usar los métodos [**Cells.insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) o [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRow-number-) en un ciclo.  

Aspose.Cells funciona de la misma manera que lo hace Microsoft Excel. Cuando se agregan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia abajo y hacia la derecha. Cuando se eliminan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia arriba o hacia la izquierda. Cualquier referencia en otras hojas de cálculo y celdas se actualiza cuando se agregan o eliminan filas.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object.
// Load a template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));

// Get the first worksheet in the book.
const sheet = workbook.getWorksheets().get(0);

// Insert 10 rows at row index 2 (insertion starts at 3rd row)
sheet.getCells().insertRows(2, 10);

// Delete 5 rows now. (8th row - 12th row)
sheet.getCells().deleteRows(7, 5);

// Save the excel file.
workbook.save(path.join(dataDir, "out_book1.out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
