---  
title: 通过 Node.js 结合 C++ 将 CSV、TSV 和 TXT 转换为 Excel  
linktitle: 将 CSV、TSV 和 TXT 转换为 Excel  
type: docs  
weight: 30  
url: /zh/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/  
---  

{{% alert color="primary" %}}  
 使用 Aspose.Cells，可以将 CSV 文件转换为 Excel、OpenOffice、PDF、JSON 等多种格式。  
{{% /alert %}}  

## **打开 CSV 文件**  

逗号分隔值（CSV）文件包含记录，其中值由逗号分隔。 数据存储为表格，其中每列由逗号字符分隔并由双引号字符引用。 如果字段值包含双引号字符，则用一对双引号字符进行转义。 您还可以使用 Microsoft Excel 将电子表格数据导出到 CSV。  

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

## **打开 CSV 文件并替换无效字符**  

在Excel中，打开带有特殊字符的CSV文件时，字符会自动被替换。Aspose.Cells API也会执行相同操作，以下代码示例演示了这一点。  

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
// Opening Tab Delimited Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(path.join(dataDir, "Book1TabDelimited.txt"), loadOptions5);
console.log("Tab delimited file opened successfully!");
```  

### **打开制表符分隔数值（TSV）文件**  

Tab分隔值（TSV）文件包含电子表格数据，但没有任何格式。它与Tab分隔文件相同，数据以行和列的形式排列。  

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

## **高级主题**  
- [加载或导入带公式的CSV文件](/cells/zh/nodejs-cpp/load-or-import-csv-file-with-formulas/)  
- [读取带有多种编码的CSV文件](/cells/zh/nodejs-cpp/reading-csv-file-with-multiple-encodings/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
