---
title: C++でウォーターフォールチャートを作成する方法
linktitle: ウォーターフォールチャートの作成方法
type: docs
weight: 160
url: /ja/cpp/creating-waterfall-chart/
description: ExcelでC++とAspose.Cells for C++ APIを使用してウォーターフォールチャートを作成します。
keywords: C++でExcelにウォーターフォールチャートを作成する、C++でExcelにウォーターフォールチャートを作成、C++でExcelでウォーターフォールチャートを作る、Excelでウォーターフォールチャートを作成、プログラムによるウォーターフォールチャートの作成方法、C++でExcelにウォーターフォールチャートを作成する方法
---

{{% alert color="primary" %}}

ウォーターフォールチャートは、通常、出発位置が増加または減少する方法を示すために使用される特別なタイプのチャートです。Microsoft Excelには、カラム、折れ線、円、棒、レーダーなどの事前定義済みのチャートタイプが多数ありますが、ウォーターフォールチャートは基本的なグラフを超えたものであり、既存のチャートタイプを使用して少しのカスタマイズまたはより多くのカスタマイズで作成できます。

{{% /alert %}}

Aspose.Cells APIを使用してラインチャートのヘルプを受けてウォーターフォールチャートを作成することが可能です。APIでは、チャートの外観をウォーターフォールの形状にするために[**Series.GetUpBars()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getupbars/)や[**Series.GetDownBars()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getdownbars/)のプロパティを設定することができます。

以下のコードスニペットは、Aspose.Cells for C++ APIを使用してゼロからウォーターフォールチャートを作成する例です。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an instance of Workbook
    Workbook workbook;

    // Retrieve the first Worksheet in Workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Retrieve the Cells of the first Worksheet
    Cells cells = worksheet.GetCells();

    // Input some data which chart will use as source
    cells.Get(U16String(u"A1")).PutValue(U16String(u"Previous Year"));
    cells.Get(U16String(u"A2")).PutValue(U16String(u"January"));
    cells.Get(U16String(u"A3")).PutValue(U16String(u"March"));
    cells.Get(U16String(u"A4")).PutValue(U16String(u"August"));
    cells.Get(U16String(u"A5")).PutValue(U16String(u"October"));
    cells.Get(U16String(u"A6")).PutValue(U16String(u"Current Year"));

    cells.Get(U16String(u"B1")).PutValue(8.5);
    cells.Get(U16String(u"B2")).PutValue(1.5);
    cells.Get(U16String(u"B3")).PutValue(7.5);
    cells.Get(U16String(u"B4")).PutValue(7.5);
    cells.Get(U16String(u"B5")).PutValue(8.5);
    cells.Get(U16String(u"B6")).PutValue(3.5);

    cells.Get(U16String(u"C1")).PutValue(1.5);
    cells.Get(U16String(u"C2")).PutValue(4.5);
    cells.Get(U16String(u"C3")).PutValue(3.5);
    cells.Get(U16String(u"C4")).PutValue(9.5);
    cells.Get(U16String(u"C5")).PutValue(7.5);
    cells.Get(U16String(u"C6")).PutValue(9.5);

    // Add a Chart of type Waterfall in same worksheet as of data
    int idx = worksheet.GetCharts().Add(ChartType::Waterfall, 4, 4, 25, 13);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(idx);

    // Add Series
    chart.GetNSeries().Add(U16String(u"$B$1:$C$6"), true);

    // Add Category Data
    chart.GetNSeries().SetCategoryData(U16String(u"$A$1:$A$6"));

    // Series has Up Down Bars
    chart.GetNSeries().Get(0).SetHasUpDownBars(true);

    // Set the colors of Up and Down Bars
    chart.GetNSeries().Get(0).GetUpBars().GetArea().SetForegroundColor(Color::Green());
    chart.GetNSeries().Get(0).GetDownBars().GetArea().SetForegroundColor(Color::Red());

    // Make both Series Lines invisible
    chart.GetNSeries().Get(0).GetBorder().SetIsVisible(false);
    chart.GetNSeries().Get(1).GetBorder().SetIsVisible(false);

    // Set the Plot Area Formatting Automatic
    chart.GetPlotArea().GetArea().SetFormatting(FormattingType::Automatic);

    // Delete the Legend
    chart.GetLegend().GetLegendEntries().Get(0).SetIsDeleted(true);
    chart.GetLegend().GetLegendEntries().Get(1).SetIsDeleted(true);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## 関連記事

- [チャートの作成](/cells/ja/cpp/creating-charts/)
- [チャートのカスタマイズ](/cells/ja/cpp/customizing-charts/)
