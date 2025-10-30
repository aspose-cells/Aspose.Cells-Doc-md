---
title: Node.jsをC++経由で使ってファイルを開くさまざまな方法
linktitle: ファイルを開くさまざまな方法
type: docs
weight: 10
url: /ja/nodejs-cpp/different-ways-to-open-files/
description: この記事では、Aspose.Cells for Node.js via C++ APIを使ってExcelファイルを開く方法を解説します。
keywords: Node.jsでExcelファイルをExcelを使わずに開く方法、Node.jsを使ってExcelファイルを開くにはどうすればいいですか。
---

{{% alert color="primary" %}}

Aspose.Cellsを利用すれば、ファイルを開いてデータを取得したり、デザイナーテンプレートを使用して開発の効率化を図ることが簡単にできます。

{{% /alert %}}

## **パスを使用してExcelファイルを開く方法**

開発者は、ローカルコンピュータ上のファイルパスを指定して、そのMicrosoft Excelファイルを[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスのコンストラクタに渡すことで開くことができます。パスは単に*文字列*として渡してください。Aspose.Cellsは自動的にファイルのフォーマットタイプを認識します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(filePath);
console.log("Workbook opened using path successfully!");
```

## **ストリームを使用してExcelファイルを開く方法**

Excelファイルをストリームとして開くのも簡単です。そのためには、ファイルを含む*Stream*オブジェクトを受け取るオーバーロードされたコンストラクタのバージョンを使用します。

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book2.xls");
// Opening through Stream
// Create a Stream object
const fstream = fs.createReadStream(filePath);

// Creating a Workbook object, open the file from a Stream object
// That contains the content of file and it should support seeking
const chunks = [];
fstream.on('data', (chunk) => {
chunks.push(chunk);
```

## **データだけを含むファイルを開く方法**

データのみのファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)クラスと[**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter)クラスを使用して、読み込むテンプレートファイルのクラスの関連属性とオプションを設定します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load only specific sheets with data and formulas
// Other objects, items etc. would be discarded

// Instantiate LoadOptions specified by the LoadFormat
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Set LoadFilter property to load only data & cell formatting
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), loadOptions);
console.log("File data imported successfully!");
```

## **表示されているシートのみを読み込む方法**

[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)のロード中に、時にはワークブック内の表示されているシートのデータだけが必要な場合があります。Aspose.Cellsは、ワークブックのロード時に非表示のシートのデータをスキップすることを可能にします。これを行うには、[**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter)クラスを継承したカスタム関数を作成し、そのインスタンスを[**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--)プロパティに渡します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sampleFile = "output.xlsx";
const samplePath = path.join(dataDir, sampleFile);

// Create a sample workbook
// and put some data in first cell of all 3 sheets
const createWorkbook = new AsposeCells.Workbook();
createWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet2").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet3").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().get("Sheet3").setIsVisible(false);
createWorkbook.save(samplePath);

// Load the sample workbook
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setLoadFilter(new AsposeCells.LoadFilter()); // Corrected line by defining LoadFilter properly

const loadWorkbook = new AsposeCells.Workbook(samplePath, loadOptions);
console.log(`Sheet1: A1: ${loadWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A2: ${loadWorkbook.getWorksheets().get("Sheet2").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A3: ${loadWorkbook.getWorksheets().get("Sheet3").getCells().get("A1").getValue()}`);
```

こちらは、上記のスニペットで参照されている*CustomLoad*クラスの実装例です。

```javascript
const { Workbook, LoadDataFilterOptions } = require("aspose.cells.node");

class CustomLoad {
startSheet(sheet) {
if (sheet.isVisible()) {
// Load everything from visible worksheet
this.loadDataFilterOptions = LoadDataFilterOptions.All;
} else {
// Load nothing
this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
}
}
}
```

{{% alert color="primary" %}}

Aspose.Cellsを使用して、ネイティブでないExcelファイルや他のファイル形式（例：PPT/PPTX、DOC/DOCXなど）を開こうとすると例外がスローされます。

{{% /alert %}} 

{{% alert color="primary" %}}

大規模なスプレッドシートを読み込む際に、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)コンストラクタが*OutOfMemoryError*をスローする可能性が高くなります。この例外は、利用可能なメモリが十分でなく、完全にスプレッドシートをメモリに読み込むことができないことを示しています。そのため、メモリ設定を有効にしてスプレッドシートを読み込みます。

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
