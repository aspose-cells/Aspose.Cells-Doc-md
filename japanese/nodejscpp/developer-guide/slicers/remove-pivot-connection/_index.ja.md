---
title: ピボット接続をNode.jsをC++経由で削除
linktitle: ピボット接続を解除する
type: docs
weight: 30
url: /ja/nodejs-cpp/remove-pivot-connection/
description: Aspose.Cells for Node.js via C++を使用してピボット接続を削除する方法を学ぶ
keywords: Office 2013、2016、2019、Office 365なしでNode.jsをC++経由でピボット接続を削除
---

## **可能な使用シナリオ**

Excelでスライサーとピボットテーブルの関連付けを解除したい場合は、スライサーを右クリックして「レポート接続...」を選択します。オプションリストのチェックボックスで操作できます。同様に、Aspose.Cells APIを使用してプログラム的にスライサーとピボットテーブルの関連付けを解除する場合は、[**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#removePivotConnection-pivottable-)メソッドを使用してください。これにより関連付けが解除されます。

## **スライサーとピボットテーブルの非連携**

次のサンプルコードは、既存のスライサーを含む[サンプルExcelファイル](remove-pivot-connection.xlsx)をロードし、スライサーにアクセスしてピボットテーブルとの関連付けを解除します。最後に、ワークブックを[出力Excelファイル](remove-pivot-connection-out.xlsx)として保存します。

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "remove-pivot-connection.xlsx");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove PivotTable connection.
slicer.removePivotConnection(pivotTable);
// Save the workbook in output XLSX format.
workbook.save(path.join(dataDir, "remove-pivot-connection-out.xlsx"));
``` 
