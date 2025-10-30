---
title: Node.jsとC++を用いたシートのコピーと移動
linktitle: ワークシートのコピーと移動
type: docs
weight: 10
url: /ja/nodejs-cpp/copying-and-moving-worksheets/
description: この記事では、Node.js APIとC++を使用して、Excelワークブック内およびワークブック間のシートのコピーと移動をプログラム的に行うサンプルコードを含めて説明しています。
keywords: シートのコピー Node.js、シートの移動 Node.js
---

{{% alert color="primary" %}}

時には、共通のフォーマットとデータを持つワークシートの数が必要です。たとえば、四半期予算で作業する場合、同じ列見出し、行見出し、数式を含むシートを持つワークブックを作成したいと思うかもしれません。これを行う方法があります：1つのシートを作成してからコピーすることです。

Aspose.Cells for Node.js via C++は、ワークブック内または間でのシートのコピーと移動をサポートします。データ、書式設定、表、マトリックス、チャート、画像その他のオブジェクトを含むシートは、最高の精度でコピーされます。

{{% /alert %}}

## **Microsoft Excelでシートを移動またはコピーする**

Microsoft Excelでワークブック内またはワークブック間でワークシートをコピーおよび移動する手順は次のとおりです。

1. 別のワークブックにシートを移動またはコピーするには、シートを受け取るワークブックを開きます。
1. 移動またはコピーしたいシートを含むワークブックに切り替え、そのシートを選択します。
1. **編集**メニューで**シートの移動またはコピー**をクリックします。
1. **ブックへ**ダイアログボックスで、シートを受け取るワークブックをクリックします。
1. 選択したシートを新しいワークブックに移動またはコピーするには、**新しいブック**をクリックします。
1. **前のシート**ボックスで、移動またはコピーされたシートが挿入される前のシートをクリックします。
1. 移動ではなくシートをコピーする場合は、**コピーを作成**チェックボックスを選択します。

### **Aspose.Cells for Node.js via C++を使ったワークブック内のシートのコピー**

Aspose.Cellsは[**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#addCopy-number-)というオーバーロードされたメソッドを提供し、これはコレクションにワークシートを追加し、既存のワークシートからデータをコピーするために使用されます。メソッドの1つのバージョンは、ソースワークシートのインデックスをパラメーターとして取ります。もう1つのバージョンは、ソースワークシートの名前をパラメーターとして取ります。

次の例は、ブック内で既存のワークシートをコピーする方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Open an existing Excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to
// the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Copy data to a new sheet from an existing
// sheet within the Workbook.
sheets.addCopy("Sheet1");

// Save the Excel file.
wb.save(path.join(dataDir, "CopyWithinWorkbook_out.xls"));
```

### **ブック間でのワークシートのコピー**

Aspose.Cellsは、[**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-)というメソッドを提供しており、これを使用してソースシートから別のシートへデータと書式設定をコピーします。このメソッドは、ソースシートのオブジェクトをパラメータとして受け取ります。

次の例は、ワークブックから別のワークブックにワークシートをコピーする方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Create a Workbook.
// Open a file into the first book.
const excelWorkbook0 = new AsposeCells.Workbook(inputPath);

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Copy the first sheet of the first book into second book.
excelWorkbook1.getWorksheets().get(0).copy(excelWorkbook0.getWorksheets().get(0));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xls"));
```

次の例は、ワークブックから別のワークブックにワークシートをコピーする方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook.
const excelWorkbook0 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws0 = excelWorkbook0.getWorksheets().get(0);

// Put some data into header rows (A1:A4)
for (let i = 0; i < 5; i++) {
ws0.getCells().get(i, 0).putValue(`Header Row ${i}`);
}

// Put some detail data (A5:A999)
for (let i = 5; i < 1000; i++) {
ws0.getCells().get(i, 0).putValue(`Detail Row ${i}`);
}

// Define a pagesetup object based on the first worksheet.
const pagesetup = ws0.getPageSetup();

// The first five rows are repeated in each page...
// It can be seen in print preview.
pagesetup.setPrintTitleRows("$1:$5");

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Name the worksheet.
ws1.setName("MySheet");

// Copy data from the first worksheet of the first workbook into the
// first worksheet of the second workbook.
ws1.copy(ws0);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetFromWorkbookToOther_out.xls"));
```

### **ワークブック内でのワークシートの移動**

Aspose.Cellsは、同じスプレッドシート内でシートを別の場所に移動するための[**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#moveto-number-)というメソッドも提供しています。このメソッドはターゲットシートのインデックスをパラメータとして受け取ります。

次の例は、ワークブック内でワークシートを別の場所に移動する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "sample1.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get the first worksheet.
const worksheet = sheets.get(0);

// Move the first sheet to the third position in the workbook.
worksheet.moveTo(2);

// Save the excel file.
wb.save(path.join(dataDir, "MoveWorksheet_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
