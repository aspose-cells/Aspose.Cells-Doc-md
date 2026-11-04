---
title: ピボットテーブルの一部をフォーマットする
description: Aspose.Cells for Python via .NET を使用して、PivotTable.format を通じてセマンティックな PivotArea 領域または CellArea 四角形にスタイルを適用し、フォーマットは PivotTable.pivot_formats に保存され、ピボットテーブルがリフレッシュされたときに保持されます。
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Python via .NET, ピボットテーブル, フォーマット, PivotArea, CellArea, PivotTable.format, pivot_formats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, select_field, format_all, Python via .NET
type: docs
weight: 20
url: /ja/python-net/format-part-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
`PivotTable.format_all` はピボットテーブル全体に単一のスタイルを適用しますが、ラベル、値、合計、レポートの特定領域を区別しません。実務では、ピボットテーブルの一部だけを目立たせることが多く、対象となるのは特定の行フィールドに属するラベル、あるフィールドが生成する値セル、総計行、または最初の 2 行などの任意の矩形です。ピボットテーブルのワークシート上のセルに直接スタイルを適用しても同等ではありません。Excel はピボットテーブルの書式設定を普通のセルスタイルレコードではなく、セマンティックな `PivotArea` 領域として保存します。`PivotArea` の書式はフィールドのラベルやデータ値などの領域に結び付けられ、ピボットテーブルが再計算、リフレッシュ、拡張されると再解決されます。一方、セルに直接書き込まれたスタイルはそのセル位置に属し、ピボットモデルによって追跡されません。  
Aspose.Cells は完全な `PivotTable.format` オーバーロードセットを公開しており、両方の書式設定が利用可能です。
- `format(PivotArea, Style)` は `PivotArea.select` または `PivotArea.select_field` で構築されたセマンティック領域にスタイルを結び付けます。
- `format(CellArea, Style)` はピボットテーブル内部のワークシート矩形にスタイルを結び付けます。
- `format(int row, int column, Style)` は単一セルを対象とします。
- `format_all(Style)` はピボットテーブル全体をフォーマットします。

## **PivotArea のフォーマット**
セマンティック領域のワークフローは、ハイライトがフィールドまたはレポート領域に追従する必要がある場合に推奨されます。
1. `PivotArea(pivot_table)` で `PivotArea` を作成します。このオブジェクトは特定のピボットテーブルに属するセマンティック領域を表します。
1. `PivotArea.select(PivotFieldType axis_type, int field_position, PivotTableSelectionType selection_type)` で指定軸上のゼロベース位置にあるフィールドを選択します。  
   - `PivotTableSelectionType.DATA_AND_LABEL` はフィールドのラベルとデータの両方を選択します。  
   - `PivotTableSelectionType.LABEL_ONLY` はフィールドのラベルのみを選択します。  
   - `PivotTableSelectionType.DATA_ONLY` はフィールドのデータセルのみを選択します。
1. `PivotArea.select_field(PivotFieldType axis_type, string field_name)` でフィールド名から選択します。行フィールドを名前で選択すると、領域はそのフィールドのアイテムが生成する値セルに解決されます。
1. `Workbook.create_style()` で `Style` を作成し、フォント、前景色、単色背景パターンを設定してから、`PivotTable.format(area, style)` に渡します。
1. `PivotArea` のオーバーロードを呼び出すたびに、`PivotTable.pivot_formats` に `PivotTableFormat` エントリが 1 つ追加されます。
1. フィールドに結び付けられた書式はピボットデータの計算時に描画されます。したがって、書式を適用した後は `PivotTable.calculate_data()` を呼び出し、スタイルが表示されるようにします。  
以下の例は、果物の売上ピボットテーブルを作成し、`Fruit` 行ラベルを `PivotArea.select` と `PivotTableSelectionType.LABEL_ONLY` でスタイル設定し、同じ行フィールドで生成された値セルを `PivotArea.select_field` でスタイル設定し、最後にピボットテーブルを再計算して両方のスタイルを描画します。

```python
from aspose.cells.pivot import PivotArea, PivotFieldType, PivotTableSelectionType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Bold yellow fill on the row field's label cells
label_style = workbook.create_style()
label_style.font.is_bold = True
label_style.foreground_color = Color.yellow
label_style.pattern = ac.BackgroundType.SOLID
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.create_style()
value_style.foreground_color = Color.light_green
value_style.pattern = ac.BackgroundType.SOLID
value_area = PivotArea(pivot_table)
value_area.select_field(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculate_data()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
```

## **ピボットテーブルのセル領域のフォーマット**
関心領域が単なるワークシート矩形であり、セマンティックなピボット領域でない場合は `PivotTable.format(CellArea, Style)` を使用します。  
`CellArea` は `start_row`, `start_column`, `end_row`, `end_column` プロパティで記述されます。これらの値はゼロベースのワークシート座標で、終了座標は矩形に含まれる最後の行と列を示すため、開始位置から終了位置までのセルが対象となります。  
フィールドに結び付けられた書式とは異なり、`CellArea` の書式は即座にセルに適用されます。`calculate_data()` を再度呼び出す必要はありません。  
`CellArea` 矩形にはラベルセルと値セルが混在することがあります。次のセクションでは、Aspose.Cells と Excel がその矩形を内部でどのように表現しているかを説明します。  
以下の例は、ピボットテーブルの矩形 `E4:F5` を斜体のライトブルー スタイルでフォーマットし、さらに再計算せずにブックを保存します。

```python
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
```

## **PivotArea と CellArea のマッピング**
Excel はピボットテーブルの書式設定を普通のワークシートセルスタイルレコードではなく `pivotArea` レコードとして保存します。このモデルは Aspose.Cells でも使用されており、書式設定要求は記録時にピボット領域に変換されます。  
ユーザーが提供した `CellArea` と内部に保存されるピボット領域との関係は多対多です。
- 1 つの `CellArea` が複数のピボット領域を生成することがあります。矩形がラベルセルと値セルの両方を含む場合、ラベル用とデータ用の別個のルールに分解されます。ピボットモデルはラベル書式とデータ書式を独立して扱うためです。
- 1 つのピボット領域が複数の独立した `CellArea` インスタンスに解決されることがあります。総計行や連続しないアイテムを持つフィールドなど、セマンティック領域は複数の矩形にまたがることがあります。このため `PivotArea.get_cell_areas()` は単一矩形ではなくコレクションを返します。  
`PivotTable.format` を通じて行われたすべての書式操作は `PivotTable.pivot_formats` に記録されます。各 `PivotTableFormat` エントリは関連付けられた `PivotArea` と適用された `Style` を公開します。`PivotArea` のオーバーロードは呼び出しごとに正確に 1 件のエントリを追加しますが、異なるセマンティック領域を含む `CellArea` は複数のエントリを追加する可能性があります。  
保存された領域を区別するために、各 `PivotArea` は `only_label` と `only_data` フラグを公開します。以下の例はラベルと値の両方をカバーする単一矩形をフォーマットし、`PivotTable.pivot_formats` を調査して各保存されたピボット領域が解決する `CellArea` 座標を出力します。

```python
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
# ONE rectangle in...
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print(f"Stored formats: {len(pivot_table.pivot_formats)}")
for i in range(len(pivot_table.pivot_formats)):
    stored_area = pivot_table.pivot_formats[i].pivot_area
    print(f"Format {i}: OnlyLabel={stored_area.only_label}, OnlyData={stored_area.only_data}")
    for resolved in stored_area.get_cell_areas():
        print(
            f"    rows {resolved.start_row + 1}-{resolved.end_row + 1}, "
            f"columns {resolved.start_column + 1}-{resolved.end_column + 1}"
        )
workbook.save("FormatPivotAreasMap.xlsx")
```

{{% alert color="primary" %}}
書式がピボット領域として保存されているため、普通のセルスタイルとしてではなく、再計算やリフレッシュ後も保持されます。ピボットテーブルが `PivotTable.refresh_data` でリフレッシュされたり、`calculate_data` で再計算されたり、保存後に再読み込みされたりすると、保存された各ピボット領域は現在の位置に再解決され、スタイルが再適用されます。
{{% /alert %}}

ハイライトがリフレッシュ間でフィールドまたはセマンティック領域に結び付く必要がある場合は `select` または `select_field` で構築した `PivotArea` を使用し、現在のピボットテーブルレイアウト内の固定矩形をフォーマットするだけで良い場合は `CellArea` を使用してください。単一セルを対象とする `format(int row, int column, Style)` オーバーロードも利用可能です。ピボットテーブル全体を一度に再スタイル化したい場合は、親ページで説明されている `format_all` を使用します。

## **関連項目**
- [ピボットテーブルへのスタイルの適用](/cells/ja/python-net/apply-style-to-pivot-table/)
- [ピボットテーブルの行および列フィールドの追加](/cells/ja/python-net/pivot-table-add-row-and-column-fields/)
- [ピボットテーブルの値フィールドの管理](/cells/ja/python-net/manage-value-fields/)
- [ピボットテーブルのリフレッシュ](/cells/ja/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}