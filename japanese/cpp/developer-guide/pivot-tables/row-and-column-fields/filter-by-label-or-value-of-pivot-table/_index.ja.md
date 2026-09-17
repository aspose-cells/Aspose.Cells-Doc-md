---
title: ラベルまたは値によるピボットテーブルのフィルター処理
linktitle: ラベルまたは値によるピボットテーブルのフィルター処理
description: Aspose.Cells for C++ は包括的なピボットテーブルのフィルター機能をサポートしています。この記事では、ラベルフィルター、日付フィルター、値フィルター、トップ10フィルター、およびピボットアイテムの隐藏/再表示を使用してピボットテーブルのデータをフィルターする方法を説明します。
keywords: Aspose.Cells, C++ library, spreadsheet, pivot table, filter, label filter, value filter, date filter, top 10 filter, pivot item, hide pivot item
type: docs
weight: 10
url: /ja/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルター処理するための 5 つの実用的な策略を提供します。テキストベースの行フィールドまたは列フィールドにラベルフィルターを適用したり、フィールドに日時セルまたは空白のみが含まれている場合に日付フィルターを使用したり、データフィールドの集計値に対して値フィルターを適用したり、値フィールドでランク付けするためにトップ10フィルターを使用したり、`IsHidden` プロパティを使用して個々のピボットアイテムを手動で非表示および再表示したりすることができます。各策略は `PivotField` クラスおよび `PivotItem` クラスの専用 API を介して公開されます。
{{% /alert %}}

## **Introduction**
ピボットテーブルは強力な分析ツールですが、生の概要には特定のレポートで必要とされるよりもはるかに多くの情報が含まれていることがよくあります。フィルター処理は、ピボットテーブルを特定のレポートにとって重要な行、列、または値に絞り込むための主要なメカニズムです。Aspose.Cells for C++ は Microsoft Excel で利用可能なフィルター機能をミラーリングし、プログラムで公開してレポート生成を完全に自動化できるようにします。
この記事で扱うフィルター戦略は次のとおりです。
1. **ラベルフィルター** — 行または列フィールドのアイテムをテキストラベルに基づいてフィルターします。
2. **日付フィルター** — 日時値（または空白）のみを含む行または列フィールドをフィルターします。
3. **値フィルター** — データフィールドの集計値に基づいてアイテムをフィルターします。
4. **トップ10フィルター** — 値フィールドでランク付けされた上位または下位 N 個のアイテムのみを表示します。
5. **ピボットアイテムの非表示/再表示** — フィールド内の各個別アイテムの表示を手動で制御します。
各アプローチは、`PivotField` クラスの異なるメソッドまたは `PivotItem` クラスのプロパティを使用します。フィルターを適用した後、キャッシュされたデータと計算値が新しいフィルター状態を反映するように、ピボットテーブルで `RefreshData()` と `CalculateData()` を呼び出す必要があります。

## **Label Filter**
ラベルフィルターを使用すると、行または列欄のアイテムを、テキストキャプションをパターンと比較することでフィルターできます。これは、特定の文字で始まる名前、特定の単語を含む名前、またはその他のキャプション基準に一致する製品のみを表示する場合に便利です。
Aspose.Cells は、`PivotField.FilterByLabel(PivotFilterType, const char16_t*)` メソッドを介してラベルフィルターを公開しています。`PivotFilterType` 列挙体には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2 番目の引数は、比較に使用されるラベル文字列を提供します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、キャプションが指定されたプレフィックスで始まるアイテムのみが表示されるようにするラベルフィルターを適用し、ピボットテーブルを更新して結果を保存します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // ピボットテーブルを含む既存のワークブックを読み込む
    Workbook wb(fileName);
    // インデックスでワークシートにアクセスする（最初のワークシート）
    Worksheet ws = wb.GetWorksheets().Get(0);
    // インデックスでピボットテーブルにアクセスする
    PivotTable pt = ws.GetPivotTables().Get(0);
    // 最初の行の PivotField を取得する
    PivotField rowField = pt.GetRowFields().Get(0);
    // ラベルフィルターを適用する — ラベルが指定されたプレフィックスで始まる行項目のみを表示する
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // フィルターを有効にするため、ピボットテーブルのデータを更新して再計算する
    pt.RefreshData();
    // ワークブックをディスクに保存する
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Date Filter**
日付フィルターを使用すると、今日、先週、今月、次の四半期、特定の期間などの日付ベースの基準でピボットテーブルを絞り込むことができます。これらは、日時情報を格納するフィールドに対してのみ機能する特殊なフィルターです。

{{% alert color="primary" %}}
日付フィルターは、行または列エリアに日時セルまたは空白値のみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルターは期待される結果を生成しません。このフィルターを適用する前に、フィールドが日付として書式設定されており、すべての値が有効な `DateTime` インスタンスまたは空のセルであることを確認してください。
{{% /alert %}}

Aspose.Cells は、`PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)` メソッドを介して日付フィルターを公開しています。`PivotFilterType` 列挙体には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの専用日付値が含まれます。選択したフィルタータイプに応じて、1 つまたは 2 つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行エリアに日付フィールドを含むピボットテーブルを含むワークブックを読み込み、表示されるアイテムを特定の日付範囲に制限する日付フィルターを適用し、ピボットテーブルを更新して、ワークブックを保存します。

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
    // ピボットテーブルを含む既存のワークブックを読み込む
    Workbook workbook(U16String(inputPath.c_str()));
    // ピボットテーブルを保持するワークシートにアクセスする（インデックスで）
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // インデックスでピボットテーブルにアクセスする
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // 行エリアから日付のPivotFieldを取得する
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // Betweenフィルターの日付条件を定義する
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // ピボットフィールドに日付フィルターを適用する
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // フィルターを反映させるため、ピボットテーブルを更新して再計算する
    // ワークブックを保存する
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Value Filter**
値フィルターは、ピボットテーブルがデータ領域で計算する集計値に対して機能します。テキストラベルを照合する代わりに、数値の合計をしきい値と比較します。一般的な使用例としては、売上合計が目標金額を超える製品のみを表示したり、取引回数が範囲内にある地域のみを表示したりすることが挙げられます。
Aspose.Cells は、`PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)` メソッドを介して値フィルターを公開しています。`filterType` パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を使用します。`valueField` パラメータは評価するデータフィールドを指定し、最後の引数はしきい値を提供します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集計された売上が数値のしきい値を超えるアイテムのみを保持する値フィルターを適用し、ピボットテーブルを更新して、ワークブックを保存します。

```cpp
#include "Aspose.Cells.h"
#include <cfloat>
using namespace Aspose::Cells;
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

## **Top 10 Filter**
トップ10フィルターは、選択された値フィールドに基づいて最高位または最低位の N 個のアイテムのみを保持する特殊な形式の値フィルターです。これは、「収益によるトップ10製品」や「販売数によるボトム5地域」などのランキングレポートによく使用されます。

{{% alert color="primary" %}}
トップ10フィルターは、ピボットテーブルのデータ領域に1つ以上の値ピボットフィールドがある場合にのみ有効です。値フィールドが少なくとも1つない場合、アイテムをランク付けするための集計メジャーが存在せず、フィルターを適用できません。
{{% /alert %}}

Aspose.Cells は、`PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` メソッドを介してトップ10フィルターを公開しています。`itemCount` パラメータは保持するアイテムの数を定義し、`isTop` は上位アイテム(true)を保持するか下位アイテム(false)を保持するかを示し、`valueField` はランク付けに使用されるデータフィールドを参照し、`filterType` は値の計算方法を制御します(通常は `Sum` ですが、`Count` や `Percent` もあります)。
次の例では、値フィールドを含むピボットテーブルを含むワークブックを読み込み、売上合計で上位10件のアイテムのみを保持するトップ10フィルターを適用し、ピボットテーブルを更新して、ワークブックを保存します。

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

## **Filter by Hiding or Unhiding Pivot Items**
構造化されたフィルターAPIに加えて、Aspose.Cells では各個別のピボットアイテムの表示を直接制御できます。`PivotField` の `PivotItems` コレクションを反復処理し、`IsHidden` プロパティを切り替えることで、数式ベースのフィルターを適用せずに特定のアイテムを選択的に非表示にできます。`IsHidden = true` を設定するとアイテムがピボットテーブルから非表示になります。`IsHidden = false` を設定するとアイテムの非表示が解除され、再び表示されるようになります。
このアプローチは、フィルター規則が不規則またはアイテム固有の場合に役立ちます。たとえば、特定のレポートに表示すべきではない少数の名前付きカテゴリを非表示にする場合などです。以下の例では、ピボットテーブルを読み込み、特定のアイテムを名前で非表示にし、非表示を解除する方法を実演し、ピボットテーブルを更新して、ワークブックを保存します。

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // ピボットテーブルを含む既存のワークブックを読み込む
    Workbook workbook(u"pivot_table_sample.xlsx");
    // ピボットテーブルを含む最初のワークシートにアクセスする
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // インデックスでピボットテーブルにアクセスする(シート上の最初のピボットテーブル)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // 対象のPivotFieldを取得する(アイテムの非表示/表示を切り替える最初の行ラベルフィールド)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // 選択したPivotFieldのPivotItemsコレクションを反復処理する
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // 特定の名前/条件に一致するピボットアイテムを非表示にする
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // 非表示解除のデモ: 以前に非表示にしたピボットアイテムを再表示する
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // 変更を有効にするためにピボットテーブルを更新して再計算する
    pivotTable.CalculateData();
    // ワークブックを保存する — 非表示アイテムは基になるデータには残るが
    // 表示されるピボットテーブルの出力からは除外される
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Summary**
Aspose.Cells for C++ は、Microsoft Excel にあるフィルター機能と一致する完全なピボットテーブルフィルター機能を提供します。ラベルフィルター、日付フィルター、値フィルターは最も一般的な分析シナリオをカバーし、トップ10フィルターはランキングレポートを処理します。フィルター規則が不規則な場合、`PivotItem.IsHidden` プロパティは柔軟なアイテムレベルの代替手段を提供します。これらの戦略を組み合わせる（たとえば、ラベルフィルターを適用してから特定のアイテムを非表示にする）ことで、コードから正確に対象を絞ったピボットテーブルレポートを完全に構築できます。

## Related Articles
- [Insert Pivot Table](/cells/ja/cpp/pivot-tables/)
- [Add Pivot Table Row and Column Fields in Aspose.Cells for C++](/cells/ja/cpp/pivot-table-add-row-and-column-fields/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for C++](/cells/ja/cpp/add-page-field-in-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for C++](/cells/ja/cpp/manage-value-fields/)
- [Refresh Pivot Tables and Pivot Caches in Aspose.Cells for C++](/cells/ja/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}