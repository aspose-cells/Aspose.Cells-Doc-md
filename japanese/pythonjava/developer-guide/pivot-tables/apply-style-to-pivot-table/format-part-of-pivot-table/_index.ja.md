---
title: ピボットテーブルの一部の書式設定
linktitle: ピボットテーブルの一部の書式設定
description: Aspose.Cells for Python via Java でピボットテーブルの一部を書式設定します。PivotTable.format を使用して意味的な PivotArea 領域または CellArea 矩形にスタイルを適用し、書式は PivotTable.getPivotFormats() に保存され、ピボットテーブルが更新されても保持されます。
keywords: Aspose.Cells, Aspose.Cells for Python via Java, ピボットテーブル, 書式設定, PivotArea, CellArea, PivotTable.format, getPivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Python
type: docs
weight: 20
url: /ja/python-java/format-part-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
`PivotTable.formatAll` はピボットテーブル全体に単一のスタイルを適用し、親ページで取り上げられています。ラベル、値、合計、またはレポートの特定の領域を区別しません。  
実際には、ピボットテーブルの一部だけを強調表示する必要があることが多いです。一般的な対象としては、ある行フィールドに属するラベル、そのフィールドによって生成された値セル、総計行、または最初の 2 行のような任意の矩形があります。  
ピボットテーブルのワークシート上のセルに直接スタイルを適用しても同等ではありません。Excel はピボットテーブルの書式設定を普通のセルスタイル レコードではなく、意味的な `PivotArea` 領域として保存します。ピボット領域の書式はフィールドのラベルやデータ値などの領域に結び付けられ、ピボットテーブルが再計算、更新、または拡張される際に再解決されます。一方、セルに直接書き込まれたスタイルはそのセル位置に属し、ピボットモデルによって追跡されません。  
Aspose.Cells は完全な `PivotTable.format` オーバーロード ファミリーを提供しており、両方の書式設定方法が利用可能です。  
- `format(PivotArea, Style)` は、`PivotArea.select` または `PivotArea.selectField` で構築された意味的領域にスタイルを結び付けます。  
- `format(CellArea, Style)` は、ピボットテーブル内のワークシート矩形にスタイルを結び付けます。  
- `format(int row, int column, Style)` は単一のセルを対象とします。  
- `formatAll(Style)` はピボットテーブル全体を書式設定します。  

## **ピボット領域の書式設定**
フィールドやレポートの領域にハイライトを付随させる必要がある場合、意味的領域ワークフローが推奨されます。  
1. `PivotArea(pivot_table)` を使用して `PivotArea` を作成します。このオブジェクトは、特定のピボットテーブルに属する意味的領域を表します。  
1. `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` を使用して、指定された軸上のゼロベース位置でフィールドを選択します。  
   - `PivotTableSelectionType.DATA_AND_LABEL` はフィールドのラベルとデータの両方を選択します。  
   - `PivotTableSelectionType.LABEL_ONLY` はフィールドのラベルのみを選択します。  
   - `PivotTableSelectionType.DATA_ONLY` はフィールドのデータセルのみを選択します。  
1. `PivotArea.selectField(PivotFieldType axisType, String fieldName)` を使用してフィールド名で選択します。行フィールドを名前で選択すると、領域はそのフィールドの項目が生成する値セルに解決されます。  
1. `workbook.createStyle()` で `Style` を作成し、フォント、前景色、単色背景パターンを設定してから、そのスタイルを `PivotTable.format(area, style)` に渡します。  
1. `PivotArea` のオーバーロードを呼び出すたびに、`PivotTable.getPivotFormats()` に `PivotTableFormat` エントリが 1 つ追加されます。  
1. フィールドにアンカーされた書式はピボットデータが計算される際に適用されます。したがって、書式を適用した後に `PivotTable.calculateData()` を呼び出し、スタイルが表示されるようにします。  
以下の例は小規模なフルーツ販売ピボットテーブルを作成し、`PivotArea.select` と `PivotTableSelectionType.LABEL_ONLY` を使用して `Fruit` 行ラベルにスタイルを適用し、同じ行フィールドで生成された値セルに `PivotArea.selectField` でスタイルを適用し、最後にピボットテーブルを再計算して両方のスタイルを描画します。

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
    Style,
    Color,
    BackgroundType,
    PivotArea,
    PivotFieldType,
    PivotTableSelectionType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Fruit sales data
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
# Bold yellow fill on the row field's label cells
label_style = workbook.createStyle()
label_style.getFont().setBold(True)
label_style.setForegroundColor(Color.getYellow())
label_style.setPattern(BackgroundType.SOLID)
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.createStyle()
value_style.setForegroundColor(Color.getLightGreen())
value_style.setPattern(BackgroundType.SOLID)
value_area = PivotArea(pivot_table)
value_area.selectField(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculateData()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **ピボットテーブルのセル領域の書式設定**
関心領域が意味的なピボット領域ではなく、単純なワークシート矩形である場合は `PivotTable.format(CellArea, Style)` を使用します。  
`CellArea` は `getStartRow()`, `getStartColumn()`, `getEndRow()`, `getEndColumn()` プロパティで記述されます。これらの値はゼロベースのワークシート座標で、終了座標は矩形に含まれる最終行と列を示すため、開始位置から終了位置までのセルを含みます。  
フィールドにアンカーされた書式とは異なり、`CellArea` の書式はセルに即座に適用されます。スタイルを表示させるために `PivotTable.calculateData()` を再度呼び出す必要はありません。  
`CellArea` 矩形はラベルセルと値セルを同時に含むことがあります。次のセクションでは、Aspose.Cells と Excel がその矩形を内部的にどのように表現しているかを説明します。  
以下の例はピボットテーブルの矩形 `E4:F5` に斜体の薄い青色スタイルを適用し、再計算せずにワークブックを保存します。

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
    CellArea,
    PivotFieldType,
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
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
jpype.shutdownJVM()
```

## **ピボット領域とセル領域のマッピング**
Excel はピボットテーブルの書式設定を通常のワークシートセルスタイル レコードではなく `pivotArea` レコードとして保存します。同様のモデルが Aspose.Cells でも使用されており、書式設定要求は記録時にピボット領域へ変換されます。  
ユーザーが提供する `CellArea` と内部で保存されるピボット領域の関係は、双方向に多対多です。  
- 1 つの `CellArea` は複数のピボット領域を生成することがあります。矩形がラベルセルと値セルの両方を跨る場合、ピボットモデルはラベル書式とデータ書式を独立して扱うため、別々のラベル規則とデータ規則に分解されます。  
- 1 つのピボット領域は、いくつかの離散した `CellArea` インスタンスへと解決することがあります。総計行や項目が連続しないフィールドなどの意味的領域は、複数の矩形にまたがることがあります。そのため、`PivotArea.getCellAreas()` は単一の矩形ではなくコレクションを返します。  
`PivotTable.format` で実行されたすべての書式操作は `PivotTable.getPivotFormats()` に記録されます。各 `PivotTableFormat` エントリは関連付けられた `PivotArea` と適用された `Style` を示します。`PivotArea` のオーバーロードは呼び出しごとに正確に 1 件のエントリを追加しますが、異なる意味的領域を含む `CellArea` は複数のエントリを追加することがあります。  
保存された領域を区別するために、各 `PivotArea` は `getOnlyLabel()` と `getOnlyData()` フラグを公開しています。以下の例はラベルと値の両方をカバーする単一の矩形をフォーマットし、`PivotTable.getPivotFormats()` を調査し、各保存されたピボット領域が解決する `CellArea` の座標を出力します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import Color, CellArea, Style, BackgroundType
from asposecells.api import PivotTable, PivotArea, PivotFieldType
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
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
# ONE rectangle in...
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print("Stored formats: " + str(pivot_table.getPivotFormats().getCount()))
for i in range(pivot_table.getPivotFormats().getCount()):
    stored_area = pivot_table.getPivotFormats().get(i).getPivotArea()
    print(
        f"Format {i}: OnlyLabel={stored_area.getOnlyLabel()}, "
        f"OnlyData={stored_area.getOnlyData()}"
    )
    for resolved in stored_area.getCellAreas():
        print(
            f"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, "
            f"columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}"
        )
# This prints:
# Stored formats: 2
# Format 0: OnlyLabel=True, OnlyData=False
#     rows 4-5, columns 5-5        (E4:E5, the label part)
# Format 1: OnlyLabel=False, OnlyData=True
#     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
書式が普通のセルスタイルではなくピボット領域として保存されているため、再計算や更新後も保持されます。`PivotTable.refreshData()` でピボットテーブルを更新したり、`PivotTable.calculateData()` で再計算したり、保存して再ロードしたりすると、保存されたすべてのピボット領域が現在の領域位置に再解決され、スタイルが再適用されます。
{{% /alert %}}

ハイライトをリフレッシュ後もフィールドや意味的領域に付随させる必要がある場合は、`select` または `selectField` で構築した `PivotArea` を使用し、現在のピボットテーブルレイアウト内の固定矩形をフォーマットするだけでよい場合は `CellArea` を使用します。単一セルの `format(int row, int column, Style)` オーバーロードは個別のセルを対象とします。ピボットテーブル全体を一度に再スタイル設定したい場合は、親ページで説明されている `formatAll` を使用してください。

## **関連記事**
- [ピボットテーブルへのスタイル適用](/cells/ja/python-java/apply-style-to-pivot-table/)
- [ピボットテーブルの行および列フィールドの追加](/cells/ja/python-java/pivot-table-add-row-and-column-fields/)
- [ピボットテーブルの値フィールドの管理](/cells/ja/python-java/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}