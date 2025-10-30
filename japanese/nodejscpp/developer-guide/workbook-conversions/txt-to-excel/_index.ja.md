---  
title: CSV、TSV、TXTをExcelに変換する  
linktitle: CSV、TSV、TXTをExcelに変換する  
type: docs  
weight: 30  
url: /ja/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/  
---  

{{% alert color="primary" %}}  
Aspose.Cellsを使えば、CSVファイルをExcel、OpenOffice、PDF、JSONなど多くのフォーマットに変換できます。  
{{% /alert %}}  

## **CSV ファイルを開く**  

コンマ区切り値（CSV）ファイルには、値がコンマで区切られたレコードが含まれています。データは、各列がコンマ文字で区切られ、二重引用符で引用された表として保存されます。フィールド値に二重引用符文字が含まれる場合は、それを二重引用符文字のペアでエスケープします。Microsoft Excel を使用してスプレッドシートデータを CSV にエクスポートすることもできます。  

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

## **CSV ファイルを開くと無効な文字を置換する**  

Excelで、特殊文字を含むCSVファイルを開くと、文字が自動的に置き換えられます。Aspose.Cells APIも同様に動作し、以下のコード例で示します。  

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


### **カスタム区切り記号を使用してテキストファイルを開く**  

テキストファイルは、書式なしでスプレッドシートデータを保持するために使用されます。この種のファイルは、カスタマイズされた区切り記号を持つプレーンテキストファイルです。  

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

### **タブ区切りファイルを開く**  

タブ区切り（テキスト）ファイルはスプレッドシートのデータを含みますが、フォーマットはありません。データは表やスプレッドシートのように行と列に配置され、基本的には各列の間にタブが挿入されたプレーンテキストファイルです。  

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

### **タブ区切り値（TSV）ファイルを開く**  

タブ区切り値（TSV）ファイルもスプレッドシートのデータを含み、フォーマットはありません。これは、データが行と列に配置されている点で、タブ区切り（Tab Delimited）ファイルと同じです。  

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

## **高度なトピック**  
- [数式を持つCSVファイルを読み込むまたはインポートする](/cells/ja/nodejs-cpp/load-or-import-csv-file-with-formulas/)  
- [複数のエンコーディングを持つCSVファイルの読み込み](/cells/ja/nodejs-cpp/reading-csv-file-with-multiple-encodings/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
