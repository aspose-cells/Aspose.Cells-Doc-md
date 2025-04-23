---  
title: Автоматическая подгонка строк и столбцов с Node.js через C++  
linktitle: Автоподбор строк и столбцов  
type: docs  
weight: 20  
url: /ru/nodejs-cpp/autofit-rows-and-columns/  
description: В этой статье показано, как автоматически подгонять строки, столбцы, строки объединённых ячеек и строки в диапазоне ячеек с помощью Aspose.Cells for Node.js via C++.  
keywords: Автоматическая подгонка строк Node.js через C++, автоматическая подгонка столбцов Node.js через C++, автоматическая подгонка строки в диапазоне ячеек Node.js через C++, автоматическая подгонка строк объединённых ячеек Node.js через C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel позволяет автоматически масштабировать ширину и высоту ячеек в соответствии с их содержимым. Эта функция также доступна через Aspose.Cells for Node.js via C++, поэтому разработчики могут автоматически изменять размеры ячеек во время выполнения.  
{{% /alert %}}  

## **Автоматическая подгонка размера**  

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получить доступ к каждому листу Excel. Лист представляет класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет широкий спектр свойств и методов для управления листом. В этой статье рассматривается использование класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) для автоматической подгонки строк или столбцов.  

### **Автоматическая подгонка строки - простой**  

Самый простой способ автоматически подогнать ширину и высоту строки — вызвать метод [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Метод [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) принимает индекс строки (подгоняемой) в качестве параметра.  

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

### **Как автоматически подогнать строку в диапазоне ячеек**  

Строка состоит из многих столбцов. Aspose.Cells позволяет автоматически подгонять строку на основе содержимого в диапазоне ячеек внутри строки, вызвав переопределённую версию метода [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-). Он принимает следующие параметры:  

- Индекс строки, индекс строки, которую нужно автоматически подогнать.  
- Индекс первого столбца, индекс первого столбца строки.  
- Индекс последнего столбца, индекс последнего столбца строки.  

Метод [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-) проверяет содержимое всех столбцов в строке и затем автоматически подгоняет ее.  

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

### **Как автоматически подогнать столбец в диапазоне ячеек**  

Столбец состоит из множества строк. Можно автоматически подогнать ширину столбца на основе содержимого в диапазоне ячеек этого столбца, вызывая перегруженную версию метода [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-), который принимает следующие параметры:  

- Индекс столбца, индекс столбца, который нужно автоматически подогнать.  
- Индекс первой строки, индекс первой строки столбца.  
- Индекс последней строки, индекс последней строки столбца.  

Метод [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) проверяет содержимое всех строк в столбце и затем автоматически подгоняет его.  

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

### **Как автоматически подогнать строки для объединенных ячеек**  

С помощью Aspose.Cells возможно автоматически подгонять строки даже для ячеек, объединённых с помощью API [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions). Класс [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) предоставляет свойство [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--), которое можно использовать для автоматической подгонки строк для объединённых ячеек. [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) принимает [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype) перечислимые значения, в которых указаны следующие члены.  

- None: игнорировать объединённые ячейки.  
- FirstLine: расширяет только высоту первой строки.  
- LastLine: расширяет только высоту последней строки.  
- EachLine: расширяет высоту каждой строки.  

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
Также попробуйте использовать перегруженные версии методов [**autoFitRows**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) и [**autoFitColumns**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-), которые принимают диапазон строк/столбцов и экземпляр [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) для автоматической подгонки выбранных строк/столбцов с желаемыми [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) соответственно.  

Подписи указанных методов следующие:  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
1. autoFitColumns(int первыйСтолбец, int последнийСтолбец, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) параметры)  
{{% /alert %}}  

## **Важно знать**  

{{% alert color="primary" %}}  
Если ячейка объединена, то методы autoFit не будут применяться, что соответствует поведению в Microsoft Excel. Можно обойти это, используя API autofilter. Более того, если в ячейке текст обернут, метод [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) также не будет применяться. Еще одна важная особенность: методы *autoFit* требуют много времени. Поэтому вызывайте эти методы как можно реже, чтобы обеспечить эффективность приложения.  
{{% /alert %}}  

## **Продвинутые темы**  
- [AutoFit строк для объединенных ячеек](/cells/ru/nodejs-cpp/autofit-rows-for-merged-cells/)  

