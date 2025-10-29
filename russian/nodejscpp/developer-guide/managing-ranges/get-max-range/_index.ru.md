---  
title: Получить максимальный диапазон на листе с помощью Node.js через C++  
linktitle: Получить максимальный диапазон на рабочем листе  
type: docs  
weight: 360  
url: /ru/nodejs-cpp/get-max-range-in-a-worksheet/  
description: В этой статье описывается, как получать максимальный диапазон, максимальный диапазон данных и максимальный отображаемый диапазон файлов Excel с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

При чтении данных с рабочего листа нам необходимо знать максимальную область.  

При копировании всех данных с рабочего листа нам необходимо знать максимальную область.  

При экспорте определенной области в HTML и PDF необходимо знать максимальную область.  

Aspose.Cells for Node.js via C++ содержит различные способы определения максимального диапазона на листе.  

{{% /alert %}}  

## **Получение максимального диапазона**  
В Aspose.Cells, если объекты [**row**](https://reference.aspose.com/cells/nodejs-cpp/row/) и [**column**](https://reference.aspose.com/cells/nodejs-cpp/column/) инициализированы, эти строки и столбцы будут учитываться при определении максимальной области, даже если в пустых строках или столбцах нет данных.  

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

## **Получение максимального диапазона данных**  
В большинстве случаев нам нужно получить все диапазоны, содержащие все данные, даже если пустые ячейки за пределами диапазона отформатированы.  
И настройки о формах, таблицах и сводных таблицах будут игнорироваться.  

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

## **Получение максимального диапазона отображения**  
Когда мы экспортируем все данные с листа в HTML, PDF или изображения, нам необходимо получить область, содержащую все видимые объекты, включая данные, стили, графику, таблицы и сводные таблицы.  
Следующие коды показывают, как отобразить максимальную дисплей-область в HTML:  

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

Вот [исходный файл Excel](Book1.xlsx).  

{{< app/cells/assistant language="nodejs-cpp" >}}
