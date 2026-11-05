---
title: ピボットテーブルに条件付き書式を追加する
linktitle: ピボットテーブルに条件付き書式を追加する
description: Aspose.Cells for Python via Java でピボットテーブルに条件付き書式を追加します。applyTo と PivotConditionFormatScopeType のスコープでデータ領域にルールをアンカーするか、addCellArea と getPivotAreas で対象を定義し、getFormatConditions().addCondition を使用してルールとスタイルを添付します。
keywords: Aspose.Cells for Python via Java, ピボットテーブル, 条件付き書式, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Python via Java
type: docs
weight: 30
url: /ja/python-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **想定使用シナリオ**
親ページおよび兄弟ページで説明されているスタイルは静的です。`PivotArea` または `CellArea` 領域は一度塗りつぶされ、値がどうであってもその書式設定が保持されます。条件付き書式はルール駆動の対応物で、200 を超えるすべての金額をハイライトしたり、中央値の 50% を色付けしたり、下位ランクの項目に旗印を付けたりします。そして、ピボットテーブルが再計算または更新されるたびにハイライトが値に追随します。
In Aspose.Cells では、ピボットテーブルの条件付き書式は `PivotTable.getConditionalFormats()` コレクションに格納されます。各エントリは `PivotConditionalFormat` で、次の 2 つの質問に独立して答えます:
- **ルールはどこに適用されますか？** 対象領域は、Excel のユーザーインターフェイスのスコープ ピッカーに相当する `PivotConditionalFormat.applyTo(int row, int column, PivotConditionFormatScopeType scope)` で定義するか、`PivotConditionalFormat.addCellArea(CellArea)` と `PivotConditionalFormat.getPivotAreas()` コレクションで明示的に領域を指定します。
- **ルールは何をテストしますか？** 1 つまたは複数の条件は、`PivotConditionalFormat.getFormatConditions()` に `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` を使用して追加され、各条件はそれぞれの `Style` を持ちます。

{{% alert color="primary" %}}
ピボット条件付き書式の `PivotConditionalFormat.getFormatConditions()` オブジェクトに対して `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` または `FormatConditionCollection.addArea(CellArea)` を呼び出さないでください。これら 2 つのオーバーロードは通常のワークシート条件付き書式 API から継承されたもので、ピボットテーブルでは機能しません。セル領域はピボット領域に変換されず、要求は黙って無視されます。常に `PivotConditionalFormat` 自体で領域を定義（`applyTo`、`addCellArea`、または `getPivotAreas()`）し、`addCondition` のいずれかのオーバーロードでルールを追加してください。
{{% /alert %}}

## **スコープを使用してルールを適用する（Excel UI の方法）**
最初の方法は、Excel のユーザーインターフェイスと同様にルールを配置します。ピボットテーブルのセルはゼロベースのワークシート座標で名前付けされ、`PivotConditionFormatScopeType` スコープはそのセルからルールがどれだけ広がるかを Aspose.Cells に指示します:
- `PivotConditionFormatScopeType.DATA` - ピボットテーブルが生成するすべての値セル（合計行を含む）。
- `PivotConditionFormatScopeType.FIELD` - セルが識別するフィールドに属する値セル（合計行は除外）。セルは行フィールド ラベルなどのフィールドセルである必要があり、値セルを渡すと例外がスローされます。
- `PivotConditionFormatScopeType.SELECTION` - セルが選択する交差点の値セルのみで、通常は単一の値セルです。
以下の例は、左上隅が E3 にある果物販売のピボットテーブルを作成し、`DATA` スコープでセル F4（行 3、列 5）に条件付き書式をアンカーし、200 を超えるすべての金額を赤背景に白太字でハイライトします。Apple が 220、Banana が 330、Cherry が 200、合計が 750 の場合、ルールは F4、F5、F7 を書式設定します。解決された領域はデータ列全体の F4:F7 で、条件を満たすセルだけがハイライトされます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Color,
    BackgroundType,
    PivotFieldType,
    PivotConditionFormatScopeType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Anchor the conditional format at F4 (row 3, column 5) with the Data scope
index = pivot_table.getConditionalFormats().add()
format = pivot_table.getConditionalFormats().get(index)
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA)
# Rule - highlight amounts greater than 200
condition_index = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.GREATER_THAN,
    "200",
    None,
)
style = workbook.createStyle()
style.getFont().setBold(True)
style.getFont().setColor(Color.getWhite())
style.setForegroundColor(Color.getRed())
style.setPattern(BackgroundType.SOLID)
format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatData.xlsx")
jpype.shutdownJVM()
```

`FIELD` スコープで同じルールを行フィールド ラベル E4（行 3、列 4）にアンカーすると、対象は F4:F6 となります。これは合計行を除く同じデータ列です。スコープが全体の値領域ではなく `Fruit` フィールドを表すためです。`SELECTION` スコープを F4 にアンカーすると、対象は F4 のみになります。

## **領域を手動で定義する**
2 番目の方法はスコープ ピッカーを省略し、`PivotConditionalFormat` 上で領域を明示的に指定します。

### **addCellArea() を使用したワークシート矩形**
`addCellArea(CellArea)` は、指定された矩形をルールの対象として記録します。座標はゼロベースのワークシート座標で、領域は提供された矩形そのものです。データ列への拡張や合計行のロジックはありません。対象セルが現在のピボットレイアウトの既知の固定矩形である場合に使用します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    CellArea,
    Color,
    BackgroundType,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Target the rectangle F4:F6 (the value cells without the grand total)
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = CellArea()
area.StartRow = 3
area.StartColumn = 5
area.EndRow = 5
area.EndColumn = 5
conditional_format.addCellArea(area)
# Rule - italic on light yellow for amounts between 150 and 300
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.BETWEEN,
    "150",
    "300",
)
style = workbook.createStyle()
style.getFont().setItalic(True)
style.setForegroundColor(Color.getLightYellow())
style.setPattern(BackgroundType.SOLID)
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatCellArea.xlsx")
jpype.shutdownJVM()
```

### **getPivotAreas() を使用した意味的ピボット領域**
`getPivotAreas()` コレクションは、兄弟ページで静的スタイルに使用されているのと同じ意味的領域モデルです。`PivotArea` を作成し、`PivotArea.select(...)` または `PivotArea.selectField(...)` でフィールドまたは領域を選択し、`getPivotAreas().addPivotArea(PivotArea)` で追加します。意味的領域はそのフィールドに付随したままになるため、ピボットテーブルが更新されレイアウトが変わっても条件付き書式はフィールドに追随します。`getPivotAreas().add(PivotArea)` のオーバーロードもコンパイルは通りますが、廃止予定とマークされているため、`addPivotArea` を使用してください。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Color,
    PivotArea,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Attach the rule to the Amount data field as a semantic region
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = PivotArea(pivot_table)
area.selectField(PivotFieldType.DATA, "Amount")
conditional_format.getPivotAreas().addPivotArea(area)
# Rule - grey text for amounts below 150
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.LESS_THAN,
    "150",
    None,
)
style = workbook.createStyle()
style.getFont().setColor(Color.getGray())
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **ルールの格納場所とリロード後の持続方法**
`PivotTable.getConditionalFormats().add()` 呼び出しは、ピボットテーブルに `PivotConditionalFormat` を 1 つ追加します。条件、数式、スタイルはワークブックに保存され、以下の例でファイルを再度開くと、同じルールがタイプ、演算子、数式がそのまま保持された状態で表示され、`PivotConditionalFormat.getCellAreas()` は同じ領域を報告します。条件が一度も設定されていないエントリは、ワークブックが保存される際に削除されます。これは、Excel がルールのない条件付き書式を破棄するのと同様です。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
print("Conditional formats: " + str(pivot_table.getConditionalFormats().getCount()))
for i in range(pivot_table.getConditionalFormats().getCount()):
    pivot_format = pivot_table.getConditionalFormats().get(i)
    format_conditions = pivot_format.getFormatConditions()
    for j in range(format_conditions.getCount()):
        condition = format_conditions.get(j)
        print(
            f"Format {i}: {condition.getType()} "
            f"{condition.getOperator()} formula1={condition.getFormula1()}"
        )
    for area in pivot_format.getCellAreas():
        print(
            f"    rows {area.StartRow + 1}-{area.EndRow + 1}, "
            f"columns {area.StartColumn + 1}-{area.EndColumn + 1}"
        )
# This prints:
# Conditional formats: 1
# Format 0: CellValue GreaterThan formula1==200
#     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
jpype.shutdownJVM()
```

## **関連項目**
- [ピボットテーブルへのスタイル適用](/cells/ja/python-java/apply-style-to-pivot-table/)
- [ピボットテーブルの一部の書式設定](/cells/ja/python-java/format-part-of-pivot-table/)
- [ピボットテーブルで上位 10 件の表示またはフィルター](/cells/ja/python-java/top-10-show-or-filter-in-pivot-table/)
- [ラベルまたは値でピボットテーブルをフィルタリング](/cells/ja/python-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python" >}}