---
title: ラベルまたは値によるピボットテーブルのフィルター処理
linktitle: ラベルまたは値によるピボットテーブルのフィルター処理
description: Aspose.Cells for C++ は、lloquat&amp;、#x3010;Ash; ピボットテーブルの包括的なフィルター処理機能を備えています。このiscale; Bibliothek; 、ラベルフィルター、日付フィルター、値フィルター、上位 10 個フィルター、およびピボット項目の非表示または再表示を使用して、ピボットテーブルのデータをフィルター処理する方法を説明します。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, ピボットテーブル, フィルター, ラベルフィルター, 値フィルター, 日付フィルター, 上位 10 個フィルター, ピボット項目, ピボット項目の非表示
type: docs
weight: 10
url: /ja/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルター処理するための実用的な戦略を 5 つ提供しています。テキストベースの行フィールドまたは列フィールドにラベルフィルターを適用したり、フィールドに日付時刻セルまたは空白のみが含まれる場合に日付フィルターを使用したり、集約された数値に値フィルターを適用したり、値フィールドに基づいて順位付けを行う上位 10 個フィルターを使用したり、`IsHidden` プロパティを使用して個々のピボット項目を手動で非表示または再表示したりできます。各戦略には、`PivotField` クラスと `PivotItem` クラスの専用 API が用意されています。
{{% /alert %}}

## **はじめに**
ピボットテーブルは強力な分析ツールですが、集計結果には、レポートに表示する必要のない情報が多数含まれることがよくあります。フィルター処理は、特定のレポートに必要な行、列、または値までピボットテーブルを絞り込むための主な手段です。Aspose.Cells for C++ は、Microsoft Excel で利用できるフィルター処理機能をプログラムから利用できるようにしており、レポート生成を完全に自動化できます。
以下のフィルター処理方法を示します。
1. **ラベルフィルター** — テキストラベルに基づいて、行または列フィールドの項目をフィルター処理します。
2. **日付フィルター** — 日時値（または空白）のみを含む行または列フィールドをフィルター処理します。
3. **値フィルター** — データフィールドの集約値に基づいて項目をフィルター処理します。
4. **上位 10 個フィルター** — 値フィールドに基づいて順位付けされた上位または下位 N 個の項目だけを表示します。
5. **ピボット項目の非表示 / 再表示** — フィールド内の個々の項目の表示状態を手動で制御します。
方法ごとに異なる `PivotField` クラスのメソッド、または `PivotItem` クラスのプロパティを使用します。フィルターを適用した後は、ピボットテーブルで `GetPivotCache().Refresh()` を呼び出し、キャッシュされたデータと計算された値が新しいフィルター状態を反映するようにする必要があります。

## **ラベルフィルター**
ラベルフィルターでは、行または列フィールドの各項目について、テキストキャプションとパターンを比較してフィルター処理できます。製品名が特定の文字で始まる項目だけを表示する場合や、特定の語を含む項目だけを表示する場合など、キャプションに基づく条件に一致する項目のみを表示したい場合に便利です。
Aspose.Cells は、`PivotField.FilterByLabel(PivotFilterType, const char16_t*)` メソッドを通じてラベルフィルター処理を提供します。`PivotFilterType` 列挙体には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2 番目の引数には、比較に使用するラベル文字列を指定します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、キャプションが指定した接頭辞で始まる項目だけが残るようにラベルフィルターを適用し、ピボットテーブルを更新して結果を保存します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // Load the existing workbook containing a pivot table
    Workbook wb(fileName);
    // Access the worksheet by index (first worksheet)
    Worksheet ws = wb.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Retrieve the first row PivotField
    PivotField rowField = pt.GetRowFields().Get(0);
    // Apply the label filter — show only row items whose labels begin with the supplied prefix
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // Refresh and recalculate the pivot table data so the filter takes effect
    pt.GetPivotCache().Refresh();
    // Save the workbook back to disk
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **日付フィルター**
日付フィルターでは、今日、先週、今月、来四半期、または特定の日付範囲など、日付に基づく条件でピボットテーブルを絞り込めます。これらは、日付時刻情報を格納するフィールドに対してのみ機能する特殊なフィルターです。

{{% alert color="primary" %}}
日付フィルターは、行領域または列領域に日付時刻セルまたは空白値のみが含まれている場合にのみ機能します。対象のフィールドに数値やテキストなど他のデータ型が含まれている場合、日付フィルターは想定どおりの結果になりません。フィルターを適用する前に、フィールドが日付として書式設定されていること、およびすべての値が有効な `DateTime` インスタンスまたは空セルであることを確認してください。
Aspose.Cells は、`PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)` メソッドを通じて日付フィルター処理を提供します。`PivotFilterType` 列挙体には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの専用の日付値が含まれます。選択したフィルターの種類に応じて、1 つまたは 2 つの `DateTime` 値を指定します（`Between` の場合は開始日と終了日を指定します）。
次の例では、行領域に日付フィールドを持つピボットテーブルを含むワークブックを読み込み、表示される項目を特定の日付範囲に制限する日付フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    std::string inputPath = "sample.xlsx";
    std::string outputPath = "output_filtered.xlsx";
    if (!std::filesystem::exists(inputPath))
    {
        // Source workbook not found.
        Aspose::Cells::Cleanup();
        return -1;
    }
    // Load the existing workbook that contains the pivot table
    Workbook workbook(U16String(inputPath.c_str()));
    // Access the worksheet that holds the pivot table (by index)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // Retrieve the date PivotField from the row area
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // Define the date criterion for the Between filter
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // Apply the date filter on the pivot field
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    // Persist the workbook
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **値フィルター**
値フィルターは、ピボットテーブルがデータ領域で計算する集約値に対して作用します。テキストラベルを照合するのではなく、数値の合計をしきい値と比較します。売上合計が目標金額を超える製品だけを表示する場合や、取引件数が特定の範囲内にある地域だけを表示する場合などに利用できます。
Aspose.Cells は、`PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)` メソッドを通じて値フィルター処理を提供します。`filterType` パラメーターでは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を使用します。`valueField` パラメーターは、評価対象のデータフィールドを指定し、最後の引数にはしきい値を指定します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集約された売上が数値のしきい値を超える項目だけを残す値フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。

```cpp
#include "Aspose.Cells.h"
#include <cfloat>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sample.xlsx");
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    int dataFieldIndex = -1;
    int dataFieldCount = pivotTable.GetDataFields().GetCount();
    for (int i = 0; i < dataFieldCount; i++)
    {
        PivotField current = pivotTable.GetDataFields().Get(i);
        if (current.GetName() == dataField.GetName())
        {
            dataFieldIndex = i;
            break;
        }
    }
    if (dataFieldIndex >= 0)
    {
        rowField.FilterByValue(dataFieldIndex, PivotFilterType::ValueGreaterThan, 5000, DBL_MAX);
    }
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **上位 10 個フィルター**
上位 10 個フィルターは値フィルターの特殊な形式であり、選択した値フィールドに基づいて、上位または下位 N 個の項目だけを残します。「売上上位 10 製品」や「販売件数下位 5 地域」などの順位付け用レポートで一般に使用されます。

{{% alert color="primary" %}}
上位 10 個フィルターは、ピボットテーブルのデータ領域に 1 つ以上の値ピボットフィールドがある場合にのみ有効です。値フィールドが 1 つもない場合、項目を順位付けするための集約値が存在しないため、このフィルターを適用できません。
Aspose.Cells は、`PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)` メソッドを通じて上位 10 個フィルター処理を提供します。`valueFieldIndex` パラメーターは、集約値によって項目を順位付けするデータフィールドのインデックスです。`type` は `itemCount` の単位を指定します（`PivotFilterType::Count` は固定数の項目を残し、`PivotFilterType::Percent` は項目の割合を残すため、`itemCount` には割合の値を直接指定します）。`isTop` は、上位項目を残す場合は true、下位項目を残す場合は false を示します。`itemCount` は、残す項目数または割合を指定します。
次の例では、値フィールドを含むピボットテーブルを読み込み、売上の合計に基づいて上位 10 個の項目だけを残す上位 10 個フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <stdexcept>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String inputPath(u"input.xlsx");
    U16String outputPath(u"output.xlsx");
    Workbook workbook(inputPath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    if (pivotTable.GetDataFields().GetCount() == 0) {
        throw std::runtime_error("Pivot table has no value (data) PivotField.");
    }
    PivotField valueField = pivotTable.GetDataFields().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    int valueFieldIndex = 0;
    rowField.FilterTop10(valueFieldIndex, PivotFilterType::Count, true, 10);
    // Refresh the pivot table data and recalculate it so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    workbook.Save(outputPath);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **ピボット項目の非表示または再表示によるフィルタリング**
構造化されたフィルター API に加えて、Aspose.Cells では個々のピボット項目の表示状態を直接制御できます。`PivotField` の `PivotItems` コレクションを反復処理し、`IsHidden` プロパティを切り替えることで、数式ベースのフィルターを適用せずに、特定の項目だけを選択的に非表示にできます。`IsHidden = true` に設定すると、その項目はピボットテーブルから非表示になります。`IsHidden = false` に設定すると、その項目が再表示され、再び表示されます。
この方法は、フィルター条件が不規則である場合や項目ごとに異なる場合、または特定のレポートに表示してはならない少数のカテゴリを非表示にする場合などに便利です。次の例では、ピボットテーブルを含むワークブックを読み込み、名前で指定した項目を非表示にし、その項目を再表示する方法を示します。ピボットテーブルを更新してワークブックを保存します。

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load an existing workbook containing a pivot table
    Workbook workbook(u"pivot_table_sample.xlsx");
    // Access the first worksheet which contains the pivot table
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index (the first pivot table on the sheet)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // Iterate through the PivotItems collection of the selected PivotField
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // Hide pivot items that match a specific name/criterion
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // Demonstrate unhiding: re-show a previously hidden pivot item
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // Refresh and recalculate the pivot table so changes take effect
    pivotTable.GetPivotCache().Refresh();
    // Save the workbook — hidden items stay in the underlying data
    // but are excluded from the displayed pivot table output
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **まとめ**
Aspose.Cells for C++ は、Microsoft Excel に備わるものと同等のピボットテーブルフィルター処理機能を一式提供します。ラベルフィルター、日付フィルター、値フィルターは最も一般的な分析シナリオに対応し、上位 10 個フィルターは順位付け用レポートに対応します。フィルター条件が不規則な場合は、`PivotItem.IsHidden` プロパティが、項目単位の柔軟な代替手段となります。これらの戦略を組み合わせる（たとえば、ラベルフィルターを適用してから特定の項目を非表示にする）と、コードを介してピボットテーブルのレポートを正確に絞り込めます。

## 関連記事
- [ピボットテーブルを挿入](/cells/ja/cpp/create-pivot-table/)
- [Aspose.Cells for C++ でピボットテーブルの行と列フィールドを追加](/cells/ja/cpp/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for C++ でピボットテーブルにフィルターフィールドを追加](/cells/ja/cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for C++ でピボットテーブルの値フィールドを管理](/cells/ja/cpp/manage-value-fields/)
- [Aspose.Cells for C++ でピボットテーブルとピボットキャッシュを更新](/cells/ja/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}