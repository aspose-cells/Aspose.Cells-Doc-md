---
title: إدارة DataLabels لمخططات Excel باستخدام ++C
linktitle: علامات البيانات
type: docs
weight: 50
url: /ar/cpp/insert-datalabels-to-chart/
description: تعلم كيفية إدارة علامات البيانات بشكل فعال في مخططات Excel باستخدام Aspose.Cells for C++. يغطي دليلنا الشامل مهام الإدارة المختلفة، بما في ذلك إضافة، إزالة، وتعديل العلامات لتحسين قابلية قراءة واستخدام المخطط.
keywords: Aspose.Cells for C++، مخططات Excel، علامات البيانات، الإدارة، القابلية للقراءة، الاستخدام، الإضافة، الإزالة، التعديل.
---

{{% alert color="primary" %}}

علامات البيانات هي جزء مهم من المخطط. يمكننا بسهولة معرفة القيمة، النسبة المئوية، إلخ. لكل سلسلة.

{{% /alert %}}

## **خيارات علامات البيانات**
 تتيح Aspose.Cells أيضًا إدارة علامات البيانات للمخطط في وقت التشغيل باستخدام كائن [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/). من السهل تحريك، تحديث، وتنسيق علامات البيانات للمخطط.

|![todo:image_alt_text](chart_datalabels.png)|

## **إدارة علامات البيانات في الرسم البياني**
 إدارة علامات البيانات للمخطط بسهولة باستخدام Aspose.Cells [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/).

يوضح الكود التالي كيفية إدارة علامات البيانات:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
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

    // Show value labels
    chart.GetNSeries().Get(0).GetDataLabels().SetShowValue(true);

    // Show series name labels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowSeriesName(true);

    // Move labels to center
    chart.GetNSeries().Get(1).GetDataLabels().SetPosition(LabelPositionType::Center);

    // Save the file
    workbook.Save(u"chart_datalabels.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **الموضوعات المتقدمة**
- [إضافة تسميات مخصصة إلى نقاط البيانات في سلسلة الرسم البياني](/cells/ar/cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)
- [تعطيل التفاف النص لعلامات البيانات في الرسم البياني](/cells/ar/cpp/disable-text-wrapping-for-data-labels-of-the-chart/)
- [تغيير شكل تسمية بيانات الرسم البياني لتناسب النص](/cells/ar/cpp/resize-chart-s-data-label-shape-to-fit-text/)
- [تسمية بيانات مخصصة نصية غنية الرسم البياني](/cells/ar/cpp/rich-text-custom-data-label-of-chart-point/)
- [تعيين نوع الشكل لتسميات بيانات الرسم البياني](/cells/ar/cpp/set-the-shape-type-of-data-labels-of-chart/)
- [عرض نطاق الخلايا كعلامات البيانات](/cells/ar/cpp/showing-cell-range-as-the-data-labels/)
