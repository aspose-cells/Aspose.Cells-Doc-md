---
title: Node.jsをC++経由でピボット接続を追加
linktitle: ピボット接続を追加する
type: docs
weight: 30
url: /ja/nodejs-cpp/add-pivot-connection/
description: Aspose.Cells for Node.js via C++を使用してピボット接続を追加する方法を学ぶ
keywords: Office 2013、2016、2019、Office 365なしでNode.jsをC++経由でピボット接続を追加
---

## **可能な使用シナリオ**

Excelでスライサーとピボットテーブルを関連付ける場合は、スライサーを右クリックして「レポート接続...」を選択します。オプションリストのチェックボックスで操作できます。同様に、Aspose.Cells APIを使用してプログラム的にスライサーとピボットテーブルを関連付ける場合は、[**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#addPivotConnection-PivotTable-)メソッドを使用してください。これによりスライサーとピボットテーブルの関連付けが行われます。

## **スライサーとピボットテーブルを関連付ける**

以下のサンプルコードは、既存のスライサーを含む[サンプルExcelファイル](add-pivot-connection.xlsx)をロードし、スライサーにアクセスしてスライサーとピボットテーブルの関連付けを行います。最後に、ワークブックを[出力Excelファイル](add-pivot-connection-out.xlsx)として保存します。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "add-pivot-connection.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0); 

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Adds PivotTable connection.
slicer.addPivotConnection(pivotTable);

workbook.save(path.join(dataDir, "add-pivot-connection-out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
