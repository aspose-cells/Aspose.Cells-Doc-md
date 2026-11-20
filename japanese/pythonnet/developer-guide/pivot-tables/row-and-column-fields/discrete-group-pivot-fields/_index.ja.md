---
title: ピボットフィールド項目の個別グループ化
linktitle: 個別グループ化
description: Aspose.Cells for Python via .NET で、DiscreteGroupItem と pivot_field_group_options.discrete_group_items を使用して、果物や野菜などのカスタムグループにピボットフィールド項目をグループ化する方法を学びます。
keywords: Aspose.Cells for Python via .NET, ピボットテーブル, 個別グループ化, DiscreteGroupItem, PivotFieldGroupOptions, ピボット項目のグループ化, カスタムグループ, PivotField.group, Python, Excel ピボットテーブル
type: docs
weight: 90
url: /ja/python-net/discrete-group-pivot-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **利用可能なシナリオ**
- 自動グループ化は、日付を月や四半期単位にまとめ、数値を範囲ごとにまとめるなど、データ型に基づいて項目をグループ化します。個別グループ化は逆に、指定した互いに無関係な項目を、任意の名前を持つカスタムグループにまとめます。たとえば、商品を果物と野菜に分類したり、店舗を地域ごとに分類したり、アカウントをゾーンごとに分類したりできます。Aspose.Cells では、`DiscreteGroupItem` クラスと `pivot_field_group_options.discrete_group_items` プロパティを使用して個別グループ化を実現できます。
- `DiscreteGroupItem` は、グループ名と、そのグループに属する項目を表します。項目は、名前 (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) またはソースデータ内の 0 始まりの位置 (`DiscreteGroupItem("fruit", [0, 3])`) の 2 つの方法で識別できます。どちらの形式でも同じ結果になります。
- オプションを `pivot_field.group(PivotFieldGroupOptions)` に渡すことで、ピボットテーブルの行領域または列領域にあるフィールドに個別グループ化を適用できます。

## **項目名に基づいてピボットフィールド項目をグループ化**
次の例では、小さな売上リスト (商品、日付、金額) を作成し、`product` を行領域、`date` を列領域、`amount` をデータ領域に配置してピボットテーブルを構築します。その後、項目名に基づいて、果物 (ぶどう、さくらんぼ) と野菜 (にんじん、じゃがいも) の 2 つのカスタムグループを定義します。結果として、グループ名を外側のレベルに表示し、元の項目をその下に入れ子として表示する 2 階層の行レイアウトになります。これにより、カスタムグループごとおよび項目ごとに傾向を確認できます。

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# Group specific items into custom groups using 0-based source-appearance indexes
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotField.xlsx")
```

`calculate_data()` の実行後、ピボットテーブルの行領域には、果物 (ぶどう 50、さくらんぼ 80) と野菜 (にんじん 60、じゃがいも 70)、および総計 260 が表示され、列ラベルには 4 つの日付 (2/5/2021、3/8/2022、4/10/2023、5/16/2024) が引き続き表示されます。

## **項目インデックスに基づいてピボットフィールド項目をグループ化**
項目名が長い場合やローカライズされている場合は、`DiscreteGroupItem` の 2 番目のコンストラクターでインデックスを使用して項目を識別します。インデックスは、項目がソースデータに現れる順序における 0 始まりの位置であり、アルファベット順ではありません。上記のサンプルデータでは、ぶどうは項目 0、にんじんは項目 1、じゃがいもは項目 2、さくらんぼは項目 3 となるため、果物のグループは `{ 0, 3 }`、野菜のグループは `{ 1, 2 }` になります。結果は、項目名に基づいてグループ化した例と完全に同じです。

```python
import aspose.cells as ac
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
from datetime import datetime
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
# (zero-based positions in the order the items appear in the source data)
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
```

## **注意**

{{% alert color="primary" %}}
- どのカスタムグループにも割り当てられていない項目が失われることはありません。これらの項目は、カスタムグループと同じレベルにピボットテーブルに残り、それぞれが単独の項目エントリとして表示されます。上記の例では、果物グループのみを定義すると、行領域には果物グループの横ににんじんとじゃがいもが単独の項目として残ります。
- `pivot_field_group_options.new_pivot_field` プロパティは、個別グループ化のレイアウトを制御します。デフォルト値は `True` で、グループ化されたフィールドを元のフィールドの横に新しい外側フィールドとして追加し、上述の 2 階層のレイアウトを実現します (`row_fields` は 2 に増加します)。`False` に設定すると、代わりに元のフィールドが置き換えられます。この場合、行領域には、グループ名とその集計値のみを含む 1 階層が表示され、果物は 130 (50 + 80)、野菜は 130 (60 + 70) となります。
- `DiscreteGroupItem` の名前ベースとインデックスベースのコンストラクターは、同じ `discrete_group_items` リスト内で併用できます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブル内でピボットフィールドをグループ化](/cells/ja/python-net/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルに行と列のフィールドを追加](/cells/ja/python-net/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値でピボットテーブルをフィルタリング](/cells/ja/python-net/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにスタイルを適用](/cells/ja/python-net/apply-style-to-pivot-table/)
- [ピボットテーブルを更新](/cells/ja/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}