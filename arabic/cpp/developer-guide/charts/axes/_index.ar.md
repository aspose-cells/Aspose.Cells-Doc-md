---
title: إدارة محاور الرسوم البيانية في Excel باستخدام C++
description: تعلم كيفية تكوين محاور الرسم البياني في Aspose.Cells for C++. سيرشدك دليلنا إلى كيفية تعديل المحاور الأساسية والثانوية، وتعيين نطاقاتها، وتغيير خصائصها لتعزيز الرسوم البيانية الخاصة بك.
keywords: Aspose.Cells for C++، محاور الرسوم البيانية، التكوين، المحاور الأساسية، المحاور الثانوية، النطاق، الخصائص.
linktitle: المحاور
type: docs
weight: 50
url: /ar/cpp/chart-axes/
---

{{% alert color="primary" %}}

في رسوم بيانية Excel، هناك 3 أنواع من المحاور:
1. المحور الأفقي (الفئة) : محور X
1. المحور الرأسي (القيمة) : محور Y
1. محور العمق (السلسلة) : محور Z

{{% /alert %}}

## **خيارات المحور**
يتيح Aspose.Cells أيضًا إدارة محاور الرسوم البيانية في وقت التشغيل. باستخدام كائن [Axis](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/)، يمكنك تغيير جميع خيارات المحور كما هو الحال في Excel.

|![todo:image_alt_text](chart_axes.png)|

## **إدارة محاور X و Y**

في رسومات Excel، تعتبر المحاور الأفقي والرأسي أكثر المحاور استخدامًا.

يوضح مقتطف الشفرة التالي كيفية تعيين خيارات محاور X و Y.

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
    worksheet.GetCells().Get(u"A1").PutValue(u"Series1");
    worksheet.GetCells().Get(u"A2").PutValue(50);
    worksheet.GetCells().Get(u"A3").PutValue(100);
    worksheet.GetCells().Get(u"A4").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Series2");
    worksheet.GetCells().Get(u"B2").PutValue(60);
    worksheet.GetCells().Get(u"B3").PutValue(32);
    worksheet.GetCells().Get(u"B4").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Hiding X axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Setting max value of Y axis
    chart.GetValueAxis().SetMaxValue(200);

    // Setting major unit
    chart.GetValueAxis().SetMajorUnit(50);

    // Save the file
    workbook.Save(u"chart_axes.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **الموضوعات المتقدمة**
- [تغيير اتجاه التسمية التلقائية](/cells/ar/cpp/change-tick-label-direction/)
- [تحديد أي محور موجود في الرسم البياني](/cells/ar/cpp/determine-which-axis-exists-in-the-chart/)
- [التعامل مع الوحدات التلقائية لمحور الرسم البياني مثل Microsoft Excel](/cells/ar/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)
- [قراءة تسميات المحور بعد حساب الرسم البياني](/cells/ar/cpp/read-axis-labels-after-calculating-the-chart/)
- [كيفية تعيين محور الفئة في رسم بياني Excel](/cells/ar/cpp/how-to-set-category-axis/)
{{< app/cells/assistant language="cpp" >}}
