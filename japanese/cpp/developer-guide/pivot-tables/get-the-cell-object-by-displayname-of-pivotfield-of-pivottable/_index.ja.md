---
title: C++を使ってピボットテーブルの表示名からセルオブジェクトを取得する
linktitle: ピボットテーブルのピボットフィールドの表示名からセルオブジェクトを取得する方法
type: docs
weight: 70
url: /ja/cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: ピボットフィールドの表示名からセルオブジェクトを取得し、書式設定を適用する方法をAspose.Cells for C++を使って学びます。
---

{{% alert color="primary" %}}

 Aspose.Cellsは [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getcellbydisplayname/) メソッドを提供しており、これを使ってピボットフィールドの表示名からセルオブジェクトにアクセスできます。このメソッドはピボットフィールドヘッダーをハイライトまたは書式設定したいときに便利です。この記事では、データフィールドの表示名からセルオブジェクトを取得し、それに書式設定を適用する方法を説明しています。

{{% /alert %}}

## ** ピボットテーブルの表示名からセルオブジェクトを取得する**

 次のコードは、シートの最初のピボットテーブルにアクセスし、次にピボットテーブルの2番目のデータフィールドの表示名からセルを取得します。次に、そのセルの塗りつぶし色とフォント色をライトブルーと黒に変更します。以下はコード実行前後のピボットテーブルの見た目を示すスクリーンショットです。

|**ピボットテーブル - 実行前**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"source.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    Cell cell = pivotTable.GetCellByDisplayName(pivotTable.GetDataFields().Get(0).GetDisplayName());

    Style style = cell.GetStyle();
    style.SetForegroundColor(Color::LightBlue());
    style.GetFont().SetColor(Color::Black());

    pivotTable.Format(cell.GetRow(), cell.GetColumn(), style);
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Pivot table formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

|**ピボットテーブル - 実行後**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
