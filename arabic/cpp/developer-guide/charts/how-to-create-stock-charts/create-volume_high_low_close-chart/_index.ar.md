---
title: إنشاء رسم بياني للحجم العالي والمنخفض والإغلاق مع C++
linktitle: إنشاء رسم بياني للمخزون  ارتفاع  منخفض  إغلاق (VHLC)
description: تعلم كيفية إنشاء رسم بياني للحجم العالي والمنخفض والإغلاق باستخدام Aspose.Cells for C++. دليلنا سيظهر كيفية رسم بيانات سوق الأسهم، بما في ذلك الحجم، والأسعار العليا والمنخفضة والإغلاق، على رسم بياني لتحليل أفضل وتصوير البيانات.
keywords: Aspose.Cells for C++، رسم بياني للحجم العالي والمنخفض والإغلاق، بيانات سوق الأسهم، التحليل، التصور.
type: docs
weight: 183
url: /ar/cpp/create-volume-high-low-close-stock-chart/
---

## **سيناريوهات الاستخدام المحتملة**
الرسم البياني الثالث الذي سنلقي نظرة عليه هو رسم بياني للحجم العالي والمنخفض والإغلاق. مرة أخرى، من المهم تكرار أن البيانات يجب أن تكون في الترتيب الصحيح. إذا احتجت إلى إعادة ترتيب جدول البيانات الخاص بك، يجب أن تفعله قبل إعداد رسمك البياني. يتضمن هذا الرسم عمودًا للحجم بعد العمود التصنيفي الأول، وتظهر الرسوم البيانية عمودًا على المحور الرئيسي يوضح هذا الحجم، بينما تنتقل الأسعار إلى المحور الثانوي.

![todo:image_alt_text](data.png)
## **رسم بياني للمخزون - ارتفاع - منخفض - إغلاق (VHLC)**

![todo:image_alt_text](sample.png)
## **الكود المثالي**
الكود عينة التالي يقوم بتحميل ملف Excel عينة ويولّد ملف Excel الناتج.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);

    // Set category data 
    chart.GetNSeries().SetCategoryData(u"A2:A9");

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{ 79, 129, 189 });

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


{{< app/cells/assistant language="cpp" >}}
