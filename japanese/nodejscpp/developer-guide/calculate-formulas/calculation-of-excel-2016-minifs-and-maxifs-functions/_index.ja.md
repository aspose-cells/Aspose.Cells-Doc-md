---
title: Node.jsをC++経由で使用したExcel 2016のMINIFSおよびMAXIFS関数の計算
description: この記事では、Aspose.Cellsライブラリを使用してNode.jsをC++経由でMicrosoft Excel 2016のMINIFSとMAXIFS関数を計算する方法を紹介します。既存のExcelファイルを読み込むか新規作成し、Aspose.Cellsメソッドを使用してこれらの関数を計算し、結果を保存します。
keywords: Aspose.Cells、Excel、2016、MINIFS関数、MAXIFS関数、計算 Node.jsをC++経由で
type: docs
weight: 300
url: /ja/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **可能な使用シナリオ**
Microsoft Excel 2016はMINIFSおよびMAXIFS関数をサポートしています。これらの関数はExcel 2013以前のバージョンではサポートされていません。Aspose.Cells for Node.js via C++もこれらの関数の計算をサポートしています。以下のスクリーンショットはこれらの関数の使用例を示しています。スクリーンショット内の赤いコメントを読んでこれらの関数の動作を理解してください。

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Excel 2016のMINIFSおよびMAXIFS関数の計算**
次のサンプルコードは、[サンプルExcelファイル](5115149.xlsx)を読み込み、[Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)メソッドを呼び出してAspose.Cells for Node.js via C++を通じて数式を計算し、その結果を[出力PDF](5115154.pdf)に保存します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleMINIFSAndMAXIFS.xlsx");

// Load your source workbook containing MINIFS and MAXIFS functions
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Perform Aspose.Cells formula calculation
workbook.calculateFormula();

// Save the calculations result in pdf format
const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);
const outputFilePath = path.join(dataDir, "outputMINIFSAndMAXIFS.pdf");
workbook.save(outputFilePath, options);
```
