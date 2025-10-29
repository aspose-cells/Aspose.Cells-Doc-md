---  
title: Копирование строк и столбцов с Node.js через C++  
linktitle: Копирование строк и колонок  
type: docs  
weight: 40  
url: /ru/nodejs-cpp/copying-rows-and-columns/  
description: Эта статья показывает, как копировать строки и столбцы с помощью API Aspose.Cells for Node.js via C++.  
keywords: Node.js через C++, как копировать строки и столбцы, копировать строки в Node.js, копировать столбцы с помощью Node.js, как вставлять строки и столбцы с помощью Aspose.Cells for Node.js via C++, вставлять несколько строк и столбцов, как копировать и вставлять одну строку или столбец.  
---  

## **Введение**  

Иногда вам нужно скопировать строки и столбцы в рабочем листе без копирования всего листа. С помощью Aspose.Cells это возможно скопировать строки и столбцы внутри или между книгами.  
При копировании строки (или столбца) копируются также содержащиеся в нем данные, включая формулы - с обновленными ссылками - и значения, комментарии, форматирование, скрытые ячейки, изображения и другие объекты рисования.  

## **Как скопировать строки и столбцы с помощью Microsoft Excel**  

1. Выберите строку или колонку, которую вы хотите скопировать.  
1. Чтобы скопировать строки или колонки, нажмите **Копировать** на панели **Стандартные функции** или нажмите **CTRL**+**C**.  
1. Выберите строку или колонку ниже или справа от места, куда вы хотите скопировать ваш выбор.  
1. При копировании строк или колонок нажмите **Скопированные ячейки** на меню **Вставка**.  

{{% alert color="primary" %}}  
Если вы щелкнете **Вставить** на панели инструментов **Стандарт** или нажмете **CTRL**+**V** вместо того, чтобы щелкнуть команду на вкладке **Вставка**, содержимое ячеек назначения будет заменено.  
{{% /alert %}}  

## **Как вставить строки и столбцы с использованием опций вставки в программе Microsoft Excel**  

1. Выберите ячейки, содержащие данные или другие параметры, которые вы хотите скопировать.  
1. На вкладке "Главная" нажмите **Копировать**.  
1. Щелкните первую ячейку в области, куда вы хотите **вставить** скопированное.  
1. На вкладке "Главная" щелкните стрелку рядом с **Вставить**, затем выберите **Специальная вставка**.  
1. Выберите нужные **опции**.  

## **Как копировать строки и столбцы с помощью Aspose.Cells for Node.js via C++**  

## **Как скопировать отдельные строки**  

Aspose.Cells предоставляет метод [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) класса [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Этот метод копирует все типы данных, включая формулы, значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходной строки в целевую.  

Метод [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) принимает следующие параметры:  

- исходный объект [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells),  
- индекс исходной строки, и  
- индекс строки назначения.  

Используйте этот метод для копирования строки внутри листа или в другой лист. Метод [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) работает аналогично в Microsoft Excel. Например, вам не нужно явно задавать высоту целевой строки — это значение также копируется.  

Следующий пример показывает, как скопировать строку в листе. Используется шаблонный файл Excel, копируется вторая строка (со всеми данными, форматами, комментариями, изображениями и т. д.) и вставляется на 12-ую строку того же листа.  

Можно пропустить шаг получения высоты исходной строки, используя метод [**Cells.getRowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRowHeight-number-boolean-cellsunittype-), а затем установить высоту целевой строки методом [**Cells.setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-), потому что метод [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) автоматически позаботится о высоте строки.  

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
При копировании строк важно учитывать связанные изображения, диаграммы или другие объекты рисования, так же как и в Microsoft Excel:  

1. Если индекс исходной строки равен 5, изображение, диаграмма и т. д. копируются, если они содержатся в трех строках (начальный индекс строки равен 4, а конечный индекс строки равен 6).  
1. Существующие изображения, диаграммы и т. д. в целевой строке не будут удалены.  
{{% /alert %}}  

## **Как скопировать несколько строк**  

Также можно копировать несколько строк на новую позицию, используя метод [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-), который принимает дополнительный целочисленный параметр, указывающий количество копируемых исходных строк.  

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

## **Как копировать столбцы**  

Aspose.Cells предоставляет метод [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) класса [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), который копирует все типы данных, включая формулы — с обновленными ссылками — и значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходного столбца в целевой.  

Метод [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) принимает следующие параметры:  

- исходный объект [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells),  
- индекс исходного столбца, и  
- индекс столбца назначения.  

Используйте метод [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) для копирования столбца внутри листа или в другой лист.  

В этом примере копируется столбец из листа и вставляется в лист другой книги.  

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

## **Как скопировать несколько столбцов**  

Аналогично методу [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-), API Aspose.Cells также предоставляет метод [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) для копирования нескольких исходных столбцов в новое место.  

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

## **Как вставить строки и столбцы с параметрами вставки**  

Теперь Aspose.Cells предоставляет [**PasteOptions**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/) при использовании функций [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) и [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-). Это позволяет установить соответствующий параметр вставки, аналогичный Excel.  

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
