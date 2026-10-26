---
title: ピボットテーブルを挿入する
linktitle: ピボットテーブルを挿入する
description: Aspose.Cells for Python via .NET を使用してピボットテーブルを作成し、書式を設定します。
keywords: ピボットテーブルの作成, ピボットテーブルの挿入, ピボットテーブルの書式設定
type: docs
weight: 160
url: /ja/python-net/create-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ピボットテーブルとは？**
ピボットテーブルは、対話型の集計レポートです。長い数式を一切使うことなく、行ごとに並んだ大量の生データをコンパクトなマトリクスに要約します。どの列を行ラベルとするか、どの列を列ラベルとするか、どの列を値として集計するかを指定すると、ピボットテーブルがグループ化と計算を実行します。
- **要約** — 製品別、地域別、四半期別の総売上などを、長い数式の連鎖を使わずに集計します。
- **比較** — カテゴリを行、期間を列に配置することで、フラットなリストを傾向が一目で確認できるクロスレポートに変換します。
- **ドリルダウン** — 任意の集計値をダブルクリックして、その集計値の元になったソース行を確認できます。
- **更新** — ソースデータが変化すると、一度更新するだけでレポート全体を再計算できます。
代表的な使用場面は、販売ダッシュボード、経費の内訳、在庫分析など、「これらの数値はカテゴリと時間ごとにどのように分かれるか？」という質問に応える用途です。Aspose.Cells for Python via .NET を使用すると、同じピボットテーブルをプログラムで作成できます。したがって、アプリケーションが生成するワークブックには、生データだけでなく、すぐに使用できるレポートを含めることができます。

### **ピボットテーブルのオブジェクトモデル**
Aspose.Cells for Python via .NET は、ピボットテーブルの作成と制御に使用する専用のクラス群を [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) namespace に提供します。これらのクラスは、ピボットテーブルの構成要素となる [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) オブジェクトを作成して設定するために使用されます。対象となるオブジェクトは次のとおりです。
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) は、[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) 内のフィールドを表します。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) は、[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) 内のすべての [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) オブジェクトのコレクションを表します。
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) は、ワークシート上のピボットテーブルを表します。
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) は、ワークシート上のすべての [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) オブジェクトのコレクションを表します。

### **Aspose.Cells を使用して単純なピボットテーブルを作成する**
ピボットテーブルの作成は、次の 3 つの手順で行います。ソースデータをワークシートのセルに書き込み、指定した位置にピボットテーブルを追加して、行、列、データ領域にピボットフィールドを配置します。
1. [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) オブジェクトの [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) メソッドを使用して、ワークシートのセルにデータを追加します。このデータはピボットテーブルのデータソースとして使用されます。
2. [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) コレクションの [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) メソッド (`add(source_data, row, column)`) を呼び出して、ワークシートにピボットテーブルを追加します。`source_data` はソース範囲（例: "A1:C8"）です。`row` と `column` は、ピボットテーブルの左上隅となる配置先セルの 0 始まりの行番号と列番号です（セル E3 の場合、行 2、列 4 を意味します）。このメソッドは、新しい [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) オブジェクトを直接返します。
3. [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) オブジェクトの `add_field_to_area` メソッドでピボットフィールドを配置します。フィールド名を行領域 (`PivotFieldType.ROW`)、列領域 (`PivotFieldType.COLUMN`)、またはデータ領域 (`PivotFieldType.DATA`) に指定します。
4. ワークブックを保存します。ピボットテーブルは保存されたファイルに書き込まれます。
サンプルコードを実行すると、ワークシートにピボットテーブルが追加されます。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

# 新しいワークブックを作成し、最初のワークシートを取得する
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# ソースデータ（スポーツと四半期ごとの売上）を書き込む
sheet.cells.get("A1").put_value("Sport")
sheet.cells.get("B1").put_value("Quarter")
sheet.cells.get("C1").put_value("Sales")
sheet.cells.get("A2").put_value("Golf")
sheet.cells.get("B2").put_value("Qtr3")
sheet.cells.get("C2").put_value(1500)
sheet.cells.get("A3").put_value("Golf")
sheet.cells.get("B3").put_value("Qtr4")
sheet.cells.get("C3").put_value(2000)
sheet.cells.get("A4").put_value("Tennis")
sheet.cells.get("B4").put_value("Qtr3")
sheet.cells.get("C4").put_value(600)
sheet.cells.get("A5").put_value("Tennis")
sheet.cells.get("B5").put_value("Qtr4")
sheet.cells.get("C5").put_value(1500)
sheet.cells.get("A6").put_value("Tennis")
sheet.cells.get("B6").put_value("Qtr3")
sheet.cells.get("C6").put_value(4070)
sheet.cells.get("A7").put_value("Tennis")
sheet.cells.get("B7").put_value("Qtr4")
sheet.cells.get("C7").put_value(5000)
sheet.cells.get("A8").put_value("Golf")
sheet.cells.get("B8").put_value("Qtr3")
sheet.cells.get("C8").put_value(6430)

# 宛先セル E3 に、A1:C8 をデータソースとするピボットテーブルを追加する
pivot_table = sheet.pivot_tables.add("A1:C8", 2, 4)

# ピボットフィールドを割り当てる: Sport を行、Quarter を列、Sales をデータに割り当てる
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Quarter")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")

# ワークブックを保存する
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
セル範囲をデータソースとして割り当てる場合、その範囲は左上隅から右下隅に向かって指定する必要があります。たとえば、"A1:C3" は有効ですが、"C3:A1" は無効です。
{{% /alert %}}

## 関連記事
- [Aspose.Cells for Python via .NET でピボットテーブルにフィルターフィールドを追加](/cells/ja/python-net/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via .NET でピボットテーブルにスタイルを適用](/cells/ja/python-net/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドレイアウトを変更](/cells/ja/python-net/change-page-field-layout/)
- [ラベルまたは値によるピボットテーブルのフィルタリング](/cells/ja/python-net/filter-by-label-or-value-of-pivot-table/)
- [Aspose.Cells for Python via .NET でピボットテーブルの値フィールドを管理](/cells/ja/python-net/manage-value-fields/)

{{< app/cells/assistant language="python-net" >}}