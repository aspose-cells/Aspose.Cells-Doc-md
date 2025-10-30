---  
title: Administrar hojas de cálculo de archivos de Microsoft Excel con Node.js vía C++  
linktitle: Hojas de cálculo  
type: docs  
weight: 90  
url: /es/nodejs-cpp/manage-worksheets/  
description: Agregar, quitar y activar hojas de cálculo usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Los desarrolladores pueden crear y administrar fácilmente hojas de cálculo en archivos de Microsoft Excel programáticamente utilizando la API flexible de Aspose.Cells. Este tema describe los enfoques para agregar y eliminar hojas de cálculo en archivos de Microsoft Excel.  
{{% /alert %}}  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en el archivo de Excel.  

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una amplia gama de propiedades y métodos para administrar las hojas.  

## **Añadir hojas de cálculo a un nuevo archivo de Excel**  

Para crear un nuevo archivo de Excel programáticamente:  

1. Cree un objeto de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  
1. Llame al método [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#add-sheettype-) de la clase [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection). Se añade automáticamente una hoja vacía al archivo de Excel. Puede referenciarse pasando el índice de la hoja nueva a la colección [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--).  
1. Obtenga una referencia de la hoja de cálculo.  
1. Realice el trabajo en las hojas de cálculo.  
1. Guarde el archivo de Excel nuevo con hojas de cálculo nuevas llamando al método [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().getCount();
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Añadir hojas de cálculo a una hoja de cálculo de diseñador**  

El proceso de agregar hojas de cálculo a una hoja de cálculo de diseño es igual que el de agregar una nueva hoja, salvo que el archivo de Excel ya existe y debe abrirse antes de agregar hojas. Una hoja de cálculo de diseño puede abrirse utilizando la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

## **Acceso a las hojas de cálculo usando el nombre de la hoja**  

Acceda a cualquier hoja de cálculo especificando su nombre o índice  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing a worksheet using its sheet name
const worksheet = workbook.getWorksheets().get("Sheet1");
const cell = worksheet.getCells().get("A1");
console.log(cell.getValue());
```  

## **Eliminar hojas de cálculo utilizando el nombre de la hoja**  

Para eliminar hojas de cálculos de un archivo, llame al método [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) de la clase [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection). Pase el nombre de la hoja al método [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) para eliminar una hoja específica.  

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

// Removing a worksheet using its sheet name
workbook.getWorksheets().removeAt("Sheet1");

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Eliminar hojas de cálculo utilizando el índice de la hoja**  

Eliminar hojas de trabajo por nombre funciona bien cuando se conoce el nombre de la hoja. Si no conoces el nombre de la hoja, usa una versión sobrecargada del método [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) que toma el índice de la hoja en lugar del nombre de la misma.  

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

// Removing a worksheet using its sheet index
workbook.getWorksheets().removeAt(0);

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Activar hojas y hacer que una celda sea activa en la hoja de cálculo**  

A veces, necesitas que una hoja de trabajo específica esté activa y visible cuando un usuario abre un archivo de Microsoft Excel en Excel. De manera similar, podrías querer activar una celda específica y configurar las barras de desplazamiento para mostrar la celda activa. Aspose.Cells es capaz de realizar todas estas tareas.  

Una **hoja activa** es una hoja en la que está trabajando: el nombre de la hoja activa en la pestaña aparece en negrita de forma predeterminada  

Una **celda activa** es una celda seleccionada, la celda en la que se ingresa datos cuando comienza a escribir. Solo una celda está activa a la vez. La celda activa se resalta con un borde grueso  

### **Activar hojas y hacer que una celda sea activa**  

Aspose.Cells proporciona llamadas específicas a la API para activar una hoja y una celda. Por ejemplo, la propiedad [**WorksheetCollection.getActiveSheetIndex()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getActiveSheetIndex--) es útil para establecer la hoja activa en un libro. De manera similar, la propiedad [**Worksheet.getActiveCell()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getActiveCell--) se usa para establecer y obtener una celda activa en la hoja de cálculo.  

Para asegurarte de que las barras de desplazamiento horizontales o verticales estén en la posición de fila y columna que deseas mostrar datos específicos, usa las propiedades [**Worksheet.getFirstVisibleRow()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleRow--) y [**Worksheet.getFirstVisibleColumn()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleColumn--).  

El siguiente ejemplo muestra cómo activar una hoja de cálculo y hacer que una celda sea activa en ella. En la salida generada, las barras de desplazamiento se desplazarán para que la segunda fila y la segunda columna sean su primera fila y columna visibles  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Add a worksheet if collection is empty
const worksheets = workbook.getWorksheets();
if (worksheets.getCount() === 0) {
worksheets.add();
}

// Get the first worksheet in the workbook.
const worksheet1 = worksheets.get(0);

// Get the cells in the worksheet.
const cells = worksheet1.getCells();

// Input data into B2 cell.
cells.get(1, 1).putValue("Hello World!");

// Set the first sheet as an active sheet.
workbook.getWorksheets().setActiveSheetIndex(0);

// Set B2 cell as an active cell in the worksheet.
worksheet1.setActiveCell("B2");

// Set the B column as the first visible column in the worksheet.
worksheet1.setFirstVisibleColumn(1);

// Set the 2nd row as the first visible row in the worksheet.
worksheet1.setFirstVisibleRow(1);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Temas avanzados**  
- [Copiar y mover hojas de cálculo](/cells/es/nodejs-cpp/copying-and-moving-worksheets/)  
- [Contar el número de celdas en la hoja de cálculo](/cells/es/nodejs-cpp/count-number-of-cells-in-the-worksheet/)  
- [Detectar hojas de cálculo vacías](/cells/es/nodejs-cpp/detecting-empty-worksheets/)  
- [Buscar si la hoja de trabajo es una hoja de diálogo](/cells/es/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [Obtener el ID único de la hoja de trabajo](/cells/es/nodejs-cpp/get-worksheet-unique-id/)  
- [Crear, manipular o eliminar escenarios de hojas de trabajo](/cells/es/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [Gestionar saltos de página](/cells/es/nodejs-cpp/managing-page-breaks/)  
- [Funciones de configuración de página](/cells/es/nodejs-cpp/page-setup-features/)   
- [Utilizar la propiedad SheetId de OpenXml usando Aspose.Cells](/cells/es/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [Vistas de hojas de trabajo](/cells/es/nodejs-cpp/worksheet-views/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
