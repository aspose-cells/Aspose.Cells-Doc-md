---
title: C++を用いたピボットテーブルセルの書式設定
linktitle: ピボットテーブルセルの書式設定
type: docs
weight: 30
url: /ja/cpp/format-pivot-table-cells/
description: Aspose.CellsをC++とともに使用してピボットテーブルのセルをフォーマットする方法を学びます。
---

{{% alert color="primary" %}}

時々、ピボットテーブルセルの書式を設定したいことがあります。たとえば、ピボットテーブルセルに背景色を適用したい場合があります。Aspose.Cells では、この目的で使用できる２つの方法 [**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) および [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) を提供しています。

[**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/)はピボットテーブル全体にスタイルを適用し、[**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/)はピボットテーブルの単一セルにスタイルを適用します。

{{% /alert %}}

以下のサンプルコードは、二つのピボットテーブルを含むサンプルExcelファイル（pivot_format.xlsx）を読み込み、ピボットテーブル全体のフォーマットと個々のセルのフォーマットを実現します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"pivot_format.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(u"Sheet1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(1);

    Style style = workbook.CreateStyle();
    style.SetPattern(BackgroundType::Solid);
    style.SetBackgroundColor(Color::LightBlue());
    pivotTable.FormatAll(style);

    style = workbook.CreateStyle();
    style.SetPattern(BackgroundType::Solid);
    style.SetBackgroundColor(Color::Yellow());

    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(0);
    pivotTable2.Format(16, 5, style);

    workbook.Save(u"out.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 関連記事

- [ピボットテーブルの書式設定](/cells/ja/cpp/formatting-pivot-table/)
- [行と列のフォーマット](/cells/ja/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
