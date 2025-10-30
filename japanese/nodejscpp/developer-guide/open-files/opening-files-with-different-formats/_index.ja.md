---
title: Node.jsを介してC++で異なるフォーマットのファイルを開く
linktitle: さまざまな形式のファイルを開く
type: docs
weight: 30
url: /ja/nodejs-cpp/opening-files-with-different-formats/
description: Aspose.Cells for Node.js via C++ APIは、XLSX、HTML、CSV、ODS、TSV、SXC、FODSなどのさまざまなフォーマットを開く/読み取ることを可能にします。
keywords: xlsx ファイルを開く、html ファイルを開く、fods ファイルを読む、ods ファイルを読む、sxc ファイルを読む、csv ファイルを開く、タブ区切り、SpreadsheetML、tsv、mhtml
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、さまざまなフォーマットのファイルを開くことができます。**Aspose.Cells**は、Microsoft Excelのスプレッドシート（XLS、XLSX、XLSM、XLSB）、SpreadsheetML、カンマ区切り値（CSV）、タブ区切りまたはTSVファイルなどを開くことが可能です。

すべてのサポートされるファイル形式を知りたい場合は、次のページを参照してください:
[サポートされているファイル形式](https://docs.aspose.com/cells/nodejs-cpp/supported-file-formats/)

{{% /alert %}}

## **異なるフォーマットのファイルを開く**

Aspose.Cells は、SpreadsheetML、コンマ区切り値（CSV）、タブ区切りまたはタブ区切り値（TSV）、ODS ファイルなどの異なる形式のスプレッドシートファイルを開くことができます。このようなファイルを開くには、開く異なる Microsoft Excel バージョンのファイルを開くときと同じ方法を使用できます。

### **SpreadsheetML ファイルを開く**

SpreadsheetMLファイルは、書式設定や数式など、スプレッドシートに関するすべての情報を含むXMLによるスプレッドシートの表現です。Microsoft Excel XP以降に、ExcelにはスプレッドシートをSpreadsheetMLファイルにエクスポートするXMLエクスポートオプションが追加されました。

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

### **HTML ファイルを開く**

Aspose.Cellsは、HTMLファイルをWorkbookオブジェクトに開くことを可能にします。HTMLファイルはMicrosoft Excel向きである必要があります。つまり、MS-Excelが開くことができる必要があります。

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

### **CSV ファイルを開く**

カンマ区切り値（CSV）ファイルは、値がカンマで区切られたレコードを含みます。データは表として保存され、各列はカンマ文字で区切られ、二重引用符で囲まれています。フィールド値に二重引用符が含まれる場合、それは二重引用符のペアでエスケープされます。Microsoft Excelを使用してスプレッドシートデータをCSVにエクスポートすることもできます。

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

#### **CSV ファイルを開くと無効な文字を置換する**

Excelで、特殊文字を含むCSVファイルを開くと、文字が自動的に置き換えられます。Aspose.Cells APIも同様に動作し、以下のコード例で示します。

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
const filePath = path.join(dataDir, "Book1TabDelimited.txt");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(filePath, loadOptions5);
console.log("Tab delimited file opened successfully!");
```

### **タブ区切り値（TSV）ファイルを開く**

TSV（タブ区切り値）ファイルは、書式設定なしのスプレッドシートデータを含みます。これは、タブ区切りファイルと同じで、データは表やスプレッドシートのように行と列に配置されます。

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

### **SXCファイルを開く**

StarOffice CalcはMicrosoft Excelに似ており、数式、チャート、関数、マクロをサポートします。このソフトウェアで作成されたスプレッドシートはSXC拡張子で保存されます。SXCファイルは、OpenOffice.org Calcのスプレッドシートファイルにも使用されます。Aspose.CellsはSXCファイルを読み取ることができます（以下のコード例による）。

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

### **FODSファイルを開く**

FODSファイルは、圧縮なしのOpenDocument XMLとして保存されたスプレッドシートです。Aspose.Cellsは、FODSファイルを読み取ることもできます（以下のコード例による）。

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
