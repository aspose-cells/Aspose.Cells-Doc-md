---
title: ワークブック内外でワークシートをコピーおよび移動するNode.js経由のC++サンプル
linktitle: ワークブック内およびワークブック間でワークシートをコピーおよび移動する
type: docs
weight: 80
url: /ja/nodejs-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Aspose.Cells for Node.js via C++を使ったワークブック内外でのワークシートのコピーと移動方法を学び、効率的にワークブック構造を管理します。
---

{{% alert color="primary" %}}

時には、共通の書式設定およびデータ入力の複数のワークシートが必要なことがあります。例えば、四半期予算を扱う場合、同じ列見出し、行見出し、および数式を含むシートを作成したいかもしれません。これを行う方法があります。1つのシートを作成し、それを3回コピーすることです。

Aspose.Cells for Node.js via C++は、ワークブック内外でのワークシートのコピーや移動をサポートします。データ、書式設定、表、マトリクス、チャート、画像、その他のオブジェクトも高精度でコピーされます。

{{% /alert %}}

## **ワークシートのコピーおよび移動**

### **ワークブック内のワークシートのコピー**

すべての例で最初のステップは同じです。

1. Microsoft Excelにデータを含む2つのワークブックを作成します。この例では、Microsoft Excelで新しいワークブックを2つ作成し、ワークシートにデータを入力しました。

- FirstWorkbook.xlsx（3枚のワークシート）。
- SecondWorkbook.xlsx（1枚のワークシート）。

1. Aspose.Cellsをダウンロードしてインストールします。
   1. [Aspose.Cells for Node.js via C++をダウンロード](https://downloads.aspose.com/cells/nodejs-cpp)。
   1. 開発コンピュータにインストールします。
      すべての[Aspose](http://www.aspose.com/)コンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限がなく、生成された文書にウォーターマークしか挿入されません。
1. プロジェクトを作成します。
   1. 開発環境を開始します。
   1. 新しいコンソールアプリケーションを作成します。
1. 参照を追加します。
   1. Aspose.Cells をプロジェクトに追加します。
      例として、...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dllへのリファレンスを追加します。
1. ワークブック内のワークシートをコピーします。
   最初の例では、FirstWorkbook.xlsx の最初のワークシート（Copy）をコピーします。

このコードを実行すると、ワークシート「Copy」が「Last Sheet」としてFirstWorkbook.xlsx内にコピーされます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open a file into the first book.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "FirstWorkbook.xlsx"));

// Copy the first sheet of the first book within the workbook
excelWorkbook1.getWorksheets().get(2).copy(excelWorkbook1.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "FirstWorkbookCopied_out.xlsx"));
```

### **ワークブック内のワークシートを移動**

以下のコードは、ワークブック内のワークシートを別の位置に移動する方法を示しています。このコードを実行すると、FirstWorkbook.xlsx内でインデックス1の「Move」という名前のワークシートがインデックス2に移動します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "FirstWorkbook.xlsx");
// Open a file into the first book.
const excelWorkbook2 = new AsposeCells.Workbook(filePath);

// Move the sheet
const worksheets = excelWorkbook2.getWorksheets();
const worksheet = worksheets.get(0);
worksheet.moveTo(1);

// Save the file.
excelWorkbook2.save(path.join(dataDir, "FirstWorkbookMoved_out.xlsx"));
```

### **ワークブック間でワークシートをコピーする**

コードを実行すると、「Copy」という名前のワークシートが「SecondWorkbook.xlsx」にコピーされ、「Sheet2」という名前になります。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const excelWorkbook3 = new AsposeCells.Workbook();
const excelWorkbook4 = new AsposeCells.Workbook();

// Create source worksheet
excelWorkbook3.getWorksheets().add("Copy");

// Add new worksheet into second Workbook
excelWorkbook4.getWorksheets().add();

// Copy the first sheet of the first book into second book.
excelWorkbook4.getWorksheets().get(1).copy(excelWorkbook3.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook4.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xlsx"));
```

### **ワークブック間でワークシートを移動する**

このコードを実行すると、「Move」という名前のワークシートがFirstWorkbook.xlsx から「Sheet3」の名前でSecondWorkbook.xlsxに移動します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbooks instead of opening existing files
const excelWorkbook5 = new AsposeCells.Workbook();
const excelWorkbook6 = new AsposeCells.Workbook();

// Add New Worksheet
excelWorkbook6.getWorksheets().add();

// Copy the sheet from first book into second book.
excelWorkbook6.getWorksheets().get(0).copy(excelWorkbook5.getWorksheets().get(0));

// Remove the copied worksheet from first workbook
excelWorkbook5.getWorksheets().removeAt(0);

// Save the file.
excelWorkbook5.save(path.join(dataDir, "FirstWorkbookWithMove_out.xlsx"));

// Save the file.
excelWorkbook6.save(path.join(dataDir, "SecondWorkbookWithMove_out.xlsx"));
```
