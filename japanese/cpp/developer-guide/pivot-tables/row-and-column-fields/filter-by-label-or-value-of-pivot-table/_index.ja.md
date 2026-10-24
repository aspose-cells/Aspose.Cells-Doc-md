---
title: ラベルまたは値によるピボットテーブルのフィルター処理
linktitle: ラベルまたは値によるピボットテーブルのフィルター処理
description: Aspose.Cells for C++ は、包括的なピボットテーブルのフィルター処理機能をサポートします。この記事では、ラベルフィルター、日付フィルター、値フィルター、上位 10 フィルター、およびピボット項目の非表示または表示を使って、ピボットテーブルのデータをフィルターする方法を説明します。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, ピボットテーブル, フィルター, ラベルフィルター, 値フィルター, 日付フィルター, 上位 10 フィルター, ピボット項目, ピボット項目の非表示
type: docs
weight: 10
url: /ja/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルターするための実用的な戦略を 5 つ提供します。テキストベースの行または列フィールドにはラベルフィルターを、日時セルまたは空白のみを含むフィールドには日付フィルターを、集約された数値には値フィルターを、値フィールドに基づいて順位付けする場合には上位 10 フィルターを適用できます。また、`IsHidden` プロパティを使用して、個々のピボット項目を手動で非表示または表示することもできます。各戦略は、`PivotField` および `PivotItem` クラスの専用 API を通じて利用できます。
{{% /alert %}}

## **はじめに**
ピボットテーブルは強力な分析ツールですが、集計結果には、レポートに掲載する情報よりずっと多くの情報が含まれることがよくあります。フィルター処理は、特定のレポートで重要な行、列、または値にピボットテーブルを絞り込む主要な手段です。Aspose.Cells for C++ は、Microsoft Excel で利用できるフィルター機能を再現し、プログラムから利用できるようにすることで、レポート生成を完全に自動化できます。
次のフィルター処理戦略について説明します。
1. **ラベルフィルター** — テキストラベルに基づいて、行または列フィールドの項目をフィルターします。
2. **日付フィルター** — 日時値または空白のみを含む行または列フィールドをフィルターします。
3. **値フィルター** — データフィールドの集計値に基づいて項目をフィルターします。
4. **上位 10 フィルター** — 値フィールドに基づいて順位付けされた上位または下位 N 項目のみを表示します。
5. **ピボット項目の非表示 / 表示** — フィールド内の個々の項目の表示を手動で制御します。
各アプローチでは、`PivotField` クラスの異なるメソッド、または `PivotItem` クラスのプロパティを使用します。フィルターを適用した後、新しいフィルター状態がキャッシュされたデータと計算済み値に反映されるように、ピボットテーブルの `RefreshData()` と `CalculateData()` を呼び出す必要があります。

## **ラベルフィルター**
ラベルフィルターは、行または列フィールドの項目のテキストキャプションをパターンと比較することで、該当する項目をフィルターできます。これは、製品名が特定の文字で始まる製品、特定の語を含む製品、またはキャプションに基づくその他の条件に一致する製品だけを表示したい場合に便利です。
Aspose.Cells は、`PivotField.FilterByLabel(PivotFilterType, const char16_t*)` メソッドを通じてラベルフィルター機能を提供します。`PivotFilterType` 列挙体には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2 番目の引数には、比較に使用するラベル文字列を指定します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、指定したプレフィックスでキャプションが始まる項目だけが残るようにラベルフィルターを適用し、ピボットテーブルを更新して結果を保存します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // ピボットテーブルを含む既存のブックを読み込む
    Workbook wb(fileName);
    // インデックスでワークシートにアクセスする（最初のワークシート）
    Worksheet ws = wb.GetWorksheets().Get(0);
    // インデックスでピボットテーブルにアクセスする
    PivotTable pt = ws.GetPivotTables().Get(0);
    // 最初の行の PivotField を取得する
    PivotField rowField = pt.GetRowFields().Get(0);
    // ラベルフィルターを適用する — 指定したプレフィックスで始まる行項目だけを表示する
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // フィルターを反映するため、ピボットテーブルのデータを更新して再計算する
    pt.RefreshData();
    // ブックをディスクに保存する
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **日付フィルター**
日付フィルターでは、今日、先週、今月、来四半期、または特定の日付範囲など、日付を基準とした条件によってピボットテーブルを絞り込めます。これらは、日時情報を格納するフィールドにのみ作用する特殊なフィルターです。

{{% alert color="primary" %}}
日付フィルターは、行または列領域に日時セルまたは空白値のみが含まれる場合にのみ機能します。基となるフィールドに数値やテキストなど他のデータ型が含まれている場合、日付フィルターは期待どおりの結果を得られません。このフィルターを適用する前に、フィールドが日付として書式設定され、すべての値が有効な `DateTime` インスタンスまたは空のセルであることを確認してください。
Aspose.Cells は、`PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)` メソッドを通じて日付フィルター機能を提供します。`PivotFilterType` 列挙体には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの専用値が含まれます。選択したフィルターの種類に応じて、`DateTime` 値を 1 つまたは 2 つ指定します（`Between` の場合は開始日と終了日を指定します）。
次の例では、行領域に日付フィールドを持つピボットテーブルのあるワークブックを読み込み、表示可能な項目を特定の日付範囲に制限する日付フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
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
        // ソースワークブックが見つかりません。
        Aspose::Cells::Cleanup();
        return -1;
    }
    // ピボットテーブルを含む既存のワークブックを読み込みます
    Workbook workbook(U16String(inputPath.c_str()));
    // インデックスでピボットテーブルを保持するワークシートにアクセスします
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // インデックスでピボットテーブルにアクセスします
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // 行領域から日付 PivotField を取得します
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // Between フィルターの日付条件を定義します
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // ピボットフィールドに日付フィルターを適用します
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // フィルターを反映するため、ピボットテーブルを更新して再計算します
    // ワークブックを保存します
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **値フィルター**
値フィルターは、ピボットテーブルのデータ領域で計算される集計値に作用します。テキストラベルを照合するのではなく、数値の合計をしきい値と比較します。代表的な使用例として、売上合計が目標金額を超える製品だけを表示する、取引件数が特定の範囲に収まる地域だけを表示する、といった操作があります。
Aspose.Cells は、`PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)` メソッドを通じて値フィルター機能を提供します。`filterType` パラメーターには、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を指定します。`valueField` パラメーターは評価するデータフィールドを指定し、最後の引数にはしきい値を指定します。
次の例では、ピボットテーブルのあるワークブックを読み込み、集計された売上が数値のしきい値を超える項目だけを残す値フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。

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
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **上位 10 フィルター**
上位 10 フィルターは値フィルターの一種であり、選択した値フィールドに基づいて、上位または下位 N 項目だけを残します。「売上収益による上位 10 製品」や「売上件数による下位 5 地域」などの順位レポートで広く使用されます。

{{% alert color="primary" %}}
上位 10 フィルターは、データ領域に 1 つ以上の値ピボットフィールドがある場合にのみ有効です。値フィールドが 1 つもない場合、項目を順位付けするために使用できる集計済みの指標が存在せず、このフィルターは適用できません。
Aspose.Cells は、`PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` メソッドを通じて上位 10 フィルター機能を提供します。`itemCount` パラメーターは残す項目数を指定し、`isTop` は上位項目（true）を残すか、下位項目（false）を残すかを指定します。`valueField` は順位付けに使用するデータフィールドを参照し、`filterType` は値の計算方法を制御します（通常は `Sum` ですが、`Count` と `Percent` も使用できます）。
次の例では、値フィールドを含むピボットテーブルのあるワークブックを読み込み、売上合計による上位 10 項目だけを残す上位 10 フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
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
    rowField.FilterTop10(10, PivotFilterType::Sum, true, valueFieldIndex);
    workbook.Save(outputPath);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **ピボット項目の非表示または表示によるフィルター**
構造化されたフィルター API に加えて、Aspose.Cells では個々のピボット項目の表示を直接制御できます。`PivotField` の `PivotItems` コレクションを反復し、`IsHidden` プロパティを切り替えることで、数式ベースのフィルターを適用せずに特定の項目だけを非表示にできます。`IsHidden = true` に設定すると、その項目がピボットテーブルから非表示になります。`IsHidden = false` に設定すると、非表示が解除され、項目が再び表示されます。
この方法は、フィルター条件が一定でない場合や項目ごとに異なる場合（特定のレポートに表示したくない名前付きのカテゴリーを少数だけ非表示にする場合など）に便利です。次の例では、ピボットテーブルを読み込み、名前で指定した項目を非表示にし、その項目を表示する方法を示したうえで、ピボットテーブルを更新してワークブックを保存します。

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // ピボットテーブルを含む既存のワークブックを読み込む
    Workbook workbook(u"pivot_table_sample.xlsx");
    // ピボットテーブルを含む最初のワークシートにアクセスする
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // インデックスでピボットテーブルにアクセスする（シート上の最初のピボットテーブル）
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // 対象のPivotFieldを取得する（項目を非表示／表示する最初の行ラベルフィールド）
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // 選択したPivotFieldのPivotItemsコレクションを反復処理する
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // 特定の名前／条件に一致するピボット項目を非表示にする
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // 表示のデモ：以前非表示にしたピボット項目を再表示する
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // 変更を反映するため、ピボットテーブルを更新して再計算する
    pivotTable.CalculateData();
    // ワークブックを保存する――非表示の項目は元のデータには残るが、
    // 表示されるピボットテーブルの出力からは除外される
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **概要**
Aspose.Cells for C++ は、Microsoft Excel にあるものと同等の完全なピボットテーブルのフィルター機能を提供します。ラベル、日付、値のフィルターは最も一般的な分析シナリオに対応し、上位 10 フィルターは順位レポートを処理します。フィルター条件が一定でない場合は、`PivotItem.IsHidden` プロパティが柔軟な項目単位の代替手段となります。これらの戦略を組み合わせる（たとえば、ラベルフィルターを適用してから特定の項目を非表示にする）ことで、コードだけで正確に絞り込んだピボットテーブルのレポートを作成できます。

## 関連記事
- [ピボットテーブルの作成](/cells/ja/cpp/create-pivot-table/)
- [Aspose.Cells for C++ でピボットテーブルに行と列フィールドを追加](/cells/ja/cpp/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for C++ でピボットテーブルにフィルターフィールドを追加](/cells/ja/cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for C++ でピボットテーブルの値フィールドを管理](/cells/ja/cpp/manage-value-fields/)
- [Aspose.Cells for C++ でピボットテーブルと PivotCache を更新](/cells/ja/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}