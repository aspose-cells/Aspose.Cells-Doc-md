---  
title: Найти максимальное количество поддерживаемых строк и столбцов в форматах XLS и XLSX с помощью Node.js через C++  
linktitle: Найдите максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX  
type: docs  
weight: 20  
url: /ru/nodejs-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/  
---  

## **Возможные сценарии использования**  

Различные форматы Excel поддерживают разное количество строк и столбцов. Например, XLS поддерживает 65536 строк и 256 столбцов, а XLSX — 1048576 строк и 16384 столбца. Если хотите узнать, сколько строк и столбцов поддерживает конкретный формат, используйте свойства [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) и [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--).  

## **Найдите максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX**  

Следующий пример создает рабочую книгу сначала в формате XLS, затем в XLSX. После создания он выводит значения свойств [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) и [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--). Пожалуйста, ознакомьтесь с выводом в консоли приведенного ниже кода для справки.  

## **Образец кода**  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Print message about XLS format.
console.log("Maximum Rows and Columns supported by XLS format.");

// Create workbook in XLS format.
let wb = new AsposeCells.Workbook(AsposeCells.FileFormatType.Excel97To2003);

// Print the maximum rows and columns supported by XLS format.
let maxRows = wb.getSettings().getMaxRow() + 1;
let maxCols = wb.getSettings().getMaxColumn() + 1;
console.log("Maximum Rows: " + maxRows);
console.log("Maximum Columns: " + maxCols);
console.log();

// Print message about XLSX format.
console.log("Maximum Rows and Columns supported by XLSX format.");

// Create workbook in XLSX format.
wb = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Print the maximum rows and columns supported by XLSX format.
maxRows = wb.getSettings().getMaxRow() + 1;
maxCols = wb.getSettings().getMaxColumn() + 1;
console.log("Maximum Rows: " + maxRows);
console.log("Maximum Columns: " + maxCols);
```  

## **Вывод в консоль**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}  

