---
title: إدارة أسطورة مخططات Excel باستخدام C++
linktitle: أسطورة
description: تعلم كيف تستخدم Aspose.Cells for C++ للاستفادة بشكل فعال من أساطير المخططات وتخصيصها في Microsoft Excel. يشرح دليلنا الشامل وظيفة الأسطورة، كيفية الوصول إليها وتعديلها، بالإضافة إلى تحسين تصور البيانات وفهمها مع الأساطير.
keywords: Aspose.Cells for C++، أساطير المخططات، Microsoft Excel، التصور، فهم البيانات.
type: docs
weight: 50
url: /ar/cpp/chart-legend/
---

## **خيارات الأسطورة**
كما تسمح Aspose.Cells بإدارة أسطورة المخطط في وقت التشغيل. مع كائن [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/)، يمكن نقل الأسطورة وتحديثها وتنسيقها.

|![todo:image_alt_text](chart_legend.png)|

## **ضبط أسطورة الرسم البياني**
من السهل إدارة أسطورة المخطط باستخدام Aspose.Cells [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/).

يوضح مقتطف الكود التالي كيفية إدارة الأسطورة:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Move the legend to left
    chart.GetLegend().SetPosition(LegendPositionType::Left);

    // Set font color of the legend
    chart.GetLegend().GetFont().SetColor(Color::Blue());

    // Save the file
    workbook.Save(u"chart_legend.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مواضيع متقدمة**
- [ضبط نص إدخال وسام الرسم البياني على لا شيء باستخدام Aspose.Cells](/cells/ar/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
