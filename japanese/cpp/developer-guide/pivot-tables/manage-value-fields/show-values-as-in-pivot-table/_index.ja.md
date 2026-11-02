---
title: Aspose.Cells for C++ のピボットテーブルで「値の表示形式」
linktitle: Aspose.Cells for C++ のピボットテーブルで「値の表示形式」
description: Aspose.Cells for C++ を使用して、ピボットテーブルのデータフィールド値を合計に対するパーセンテージ、ベース項目との差分、累積合計、ランクなどとして表示できます。
keywords: Aspose.Cells, C++, ピボットテーブル, 値の表示形式, データ表示形式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /ja/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
ピボットテーブルは通常、`Sum` や `Count` といった集計関数で各データフィールドを集計します。Excel の **Show Values As** 機能は、集計結果を二次計算で置き換え、たとえば全体合計に対する割合、累積合計、基準項目との差分、ランクなどを表示できるようにします。これにより、補助数式や計算列を使用せずに比較分析が可能になります。  
典型的な使用例としては、行・列・全体合計に対するパーセンテージによる全体シェア分析、期間フィールドでの累積レポート、ベース項目との差分またはパーセンテージ差によるベンチマーク分析、最小から最大（または逆）へのランク付けなどがあります。  
Aspose.Cells for C++ では、`PivotFieldDataDisplayFormat` が二次計算を選択します。`PivotField.GetShowValuesSetting()` アクセサは `PivotShowValuesSetting` オブジェクトを返し、`SetCalculationType`、`SetBaseFieldIndex`、`SetBaseItemPositionType`、`SetBaseItemIndex` メソッドで動作を構成します。便利メソッド `PivotField.ShowValuesAs(...)` は同じ 4 つの設定を一度に適用します。これらの設定は `PivotTable.GetDataFields()` で取得したデータ フィールドまたは値フィールドに適用します。

## **PivotFieldDataDisplayFormat 列挙体メンバー**
データフィールドは集計関数（Sum や Count など）を保持したまま、Show Values As によって表示方法のみが変換されます。  
直接 `PivotShowValuesSetting` の値を設定する方法（最終セクション参照）に加えて、1 回の呼び出しで同じ構成を適用できる便利メソッドがあります：

```cpp
void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int32_t baseField, PivotItemPositionType baseItemPositionType, int32_t baseItem);
```

| パラメータ | 意味 | 必要な場合 |
| --- | --- | --- |
| `displayFormat` | 適用する `PivotFieldDataDisplayFormat` の二次計算。 | 常に必須。 |
| `baseField` | ピボットテーブルのベースフィールドの 0 ベースインデックス（例: ベース項目が属する行フィールドのインデックス）。 | 以下の 6 つの基準関連フォーマット（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfRunningTotalIn`、`PercentageOfParentTotal`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItemPositionType` | 現在の項目に対するベース項目の選択方法: `PivotItemPositionType::Previous`、`::Next`、または `::Custom`。 | 3 つの基準項目フォーマット（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItem` | ベース項目の 0 ベースインデックス。 | `baseItemPositionType` が `Custom` のときにのみ使用（正確なベース項目を指定）。`Previous` / `Next` およびベース項目形式以外では無視され、`0` を渡してください。 |

| 計算タイプ | 動作 | ベース項目パラメータ |
| --- | --- | --- |
| `Normal` | 二次計算なし。集計値がそのまま表示されます（デフォルト）。 | — |
| `DifferenceFrom` | ベースフィールドのベース項目の値との差として表示します。 | `baseField` + `Previous`/`Next`/`Custom`（`Custom` のみ `baseItem`） |
| `PercentageOf` | ベースフィールドのベース項目の値に対するパーセンテージとして表示します。 | `baseField` + `Previous`/`Next`/`Custom`（`Custom` のみ `baseItem`） |
| `PercentageDifferenceFrom` | ベースフィールドのベース項目の値に対するパーセンテージ差として表示します。 | `baseField` + `Previous`/`Next`/`Custom`（`Custom` のみ `baseItem`） |
| `RunningTotalIn` | ベースフィールドの項目順に従って累積合計として表示します。 | `baseField`（累積対象のフィールド） |
| `PercentageOfRow` | 行合計に対するパーセンテージとして表示します。 | — |
| `PercentageOfColumn` | 列合計に対するパーセンテージとして表示します。 | — |
| `PercentageOfTotal` | 全体合計に対するパーセンテージとして表示します。 | — |
| `Index` | Excel のインデックス式 ((value * grand total) / (row total * column total)) に基づいて表示します。 | — |
| `PercentageOfParentRowTotal` | ネストされた行フィールドの場合、親行合計に対するパーセンテージとして表示します。 | — |
| `PercentageOfParentColumnTotal` | ネストされた列フィールドの場合、親列合計に対するパーセンテージとして表示します。 | — |
| `PercentageOfParentTotal` | 親合計に対するパーセンテージとして表示します。 | `baseField`（基準となる親フィールド） |
| `PercentageOfRunningTotalIn` | ベースフィールドの累積合計に対するパーセンテージとして表示します。 | `baseField`（累積対象のフィールド） |
| `RankSmallestToLargest` | 値を最小 (1) から最大へランク付けします。 | — |
| `RankLargestToSmallest` | 値を最大 (1) から最小へランク付けします。 | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` は `PivotShowValuesSetting` の 4 つの値（`CalculationType`、`BaseFieldIndex`、`BaseItemPositionType`、`BaseItemIndex`）を設定します。メソッドと設定オブジェクトは同一の状態を構成する 2 つの手段であり、Excel の Show Values As ダイアログのベースフィールドおよびベース項目選択と同様の動作を行います。
{{% /alert %}}

## **合計に対するパーセンテージで表示**
`PivotField.ShowValuesAs` メソッドに `PivotFieldDataDisplayFormat::PercentageOfTotal` を指定して呼び出すと、すべてのデータフィールドセル（合計行も含む）が全体合計に対するシェアとして変換されます。表示される数値は結果セット全体の比率として解釈されます。この形式は全体合計に対してのみ測定するため、ベースフィールドやベース項目は不要です。したがって、末尾の引数（`0`、`PivotItemPositionType::Previous`、`0`）はフォーマットが無視するプレースホルダーです。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load or create a workbook with source data
    Workbook workbook;
    Worksheet dataSheet = workbook.GetWorksheets().Get(0);
    Cells cells = dataSheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Fruit"));
    cells.Get(0, 1).PutValue(U16String("Amount"));
    const char* fruits[6] = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
    int32_t amounts[6] = { 10, 20, 30, 40, 50, 60 };
    for (int32_t i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(amounts[i]);
    }
    // Add a pivot table on a new worksheet
    int32_t pivotSheetIndex = workbook.GetWorksheets().Add();
    PivotTable pivotTable = workbook.GetWorksheets().Get(pivotSheetIndex).GetPivotTables().Add(u"=Sheet1!A1:B7", 2, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Show the Amount data field as a percentage of the grand total with the
    // one-call method; PercentageOfTotal takes no base item, so the trailing
    // base arguments (0, Previous, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::PercentageOfTotal, 0, PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **PivotField.ShowValuesSetting の取得と構成**
`PivotField.GetShowValuesSetting()` で現在の設定を取得します。このアクセサはフィールドの `PivotShowValuesSetting` オブジェクトを返し、4 つの getter が現在適用されている Show Values As 計算を示します。設定を変更するには `PivotField.ShowValuesAs` メソッドを呼び出します。これにより 4 つの設定が一度に書き込まれるため、個別に値を割り当てる必要がなくなります。  
`PivotShowValuesSetting` オブジェクトが公開する 4 つの値は次のとおりです：
- `GetCalculationType()` / `SetCalculationType()` で `PivotFieldDataDisplayFormat` の二次計算を選択します。  
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` でベースフィールドの 0 ベースインデックスを指定します。基準関連フォーマットで使用されます。  
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` でベース項目の位置タイプ（`PivotItemPositionType::Next`、`PivotItemPositionType::Previous`、`PivotItemPositionType::Custom`）を決定します。  
- `GetBaseItemIndex()` / `SetBaseItemIndex()` で 0 ベースのベース項目インデックスを指定し、位置タイプが `Custom` の場合に使用されます。  
`ShowValuesAs` を呼び出した後、`PivotTable.CalculateData()` を再度実行してピボット本体を再計算および再描画し、設定変更を反映させてください。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"ShowValuesAsPercentageOfTotal.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(1).GetPivotTables().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    // Read the current show-values settings
    PivotShowValuesSetting settings = dataField.GetShowValuesSetting();
    std::cout << "CalculationType: " << static_cast<int32_t>(settings.GetCalculationType()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemPositionType: " << static_cast<int32_t>(settings.GetBaseItemPositionType()) << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "CalculationType now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetCalculationType()) << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **関連記事**
- [ピボットテーブルでの値フィールドの管理](/cells/ja/cpp/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/cpp/refresh-pivot-table/)
- [ピボットテーブルへのスタイルの適用](/cells/ja/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}