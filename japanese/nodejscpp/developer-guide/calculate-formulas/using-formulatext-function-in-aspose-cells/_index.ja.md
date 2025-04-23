---
title: Aspose.Cells for Node.js via C++のFormulaText関数の使用例
linktitle: Aspose.CellsでのFormulaText関数の使用
description: この記事では、Aspose.CellsライブラリのFormulaText関数を使用してMicrosoft Excelの数式を処理する方法について説明します。セルの数式テキストの取得と設定方法、変更したExcelファイルの保存方法をNode.js経由のC++で解説します。
keywords: Aspose.Cells、Excel、FormulaText関数、Node.js via C++
type: docs
weight: 60
url: /ja/nodejs-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaTextはExcel 2013以降の関数です。Excel 2010や2007などの以前のバージョンではサポートされていません。その名前の通り、指定されたセルにある数式のテキストを出力します。この記事では、Aspose.Cells for Node.js via C++を使用してこの関数を利用する方法を示します。

{{% /alert %}} 

次のサンプルコードは、Aspose.Cells for Node.js via C++とともにFormulaTextの使用例を示しています。最初にセルA1に数式を書き込み、その後、セルA2にFormulaTextを使用して数式のテキストを出力します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create a workbook object
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some formula in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.setFormula("=Sum(B1:B10)");

// Get the text of the formula in cell A2 using FORMULATEXT function
const cellA2 = worksheet.getCells().get("A2");
cellA2.setFormula("=FormulaText(A1)");

// Calculate the workbook
workbook.calculateFormula();

// Print the results of A2, It will now print the text of the formula inside cell A1
console.log(cellA2.getStringValue());
```
## **コンソール出力**
上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
