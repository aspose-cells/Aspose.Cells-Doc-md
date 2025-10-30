---  
title: Convertir texto a columnas usando Aspose.Cells for Node.js via C++  
linktitle: Convertir texto en columnas  
type: docs  
weight: 30  
url: /es/nodejs-cpp/convert-text-to-columns-using-aspose-cells/  
description: Aprende cómo convertir texto a columnas en Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Puedes convertir tu texto a columnas usando Microsoft Excel. Esta función está disponible en *Herramientas de datos* en la pestaña *Datos*. Para dividir el contenido de una columna en varias columnas, los datos deben contener un delimitador específico como una coma (u otro carácter) según el cual Microsoft Excel divide el contenido de una celda en varias celdas. Aspose.Cells for Node.js via C++ también ofrece esta función a través de [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-).  

## **Convertir texto a columnas usando Aspose.Cells for Node.js via C++**  

El código ejemplo siguiente explica el uso del método [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-). Primero añade algunos nombres de personas en la columna A de la primera hoja. El nombre y apellido están separados por un espacio. Luego aplica el método [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) en la columna A y lo guarda como un archivo Excel de salida. Si abres el [archivo Excel de salida](25395213.xlsx), verás que los nombres están en la columna A mientras que los apellidos están en la columna B, como se muestra en esta captura.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add people name in column A. First name and last name are separated by space.
ws.getCells().get("A1").putValue("John Teal");
ws.getCells().get("A2").putValue("Peter Graham");
ws.getCells().get("A3").putValue("Brady Cortez");
ws.getCells().get("A4").putValue("Mack Nick");
ws.getCells().get("A5").putValue("Hsu Lee");

// Create text load options with space as separator.
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(' ');

// Split the column A into two columns using TextToColumns() method.
// Now column A will have first name and column B will have second name.
ws.getCells().textToColumns(0, 0, 5, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputTextToColumns.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
