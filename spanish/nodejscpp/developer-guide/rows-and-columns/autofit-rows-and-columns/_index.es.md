---  
title: Ajustar automáticamente filas y columnas con Node.js a través de C++  
linktitle: Ajustar automáticamente filas y columnas  
type: docs  
weight: 20  
url: /es/nodejs-cpp/autofit-rows-and-columns/  
description: Este artículo muestra cómo ajustar automáticamente las filas, columnas, filas de celdas combinadas y filas en un rango de celdas usando Aspose.Cells for Node.js via C++.  
keywords: Ajuste automático de filas de Node.js mediante C++, ajuste automático de columnas de Node.js mediante C++, ajuste automático de fila en un rango de celdas de Node.js mediante C++, ajuste automático de filas de celdas combinadas de Node.js mediante C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel permite a los usuarios ajustar el tamaño de las celdas automáticamente según su contenido. Esta función también está disponible a través de Aspose.Cells for Node.js via C++, por lo que los desarrolladores pueden ajustar automáticamente las dimensiones de una celda en tiempo de ejecución.  
{{% /alert %}}  

## **Ajuste automático**  

Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja en un archivo Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) ofrece una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Este artículo analiza cómo usar la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) para ajustar filas o columnas automáticamente.  

### **Ajuste automático de fila - Simple**  

El enfoque más sencillo para ajustar automáticamente el ancho y la altura de una fila es llamar al método [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). El método [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) toma un índice de fila (de la fila a redimensionar) como parámetro.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileBuffer = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1);

// Saving the modified Excel file
const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath);
```  

### **Cómo AutoAjustar una Fila en un Rango de Celdas**  

Una fila está compuesta por muchas columnas. Aspose.Cells permite a los desarrolladores ajustar automáticamente una fila basada en el contenido en un rango de celdas dentro de la fila llamando a una versión sobrecargada del método [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-). Toma los siguientes parámetros:  

- **Índice de la fila**, el índice de la fila a ajustar automáticamente.  
- **Índice de la primera columna**, el índice de la primera columna de la fila.  
- **Índice de la última columna**, el índice de la última columna de la fila.  

El método [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-) verifica el contenido de todas las columnas en la fila y luego ajusta automáticamente la fila.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileData = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1, 0, 5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **Cómo AutoAjustar una Columna en un Rango de Celdas**  

Una columna está compuesta por muchas filas. Es posible ajustar automáticamente una columna basada en el contenido en un rango de celdas en la columna llamando a una versión sobrecargada del método [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) que toma los siguientes parámetros:  

- **Índice de columna**, el índice de la columna que se va a ajustar automáticamente.  
- **Índice de la primera fila**, el índice de la primera fila de la columna.  
- **Índice de la última fila**, el índice de la última fila de la columna.  

El método [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) verifica el contenido de todas las filas en la columna y luego ajusta automáticamente la columna.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const workbook = new AsposeCells.Workbook(fs.readFileSync(inputPath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the Column of the worksheet
worksheet.autoFitColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **Cómo AutoAjustar Filas para Celdas Fusionadas**  

Con Aspose.Cells, es posible ajustar automáticamente filas incluso para celdas que han sido combinadas usando la API [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions). La clase [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) proporciona una propiedad [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) que puede ser utilizada para ajustar automáticamente filas para celdas combinadas. [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) acepta un enumerable [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype) que tiene los siguientes miembros.  

- Ninguno: Ignora las celdas combinadas.  
- PrimeraLinea: Solo expande la altura de la primera fila.  
- ÚltimaLinea: Solo expande la altura de la última fila.  
- CadaLinea: Solo expande la altura de cada fila.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first (default) worksheet
const worksheet = wb.getWorksheets().get(0);

// Create a range A1:B1
const range = worksheet.getCells().createRange(0, 0, 1, 2);

// Merge the cells
range.merge();

// Insert value to the merged cell A1
worksheet.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style = worksheet.getCells().get(0, 0).getStyle();

// Set wrapping text on
style.setIsTextWrapped(true);

// Apply the style to the cell
worksheet.getCells().get(0, 0).setStyle(style);

// Create an object for AutoFitterOptions
const options = new AsposeCells.AutoFitterOptions();

// Set auto-fit for merged cells
options.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.EachLine);

// Autofit rows in the sheet (including the merged cells)
worksheet.autoFitRows(options);

// Save the Excel file
wb.save(path.join(outputDir, "AutofitRowsforMergedCells.xlsx"));
```  

{{% alert color="primary" %}}  
También puedes intentar usar las versiones sobrecargadas de los métodos [**autoFitRows**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) y [**autoFitColumns**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) que aceptan un rango de filas/columnas y una instancia de [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) para ajustar automáticamente las filas/columnas seleccionadas con tu [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) deseado, respectivamente.  

Las firmas de los métodos mencionados anteriormente son las siguientes:  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **Importante saber**  

{{% alert color="primary" %}}  
Si una celda está combinada, entonces los métodos de ajuste automático no se aplicarán, lo cual es el mismo comportamiento que en Microsoft Excel. Puedes sortear esto usando la API de autofiltro. Además, si el texto en una celda está envuelto, el método [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) tampoco se aplicará. Otra cosa que debes saber es que los métodos *autoFit* consumen mucho tiempo. Por lo tanto, deberías llamar a estos métodos con la menor frecuencia posible para garantizar la eficiencia de tu aplicación.  
{{% /alert %}}  

## **Temas avanzados**  
- [Ajustar automáticamente filas para celdas fusionadas](/cells/es/nodejs-cpp/autofit-rows-for-merged-cells/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
