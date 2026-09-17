---
title: ピボットテーブル
description: Excelスプレッドシートファイルのピボットテーブルを作成し、書式を設定する。
linktitle: ピボットテーブル
url: /ja/python-java/create-pivot-table/
type: docs
weight: 160
keywords: ピボットテーブルを作成し、ピボットテーブルを挿入し、ピボットテーブルを書式設定します。
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ピボットテーブルの作成**
Aspose.Cells を使用すると、ピボットテーブルをスプレッドシートにプログラムで追加できます。

### **ピボットテーブルのオブジェクトモデル**
Aspose.Cells は、ピボットテーブルの作成と制御に使用されるクラスのセットを提供します。構成要素は次のとおりです:
- `PivotField` は `PivotTable` 内のフィールドを表します。
- `PivotFieldCollection` は `PivotTable` 内のすべての `PivotField` オブジェクトのコレクションを表します。
- `PivotTable` はワークシート上のピボットテーブルを表します。
- `PivotTableCollection` はワークシート上のすべての `PivotTable` オブジェクトのコレクションを表します。

### **Aspose.Cells を使用してシンプルなピボットテーブルを作成する**
1. セルの `putValue` メソッドを使用してワークシートにデータを追加します。このデータはピボットテーブルのデータソースとして使用されます。
2. ワークシートオブジェクトにカプセル化されている `PivotTables` コレクションの `add` メソッドを呼び出して、ワークシートにピボットテーブルを追加します。
3. ピボットテーブルのインデックスを渡すことによって、`PivotTables` コレクションから新しい `PivotTable` オブジェクトにアクセスします。
4. 上記で説明した `PivotTable` オブジェクトのいずれかを使用して、ピボットテーブルを管理します。

サンプル コードを実行すると、ピボットテーブルがワークシートに追加されます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

dataDir = "./"
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

cell = cells.get("A1")
cell.putValue("Sport")
cell = cells.get("B1")
cell.putValue("Quarter")
cell = cells.get("C1")
cell.putValue("Sales")

cell = cells.get("A2")
cell.putValue("Golf")
cell = cells.get("A3")
cell.putValue("Golf")
cell = cells.get("A4")
cell.putValue("Tennis")
cell = cells.get("A5")
cell.putValue("Tennis")
cell = cells.get("A6")
cell.putValue("Tennis")
cell = cells.get("A7")
cell.putValue("Tennis")
cell = cells.get("A8")
cell.putValue("Golf")

cell = cells.get("B2")
cell.putValue("Qtr3")
cell = cells.get("B3")
cell.putValue("Qtr4")
cell = cells.get("B4")
cell.putValue("Qtr3")
cell = cells.get("B5")
cell.putValue("Qtr4")
cell = cells.get("B6")
cell.putValue("Qtr3")
cell = cells.get("B7")
cell.putValue("Qtr4")
cell = cells.get("B8")
cell.putValue("Qtr3")

cell = cells.get("C2")
cell.putValue(1500)
cell = cells.get("C3")
cell.putValue(2000)
cell = cells.get("C4")
cell.putValue(600)
cell = cells.get("C5")
cell.putValue(1500)
cell = cells.get("C6")
cell.putValue(4070)
cell = cells.get("C7")
cell.putValue(5000)
cell = cells.get("C8")
cell.putValue(6430)

pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C8", "E3", "PivotTable2")
pivotTable = pivotTables.get(index)
pivotTable.setRowGrand(False)
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.COLUMN, 1)
pivotTable.addFieldToArea(PivotFieldType.DATA, 2)
workbook.save(dataDir + "pivotTable_test_out.xls")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
セルの範囲をデータソースとして割り当てる場合、範囲は左上から右下に向かって指定する必要があります。たとえば、「A1:C3」は有効ですが、「C3:A1」は無効です。
{{% /alert %}}

## 関連記事
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via Java](/cells/ja/python-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via Java](/cells/ja/python-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/ja/python-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/ja/python-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via Java](/cells/ja/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}