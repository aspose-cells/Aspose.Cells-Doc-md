---
title: C++でPivotChartをPivotOptionsと管理する方法
linktitle: Pivot Options
type: docs
weight: 10
url: /ja/cpp/how-to-manage-pivotchart-with-pivotoptions/
description: C++を使用したPivotOptionsによるPivotChartの管理方法
keywords: PivotChart
---

## PivotChartとは

ExcelのPivotChartは、PivotTableから作成されたデータの視覚的な表現です。これにより、ユーザーは情報を要約してチャート形式で表示し、データをダイナミックに視覚化して分析することができます。PivotChartは対話型であり、データの異なる視点を簡単に表示するように修正できるため、Excelでのデータ分析とプレゼンテーションにおける強力なツールとなっています。

## PivotOptionsを使用してPivotChartを管理する方法

Aspose.Cellsを使用すると、PivotChartを管理するために[**PivotOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/pivotoptions/)を使用できます。

サンプルファイルとコード:  
[サンプルファイル](Sample.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path for the sample Excel file
    U16String path = u"..\\Data\\01_SourceDirectory\\";

    // Create a Workbook object from the sample file
    Workbook book(path + u"Sample.xlsx");

    // Get the first chart from the first worksheet
    Chart chart = book.GetWorksheets().Get(0).GetCharts().Get(0);

    // Get the PivotOptions from the chart
    PivotOptions opt = chart.GetPivotOptions();

    // Hide ZoneFilter in PivotChart
    opt.SetDropZoneFilter(false); // HideZoneFilter

    // You can set more properties, try them!
    // opt.SetDropZoneCategories(false);  // HideZoneCategories
    // opt.SetDropZoneData(false);        // HideZoneData
    // opt.SetDropZoneSeries(false);      // HideZoneSeries
    // opt.SetDropZonesVisible(false);    // Hide All

    // Save the modified file to see the effect
    book.Save(path + u"HideZoneFilter.xlsx");

    std::cout << "Pivot chart updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

上記の例のコードを使用すると、次の効果が表示された結果ファイルを確認できます。

**![Output](Output.png)**
{{< app/cells/assistant language="cpp" >}}
