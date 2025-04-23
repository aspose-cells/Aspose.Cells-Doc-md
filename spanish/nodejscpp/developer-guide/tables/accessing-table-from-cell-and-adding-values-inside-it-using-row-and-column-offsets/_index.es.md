---  
title: Accediendo a una Tabla desde una celda y agregando valores dentro usando desplazamientos de fila y columna con Node.js a través de C++  
linktitle: Acceder a Tabla desde Celda y Agregar Valores en su Interior usando Desplazamientos de Fila y Columna  
type: docs  
weight: 230  
url: /es/nodejs-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
---  

{{% alert color="primary" %}}  

Normalmente, agrega valores dentro de la Tabla u Objeto de Lista usando el método [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-). Pero a veces, es posible que necesite agregar valores dentro de la Tabla u Objeto de Lista usando los desplazamientos de fila y columna.  

Para acceder a una Tabla u Objeto de Lista desde una celda, use el método [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--). Para agregar valores dentro usando desplazamientos de fila y columna, use el método [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-).  

{{% /alert %}}  

La siguiente captura de pantalla muestra el archivo Excel de origen utilizado en el código. Contiene la tabla vacía y resalta la celda D5 que se encuentra dentro de la tabla. Accederemos a esta tabla desde la celda D5 usando el método [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--) y luego agregaremos los valores dentro usando los métodos [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) y [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-).  

## Ejemplo  

### Capturas de pantalla que comparan los archivos fuente y de salida  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

La siguiente captura de pantalla muestra el archivo de Excel de salida generado por el código. Como se puede ver, la celda D5 tiene un valor y la celda F6, que está en el desplazamiento 2,2 de la tabla, tiene un valor.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### Código Node.js para acceder a la tabla desde la celda y agregar valores usando desplazamientos de fila y columna  

El siguiente código de ejemplo carga el archivo de Excel fuente como se muestra en la captura de pantalla anterior y agrega valores dentro de la tabla, y genera el archivo de Excel de salida como se muestra arriba.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Accessing_Table.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell D5 which lies inside the table
const cell = worksheet.getCells().get("D5");

// Put value inside the cell D5
cell.putValue("D5 Data");

// Access the Table from this cell
const table = cell.getTable();

// Add some value using Row and Column Offset
table.putCellValue(2, 2, "Offset [2,2]");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

