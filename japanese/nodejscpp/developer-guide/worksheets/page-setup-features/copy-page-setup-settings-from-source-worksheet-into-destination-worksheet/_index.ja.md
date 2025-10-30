---
title: Node.jsとC++を使ったソースワークシートからのページ設定の設定をコピー。
linktitle: ソースワークシートからページ設定を宛先ワークシートにコピー
type: docs
weight: 80
url: /ja/nodejs-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: この資料では、Node.js APIまたはC++ライブラリのサンプルコードを使って、ソースワークシートのページ設定をターゲットワークシートにプログラム的にコピーする方法を解説します。
keywords: ページ設定のコピーをNode.jsとC++で行い、ページ設定を他のワークシートにコピーします。
---

## **可能な使用シナリオ**

新しいシートをブックに追加すると、既定の*ページ設定*が含まれます。これらの設定（[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)）を他のシートに転送したい場合があります。本ドキュメントでは、Aspose.Cells for Node.js via C++ APIを使用して、1つのワークシートからもう1つのワークシートへページ設定をコピーする方法を説明します。

## **ソースワークシートからページ設定を宛先ワークシートにコピー**

次のサンプルコードでは、1 つのワークシートから別のワークシートにページ設定の設定をコピーする方法を示しています。参照として、次のサンプルコードとそのコンソール出力をご覧ください。

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add two test worksheets
wb.getWorksheets().add("TestSheet1");
wb.getWorksheets().add("TestSheet2");

// Access both worksheets as TestSheet1 and TestSheet2
const TestSheet1 = wb.getWorksheets().get("TestSheet1");
const TestSheet2 = wb.getWorksheets().get("TestSheet2");

// Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
TestSheet1.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3ExtraTransverse);

// Print the Paper Size of both worksheets
console.log("Before Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("Before Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();

// Copy the PageSetup from TestSheet1 to TestSheet2
TestSheet2.getPageSetup().copy(TestSheet1.getPageSetup(), new AsposeCells.CopyOptions());

// Print the Paper Size of both worksheets
console.log("After Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("After Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();
```

## **コンソール出力**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
