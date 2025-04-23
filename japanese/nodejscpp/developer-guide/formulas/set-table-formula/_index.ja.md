---
title: Node.js経由でC++を使用して、新しい行にデータを入力しながら表またはリストオブジェクトの数式を自動的に伝播させる
linktitle: テーブルの数式を設定する
type: docs
weight: 260
url: /ja/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Aspose.Cells for Node.js via C++を使用して、新しい行にデータを入力する際に表またはリストオブジェクト内の数式を自動的に伝播させる方法を学びます。
---

## **可能な使用シナリオ**
時には、表またはリストオブジェクト内の数式が新しい行に自動的に伝播されることを望む場合があります。これはMicrosoft Excelの既定の動作です。これと同じ機能をAspose.Cells for Node.js via C++で実現するには、[ListColumn.getFormula()](https://reference.aspose.com/cells/nodejs-cpp/listcolumn/#getFormula--)を使用してください。

## ** 新しい行にデータを入力しながら表またはリストオブジェクトで数式を自動的に伝播させる**
次のサンプルコードは、列Bの数式が新しいデータを入力すると自動的に新しい行に伝播するように表またはリストオブジェクトを作成します。このコードで生成された[出力エクセルファイル](5115469.xlsx)を確認してください。セルA3に数字を入力すると、セルB2の数式が自動的にセルB3に伝播するのが分かります。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Add column headings in cell A1 and B1
sheet.getCells().get(0, 0).putValue("Column A");
sheet.getCells().get(0, 1).putValue("Column B");

// Add list object, set its name and style
const listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium2);
listObject.setDisplayName("Table");

// Set the formula of second column so that it propagates to new rows automatically while entering data
listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

// Save the workbook in xlsx format
book.save(path.join(dataDir, "output_out.xlsx"));
```
