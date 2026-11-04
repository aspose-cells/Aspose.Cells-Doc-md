---
title: ピボットテーブルの一部をフォーマットする
linktitle: ピボットテーブルの一部をフォーマットする
description: Aspose.Cells for C++ で PivotTable.Format を使用して、セマンティックな PivotArea 領域または CellArea 四角形にスタイルを適用し、PivotTable.GetPivotFormats に保存された書式は、ピボットテーブルが更新されても保持されます。
keywords: Aspose.Cells, ピボットテーブル, フォーマット, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /ja/cpp/format-part-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **利用シナリオ**
`PivotTable.FormatAll` はピボットテーブル全体に単一のスタイルを適用し、親ページで説明されています。ラベル、値、合計、またはレポートの特定領域を区別しません。  
実際には、ピボットテーブルの一部だけを目立たせる必要があることが多いです。一般的な対象には、特定の行フィールドに属するラベル、そのフィールドによって生成された値セル、総合計行、または最初の 2 行のような任意の矩形があります。  
ピボットテーブルのワークシートセルに直接スタイルを適用しても同等ではありません。Excel はピボットテーブルの書式を、通常のセルスタイル レコードではなく、セマンティックな `PivotArea` 領域として保存します。PivotArea の書式はフィールドのラベルやデータ値といった領域に固定され、ピボットテーブルが再計算、更新、または拡張されると再解決されます。一方、セルに直接書き込まれたスタイルはそのセル位置に属し、ピボットモデルによって追跡されません。  
Aspose.Cells は両方の書式設定が利用できるように、完全な `PivotTable.Format` オーバーロード ファミリーを公開しています：
- `Format(const PivotArea&, const Style&)` は `PivotArea.Select` または `PivotArea.SelectField` で構築されたセマンティック領域にスタイルを固定します。
- `Format(const CellArea&, const Style&)` はピボットテーブル内のワークシート矩形にスタイルを固定します。
- `Format(int32_t row, int32_t column, const Style&)` は単一のセルを対象とします。
- `FormatAll(const Style&)` はピボットテーブル全体をフォーマットします。

## **PivotArea をフォーマットする**
ハイライトがフィールドやレポートの領域に従う必要がある場合、セマンティック領域ワークフローが推奨されます。  
1. `PivotArea pivotArea(pivotTable);` で `PivotArea` を作成します。このオブジェクトは、特定のピボットテーブルに属するセマンティック領域を表します。  
2. 指定された軸上で、ゼロベースの位置でフィールドを選択するには `PivotArea.Select(PivotFieldType axisType, int32_t fieldPosition, PivotTableSelectionType selectionType)` を使用します。  
   - `PivotTableSelectionType::DataAndLabel` はフィールドのラベルとデータの両方を選択します。  
   - `PivotTableSelectionType::LabelOnly` はフィールドのラベルのみを選択します。  
   - `PivotTableSelectionType::DataOnly` はフィールドのデータセルのみを選択します。  
3. `PivotArea.SelectField(PivotFieldType axisType, const char16_t* fieldName)` でフィールド名で選択します。行フィールドを名前で選択すると、領域はそのフィールドの項目によって生成された値セルに解決されます。  
4. `Workbook.CreateStyle()` で `Style` を作成し、フォント、前景色、単色の背景パターンを設定し、そのスタイルを `PivotTable.Format(pivotArea, style)` に渡します。  
5. `PivotArea` のオーバーロードを呼び出すたびに、`PivotTable.GetPivotFormats()` に `PivotTableFormat` エントリが 1 件追加されます。  
6. フィールドに固定された書式はピボットデータが計算されたときに適用されます。したがって、書式を適用した後に `PivotTable.CalculateData()` を呼び出して、スタイルを表示させます。  
以下の例は小規模な果物売上ピボットテーブルを作成し、`PivotArea.Select` と `PivotTableSelectionType::LabelOnly` を使用して `Fruit` 行ラベルにスタイルを適用し、同じ行フィールドで生成された値セルに `PivotArea.SelectField` でスタイルを適用し、最後にピボットテーブルを再計算して両方のスタイルを反映させます。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Fruit sales data
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Pivot table with its top-left corner at E3
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Bold yellow fill on the row field's label cells
    Style labelStyle = workbook.CreateStyle();
    labelStyle.GetFont().SetIsBold(true);
    labelStyle.SetForegroundColor(Color::Yellow());
    labelStyle.SetPattern(BackgroundType::Solid);
    PivotArea labelArea(pivotTable);
    labelArea.Select(PivotFieldType::Row, 0, PivotTableSelectionType::LabelOnly);
    pivotTable.Format(labelArea, labelStyle);
    // Light green fill on the value cells the row field produces
    Style valueStyle = workbook.CreateStyle();
    valueStyle.SetForegroundColor(Color::LightGreen());
    valueStyle.SetPattern(BackgroundType::Solid);
    PivotArea valueArea(pivotTable);
    valueArea.SelectField(PivotFieldType::Row, u"Fruit");
    pivotTable.Format(valueArea, valueStyle);
    // Field-anchored formats are painted when the data is calculated
    pivotTable.CalculateData();
    // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
    workbook.Save(u"FormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **ピボットテーブルのセル領域をフォーマットする**
対象領域がセマンティックなピボット領域ではなく、単なるワークシートの矩形である場合は `PivotTable.Format(const CellArea&, const Style&)` を使用します。  
`CellArea` は `StartRow`、`StartColumn`、`EndRow`、`EndColumn` の公開フィールドで記述されます。これらの値はゼロベースのワークシート座標で、終了座標は矩形に含まれる最終行と最終列を示すため、開始位置から終了位置までのセルがすべて含まれます。  
フィールドに固定された書式とは異なり、`CellArea` の書式はセルに即座に適用されます。スタイルを表示させるために `CalculateData()` を再度呼び出す必要はありません。  
`CellArea` の矩形はラベルセルと値セルを同時に含むことがあります。次のセクションでは、Aspose.Cells と Excel がその矩形を内部でどのように表現するかを説明します。  
以下の例はピボットテーブルの矩形 `E4:F5` をイタリック体の薄い青色スタイルでフォーマットし、追加の再計算なしでワークブックを保存します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Highlight the first two fruit rows (the rectangle E4:F5)
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // E4:F5 is italic on light blue immediately, no recalculation needed
    workbook.Save(u"FormatPivotCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **PivotArea と CellArea のマッピング方法**
Excel はピボットテーブルの書式を、通常のワークシートセルスタイル レコードではなく `pivotArea` レコードとして保存します。同じモデルが Aspose.Cells でも使用されているため、書式設定要求は記録時にピボット領域に変換されます。  
ユーザーが提供した `CellArea` と内部に保存されるピボット領域との関係は、双方向で多対多です。  
- `CellArea` は複数のピボット領域を生成することがあります。矩形がラベルセルと値セルの両方を包含する場合、ピボットモデルがラベル書式とデータ書式を独立して扱うため、ラベル用とデータ用の別々の規則に分解されます。  
- 1つのピボット領域は、いくつかの分離した `CellArea` インスタンスに解決されることがあります。総合計行のようなセマンティック領域や、項目が連続していないフィールドは複数の矩形をカバーできます。これが `PivotArea.GetCellAreas()` が単一の矩形ではなく `Vector<CellArea>` を返す理由です。  
`PivotTable.Format` で実行されたすべての書式操作は `PivotTable.GetPivotFormats()` に記録されます。各 `PivotTableFormat` エントリは関連付けられた `PivotArea` と適用された `Style` を公開します。`PivotArea` のオーバーロードは呼び出しごとに正確に 1 件のエントリを追加しますが、異なるセマンティック領域を含む `CellArea` は複数のエントリを追加することがあります。  
保存された領域を区別するために、各 `PivotArea` は `GetOnlyLabel()` と `GetOnlyData()` フラグを公開します。以下の例はラベルと値の両方をカバーする単一の矩形をフォーマットし、`PivotTable.GetPivotFormats()` を調べ、各保存されたピボット領域が解決する `CellArea` 座標を出力します。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    // ONE rectangle in...
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // ...TWO semantic pivot areas out: the label part and the data part are stored separately
    std::cout << "Stored formats: " << pivotTable.GetPivotFormats().GetCount() << std::endl;
    for (int i = 0; i < pivotTable.GetPivotFormats().GetCount(); i++)
    {
        PivotArea storedArea = pivotTable.GetPivotFormats().Get(i).GetPivotArea();
        std::cout << "Format " << i << ": OnlyLabel=" << (storedArea.GetOnlyLabel() ? "true" : "false")
                  << ", OnlyData=" << (storedArea.GetOnlyData() ? "true" : "false") << std::endl;
        Vector<CellArea> resolved = storedArea.GetCellAreas();
        for (int j = 0; j < resolved.GetLength(); j++)
        {
            std::cout << "    rows " << (resolved[j].StartRow + 1) << "-" << (resolved[j].EndRow + 1)
                      << ", columns " << (resolved[j].StartColumn + 1) << "-" << (resolved[j].EndColumn + 1) << std::endl;
        }
    }
    // This prints:
    // Stored formats: 2
    // Format 0: OnlyLabel=true, OnlyData=false
    //     rows 4-5, columns 5-5        (E4:E5, the label part)
    // Format 1: OnlyLabel=false, OnlyData=true
    //     rows 4-5, columns 6-6        (F4:F5, the data part)
    workbook.Save(u"FormatPivotAreasMap.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
書式が通常のセルスタイルではなくピボット領域として保存されるため、再計算や更新後も保持されます。ピボットテーブルが `PivotTable.RefreshData` で更新され、`CalculateData` で再計算されるか、保存して再読み込みされた場合でも、保存された各ピボット領域はその領域の現在位置に再度解決され、スタイルが再適用されます。
{{% /alert %}}

ハイライトが更新後もフィールドやセマンティック領域に固定される必要がある場合は `Select` または `SelectField` で構築された `PivotArea` を使用し、現在のピボットテーブルレイアウト内の固定矩形のフォーマットで十分な場合は `CellArea` を使用します。単一セル向けの `Format(int32_t row, int32_t column, const Style&)` オーバーロードは個別のセルを対象とします。ピボットテーブル全体を一度に再スタイル化する場合は、親ページで説明されている `FormatAll` を使用します。

## **Related Articles**
- [ピボットテーブルへのスタイル適用](/cells/ja/cpp/apply-style-to-pivot-table/)
- [ピボットテーブルの行および列フィールドの追加](/cells/ja/cpp/pivot-table-add-row-and-column-fields/)
- [ピボットテーブルの値フィールドの管理](/cells/ja/cpp/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}