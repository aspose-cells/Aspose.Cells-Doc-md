---
title: كيفية إنشاء رسم بياني لخرائط الأشجار باستخدام C++
description: تعلم كيفية إنشاء رسم بياني لخرائط الأشجار في Aspose.Cells for C++. سيرشدك دليلنا لفهم خصائص وتنسيقات مختلفة متاحة لرسوم خرائط الأشجار، بما في ذلك الألوان، التسميات، وتمثيل البيانات.
keywords: Aspose.Cells for C++، رسم بياني لخرائط الأشجار، إنشاء، خصائص، تنسيق، ألوان، تسميات، تمثيل البيانات، رسم بياني دائري، رسم بياني هرمي.
type: docs
weight: 161
url: /ar/cpp/creating-treemap-chart/
---

## **سيناريوهات الاستخدام المحتملة**
رسم بياني لخريطة الشجرة يوفر رؤية تسلسلية لبياناتك ويجعل من السهل رؤية الأنماط، مثل أي العناصر هي أفضل المبيعات في المحل. تمثل الفروع الشجرية بواسطة المستطيلات، ويتم عرض كل فرع فرعي كمستطيل أصغر. يعرض رسم بياني الخريطة الشجرية الفئات بواسطة اللون والقرب، ويمكن عرض الكثير من البيانات بسهولة مما قد يكون صعبًا مع أنواع الرسوم البيانية الأخرى.

![todo:image_alt_text](sample.png)
## **رسم بياني لخريطة الشجرة**
بعد تشغيل الكود أدناه، سترون رسم بياني لخريطة الشجرة كما هو موضح أدناه.

![todo:image_alt_text](result.png)
## **الكود المثالي**
الكود العيني التالي يقوم بتحميل [ملف Excel العيني](treemap.xlsx) ويولد [ملف Excel الناتج](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"treemap.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Treemap, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"TreeMap Chart");

    // Add series data range (D2:F13, actually)
    chart.GetNSeries().Add(u"D2:F13", true);

    // Set category data (A2:C13 is incorrect)
    chart.GetNSeries().SetCategoryData(u"A2:C13");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
