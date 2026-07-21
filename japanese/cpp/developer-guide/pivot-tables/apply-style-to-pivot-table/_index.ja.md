---
title: ピボットテーブルへのスタイルの適用
linktitle: ピボットテーブルへのスタイルの適用
description: Aspose.Cells for C++ におけるピボットテーブルへの組み込みスタイルおよびカスタムスタイルの適用方法について、レガシー XLS のオートフォーマット、Excel 2007 以降の名前付きスタイル、カスタムピボットテーブルスタイル、FormatAll ショートカットまでを学びます。
keywords: Aspose.Cells, C++, ピボットテーブル, スタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタムスタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/cpp/apply-style-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、レガシーピボットオートフォーマット (`.xls` ファイル向け) と、モダンな名前付きまたはカスタムピボットテーブルスタイル (`.xlsx`、`.xlsm`、`.xlsb` ファイル向け) の両方の適用をサポートしています。呼び出すべき API は、ワークブックを読み込んだ形式ではなく、ワークブックを保存するファイル形式によって決まります。

{{% /alert %}}

## **はじめに**

Aspose.Cells は、ピボットテーブル向けに 2 つの並列なスタイル API を提供します。どちらを選択するかは、読み込んだ形式ではなく、ワークブックを保存するファイル形式によって決まります。`.xls` ファイルから読み込んだワークブックを `.xlsx` として再保存する場合、レガシー API ではなくモダンのスタイル API が適用されます。

レガシー `.xls` 出力の場合は、`PivotTable.AutoFormatType` プロパティを `Aspose.Cells.Pivot.PivotTableAutoFormatType` 列挙型と一緒に使用します。この API は、従来の Excel がピボットテーブルに対して提供していたオートフォーマットピッカーに対応します。

モダンの `.xlsx`、`.xlsm`、`.xlsb` 出力の場合は、2 種類のスタイル API が利用可能です。

- `PivotTable.PivotTableStyleType` は組み込みの名前付きスタイル (明暗テーマ、Excel 2017 で追加されたスタイルを含む) のいずれかを選択します。これらのプリセットは読み取り専用です。
- `PivotTable.PivotTableStyleName` は、`Worksheets.TableStyles.AddPivotTableStyle(...)` を通じて自分で定義したカスタムスタイルを選択します。プリセットで提供される範囲を超えて色、罫線、フォントを変更したい場合は、カスタムスタイルが必要です。

さらに、`PivotTable.FormatAll(Style)` は、単一の `Style` オブジェクトをピボットのすべてのセルに適用するショートカットで、上記のいずれかのスタイル名 API で設定された内容を上書きします。これは、基になるテーマに関係なく統一的な外観が必要な場合に役立ちます。

## **レガシー XLS プリセットオートフォーマットの適用**

`PivotTable.AutoFormatType` は、`Aspose.Cells.Pivot.PivotTableAutoFormatType` 列挙型の値を受け取ります。利用可能な値は、`Report1` から `Report10`、`Classic`、および `Table1` から `Table10` です。

{{% alert color="primary" %}}

`AutoFormatType` が有効になるのは、ワークブックが `.xls` として保存される場合のみです。同じワークブックが `.xlsx`、`.xlsm`、または `.xlsb` として保存される場合、Excel はこのプロパティを無視し、`PivotTableStyleType` および `PivotTableStyleName` の設定にフォールバックします。

{{% /alert %}}

次の例では、新しいワークブックを読み込み、Fruit/Year/Amount のサンプルデータを入力し、ピボットテーブルを追加し、`PivotTableAutoFormatType.Report5` を適用して、結果を `.xls` として保存します。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // 新しいワークブックを作成する
    Workbook workbook;

    // 最初のワークシートを取得する
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // ヘッダー行（Fruit、Year、Amount）と、
    // 2020年と2021年にわたる grape、blueberry、kiwi、cherry の9行のデータでソースデータを入力する
    sheet.GetCells().Get(0, 0).PutValue(u"Fruit");
    sheet.GetCells().Get(0, 1).PutValue(u"Year");
    sheet.GetCells().Get(0, 2).PutValue(u"Amount");

    sheet.GetCells().Get(1, 0).PutValue(u"grape");
    sheet.GetCells().Get(1, 1).PutValue(2020);
    sheet.GetCells().Get(1, 2).PutValue(50);

    sheet.GetCells().Get(2, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(2, 1).PutValue(2020);
    sheet.GetCells().Get(2, 2).PutValue(30);

    sheet.GetCells().Get(3, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(3, 1).PutValue(2020);
    sheet.GetCells().Get(3, 2).PutValue(25);

    sheet.GetCells().Get(4, 0).PutValue(u"cherry");
    sheet.GetCells().Get(4, 1).PutValue(2020);
    sheet.GetCells().Get(4, 2).PutValue(40);

    sheet.GetCells().Get(5, 0).PutValue(u"grape");
    sheet.GetCells().Get(5, 1).PutValue(2021);
    sheet.GetCells().Get(5, 2).PutValue(60);

    sheet.GetCells().Get(6, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(6, 1).PutValue(2021);
    sheet.GetCells().Get(6, 2).PutValue(35);

    sheet.GetCells().Get(7, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(7, 1).PutValue(2021);
    sheet.GetCells().Get(7, 2).PutValue(28);

    sheet.GetCells().Get(8, 0).PutValue(u"cherry");
    sheet.GetCells().Get(8, 1).PutValue(2021);
    sheet.GetCells().Get(8, 2).PutValue(45);

    sheet.GetCells().Get(9, 0).PutValue(u"grape");
    sheet.GetCells().Get(9, 1).PutValue(2020);
    sheet.GetCells().Get(9, 2).PutValue(45);

    // 出力先セル E3 に、"Pivot1" という名前のピボットテーブルをソース範囲 A1:C10 を使用して追加する
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    // フィールドを割り当てる：Fruit -> 行、Year -> 列、Amount -> データ
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // レガシー XLS のプリセット自動フォーマット「Report5」を適用する
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);

    // ワークブックをレガシー .xls 形式で保存する
    workbook.Save(u"output.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **モダンな名前付きプリセットピボットテーブルスタイルの適用**

`PivotTable.PivotTableStyleType` は、`Aspose.Cells.PivotTableStyleType` 列挙型の値を受け取ります。この列挙型は、明テーマ `PivotTableStyleLight1` から `PivotTableStyleLight28` までと、暗テーマ `PivotTableStyleDark1` から `PivotTableStyleDark28` までをカバーしています。Excel 2017 で追加されたスタイル (第 2 波の明暗テーマ) も同じ列挙型からアクセスできます。

これは、モダンなファイル形式に対して推奨される API です。レガシーオートフォーマットとは異なり、ここで選択したスタイルは Excel で忠実にレンダリングされ、他の Office ツールを介したラウンドトリップでも保持されます。

次の例では、同じ Fruit/Year/Amount データを使用し、同じピボットテーブルを作成し、`PivotTableStyleDark1` を適用して、ワークブックを `.xlsx` として保存します。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(150);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(200);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(180);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(120);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(170);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(210);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(190);

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(130);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **カスタムピボットテーブルスタイルの定義と適用**

組み込みプリセットは変更できません。色、罫線、またはフォントを上書きする必要がある場合は、必ずカスタムピボットスタイルを定義する必要があります。ワークフローは次の 3 つのステップで構成されます。

1. `Worksheets.TableStyles.AddPivotTableStyle(string name)` を通じて、ワークブックの `TableStyles` コレクションにカスタムスタイルを追加します。これにより、新しく作成されたスタイルのインデックスが返されます。
2. `TableStyle.TableStyleElements.Add(TableStyleElementType)` を通じて要素 (`WholeTable` や `GrandTotalRow` など) を追加し、`TableStyleElement.SetElementStyle(Style)` を介して各要素に `Style` を割り当てることによって、スタイルを構成します。
3. カスタムスタイルをピボットに適用するには、`PivotTable.PivotTableStyleName` をスタイルの名前に設定します。このプロパティは組み込みプリセットを選択するものであるため、ここでは `PivotTableStyleType` を使用しないでください。

{{% alert color="primary" %}}

`PivotTableStyleName` と `PivotTableStyleType` は互換性がありません。組み込みプリセットには `PivotTableStyleType` を、`AddPivotTableStyle` を通じて定義したカスタムスタイルには `PivotTableStyleName` を使用してください。両方を設定しても問題ありませんが、レンダリングされるのは目的のソースに一致する方のみです。

{{% /alert %}}

利用可能な `TableStyleElementType` の値には、`WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels`、および `PageFieldValues` があります。

次の例では、`WholeTable` に細い黒色の罫線を持ち、`GrandTotalRow` に太字の赤色フォントを持つカスタムピボットスタイルを定義し、それを `PivotTableStyleName` を介して適用して、`.xlsx` として保存します。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    // ソースデータを入力: ヘッダー行 + 9データ行 (A1:C10)
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    // A1:C10をソースとするピボットテーブルを追加、E3に配置、"Pivot1"という名前
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // ステップ1: 新しいカスタムピボットテーブルスタイルを登録し、インデックスを取得
    int styleIndex = workbook.GetWorksheets().GetTableStyles().AddPivotTableStyle(u"CustomPivotStyle");
    TableStyle tableStyle = workbook.GetWorksheets().GetTableStyles().Get(styleIndex);

    // ステップ2: WholeTable要素を追加し、4辺すべてに細い黒い罫線を適用
    int wholeTableElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::WholeTable);
    TableStyleElement wholeTableElement = tableStyle.GetTableStyleElements().Get(wholeTableElementIndex);
    Style wholeTableStyle = workbook.CreateStyle();
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    wholeTableElement.SetElementStyle(wholeTableStyle);

    // ステップ3: GrandTotalRow要素を追加し、太字の赤いフォントを適用
    int grandTotalElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::GrandTotalRow);
    TableStyleElement grandTotalElement = tableStyle.GetTableStyleElements().Get(grandTotalElementIndex);
    Style grandTotalStyle = workbook.CreateStyle();
    grandTotalStyle.GetFont().SetIsBold(true);
    grandTotalStyle.GetFont().SetColor(Color::Red());
    grandTotalElement.SetElementStyle(grandTotalStyle);

    // ステップ4: 名前でカスタムスタイルを適用（組み込みプリセット用のPivotTableStyleTypeではなく）
    pivotTable.SetPivotTableStyleName(u"CustomPivotStyle");

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **FormatAll を使用してすべてのピボットセルに 1 つのスタイルを適用**

`PivotTable.FormatAll(Style)` は、データ領域、行ヘッダーと列ヘッダー、合計を含む、ピボットテーブルのすべてのセルに単一の `Style` オブジェクトを適用するショートカットです。以前に `PivotTableStyleType` または `PivotTableStyleName` を介して設定された内容はすべて上書きされます。

{{% alert color="primary" %}}

`FormatAll` は `PivotTableStyleType` と `PivotTableStyleName` の両方を上書きします。ピボット全体でテーマ非依存の統一された外観が必要な場合にのみ使用してください。

{{% /alert %}}

次の例では、黄色の単色塗りつぶし、太字の濃紺フォント、およびすべての辺に細い黒色の罫線を持つ `Style` を作成し、それを `FormatAll` で適用して、`.xlsx` として保存します。

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // ヘッダー行
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // データ行
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(5000);

    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(3000);

    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(4000);

    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(2000);

    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(6000);

    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(3500);

    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(4500);

    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(2500);

    worksheet.GetCells().Get(u"A10").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B10").PutValue(2021);
    worksheet.GetCells().Get(u"C10").PutValue(5500);

    // ピボットテーブルを追加: ソース範囲 A1:C10、配置先セル E3、名前 "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // ピボットフィールドを割り当てる
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // ピボットテーブルのすべてのセルに強制適用するスタイルを作成
    Style style = wb.CreateStyle();
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);
    style.GetFont().SetIsBold(true);
    style.GetFont().SetColor(Color::DarkBlue());
    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());

    // FormatAll を適用
    pivotTable.FormatAll(style);

    // ワークブックを保存
    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **どのスタイル API を使用すべきか?**

スタイル API の選択は、保存先のファイル形式によって異なります。下の表をクイックリファレンスとしてご活用ください。

| 対象ファイル形式 | 使用する API | メモ |
|---|---|---|
| `.xls` (レガシー) | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` の値 (例: `Report1`–`Report10`、`Classic`、`Table1`–`Table10`)。モダン形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb` (モダン、組み込みスタイル) | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` の値 (Excel 2017 で追加されたものを含む明暗テーマ)。 |
| `.xlsx` / `.xlsm` / `.xlsb` (モダン、カスタムスタイル) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | 組み込みプリセットでは不十分な場合に使用します。`TableStyleElement.SetElementStyle(...)` を介して構成します。 |
| 任意の形式 (統一上書き) | `PivotTable.FormatAll(Style)` | ピボット全体の他のすべてのスタイル設定を上書きするショートカットです。 |

迷った場合は、`.xlsx` として保存し、組み込みテーマには `PivotTableStyleType` を、カスタムテーマには `PivotTableStyleName` を使用してください。

## **関連記事**

- [Aspose.Cells for C++ でのピボットテーブルの更新](/cells/ja/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}