---
title: إنشاء رسم بياني للأسهم المفتوحة والعالية والمنخفضة والإغلاق مع C++
description: تعلم كيفية إنشاء رسم بياني للأسهم المفتوحة والعالية والمنخفضة والإغلاق باستخدام Aspose.Cells for C++. دليلنا سيظهر كيفية رسم بيانات سوق الأسهم، بما في ذلك الأسعار المفتوحة والعالية والمنخفضة والإغلاق، على رسم بياني لتحليل أفضل وتصوير البيانات.
keywords: Aspose.Cells for C++، رسم بياني للأسهم المفتوحة والعالية والمنخفضة والإغلاق، بيانات سوق الأسهم، التحليل، التصور.
type: docs
weight: 182
url: /ar/cpp/create-open-high-low-close-stock-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يستخدم مخطط Open-High-Low-Close (OHLC) خمسة أعمدة من البيانات، بالترتيب: الفئة، فتح، عالي، منخفض، وإغلاق. يتم إشارة نطاق الأسعار في كل فئة مرة أخرى بخط عمودي، بينما يتم تقديم نطاق بين الفتح والإغلاق بشريط عائم أوسع؛ إذا زاد السعر في الفئة (الإغلاق أعلى من الفتح)، يتم ملؤه بلون واحد، بينما إذا انخفض السعر، يتم ملؤه بلون آخر. يطلق على هذا النوع من الرسم البياني كثيرًا اسم الرسم الشمعي.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **تحسينات الرؤية في الرسم البياني**
 غالبًا ما نستخدم الألوان بدلاً من الأبيض والأسود للإشارة إلى ارتفاع وانخفاض الأسعار. في مجموعة الشموع الأولى أدناه، يظهر اللون الأحمر ارتفاع الأسعار والأخضر انخفاضها.

![todo:image_alt_text](sample2.png)

## **الكود المثالي**
الكود العينة التالي يحمل [ملف إكسل العينة](Open-High-Low-Close.xlsx) ويولد [ملف إكسل الناتج](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Open-High-Low-Close.xlsx");
    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockOpenHighLowClose, 5, 6, 20, 12);
    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);
    // Set the legend can be showed
    chart.SetShowLegend(true);
    // Set the chart title name
    chart.GetTitle().SetText(u"Open-High-Low-Close Stock");
    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);
    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);
    // Set category data
    chart.GetNSeries().GetCategoryData() = u"A2:A9";
    // Set the DownBars and UpBars with different color
    chart.GetNSeries().Get(0).GetDownBars().GetArea().SetForegroundColor(Color::Green());
    chart.GetNSeries().Get(0).GetUpBars().GetArea().SetForegroundColor(Color::Red());
    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);
    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
