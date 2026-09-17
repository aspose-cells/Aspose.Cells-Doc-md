---
title: ピボットテーブルを挿入する
description: Aspose.Cells for Node.js via Javaを使用して、Excelスプレッドシートのピボットテーブルを作成および書式設定します。
linktitle: ピボットテーブル
url: /ja/nodejs-java/create-pivot-table/
type: docs
weight: 160
keywords: ピボットテーブルの作成, ピボットテーブルの挿入, ピボットテーブルの書式設定, Aspose.Cells for Node.js via Java。
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ピボットテーブルを作成する**
Aspose.Cellsを使用すると、プログラムでスプレッドシートにピボットテーブルを追加できます。

### **ピボットテーブルのオブジェクトモデル**
Aspose.Cellsは、ピボットテーブルの作成と制御に使用されるクラスのセットを提供します。構成要素は次のとおりです:
- `PivotField` は `PivotTable` 内のフィールドを表します。
- `PivotFieldCollection` は `PivotTable` 内のすべての `PivotField` オブジェクトのコレクションを表します。
- `PivotTable` はワークシート上のピボットテーブルを表します。
- `PivotTableCollection` はワークシート上のすべての `PivotTable` オブジェクトのコレクションを表します。

### **Aspose.Cellsを使用してシンプルなピボットテーブルを作成する**
1. セルの `putValue` メソッドを使用してワークシートにデータを追加します。このデータはピボットテーブルのデータソースとして使用されます。
2. ワークシートオブジェクトにカプセル化されている `PivotTables` コレクションの `add` メソッドを呼び出して、ワークシートにピボットテーブルを追加します。
3. ピボットテーブルのインデックスを渡すことで、`PivotTables` コレクションから新しい `PivotTable` オブジェクトにアクセスします。
4. 上記の `PivotTable` オブジェクトのいずれかを使用して、ピボットテーブルを管理します。

サンプルコードを実行すると、ワークシートにピボットテーブルが追加されます。

```javascript
var dataDir = "./";

// Instantiating a Workbook object
var workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
var sheet = workbook.getWorksheets().get(0);

var cells = sheet.getCells();

// Setting the value to the cells
var cell = cells.get("A1");
cell.putValue("Sport");
cell = cells.get("B1");
cell.putValue("Quarter");
cell = cells.get("C1");
cell.putValue("Sales");

cell = cells.get("A2");
cell.putValue("Golf");
cell = cells.get("A3");
cell.putValue("Golf");
cell = cells.get("A4");
cell.putValue("Tennis");
cell = cells.get("A5");
cell.putValue("Tennis");
cell = cells.get("A6");
cell.putValue("Tennis");
cell = cells.get("A7");
cell.putValue("Tennis");
cell = cells.get("A8");
cell.putValue("Golf");

cell = cells.get("B2");
cell.putValue("Qtr3");
cell = cells.get("B3");
cell.putValue("Qtr4");
cell = cells.get("B4");
cell.putValue("Qtr3");
cell = cells.get("B5");
cell.putValue("Qtr4");
cell = cells.get("B6");
cell.putValue("Qtr3");
cell = cells.get("B7");
cell.putValue("Qtr4");
cell = cells.get("B8");
cell.putValue("Qtr3");

cell = cells.get("C2");
cell.putValue(1500);
cell = cells.get("C3");
cell.putValue(2000);
cell = cells.get("C4");
cell.putValue(600);
cell = cells.get("C5");
cell.putValue(1500);
cell = cells.get("C6");
cell.putValue(4070);
cell = cells.get("C7");
cell.putValue(5000);
cell = cells.get("C8");
cell.putValue(6430);

var pivotTables = sheet.getPivotTables();

// Adding a PivotTable to the worksheet
var index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

// Accessing the instance of the newly added PivotTable
var pivotTable = pivotTables.get(index);

// Unshowing grand totals for rows.
pivotTable.setRowGrand(false);

// Draging the first field to the row area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);

// Draging the second field to the column area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, 1);

// Draging the third field to the data area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 2);

// Saving the Excel file
workbook.save(dataDir + "pivotTable_test_out.xls");
```

{{% alert color="primary" %}}
セルの範囲をデータソースとして割り当てる場合、範囲は左上から右下に向かって指定する必要があります。たとえば「A1:C3」は有効ですが「C3:A1」は無効です。
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via Java](/cells/ja/nodejs-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Node.js via Java](/cells/ja/nodejs-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/ja/nodejs-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/ja/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Node.js via Java](/cells/ja/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}