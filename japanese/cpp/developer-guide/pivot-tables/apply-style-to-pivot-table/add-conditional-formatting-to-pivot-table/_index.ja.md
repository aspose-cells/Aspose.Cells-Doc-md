---
title: ピボットテーブルへの条件付き書式の追加
linktitle: ピボットテーブルへの条件付き書式の追加
description: Aspose.Cells for C++ でピボットテーブルに条件付き書式を追加します。ApplyTo と PivotConditionFormatScopeType のスコープでデータ領域にルールをアンカー付けするか、AddCellArea と PivotAreas で対象を定義し、FormatConditions.AddCondition を使用してルールとスタイルを適用します。
keywords: Aspose.Cells for C++, ピボットテーブル, 条件付き書式, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /ja/cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
親ページおよび兄弟ページで説明されているスタイルは静的です。`PivotArea` または `CellArea` 領域は一度塗りつぶされ、値が何であってもそのスタイルが保持されます。条件付き書式はルール駆動の対応物で、200 を超えるすべての金額をハイライトしたり、中央値の 50% をシェードしたり、下位ランクの項目にフラグを付けたりします。ハイライトはピボットテーブルが再計算または更新されるたびに値に追随します。  
Aspose.Cells では、ピボットテーブルの条件付き書式は `pivotTable.GetConditionalFormats()` コレクションに格納されています。各エントリは `PivotConditionalFormat` で、以下の2つの質問に独立して答えます：
- **ルールはどこに適用されますか？** ターゲット領域は `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` によって定義でき、これは Excel のユーザーインターフェイスのスコープピッカーに対応します。または `AddCellArea(CellArea)` と `GetPivotAreas()` コレクションを使用して、領域を明示的に指定します。
- **ルールは何をテストしますか？** `GetFormatConditions()` を使用し、`FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` によって 1 つまたは複数の条件を追加します。各条件はそれぞれの `Style` を持ちます。

{{% alert color="primary" %}}
ピボット条件付き書式の `GetFormatConditions()` オブジェクトに対して `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` や `FormatConditionCollection.AddArea(CellArea)` を呼び出さないでください。これらのオーバーロードは通常のワークシート条件付き書式 API から継承されており、ピボットテーブルでは機能しません。セル領域はピボット領域に変換されないため、リクエストは黙って無視されます。領域は必ず `PivotConditionalFormat` 自体で（`ApplyTo`、`AddCellArea`、または `GetPivotAreas()`）定義し、`AddCondition` のいずれかのオーバーロードでルールを追加してください。
{{% /alert %}}

## **スコープを使用したルールの適用（Excel UI の方法）**
最初の方法は、Excel のユーザーインターフェイスと同様にルールの位置を決めます。ピボットテーブルのセルはゼロベースのワークシート座標で指定され、`PivotConditionFormatScopeType` のスコープにより、Aspose.Cells はそのセルからルールがどの範囲まで適用されるかを判断します：
- `PivotConditionFormatScopeType::Data` - ピボットテーブルが生成するすべての値セル、総計を含みます。
- `PivotConditionFormatScopeType::Field` - セルが示すフィールドに属する値セルで、総計は除外されます。セルは行フィールドラベルなどのフィールドセルである必要があり、値セルを渡すと例外がスローされます。
- `PivotConditionFormatScopeType::Selection` - セルが選択した交差点の値セルのみで、通常は単一の値セルです。
以下の例は、左上隅が E3 の果物売上ピボットテーブルを作成し、セル F4（行 3、列 5）に `Data` スコープで条件付き書式をアンカー付け、200 円を超える金額を赤背景に白文字の太字でハイライトします。Apple が 220、Banana が 330、Cherry が 200、合計が 750 の場合、ルールは F4、F5、F7 に適用されます。解決された領域はデータ列全体の F4:F7 で、条件を満たすセルだけがハイライトされます。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    format.ApplyTo(3, 5, PivotConditionFormatScopeType::Data);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::GreaterThan, u"200", nullptr);
    Style style = workbook.CreateStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    font.SetColor(Color::White());
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatData.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

`Field` スコープで同じルールを行フィールドラベル E4（行 3、列 4）にアンカー付けすると、対象は F4:F6 となります。これは合計行を除いた同じデータ列です。スコープが全体の値領域ではなく `Fruit` フィールドを指すためです。`Selection` スコープで F4 にアンカー付けすると、対象は F4 のみになります。

## **領域を手動で定義する**
2 番目の方法はスコープピッカーを省略し、`PivotConditionalFormat` 上で領域を明示的に指定します。

### **AddCellArea を使用したワークシート矩形**
`AddCellArea(CellArea)` は、指定された矩形をルールのターゲットとして記録します。座標はゼロベースのワークシート座標で、領域は提供された矩形そのものです。データ列への拡張や総計ロジックはありません。現在のピボットレイアウトで対象セルが既知の固定矩形である場合に使用します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    U16String fruits[] = {
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Cherry"),
        U16String(u"Cherry")
    };
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));
    pivotTable.CalculateData();
    int32_t index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    CellArea area;
    area.StartRow = 3;
    area.EndRow = 5;
    area.StartColumn = 5;
    area.EndColumn = 5;
    format.AddCellArea(area);
    int32_t conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue,
        OperatorType::Between,
        u"150",
        u"300");
    Style style = workbook.CreateStyle();
    style.GetFont().SetIsItalic(true);
    style.SetForegroundColor(Color::LightYellow());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **PivotAreas を使用した意味的ピボット領域**
`GetPivotAreas()` は、兄弟ページの静的スタイルで使用されているのと同じ意味的領域モデルを提供します。`PivotArea` を作成し、`Select` または `SelectField` でフィールドまたは領域を選択し、`GetPivotAreas().AddPivotArea(PivotArea)` で追加します。意味的領域はフィールドに結び付けられたままなので、ピボットテーブルが更新されレイアウトが変わっても条件付き書式はフィールドに追随します。`GetPivotAreas().Add(PivotArea)` のオーバーロードはまだコンパイルできますが、非推奨とされているため `AddPivotArea` を使用してください。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    PivotArea area(pivotTable);
    area.SelectField(PivotFieldType::Data, u"Amount");
    format.GetPivotAreas().AddPivotArea(area);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::LessThan, u"150", nullptr);
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Gray());
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **ルールの保存場所とリロード後の持続方法**
`pivotTable.GetConditionalFormats().Add()` の呼び出しは、ピボットテーブルに `PivotConditionalFormat` を 1 つ追加します。条件、数式、スタイルはワークブックに保存されます。以下の例でファイルを再度開くと、同じルールがタイプ、演算子、数式が保持されたまま存在し、`GetCellAreas()` は同じ領域を報告します。条件が設定されていないエントリは、ワークブック保存時に削除されます。これは Excel がルールのない条件付き書式を破棄するのと同様です。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
static const char* ToString(FormatConditionType type)
{
    switch (type)
    {
    case FormatConditionType::CellValue:
        return "CellValue";
    default:
        return "Unknown";
    }
}
static const char* ToString(OperatorType op)
{
    switch (op)
    {
    case OperatorType::GreaterThan:
        return "GreaterThan";
    default:
        return "Unknown";
    }
}
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"PivotConditionalFormatData.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    auto conditionalFormats = pivotTable.GetConditionalFormats();
    int formatCount = conditionalFormats.GetCount();
    std::cout << "Conditional formats: " << formatCount << std::endl;
    for (int i = 0; i < formatCount; ++i)
    {
        PivotConditionalFormat format = conditionalFormats.Get(i);
        auto formatConditions = format.GetFormatConditions();
        int conditionCount = formatConditions.GetCount();
        for (int j = 0; j < conditionCount; ++j)
        {
            FormatCondition condition = formatConditions.Get(j);
            std::cout << "Format " << i << ": "
                      << ToString(condition.GetType()) << " "
                      << ToString(condition.GetOperator())
                      << " formula1=" << condition.GetFormula1().ToUtf8()
                      << std::endl;
        }
        Vector<CellArea> areas = format.GetCellAreas();
        for (int k = 0; k < areas.GetLength(); ++k)
        {
            CellArea area = areas[k];
            std::cout << "    rows " << area.StartRow + 1 << "-" << area.EndRow + 1
                      << ", columns " << area.StartColumn + 1 << "-" << area.EndColumn + 1
                      << std::endl;
        }
    }
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **関連項目**
- [ピボットテーブルへのスタイル適用](/cells/ja/cpp/apply-style-to-pivot-table/)
- [ピボットテーブルの一部をフォーマット](/cells/ja/cpp/format-part-of-pivot-table/)
- [ピボットテーブルで上位 10 の表示またはフィルター](/cells/ja/cpp/top-10-show-or-filter-in-pivot-table/)
- [ラベルまたは値でピボットテーブルをフィルタリング](/cells/ja/cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="cpp" >}}