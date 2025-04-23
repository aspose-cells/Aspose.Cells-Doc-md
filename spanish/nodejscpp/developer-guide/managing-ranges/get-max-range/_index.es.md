---  
title: Obtener el rango máximo en una hoja de cálculo con Node.js via C++  
linktitle: Obtener el rango máximo en una hoja de cálculo  
type: docs  
weight: 360  
url: /es/nodejs-cpp/get-max-range-in-a-worksheet/  
description: Este artículo describe cómo obtener el rango máximo, rango de datos máximo y rango de visualización máximo de archivos de Excel usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Al leer datos de la hoja de cálculo, necesitamos conocer el área máxima.  

Al copiar todos los datos de una hoja de cálculo, necesitamos conocer el área máxima.  

Al exportar un área específica a HTML y PDF, debemos conocer el área máxima.  

Aspose.Cells for Node.js via C++ contiene diferentes formas de encontrar el rango máximo en una hoja de cálculo.  

{{% /alert %}}  

## **Obteniendo el rango máximo**  
En Aspose.Cells, si los objetos [**row**](https://reference.aspose.com/cells/nodejs-cpp/row/) y [**column**](https://reference.aspose.com/cells/nodejs-cpp/column/) están inicializados, estas filas y columnas se contarán hasta el área máxima, incluso si no hay datos en filas o columnas vacías.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxRow();
let maxColumn = sheet.getCells().getMaxColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxRow();
maxColumn = sheet.getCells().getMaxColumn();
// The range is updated to A1:B10.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **Obteniendo el rango máximo de datos**  
En la mayoría de los casos, solo necesitamos obtener todos los rangos que contienen todos los datos, incluso si las celdas vacías fuera del rango están formateadas.  
Y la configuración sobre formas, tablas y tablas dinámicas se ignorará.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxDataRow();
let maxColumn = sheet.getCells().getMaxDataColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxDataRow();
maxColumn = sheet.getCells().getMaxDataColumn();
// The range is still A1:B3.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **Obteniendo el rango máximo de visualización**  
Cuando exportamos todos los datos de la hoja de cálculo a HTML, PDF o imágenes, necesitamos obtener un área que contenga todos los objetos visibles, incluidos los datos, estilos, gráficos, tablas y tablas dinámicas.  
Los siguientes códigos muestran cómo renderizar el rango de visualización máxima a HTML:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Gets the max display range.
const range = worksheets.get(0).getCells().getMaxDisplayRange();

// Save the range to html
const saveOptions = new AsposeCells.HtmlSaveOptions();
saveOptions.setExportActiveWorksheetOnly(true);
saveOptions.setExportArea(AsposeCells.CellArea.createCellArea(range.getFirstRow(), range.getFirstColumn(), range.getFirstRow() + range.getRowCount() - 1, range.getFirstColumn() + range.getColumnCount() - 1));

// Save the range.
workbook.save("html.html", saveOptions);
```  

Aquí está el [archivo de excel fuente](Book1.xlsx).  

