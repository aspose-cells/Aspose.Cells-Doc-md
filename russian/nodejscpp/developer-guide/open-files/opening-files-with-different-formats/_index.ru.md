---
title: Открытие файлов с разными форматами с помощью Node.js через C++
linktitle: Открытие файлов с различными форматами
type: docs
weight: 30
url: /ru/nodejs-cpp/opening-files-with-different-formats/
description: API Aspose.Cells for Node.js via C++ позволяет открывать/читать файлы различных форматов, таких как XLSX, HTML, CSV, ODS, TSV, SXC, FODS и др.
keywords: открыть файлы xlsx, открыть файлы html, прочитать файлы fods, прочитать файлы ods, прочитать файлы sxc, открыть файлы csv, Табличный разделитель, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

С помощью Aspose.Cells вы можете открывать файлы разных форматов. **Aspose.Cells** поддерживает широкий спектр форматов, таких как таблицы Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, значения через запятую (CSV), файлы с разделителями табуляции или TSV и другие.

Если вам нужно знать все поддерживаемые форматы файлов, обратитесь к следующим страницам:
[Поддерживаемые форматы файлов](https://docs.aspose.com/cells/nodejs-cpp/supported-file-formats/)

{{% /alert %}}

## **Открытие файлов с различными форматами**

Aspose.Cells позволяет разработчикам открывать файлы электронных таблиц различных форматов, такие как SpreadsheetML, файлы, разделенные запятыми (CSV), файлы с разделителями табуляции или табулированные значения (TSV), файлы ODS. Для открытия таких файлов разработчики могут использовать тот же метод, который они используют для открытия файлов различных версий Microsoft Excel.

### **Открытие файлов SpreadsheetML**

Файлы SpreadsheetML — это XML-представление таблиц с полной информацией о форматировании, формулах и др. Начиная с Microsoft Excel XP, добавлена возможность экспорта в XML, которая сохраняет таблицы в виде файлов SpreadsheetML.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening SpreadsheetML Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions3 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.SpreadsheetML);

// Create a Workbook object and opening the file from its path
const wbSpreadSheetML = new AsposeCells.Workbook(path.join(dataDir, "Book3.xml"), loadOptions3);
console.log("SpreadSheetML file opened successfully!");
```

### **Открытие файлов HTML**

Aspose.Cells позволяет открыть HTML-файл в объекте Workbook. HTML-файл должен быть предназначен для Microsoft Excel, то есть его сможет открыть MS-Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.html");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, loadOptions);

// Save the MHT file
wb.save(`${filePath}output.xlsx`);
```

### **Открытие файлов CSV**

Файлы Значения, разделённые запятыми (CSV), содержат записи, где значения разделены запятыми. Данные хранятся в виде таблицы, где каждый столбец разделён запятой и заключён в двойные кавычки. Если значение поля содержит двойную кавычку, она экранируется парой двойных кавычек. Также можно экспортировать данные таблицы в CSV с помощью Microsoft Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_CSV.csv");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);

// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(filePath, loadOptions4);
console.log("CSV file opened successfully!");
```

#### **Открытие файлов CSV и замена недопустимых символов**

При открытии файла CSV с особыми символами в Excel символы автоматически заменяются. То же самое выполняет API Aspose.Cells, демонстрированный в приведённом ниже коде.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const loadOptions = new AsposeCells.TxtLoadOptions();
loadOptions.setSeparator(';');
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
loadOptions.setCheckExcelRestriction(false);
loadOptions.setConvertNumericData(false);
loadOptions.setConvertDateTimeData(false);

// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, loadOptions);


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
const filePath = path.join(dataDir, "Book1TabDelimited.txt");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(filePath, loadOptions5);
console.log("Tab delimited file opened successfully!");
```

### **Открытие файлов со значениями, разделенными табуляцией (TSV)**

Файл с разделёнными табуляцией (TSV) содержит таблицу данных без форматирования. Аналогичен файлу с разделителем табуляции, где данные расположены по строкам и столбцам, как в таблицах и рабочих листах.

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

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **Открытие файлов SXC**

StarOffice Calc похож на Microsoft Excel и поддерживает формулы, диаграммы, функции и макросы. Таблицы, созданные этим программным обеспечением, сохраняются с расширением SXC. Такой же формат используется для файлов таблиц OpenOffice.org Calc. Aspose.Cells может читать файлы SXC, что демонстрируется в следующем примере кода.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Sxc);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleSXC.sxc"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **Открытие файлов FODS**

Файл FODS — это таблица, сохранённая в формате OpenDocument XML без сжатия. Aspose.Cells может читать файлы FODS, что показано в следующем примере кода.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Fods);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleFods.fods"), loadOptions);

console.log("FODS file opened successfully!");
```

