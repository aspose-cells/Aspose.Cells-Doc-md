---  
title: Конвертация CSV, TSV и TXT в Excel с Node.js через C++  
linktitle: Преобразование CSV, TSV и TXT в Excel  
type: docs  
weight: 30  
url: /ru/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/  
---  

{{% alert color="primary" %}}  
Используя Aspose.Cells, вы можете конвертировать файлы CSV в Excel, OpenOffice, PDF, JSON и многие другие форматы.  
{{% /alert %}}  

## **Открытие файлов CSV**  

Файлы с разделенными запятыми (CSV) содержат записи, в которых значения разделены запятыми. Данные хранятся в виде таблицы, где каждый столбец разделен запятой и заключен в кавычки. Если значение поля содержит символ двойной кавычки, он экранируется парой символов двойной кавычки. Вы также можете использовать Microsoft Excel для экспорта данных электронных таблиц в CSV.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(path.join(dataDir, "Book_CSV.csv"), loadOptions4);
console.log("CSV file opened successfully!");
```  

## **Открытие файлов CSV и замена недопустимых символов**  

При открытии файла CSV с особыми символами в Excel символы автоматически заменяются. То же самое выполняет API Aspose.Cells, демонстрированный в приведённом ниже коде.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const options = new AsposeCells.TxtLoadOptions();
options.setSeparator(",");
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
options.setCheckExcelRestriction(false);
options.setConvertNumericData(false);
options.setConvertDateTimeData(false);
// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, options);

console.log(workbook.getWorksheets().get(0).getName()); // (20180220142533)(ASPOSE_CELLS_T
console.log(workbook.getWorksheets().get(0).getName().length); // 31
console.log("CSV file opened successfully!");
```  


### **Открытие текстовых файлов с пользовательским разделителем**  

Текстовые файлы используются для хранения данных электронных таблиц без форматирования. Файл является своего рода обычным текстовым файлом, в котором могут быть использованы некоторые настраиваемые разделители.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book11.csv");

// Instantiate Text File's LoadOptions
const txtLoadOptions = new AsposeCells.TxtLoadOptions();

// Specify the separator
txtLoadOptions.setSeparator(",");

// Specify the encoding type
txtLoadOptions.setEncoding(AsposeCells.EncodingType.UTF8);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, txtLoadOptions);

// Save file
wb.save(path.join(dataDir, "output.txt"));
```  

### **Открытие файлов с разделителями табуляции**  

Файлы с разделением табуляцией (Text) содержат данные таблицы без форматирования. Данные расположены по строкам и столбцам, как в таблицах и электронных таблицах. По сути, файл с разделителем табуляции — это особый вид обычного текстового файла с табулятором между столбцами.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening Tab Delimited Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(path.join(dataDir, "Book1TabDelimited.txt"), loadOptions5);
console.log("Tab delimited file opened successfully!");
```  

### **Открытие файлов со значениями, разделенными табуляцией (TSV)**  

Файлы с разделителями табуляции (TSV) содержат данные таблицы, но без форматирования. Это то же самое, что и файл с разделителями табуляцией, где данные расположены по строкам и столбцам, как в таблицах и электронных таблицах.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Tsv);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTSVFile.tsv"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log("Cell Name: " + cell.getName() + " Value: " + cell.getStringValue());
```  

## **Продвинутые темы**  
- [Загрузить или импортировать файл CSV с формулами](/cells/ru/nodejs-cpp/load-or-import-csv-file-with-formulas/)  
- [Чтение файла CSV с различными кодировками](/cells/ru/nodejs-cpp/reading-csv-file-with-multiple-encodings/)  


