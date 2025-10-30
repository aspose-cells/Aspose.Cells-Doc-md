---  
title: Copiar filas y columnas con Node.js mediante C++  
linktitle: Copiando Filas y Columnas  
type: docs  
weight: 40  
url: /es/nodejs-cpp/copying-rows-and-columns/  
description: Este artículo muestra cómo copiar filas y columnas a través de la API Aspose.Cells for Node.js via C++.  
keywords: Node.js mediante C++, Cómo copiar filas y columnas, Copiar filas en Node.js, Copiar columnas usando Node.js, Cómo pegar filas y columnas usando Aspose.Cells for Node.js via C++, Pegar varias filas y columnas, Cómo copiar y pegar una fila o columna individual.  
---  

## **Introducción**  

A veces, necesitas copiar filas y columnas en una hoja de cálculo sin copiar toda la hoja. Con Aspose.Cells, es posible copiar filas y columnas dentro o entre libros de trabajo.  
Cuando se copia una fila (o columna), se copia también los datos contenidos en ella, incluidas fórmulas - con referencias actualizadas - y valores, comentarios, formato de celdas, celdas ocultas, imágenes y otros objetos de dibujo.  

## **Cómo copiar filas y columnas con Microsoft Excel**  

1. Selecciona la fila o columna que deseas copiar.  
1. Para copiar filas o columnas, haz clic en **Copiar** en la barra de herramientas **Estándar**, o presiona **CTRL**+**C**.  
1. Selecciona una fila o columna debajo o a la derecha de donde deseas copiar tu selección.  
1. Al copiar filas o columnas, haz clic en **Celdas Copiadas** en el menú **Insertar**.  

{{% alert color="primary" %}}  
Si haces clic en **Pegar** en la barra de herramientas **Estándar** o presionas **CTRL**+**V** en lugar de hacer clic en un comando en el menú **Insertar**, cualquier contenido de las celdas de destino se reemplaza.  
{{% /alert %}}  

## **Cómo pegar filas y columnas usando opciones de pegado con Microsoft Excel**  

1. Selecciona las celdas que contienen los datos u otros atributos que desees copiar.  
1. En la pestaña Inicio, haz clic en **Copiar**.  
1. Haz clic en la primera celda en el área donde quieras **pegar** lo que copiaste.  
1. En la pestaña Inicio, haz clic en la flecha junto a **Pegar**, y luego selecciona **Pegado especial**.  
1. Selecciona las **opciones** que desees.  

## **Cómo copiar filas y columnas usando Aspose.Cells for Node.js via C++**  

## **Cómo copiar filas individuales**  

Aspose.Cells proporciona el método [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) de la clase [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Este método copia todo tipo de datos incluyendo fórmulas, valores, comentarios, formatos de celdas, celdas ocultas, imágenes y otros objetos de dibujo desde la fila fuente a la fila de destino.  

El método [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) toma los siguientes parámetros:  

- el objeto fuente [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells),  
- el índice de fila de origen, y  
- el índice de fila de destino.  

Utilice este método para copiar una fila dentro de una hoja o a otra hoja. El método [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) funciona de manera similar a Microsoft Excel. Por ejemplo, no necesita establecer explícitamente la altura de la fila de destino, ese valor también se copia.  

El siguiente ejemplo muestra cómo copiar una fila en una hoja de cálculo. Utiliza un archivo de Microsoft Excel plantilla y copia la segunda fila (completa con datos, formato, comentarios, imágenes, etc.) y la pega en la fila 12 en la misma hoja.  

Puede omitir el paso que obtiene la altura de la fila fuente usando el método [**Cells.getRowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRowHeight-number-boolean-cellsunittype-) y luego establece la altura de la fila de destino usando el método [**Cells.setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-), ya que el método [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) se encarga automáticamente de la altura de la fila.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the first worksheet in the workbook.
const wsTemplate = excelWorkbook1.getWorksheets().get(0);

// Copy the second row with data, formattings, images and drawing objects
// To the 16th row in the worksheet.
wsTemplate.getCells().copyRow(wsTemplate.getCells(), 1, 15);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Al copiar filas, es importante tener en cuenta las imágenes relacionadas, gráficos u otros objetos de dibujo, ya que es lo mismo que en Microsoft Excel:  

1. Si el índice de fila de origen es 5, la imagen, el gráfico, etc., se copian si están contenidos en las tres filas (el índice de fila de inicio es 4 y el índice de fila final es 6).  
1. Las imágenes, gráficos, etc. existentes en la fila de destino no se eliminarán.  
{{% /alert %}}  

## **Cómo Copiar Múltiples Filas**  

También puede copiar varias filas en un nuevo destino usando el método [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-), que toma un parámetro adicional de tipo entero para especificar el número de filas fuente que se copiarán.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Copy the first 3 rows to 7th row
cells.copyRows(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Cómo Copiar Columnas**  

Aspose.Cells proporciona el método [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) de la clase [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), este método copia todos los tipos de datos, incluidas fórmulas — con referencias actualizadas — y valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo desde la columna fuente a la columna de destino.  

El método [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) toma los siguientes parámetros:  

- el objeto fuente [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells),  
- índice de columna de origen, y  
- el índice de columna de destino.  

Utilice el método [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) para copiar una columna dentro de una hoja o a otra hoja.  

Este ejemplo copia una columna de una hoja de cálculo y la pega en una hoja de cálculo en otro libro.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook(filePath);

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Copy the first column from the first worksheet of the first workbook into
// The first worksheet of the second workbook.
ws1.getCells().copyColumn(ws1.getCells(), ws1.getCells().getColumns().get(0).getIndex(), ws1.getCells().getColumns().get(2).getIndex());

// Autofit the column.
ws1.autoFitColumn(2);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

## **Cómo Copiar Múltiples Columnas**  

Similar al método [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-), las API de Aspose.Cells también proporcionan el método [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) para copiar múltiples columnas fuente a una nueva ubicación.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));

// Get the first worksheet's cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Copy the first 3 columns to the 7th column
cells.copyColumns(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Cómo Pegar Filas y Columnas con Opciones de Pegado**  

Aspose.Cells ahora proporciona [**PasteOptions**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/) al usar las funciones [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) y [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-). Permite configurar una opción de pegado adecuada similar a Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeChartDataSource.xlsx"));

// Access the first sheet which contains chart
const source = workbook.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = workbook.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Set PasteOptions
const pasteOptions = new AsposeCells.PasteOptions();
pasteOptions.setPasteType(AsposeCells.PasteType.Values);
pasteOptions.setOnlyVisibleCells(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options, pasteOptions);

// Save workbook in xlsx format
workbook.save(path.join(outputDir, "outputChangeChartDataSource.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
