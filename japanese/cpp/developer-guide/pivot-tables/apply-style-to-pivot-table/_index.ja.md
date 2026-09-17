---
title: Aspose.Cells for C++ でピボットテーブルにスタイルを適用する
linktitle: Aspose.Cells for C++ でピボットテーブルにスタイルを適用する
description: Aspose.Cells for C++ でピボットテーブルに組み込みスタイルとカスタムスタイルを適用する方法を学びます。レガシー XLS オートフォーマット、Excel 2007 以降の新しい名前付きスタイル、カスタムピボットテーブルスタイル、FormatAll ショートカットについて説明します。
keywords: Aspose.Cells for C++, ピボットテーブル スタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタムスタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/cpp/apply-style-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells では、`.xls` ファイル向けのレガシーピボットオートフォーマットと、`.xlsx`、`.xlsm`、`.xlsb` ファイル向けの新しい名前付きまたはカスタムピボットテーブルスタイルを適用できます。使用する API は、ワークブックの読み込み元形式ではなく、保存先のファイル形式によって決まります。
{{% /alert %}}

## **はじめに**
Aspose.Cells は、ピボットテーブル用の 2 つの並行するスタイル API を公開します。どちらを使用するかは、ワークブックの読み込み元形式ではなく、保存先の形式によって決まります。`.xls` ファイルから読み込んだワークブックを `.xlsx` として再保存する場合にも、レガシー API ではなく新しいスタイル API が適用されます。
- `PivotTable.PivotTableStyleType` は、組み込みの名前付きスタイル（明るいテーマと暗いテーマを含む。Excel 2017 で追加されたスタイルも含む）を選択します。これらの定義済みスタイルは読み取り専用です。
- `PivotTable.PivotTableStyleName` は、`Worksheets.TableStyles.AddPivotTableStyle(...)` を使用して定義したカスタムスタイルを選択します。定義済みスタイルで提供される内容を変更して、色、罫線、フォントをカスタマイズする場合は、カスタムスタイルが必要です。
さらに、`PivotTable.FormatAll(Style)` は、1 つの `Style` オブジェクトをピボットのすべてのセルに適用するショートカットです。これは、上記のいずれかのスタイル名 API を通じて設定された内容を上書きします。基になるテーマに関係なく均一な外観が必要な場合に便利です。

## **レガシー XLS の定義済みオートフォーマットを適用する**
`PivotTable.AutoFormatType` は、`Aspose.Cells.Pivot.PivotTableAutoFormatType` 列挙型の値を受け取ります。使用できる値は、`Report1` ～ `Report10`、`Classic`、および `Table1` ～ `Table10` です。
次の例では、新しいワークブックを読み込み、Fruit/Year/Amount のサンプルデータを入力し、ピボットテーブルを追加して `PivotTableAutoFormatType.Report5` を適用し、結果を `.xls` として保存します。

{{% alert color="primary" %}}
**列フィールドがない理由：** Report シリーズオートフォーマット（`Report1` ～ `Report10`、`Table1` ～ `Table10`）は、従来の Excel で、行フィールドと値だけを使用する**一次元ピボットテーブル**向けに設計されています。これらのオートフォーマットには、列フィールド見出し用の組み込みスタイルがありません。ピボットテーブルで列フィールドが必要な場合は、代わりに [シナリオ 2](#apply-a-modern-named-preset-pivot-table-style) の新しい `PivotTableStyleType` 定義済みスタイルを使用してください。このスタイルは、現在の Excel が使用する二次元レイアウト向けに設計されています。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // 新しいワークブックを作成
    Workbook workbook;
    // 最初のワークシートを取得
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // ヘッダー行（Fruit、Year、Amount）を持つソースデータを入力
    // および2020年と2021年にわたる grape、blueberry、kiwi、cherry をカバーする9行のデータ
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
    // ソース範囲 A1:C10 を使用して、宛先セル E3 に「Pivot1」という名前のピボットテーブルを追加
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);
    // フィールドを割り当て：Fruit → 行、Amount → データ
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // レガシー XLS プリセット自動フォーマット「Report5」を適用
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);
    // ワークブックをレガシー .xls 形式で保存
    workbook.Save(u"output.xls");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **新しい名前付き定義済みピボットテーブルスタイルを適用する**

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

## **カスタムピボットテーブルスタイルを定義して適用する**
組み込みの定義済みスタイルは変更できません。色、罫線、フォントを上書きする必要がある場合は、必ずカスタムピボットスタイルを定義する必要があります。作業手順は次の 3 つです。
1. `Worksheets.TableStyles.AddPivotTableStyle(string name)` を使用して、カスタムスタイルをワークブックの `TableStyles` コレクションに追加します。新しく作成されたスタイルのインデックスが返されます。
2. `TableStyle.TableStyleElements.Add(TableStyleElementType)` を使用して要素（`WholeTable` や `GrandTotalRow` など）を追加してスタイルを設定し、`TableStyleElement.SetElementStyle(Style)` を使用して各要素に `Style` を割り当てます。
3. `PivotTable.PivotTableStyleName` にスタイル名を設定して、カスタムスタイルをピボットテーブルに適用します。ここでは `PivotTableStyleType` を使用しないでください。このプロパティは組み込みの定義済みスタイルを選択するためのものです。

{{% alert color="primary" %}}
`PivotTableStyleName` と `PivotTableStyleType` は同じ目的で使用できません。組み込みの定義済みスタイルには `PivotTableStyleType` を使用し、`AddPivotTableStyle` を通じて定義したカスタムスタイルには `PivotTableStyleName` を使用します。両方を設定しても問題ありませんが、実際に適用されるのは、意図したソースに一致する一方だけです。
{{% /alert %}}

使用できる `TableStyleElementType` の値には、`WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels`、`PageFieldValues` があります。
次の例では、`WholeTable` に細い黒い罫線、`GrandTotalRow` に太字の赤いフォントを指定してカスタムピボットスタイルを定義し、`PivotTableStyleName` を使用して適用して `.xlsx` として保存します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // ソースデータを入力：ヘッダー行 + 9行のデータ (A1:C10)
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
    // A1:C10 をデータソースとするピボットテーブルを追加し、E3 に配置、名前を "Pivot1" とする
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // ステップ 1：新しいカスタムピボットテーブルスタイルを登録し、そのインデックスを取得する
    int styleIndex = workbook.GetWorksheets().GetTableStyles().AddPivotTableStyle(u"CustomPivotStyle");
    TableStyle tableStyle = workbook.GetWorksheets().GetTableStyles().Get(styleIndex);
    // ステップ 2：WholeTable 要素を追加し、上下左右の 4 辺すべてに細い黒色の境界線を適用する
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
    // ステップ 3：GrandTotalRow 要素を追加し、太字の赤色フォントを適用する
    int grandTotalElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::GrandTotalRow);
    TableStyleElement grandTotalElement = tableStyle.GetTableStyleElements().Get(grandTotalElementIndex);
    Style grandTotalStyle = workbook.CreateStyle();
    grandTotalStyle.GetFont().SetIsBold(true);
    grandTotalStyle.GetFont().SetColor(Color::Red());
    grandTotalElement.SetElementStyle(grandTotalStyle);
    // ステップ 4：カスタムスタイルを名前で適用する（PivotTableStyleType は組み込みプリセット用なので使用しない）
    pivotTable.SetPivotTableStyleName(u"CustomPivotStyle");
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **FormatAll を使用してすべてのピボットセルに 1 つのスタイルを適用する**
`PivotTable.FormatAll(Style)` は、1 つの `Style` オブジェクトを、ピボットテーブルのデータ領域、行見出し、列見出し、合計を含むすべてのセルに適用するショートカットです。`PivotTableStyleType` または `PivotTableStyleName` を通じて以前に設定された内容はすべて上書きされます。

{{% alert color="primary" %}}
`FormatAll` は、`PivotTableStyleType` と `PivotTableStyleName` の両方を上書きします。ピボットテーブル全体で、テーマに依存しない均一な外観が必要な場合にのみ使用してください。
{{% /alert %}}

次の例では、黄色の単色塗りつぶし、太字の濃紺フォント、すべての辺に細い黒い罫線を持つ `Style` を作成し、`FormatAll` を使用して適用して `.xlsx` として保存します。

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
    // ピボットテーブルの追加：ソース範囲 A1:C10、配置先セル E3、名前 "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // ピボットフィールドの割り当て
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // ピボットテーブルのすべてのセルに強制適用するスタイルの作成
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
    // FormatAll の適用
    pivotTable.FormatAll(style);
    // ワークブックの保存
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **どのスタイル API を使用すべきか**
スタイル API の選択は、保存先のファイル形式によって異なります。クイックリファレンスとして次の表を使用してください。
| 対象ファイル形式 | 使用する API | 備考 |
|---|---|---|
| `.xls`（レガシー） | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` の値（例：`Report1`～`Report10`、`Classic`、`Table1`～`Table10`）。新しい形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb`（新しい形式、組み込みスタイル） | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` の値（明るいテーマと暗いテーマを含む。Excel 2017 で追加されたものも含む）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（新しい形式、カスタムスタイル） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | 組み込みの定義済みスタイルだけでは不十分な場合に使用します。`TableStyleElement.SetElementStyle(...)` を使用して設定します。 |
| すべての形式（均一な上書き） | `PivotTable.FormatAll(Style)` | ピボットテーブル全体の他のすべてのスタイル設定を上書きするショートカットです。 |
判断に迷った場合は、`.xlsx` として保存し、組み込みテーマには `PivotTableStyleType`、カスタムテーマには `PivotTableStyleName` を使用してください。

{{< app/cells/assistant language="cpp" >}}