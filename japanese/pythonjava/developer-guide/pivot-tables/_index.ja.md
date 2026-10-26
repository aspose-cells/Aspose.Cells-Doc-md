---
title: ピボットテーブル
linktitle: ピボットテーブル
description: Aspose.Cells for Python via Java を使用してピボットテーブルを作成し、書式を設定します。
keywords: ピボットテーブルの作成, ピボットテーブルの挿入, ピボットテーブルの書式設定。
type: docs
weight: 160
url: /ja/python-java/create-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ピボットテーブルとは？**
ピボットテーブルは、対話型のサマリー レポートです。大量の行ごとの生データを、数式を一つも使わずにコンパクトなマトリックスにまとめます。どの列を行ラベルや列ラベルとして使い、どの列を値として集計するかを決めると、ピボットテーブルがグループ化と計算を行います。
- **要約** — 長い数式の連鎖を使う代わりに、製品別、地域別または四半期別の売上合計を表示します。
- **比較** — 行にカテゴリ、列に期間を配置すると、フラットなリストが横断レポートに変わり、傾向を一目で把握できます。
- **詳細表示** — 任意の集計値をダブルクリックすると、集計対象のソース行を確認できます。
- **更新** — ソースデータが変更された場合も、一度更新するだけでレポート全体が再計算されます。
代表的なユースケースは、販売ダッシュボード、経費の内訳、在庫分析などであり、「これらの数値はカテゴリと時間軸でどのように内訳されるか？」というあらゆる質問に応えます。Aspose.Cells for Python via Javaを使用すると、同じピボットテーブルをプログラムで作成できます。これにより、アプリケーションが生成するワークブックには、生のデータだけでなく、すぐに利用できるレポートを含めることができます。

### **ピボットテーブルのオブジェクトモデル**
Aspose.Cells には、ピボットテーブルの作成と制御に使用できる一連のクラスがあります。その構成要素は次のとおりです。
- `PivotField` は、`PivotTable` 内のフィールドを表します。
- `PivotFieldCollection` は、`PivotTable` 内のすべての `PivotField` オブジェクトのコレクションを表します。
- `PivotTable` は、ワークシート上のピボットテーブルを表します。
- `PivotTableCollection` は、ワークシート上のすべての `PivotTable` オブジェクトのコレクションを表します。

### **Aspose.Cells を使用して基本的なピボットテーブルを作成**
ピボットテーブルの作成は 3 つの手順で行います。ソースデータをワークシートのセルに書き込み、宛先位置にピボットテーブルを追加して、ピボットフィールドを行、列およびデータ領域に配置します。
1. ワークシートのセルに `putValue` メソッドを使用してデータを追加します。このデータはピボットテーブルのデータソースとして使用されます。
2. `PivotTables` コレクションの `add` メソッドを呼び出して、ワークシートにピボットテーブルを追加します: `add(sourceData, row, column)`。`sourceData` はソース範囲です（例: "A1:C8"）。`row` と `column` は、ピボットテーブルの左上角にある宛先セルの 0 始まりの座標です（セル E3 は行 2、列 4 を意味します）。このメソッドは、新しい `PivotTable` オブジェクトを直接返します。
3. `PivotTable` オブジェクトの `addFieldToArea` メソッドを使用して、ピボットフィールドを配置します。フィールド名を指定して、行領域 (`PivotFieldType.ROW`)、列領域 (`PivotFieldType.COLUMN`) またはデータ領域 (`PivotFieldType.DATA`) のいずれかに配置します。
4. ワークブックを保存すると、ピボットテーブルが保存したファイルに書き込まれます。
サンプルコードを実行すると、ワークシートにピボットテーブルが追加されます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

# 新しいワークブックを作成し、最初のワークシートを取得する
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# ソースデータ（スポーツ別・四半期別の売上）を書き込む
cells.get("A1").putValue("Sport")
cells.get("B1").putValue("Quarter")
cells.get("C1").putValue("Sales")
cells.get("A2").putValue("Golf")
cells.get("B2").putValue("Qtr3")
cells.get("C2").putValue(1500)
cells.get("A3").putValue("Golf")
cells.get("B3").putValue("Qtr4")
cells.get("C3").putValue(2000)
cells.get("A4").putValue("Tennis")
cells.get("B4").putValue("Qtr3")
cells.get("C4").putValue(600)
cells.get("A5").putValue("Tennis")
cells.get("B5").putValue("Qtr4")
cells.get("C5").putValue(1500)
cells.get("A6").putValue("Tennis")
cells.get("B6").putValue("Qtr3")
cells.get("C6").putValue(4070)
cells.get("A7").putValue("Tennis")
cells.get("B7").putValue("Qtr4")
cells.get("C7").putValue(5000)
cells.get("A8").putValue("Golf")
cells.get("B8").putValue("Qtr3")
cells.get("C8").putValue(6430)

# A1:C8をソースとして、宛先セルE3にピボットテーブルを追加する
pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4)

# ピボットフィールドを割り当てる：行にSport、列にQuarter、値にSales
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales")

# ワークブックを保存する
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
セル範囲をデータソースとして割り当てる場合、範囲は左上から右下への順で指定する必要があります。たとえば、"A1:C3" は有効ですが、"C3:A1" は無効です。
{{% /alert %}}

## 関連記事
- [Aspose.Cells for Python via Java を使用してピボットテーブルにフィルターフィールドを追加](/cells/ja/python-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via Java を使用してピボットテーブルにスタイルを適用](/cells/ja/python-java/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドレイアウトを変更](/cells/ja/python-java/change-page-field-layout/)
- [ラベルまたは値に基づいてピボットテーブルをフィルター処理する](/cells/ja/python-java/filter-by-label-or-value-of-pivot-table/)
- [Aspose.Cells for Python via Java を使用してピボットテーブルの値フィールドを管理する](/cells/ja/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}