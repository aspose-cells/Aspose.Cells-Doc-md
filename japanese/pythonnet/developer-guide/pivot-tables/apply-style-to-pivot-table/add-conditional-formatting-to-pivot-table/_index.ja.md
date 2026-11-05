---
title: ピボットテーブルへの条件付き書式の追加
linktitle: ピボットテーブルへの条件付き書式の追加
description: Aspose.Cells for Python via .NET でピボットテーブルに条件付き書式を追加します - apply_to と PivotConditionFormatScopeType スコープでデータ領域にルールを固定するか、add_cell_area と pivot_areas で対象を定義し、その後 format_conditions.add_condition でルールとスタイルを添付します。
keywords: Aspose.Cells, Aspose.Cells for Python via .NET, ピボットテーブル, 条件付き書式, PivotConditionalFormat, conditional_formats, apply_to, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, add_cell_area, pivot_areas, add_pivot_area, format_conditions, add_condition, FormatConditionType, Python
type: docs
weight: 30
url: /ja/python-net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **利用シナリオ**
親ページおよび兄弟ページで説明されているスタイルは静的です。`PivotArea` または `CellArea` 領域は一度塗りつぶされ、値がどうであってもそのスタイルが保持されます。条件付き書式はルール主導の対応物で、200 を超えるすべての金額をハイライトしたり、中央値の 50% をシェーディングしたり、下位の項目にフラグを付けたりします。そして、ピボットテーブルが再計算または更新されるたびにハイライトが値に追随します。
In Aspose.Cells では、ピボットテーブルの条件付き書式は `pivot_table.conditional_formats` コレクションに格納されます。各エントリは `PivotConditionalFormat` で、次の 2 つの質問に独立して答えます。
- **ルールはどこに適用されますか？** ターゲット領域は `apply_to(row: int, column: int, scope: PivotConditionFormatScopeType)` で定義でき、これは Excel のユーザーインターフェイスのスコープ選択と同等です。または `add_cell_area(cell_area: CellArea)` と `pivot_areas` コレクションを使用して領域を明示的に指定します。
- **ルールは何をテストしますか？** `format_conditions.add_condition(type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` を使用して 1 つ以上の条件を `format_conditions` に追加し、各条件はそれぞれの `style` を持ちます。

{{% alert color="primary" %}}
ピボット条件付き書式の `format_conditions` オブジェクトに対して `format_conditions.add(cell_area: CellArea, type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` や `format_conditions.add_area(cell_area: CellArea)` を呼び出さないでください。これら 2 つのオーバーロードは通常のワークシート条件付き書式 API から継承されており、ピボットテーブルでは機能しません。セル領域はピボット領域に変換されないため、リクエストは黙って無視されます。常に `pivot_conditional_format` 自体で領域を定義（`apply_to`、`add_cell_area`、または `pivot_areas`）し、`add_condition` のいずれかのオーバーロードでルールを追加してください。
{{% /alert %}}

## **スコープを使用してルールを適用する（Excel UI の方法）**
最初の方法は、Excel ユーザーインターフェイスと同様にルールの位置を決定します。ピボットテーブルのセルはゼロベースのワークシート座標で指定され、`PivotConditionFormatScopeType` スコープが Aspose.Cells に対してそのセルからルールがどれだけ広がるかを示します：
- `PivotConditionFormatScopeType.DATA` - ピボットテーブルが生成するすべての値セル（総計を含む）。
- `PivotConditionFormatScopeType.FIELD` - セルが示すフィールドに属する値セル（総計は除外）。セルは行フィールドラベルなどのフィールドセルである必要があり、値セルを指定すると例外がスローされます。
- `PivotConditionFormatScopeType.SELECTION` - セルが選択する交差点の値セルのみ（通常は単一の値セル）。

```python
from aspose.cells.pivot import PivotFieldType, PivotConditionFormatScopeType
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
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Anchor the conditional format at F4 (row 3, column 5) with the Data scope
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
format.apply_to(3, 5, PivotConditionFormatScopeType.DATA)
# Rule - highlight amounts greater than 200
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.GREATER_THAN,
    "200",
    None
)
style = workbook.create_style()
style.font.is_bold = True
style.font.color = Color.white
style.foreground_color = Color.red
style.pattern = ac.BackgroundType.SOLID
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatData.xlsx")
```

同じルールを行フィールドラベル E4（行 3、列 4）に `PivotConditionFormatScopeType.FIELD` スコープで固定すると、対象は F4:F6 になります。これは総計行を除いた同じデータ列です。スコープが全体の値領域ではなく `Fruit` フィールドを指すためです。`PivotConditionFormatScopeType.SELECTION` スコープを F4 に固定すると、対象は F4 のみになります。

## **領域を手動で定義する**
2 番目の方法はスコープ選択を省き、`PivotConditionalFormat` 上で領域を明示的に指定します。

### **add_cell_area を使用したワークシート矩形**
`add_cell_area(cell_area: CellArea)` は指定された矩形をルールの対象として記録します。座標はゼロベースのワークシート座標で、領域は提供された矩形そのものです。データ列への拡張や総計ロジックは行われません。対象のセルが現在のピボットレイアウト内の既知の固定矩形である場合に使用します。

```python
from aspose.cells import BackgroundType, FormatConditionType, OperatorType
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
# Target the rectangle F4:F6 (the value cells without the grand total)
index = pivot_table.conditional_formats.add()
conditional_format = pivot_table.conditional_formats[index]
area = ac.CellArea()
area.start_row = 3
area.start_column = 5
area.end_row = 5
area.end_column = 5
conditional_format.add_cell_area(area)
# Rule - italic on light yellow for amounts between 150 and 300
condition_index = conditional_format.format_conditions.add_condition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300"
)
style = workbook.create_style()
style.font.is_italic = True
style.foreground_color = Color.light_yellow
style.pattern = BackgroundType.SOLID
conditional_format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatCellArea.xlsx")
```

### **pivot_areas を使用した意味的ピボット領域**
`pivot_areas` は、兄弟ページが静的スタイルに使用しているのと同じ意味的領域モデルです。`PivotArea` を作成し、`select` または `select_field` でフィールドまたは領域を選択し、`pivot_areas.add_pivot_area(pivot_area)` で追加します。意味的領域はそのフィールドに付随したままになるため、ピボットテーブルが更新されレイアウトが変わっても条件付き書式がフィールドに追随します。`pivot_areas.add(pivot_area)` のオーバーロードもコンパイルは通りますが、廃止予定とマークされているため、`add_pivot_area` を使用することが推奨されます。

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
# Attach the rule to the Amount data field as a semantic region
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
area = ac.PivotArea(pivot_table)
area.select_field(PivotFieldType.DATA, "Amount")
format.pivot_areas.add_pivot_area(area)
# Rule - grey text for amounts below 150
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.LESS_THAN,
    "150",
    None
)
style = workbook.create_style()
style.font.color = Color.gray
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatPivotArea.xlsx")
```

## **ルールの保存場所とリロード後の持続性**
`pivot_table.conditional_formats.add()` の呼び出しは、ピボットテーブルに `PivotConditionalFormat` を 1 つ追加します。条件、数式、スタイルはワークブックに保存され、以下の例でファイルを再度開くと、同じルールがタイプ、演算子、数式が保持されたまま表示され、`get_cell_areas()` も同じ領域を報告します。条件が一度も設定されていないエントリは、ワークブック保存時に削除されます。これは Excel がルールのない条件付き書式を破棄するのと同様です。

```python
import aspose.cells as ac
workbook = ac.Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
print("Conditional formats: " + str(pivot_table.conditional_formats.count))
for i in range(pivot_table.conditional_formats.count):
    format = pivot_table.conditional_formats[i]
    for j in range(format.format_conditions.count):
        condition = format.format_conditions[j]
        print(f"Format {i}: {condition.type} {condition.operator} formula1={condition.formula1}")
    for area in format.get_cell_areas():
        print(
            f"    rows {area.start_row + 1}-{area.end_row + 1}, "
            f"columns {area.start_column + 1}-{area.end_column + 1}"
        )
# This prints:
# Conditional formats: 1
# Format 0: CellValue GreaterThan formula1==200
#     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **Related Articles**
- [ピボットテーブルへのスタイル適用](/cells/ja/python-net/apply-style-to-pivot-table/)
- [ピボットテーブルの一部を書式設定](/cells/ja/python-net/format-part-of-pivot-table/)
- [ピボットテーブルでトップ 10 を表示またはフィルター](/cells/ja/python-net/top-10-show-or-filter-in-pivot-table/)
- [ラベルまたは値でピボットテーブルをフィルタリング](/cells/ja/python-net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python-net" >}}