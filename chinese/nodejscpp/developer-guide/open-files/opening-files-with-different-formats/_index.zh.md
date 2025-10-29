---
title: 通过 C++ 和 Node.js 打开不同格式的文件
linktitle: 打开不同格式的文件
type: docs
weight: 30
url: /zh/nodejs-cpp/opening-files-with-different-formats/
description: Aspose.Cells for Node.js via C++ API 允许您打开/读取 XLSX、HTML、CSV、ODS、TSV、SXC、FODS 等不同格式。
keywords: 打开 xlsx 文件，打开 html 文件，读取 fods 文件，读取 ods 文件，读取 sxc 文件，打开 csv 文件，表格分隔，电子表格 ML，tsv，mhtml
---

{{% alert color="primary" %}}

使用 Aspose.Cells，您可以打开不同格式的文件。**Aspose.Cells** 可以打开多种文件格式，如 Microsoft Excel 电子表格（XLS，XLSX，XLSM，XLSB），SpreadsheetML，逗号分隔值（CSV），制表符分隔或制表符分隔值（TSV）文件等。

如果您需要了解所有支持的文件格式，请参考以下页面：
[支持的文件格式](https://docs.aspose.com/cells/nodejs-cpp/supported-file-formats/)

{{% /alert %}}

## **打开具有不同格式的文件**

Aspose.Cells 允许开发人员打开具有不同格式的电子表格文件，如电子表格 ML，逗号分隔值（CSV），表格分隔或制表符分隔值（TSV），ODS 文件。 要打开这些文件，开发人员可以使用与打开不同 Microsoft Excel 版本文件相同的方法。

### **打开电子表格 ML 文件**

SpreadsheetML 文件是电子表格的 XML 表示，包括所有相关信息，如格式、公式等。从 Microsoft Excel XP 开始，Microsoft Excel 添加了一个 XML 导出选项，可以将电子表格导出为 SpreadsheetML 文件。

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

### **打开 HTML 文件**

Aspose.Cells 允许您将 HTML 文件打开为工作簿对象。HTML 文件应以 Microsoft Excel 为导向，即 Microsoft Excel 应能打开该文件。

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

### **打开 CSV 文件**

逗号分隔值文件（CSV）包含以逗号分隔的记录。数据存储为表格形式，每列由逗号字符分隔并用双引号括起来。如果字段值包含双引号字符，则用一对双引号转义。你也可以用Microsoft Excel导出电子表格数据为CSV文件。

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

#### **打开 CSV 文件并替换无效字符**

在Excel中，打开带有特殊字符的CSV文件时，字符会自动被替换。Aspose.Cells API也会执行相同操作，以下代码示例演示了这一点。

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

### **使用自定义分隔符打开文本文件**

文本文件用于在不格式化的情况下保存电子表格数据。 文件是一种可以具有一些自定义分隔符的纯文本文件。

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

### **打开制表符分隔文件**

选项卡分隔（文本）文件包含电子表格数据，但没有任何格式。数据以类似表格和电子表格的行和列进行排列。基本上，选项卡分隔文件是一种特殊的纯文本文件，每列之间用制表符分隔。

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

### **打开制表符分隔数值（TSV）文件**

制表符分隔值（TSV）文件包含电子表格数据，但没有任何格式。它与制表符定界文件相同，数据以行和列的形式排列，如表格和电子表格中一样。

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

### **打开SXC文件**

StarOffice Calc 类似于 Microsoft Excel，支持公式、图表、函数和宏。用该软件创建的电子表格保存为 SXC 扩展名。SXC 文件也用于 OpenOffice.org Calc 电子表格文件。Aspose.Cells 可以读取 SXC 文件，如下面的代码示例所示。

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

### **打开FODS文件**

FODS 文件是以 OpenDocument XML 格式保存的不压缩电子表格。Aspose.Cells 可以读取 FODS 文件，示例代码如下。

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

{{< app/cells/assistant language="nodejs-cpp" >}}
