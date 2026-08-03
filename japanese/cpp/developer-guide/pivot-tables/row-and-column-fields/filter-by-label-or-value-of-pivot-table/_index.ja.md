---
title: ラベルまたは値によるピボットテーブルのフィルター処理
linktitle: ラベルまたは値によるピボットテーブルのフィルター処理
description: Aspose.Cells for C++ は包括的なピボットテーブルのフィルター機能をサポートしています。この記事では、ラベルフィルター、日付フィルター、値フィルター、上位10フィルター、およびピボットアイテムの表示/非表示によるピボットテーブルデータのフィルター処理方法について説明します。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, ピボットテーブル, フィルター, ラベルフィルター, 値フィルター, 日付フィルター, 上位10フィルター, ピボットアイテム, ピボットアイテムの非表示
type: docs
weight: 10
url: /ja/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルター処理するための 5 つの実用的な方法を提供します。テキストベースの行または列フィールドにラベルフィルターを適用したり、フィールドに日付時刻セルまたは空白のみが含まれる場合に日付フィルターを使用したり、集計された数値に対して値フィルターを適用したり、値フィールドによってランク付けする上位 10 フィルターを使用したり、`IsHidden` プロパティを使用して個々のピボットアイテムを手動で非表示/表示したりすることができます。各方法は `PivotField` クラスと `PivotItem` クラスの専用 API を通じて公開されています。
{{% /alert %}}
## **はじめに**
ピボットテーブルは強力な分析ツールですが、生の集計結果には、特定のレポートで必要とするよりもはるかに多くの情報が含まれていることがよくあります。フィルター処理は、ピボットテーブルを特定のレポートに必要な行、列、値だけに絞り込むための主要な仕組みです。Aspose.Cells for C++ は Microsoft Excel で利用可能なフィルター機能を反映し、レポート生成を完全に自動化できるようにプログラミング的に公開しています。
この記事で扱うフィルター戦略は次のとおりです。
1. **ラベルフィルター** — 行または列フィールドのアイテムをテキストラベルに基づいてフィルター処理します。
2. **日付フィルター** — 日付時刻値（または空白）のみを含む行または列フィールドをフィルター処理します。
3. **値フィルター** — データフィールドの集計値に基づいてアイテムをフィルター処理します。
4. **上位 10 フィルター** — 値フィールドによってランク付けされた上位または下位 N 個のアイテムのみを表示します。
5. **ピボットアイテムの表示/非表示** — フィールド内の各アイテムの表示を手動で制御します。
各アプローチは、`PivotField` クラスの異なるメソッド、または `PivotItem` クラスのプロパティを使用します。フィルターを適用した後、ピボットテーブルのキャッシュデータと計算値が新しいフィルター状態を反映するように、`RefreshData()` と `CalculateData()` をピボットテーブルで呼び出す必要があります。
## **ラベルフィルター**
ラベルフィルターを使用すると、行または列フィールドのアイテムを、テキストキャプションとパターンを比較することによってフィルター処理できます。これは、特定の文字で始まる名前、特定の単語を含む名前、またはその他のキャプションベースの基準に一致する製品のみを表示したい場合に便利です。
Aspose.Cells は、ラベルフィルターを `PivotField.FilterByLabel(PivotFilterType, const char16_t*)` メソッドを通じて公開しています。`PivotFilterType` 列挙体には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2 番目の引数は、比較に使用されるラベル文字列を提供します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、指定された接頭辞で始まるキャプションを持つアイテムのみが表示されるようにラベルフィルターを適用し、ピボットテーブルを更新して結果を保存します。
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

    // 最初の行のPivotFieldを取得する
    PivotField rowField = pt.GetRowFields().Get(0);

    // ラベルフィルターを適用する — 指定された接頭辞で始まるラベルの行項目のみを表示する
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));

    // フィルターが有効になるようにピボットテーブルのデータを更新して再計算する
    pt.RefreshData();

    // ワークブックをディスクに保存する
    wb.Save(fileName);

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **日付フィルター**
日付フィルターを使用すると、今日、先週、今月、次四半期、特定の日付範囲などの日付ベースの基準によってピボットテーブルを絞り込むことができます。これらは、日付時刻情報を格納するフィールドに対してのみ機能する特殊なフィルターです。
{{% alert color="primary" %}}
日付フィルターは、行または列領域に日付時刻セルまたは空白値のみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルターは期待される結果を生成しません。このフィルターを適用する前に、フィールドが日付として書式設定されており、すべての値が有効な `DateTime` インスタンスまたは空のセルであることを確認してください。
{{% /alert %}}
Aspose.Cells は、日付フィルターを `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)` メソッドを通じて公開しています。`PivotFilterType` 列挙体には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの専用の日付値が含まれます。選択したフィルタータイプに応じて、1 つまたは 2 つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行領域に日付フィールドを含むピボットテーブルを含むワークブックを読み込み、特定の日付範囲に可視アイテムを制限する日付フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
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

    // ピボットテーブルを含むワークシートにアクセスする(インデックス指定)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // インデックスでピボットテーブルにアクセスする
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // 行エリアから日付のPivotFieldを取得する
    PivotField dateField = pivotTable.GetRowFields().Get(0);

    // Betweenフィルターの日付基準を定義する
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};

    // ピボットフィールドに日付フィルターを適用する
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);

    // フィルターを反映させるためにピボットテーブルを更新して再計算する
    pivotTable.RefreshData();

    // ワークブックを保存する
    workbook.Save(U16String(outputPath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **値フィルター**
値フィルターは、ピボットテーブルがデータ領域で計算する集計値に対して機能します。テキストラベルを一致させる代わりに、数値の合計をしきい値と比較します。典型的な使用例には、売上合計が目標額を超える製品のみを表示する、または取引回数が範囲内の地域のみを表示するといったものがあります。
Aspose.Cells は、値フィルターを `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)` メソッドを通じて公開しています。`filterType` パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を使用します。`valueField` パラメータは評価するデータフィールドを指定し、最後の引数はしきい値を提供します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集計された売上が数値のしきい値を超えるアイテムのみを保持する値フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
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

    pivotTable.RefreshData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **上位 10 フィルター**
上位 10 フィルターは、選択した値フィールドに基づいて、最高または最低の N 個のアイテムのみを保持する値フィルターの特殊な形式です。「収益による上位 10 製品」や「販売数による下位 5 地域」などのランキングレポートで一般的に使用されます。
{{% alert color="primary" %}}
上位 10 フィルターは、ピボットテーブルのデータ領域に 1 つ以上の値ピボットフィールドがある場合にのみ有効です。少なくとも 1 つの値フィールドがないと、アイテムをランク付けするための集計尺度がなく、フィルターを適用できません。
{{% /alert %}}
Aspose.Cells は、上位 10 フィルターを `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` メソッドを通じて公開しています。`itemCount` パラメータは保持するアイテムの数を定義し、`isTop` は上位のアイテムを保持するかどうか（true）または下位のアイテムを保持するかどうか（false）を示し、`valueField` はランキングに使用されるデータフィールドを参照し、`filterType` は値の計算方法を制御します（通常は `Sum` ですが、`Count` や `Percent` も使用できます）。
次の例では、値フィールドを含むピボットテーブルを含むワークブックを読み込み、売上合計による上位 10 個のアイテムのみを保持する上位 10 フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
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

    pivotTable.RefreshData();

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **ピボットアイテムの表示/非表示によるフィルター処理**
構造化フィルター API に加えて、Aspose.Cells では各ピボットアイテムの表示を直接制御することもできます。`PivotField` の `PivotItems` コレクションを反復処理し、`IsHidden` プロパティを切り替えることで、数式ベースのフィルターを適用せずに特定のアイテムを選択的に除外できます。`IsHidden = true` を設定すると、ピボットテーブルからアイテムが非表示になります。`IsHidden = false` を設定すると、アイテムの非表示が解除され、再び表示されます。
このアプローチは、フィルター規則が不規則である場合やアイテム固有である場合（特定のレポートに表示すべきでない少数の名前付きカテゴリを非表示にするなど）に役立ちます。以下の例では、ピボットテーブルを読み込み、名前で特定のアイテムを非表示にし、非表示を解除する方法を実演し、ピボットテーブルを更新してワークブックを保存します。
```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // ピボットテーブルを含む既存のワークブックを読み込みます
    Workbook workbook(u"pivot_table_sample.xlsx");

    // ピボットテーブルを含む最初のワークシートにアクセスします
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // インデックスでピボットテーブルにアクセスします（シート上の最初のピボットテーブル）
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);

    // 対象のPivotFieldを取得します（アイテムの非表示/表示を切り替える最初の行ラベルフィールド）
    PivotField pivotField = pivotTable.GetRowFields().Get(0);

    // 選択したPivotFieldのPivotItemsコレクションを反復処理します
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);

        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();

        // 特定の名前/条件に一致するピボットアイテムを非表示にします
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }

        // 非表示解除のデモ：以前非表示にしたピボットアイテムを再度表示します
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }

    // 変更を有効にするためにピボットテーブルを更新して再計算します
    pivotTable.CalculateData();

    // ワークブックを保存します — 非表示アイテムは基になるデータに残ります
    // が、表示されるピボットテーブルの出力からは除外されます
    workbook.Save(u"output_pivot_filtered.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **まとめ**
Aspose.Cells for C++ は、Microsoft Excel で利用できるものに匹敵する完全なピボットテーブルのフィルター機能を提供します。ラベルフィルター、日付フィルター、値フィルターは最も一般的な分析シナリオをカバーし、上位 10 フィルターはランキングレポートを処理します。フィルター規則が不規則な場合は、`PivotItem.IsHidden` プロパティが柔軟でアイテムレベルの代替手段を提供します。これらの戦略を組み合わせる（たとえば、ラベルフィルターを適用してから特定のアイテムを非表示にする）ことで、完全にコードから正確にターゲットを絞ったピボットテーブルレポートを作成できます。
## 関連記事
- [ピボットテーブルの挿入](/cells/ja/cpp/pivot-tables/)
- [Aspose.Cells for C++ でピボットテーブルの行と列のフィールドを追加](/cells/ja/cpp/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for C++ でピボットテーブルにページフィールドを追加](/cells/ja/cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for C++ でピボットテーブルの値フィールドを管理](/cells/ja/cpp/manage-value-fields/)
- [Aspose.Cells for C++ でピボットテーブルとピボットキャッシュを更新](/cells/ja/cpp/refresh-pivot-table/)
{{< app/cells/assistant language="cpp" >}}