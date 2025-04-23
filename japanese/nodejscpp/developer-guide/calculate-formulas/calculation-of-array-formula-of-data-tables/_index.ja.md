---
title: Node.js via C++を使用したデータテーブルの配列式の計算
linktitle: データテーブルの配列式の計算
description: Node.jsをC++経由でMicrosoft Excelのデータテーブルの配列数式を計算するためにAspose.Cellsライブラリを使用する方法。Excelファイルを読み込むか作成し、配列数式を計算して、変更されたファイルを保存します。
keywords: Aspose.Cells、Excel、データテーブル、配列数式、計算 Node.jsをC++経由で
type: docs
weight: 70
url: /ja/nodejs-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Microsoft ExcelでData > シナリオ分析 > データテーブル...を使用してデータテーブルを作成できます。Aspose.Cellsは現在、データテーブルの配列数式の計算を可能にしています。通常どおり[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)を使用してあらゆるタイプの数式を計算してください。

{{% /alert %}}

次のサンプルコードでは、[元のExcelファイル](5115535.xlsx) を使用しました。セルB1の値を100に変更すると、黄色で塗られたデータテーブルの値が120になる様子が次の画像で示されます。サンプルコードは、[出力PDF](5115538.pdf) を生成します。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

以下は[元のExcelファイル](5115535.xlsx) から[出力PDF](5115538.pdf) を生成するために使用されたサンプルコードです。詳細についてはコメントをお読みください。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataTable.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.getCells().get("B1").putValue(100);

// Calculate formula, now it also calculates Data Table array formula
workbook.calculateFormula();

// Save the workbook in pdf format
workbook.save(path.join(dataDir, "output_out.pdf"));
```
