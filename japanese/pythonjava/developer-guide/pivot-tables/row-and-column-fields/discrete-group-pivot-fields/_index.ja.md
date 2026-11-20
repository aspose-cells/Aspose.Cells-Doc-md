---
title: ピボットフィールドのアイテムを個別にグループ化
linktitle: 個別にグループ化
description: Aspose.Cells for Python via Java の DiscreteGroupItem クラスと PivotFieldGroupOptions.getDiscreteGroupItems メソッドを使用して、果物や野菜などのカスタム名のグループにピボットフィールドのアイテムをグループ化する方法を学びます。
keywords: Aspose.Cells, ピボットテーブル, 個別グループ化, DiscreteGroupItem, PivotFieldGroupOptions, ピボットフィールドのアイテムのグループ化, カスタムグループ, PivotField.group, Python via Java, Excel ピボットテーブル
type: docs
weight: 90
url: /ja/python-java/discrete-group-pivot-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる利用シナリオ**
- 自動グループ化は、日付を月や四半期にまとめ、数値を範囲に分けるなど、データ型に基づいてアイテムをグループ化します。個別グループ化はこれとは逆に、特定の関連のないアイテムをカスタム名のグループにまとめます。たとえば、商品を果物と野菜に分類したり、店舗を地域別に、アカウントをゾーン別にまとめたりします。Aspose.Cells は `DiscreteGroupItem` クラスと `PivotFieldGroupOptions.getDiscreteGroupItems()` メソッドを通じて個別グループ化を提供します。
- `DiscreteGroupItem` は、グループ名と、そのグループに属するアイテムから構成されます。アイテムは、名前 (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) またはソースデータ内の 0 始まりの位置 (`DiscreteGroupItem("fruit", [0, 3])`) のいずれかを使って特定できます。どちらの形式でも同じ結果になります。
- 個別グループ化は、`PivotField.group(PivotFieldGroupOptions)` にオプションを渡すことで、ピボットテーブルの行領域または列領域にあるフィールドに適用されます。

## **名前でピボットフィールドのアイテムをグループ化する**
以下の例では、小さな売上データ（製品、日付、金額）を作成し、`product` を行領域、`date` を列領域、`amount` をデータ領域に配置してピボットテーブルを構築します。続いて、アイテム名に基づいて、fruit（grape、cherry）と vegetable（carrot、potato）の 2 つのカスタムグループを定義します。結果は 2 段の行レイアウトとなり、グループ名が外側のレベルに、元のアイテムがその下にネストされます。これにより、カスタムグループごと、アイテムごとに傾向を確認できます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    DiscreteGroupItem,
    PivotFieldGroupOptions,
    PivotFieldType,
    PivotTableStyleType,
)
GregorianCalendar = jpype.JPackage("java.util").GregorianCalendar
def create_date(year, month, day):
    calendar = GregorianCalendar(year, month - 1, day)
    return calendar.getTime()
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(create_date(2021, 2, 5))
cells.get(2, 1).putValue(create_date(2022, 3, 8))
cells.get(3, 1).putValue(create_date(2023, 4, 10))
cells.get(4, 1).putValue(create_date(2024, 5, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
# Group specific items into custom groups by item names
fruit = DiscreteGroupItem("fruit", ["grape", "cherry"])
vegetable = DiscreteGroupItem("vegetable", ["carrot", "potato"])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.calculateData()
pivot_table.getRowFields().get(0).group(group_options)
wb.save("outputDiscreteGroupPivotField.xlsx")
jpype.shutdownJVM()
```

`calculateData()` の後、ピボットテーブルの行領域には、fruit（grape 50、cherry 80）と vegetable（carrot 60、potato 70）が表示され、総計は 260 になります。列ラベルには、4 つの日付（2/5/2021、3/8/2022、4/10/2023、5/16/2024）が保持されます。

## **インデックスでピボットフィールドのアイテムをグループ化する**
アイテム名が長い場合やローカライズされている場合、`DiscreteGroupItem` の 2 番目のコンストラクターは、インデックスを使ってアイテムを識別します。インデックスは、アルファベット順ではなく、ソースデータに現れる順序におけるアイテムの 0 始まりの位置です。上記のサンプルデータでは、grape がアイテム 0、carrot がアイテム 1、potato がアイテム 2、cherry がアイテム 3 となるため、fruit は `{ 0, 3 }`、vegetable は `{ 1, 2 }` になります。結果は、名前による例と同一です。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotTableStyleType,
)
Date = jpype.JClass("java.util.Date")
DiscreteGroupItem = jpype.JClass("com.aspose.cells.DiscreteGroupItem")
PivotFieldGroupOptions = jpype.JClass("com.aspose.cells.PivotFieldGroupOptions")
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(Date(2021 - 1900, 2 - 1, 5))
cells.get(2, 1).putValue(Date(2022 - 1900, 3 - 1, 8))
cells.get(3, 1).putValue(Date(2023 - 1900, 4 - 1, 10))
cells.get(4, 1).putValue(Date(2024 - 1900, 5 - 1, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
pivot_table.calculateData()
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.getRowFields().get(0).group(group_options)
pivot_table.calculateData()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
jpype.shutdownJVM()
```

## **注意**

{{% alert color="primary" %}}
- どのカスタムグループにも割り当てられていないアイテムが失われることはありません。カスタムグループと同じレベルにピボットテーブル内に残され、それぞれが単独の 1 アイテムのエントリとして表示されます。上記の例では、fruit グループのみを定義した場合、carrot と potato は fruit グループと並んで、行領域に単独のエントリとして残ります。
- `PivotFieldGroupOptions.getNewPivotField()` および `setNewPivotField()` メソッドは、個別グループ化のレイアウトを制御します。`getNewPivotField()` のデフォルト値は true で、グループ化したフィールドを元のフィールドの隣に新たな外側フィールドとして追加し、上記のような 2 段のレイアウトを生成します (`getRowFields()` は 2 に増えます)。`setNewPivotField(false)` を使用すると、元のフィールドが置き換えられます。この場合、行領域にはグループ名とその集計値のみを含む 1 段のレイアウトが表示され、fruit 130 (50 + 80)、vegetable 130 (60 + 70) となります。
- `DiscreteGroupItem` の名前によるコンストラクターとインデックスによるコンストラクターは、同じ `getDiscreteGroupItems()` コレクション内で混在させることができます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブル内でピボットフィールドをグループ化する](/cells/ja/python-java/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルに行フィールドと列フィールドを追加する](/cells/ja/python-java/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値に基づいてピボットテーブルをフィルター処理する](/cells/ja/python-java/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/python-java/apply-style-to-pivot-table/)
- [ピボットテーブルを更新する](/cells/ja/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}