---
title: إنشاء رسم بياني للحجم المفتوح والعالي والمنخفض والإغلاق مع C++
description: تعلم كيفية إنشاء رسم بياني للحجم المفتوح والعالي والمنخفض والإغلاق باستخدام Aspose.Cells for C++. دليلنا سيظهر كيفية رسم بيانات سوق الأسهم، بما في ذلك الحجم، والأسعار المفتوحة والعالية والمنخفضة والإغلاق، على رسم بياني لتحليل أفضل وتصوير البيانات.
keywords: Aspose.Cells for C++، رسم بياني للحجم المفتوح والعالي والمنخفض والإغلاق، بيانات سوق الأسهم، التحليل، التصور.
type: docs
weight: 184
url: /ar/cpp/create-volume-open-high-low-close-stock-chart/
---

## **سيناريوهات الاستخدام المحتملة**
المخطط الرابع الذي سننظر إليه هو مخطط حجم فتح عالي منخفض إغلاق. من المهم تكرار أن البيانات يجب أن تكون بالترتيب الصحيح. إذا كنت بحاجة لإعادة ترتيب جدول البيانات الخاص بك، يجب أن تقوم بذلك قبل إعداد المخطط. يتضمن هذا المخطط عمودًا للحجم مباشرة بعد العمود الأول (الفئة)، ويشمل رسم بياني عمودي على المحور الرئيسي يُظهر هذا الحجم، بينما يتم نقل الأسعار إلى المحور الثانوي.

![todo:image_alt_text](data.png)

## **مخطط الأسهم لحجم فتح عالي منخفض إغلاق (VHLC)**

![todo:image_alt_text](sample.png)

## **الكود المثالي**
الكود العينة التالي يقوم بتحميل [ملف Excel عينة](Volume-Open-High-Low-Close.xlsx) وإنشاء [ملف Excel الخرج](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-Open-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeOpenHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend to be shown
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-Open-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:F9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{0xff, 79, 129, 189});

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
