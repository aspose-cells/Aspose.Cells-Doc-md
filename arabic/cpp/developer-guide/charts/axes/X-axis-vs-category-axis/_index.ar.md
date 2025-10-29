---
title: المحور السيني مقابل المحور التصنيفي باستخدام C++
linktitle: المحور X مقابل محور الفئة
description: تعلم كيفية التمييز بين المحور السيني والمحور التصنيفي في Aspose.Cells for C++. سيساعدك دليلنا على فهم الاختلافات في استخدامهما وخصائصهما، وكيفية تكوينهما وفقًا لاحتياجاتك.
keywords: Aspose.Cells for C++، المحور السيني، المحور التصنيفي، الاختلاف، الاستخدام، الخصائص، التكوين.
type: docs
weight: 180
url: /ar/cpp/X-axis-vs-category-axis/
---

## **سيناريوهات الاستخدام المحتملة**
هناك أنواع مختلفة من المحاور X. بينما يكون المحور Y محور نوع قيمة، يمكن أن يكون المحور X محور نوع فئة أو محور نوع قيمة. باستخدام محور القيمة، يتم معاملة البيانات كبيانات عددية متغيرة بشكل مستمر، ويتم وضع العلامة في نقطة على طول المحور التي تتغير وفقًا لقيمتها العددية. باستخدام محور الفئة، يتم معاملة البيانات كسلسلة من علامات النص غير الرقمية، ويتم وضع العلامة في نقطة على طول المحور وفقًا لموقعها في التسلسل. يوضح المثال أدناه الفرق بين محاور القيمة والفئة.
يتم عرض البيانات العينية لدينا في [ملف الجدول العيني](sample.png) أدناه. تحتوي العمود الأول على بيانات محور X الخاصة بنا، والتي يمكن معاملتها كفئات أو قيم. لاحظ أن الأرقام ليست منتظمة بالتساوي، ولا تظهر حتى بترتيب عددي.

![todo:image_alt_text](sample.png)

## **قم بالتعامل مع المحور X ومحور الفئة على غرار Microsoft Excel**
 سنعرض هذه البيانات على نوعين من الرسوم البيانية، الرسم البياني الأول هو XY (نقطة الانتشار) مع المحور السيني كقيم، والرسم البياني الثاني هو مخطط خطي مع المحور السيني كتصنيف.

![todo:image_alt_text](compare.png)

## **الكود المثالي**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in charts
    worksheet.GetCells().Get(u"A2").PutValue(1);
    worksheet.GetCells().Get(u"A3").PutValue(3);
    worksheet.GetCells().Get(u"A4").PutValue(2.5);
    worksheet.GetCells().Get(u"A5").PutValue(3.5);
    worksheet.GetCells().Get(u"B1").PutValue(u"Cats");
    worksheet.GetCells().Get(u"C1").PutValue(u"Dogs");
    worksheet.GetCells().Get(u"D1").PutValue(u"Fishes");
    worksheet.GetCells().Get(u"B2").PutValue(7);
    worksheet.GetCells().Get(u"B3").PutValue(6);
    worksheet.GetCells().Get(u"B4").PutValue(5);
    worksheet.GetCells().Get(u"B5").PutValue(4);
    worksheet.GetCells().Get(u"C2").PutValue(7);
    worksheet.GetCells().Get(u"C3").PutValue(5);
    worksheet.GetCells().Get(u"C4").PutValue(4);
    worksheet.GetCells().Get(u"C5").PutValue(3);
    worksheet.GetCells().Get(u"D2").PutValue(8);
    worksheet.GetCells().Get(u"D3").PutValue(7);
    worksheet.GetCells().Get(u"D4").PutValue(3);
    worksheet.GetCells().Get(u"D5").PutValue(2);

    // Create Line Chart: X as Category Axis
    int pieIdx = worksheet.GetCharts().Add(ChartType::LineWithDataMarkers, 6, 15, 20, 21);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:D5", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$5");

    // Set the first series name
    chart.GetNSeries().Get(0).SetName(u"Cats");

    // Set the second series name
    chart.GetNSeries().Get(1).SetName(u"Dogs");

    // Set the third series name
    chart.GetNSeries().Get(2).SetName(u"Fishes");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Create XY (Scatter) Chart: X as Value Axis
    pieIdx = worksheet.GetCharts().Add(ChartType::ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);

    // Retrieve the Chart object
    chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:D5", true);

    // Set X values for series
    chart.GetNSeries().Get(0).SetXValues(u"{1,3,2.5,3.5}");
    chart.GetNSeries().Get(1).SetXValues(u"{1,3,2.5,3.5}");
    chart.GetNSeries().Get(2).SetXValues(u"{1,3,2.5,3.5}");

    // Set the first series name
    chart.GetNSeries().Get(0).SetName(u"Cats");

    // Set the second series name
    chart.GetNSeries().Get(1).SetName(u"Dogs");

    // Set the third series name
    chart.GetNSeries().Get(2).SetName(u"Fishes");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"XAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
