---
title: المحور الرئيسي والثانوي باستخدام C++
linktitle: المحور الأساسي والثانوي
description: تعلم كيفية فهم والعمل مع المحاور الرئيسية والثانوية في Aspose.Cells for C++. سيساعدك دليلنا على فهم الاختلافات بين المحاور الرئيسية والثانوية، وكيفية تكوينها واستخدامها بفعالية في الرسوم البيانية الخاصة بك.
keywords: Aspose.Cells for C++، المحاور الرئيسية، المحاور الثانوية، الفهم، الاختلافات، التكوين، الاستخدام.
type: docs
weight: 190
url: /ar/cpp/primary-and-second-axis/
---

## **سيناريوهات الاستخدام المحتملة**
عندما تتفاوت الأرقام في الرسم البياني بشكل كبير بين سلاسل البيانات، أو عندما تحتوي على أنواع مختلطة من البيانات (السعر والحجم)، ارسم سلسلة بيانات واحدة أو أكثر على محور عمودي (قيمة) ثانوي. مقياس المحور العمودي الثانوي يظهر القيم لسلاسل البيانات المرتبطة. يعمل المحور الثانوي بشكل جيد في رسم بياني يظهر فيه مزيج من رسوم الأعمدة والخطوط.

## **قم بالتعامل مع المحور الأساسي والثانوي على غرار Microsoft Excel**
 يرجى مراجعة رمز العينة التالي الذي ينشئ ملف إكسل جديد ويضع قيم الرسم البياني في ورقة العمل الأولى. 
ثم نضيف رسم بياني ونعرض المحور الثانوي.

![todo:image_alt_text](excel.png)

## **الكود المثالي**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a chart
    worksheet.GetCells().Get(u"A1").PutValue(u"Region");
    worksheet.GetCells().Get(u"A2").PutValue(u"Peking");
    worksheet.GetCells().Get(u"A3").PutValue(u"New York");
    worksheet.GetCells().Get(u"A4").PutValue(u"Paris");
    worksheet.GetCells().Get(u"B1").PutValue(u"Sales Volume");
    worksheet.GetCells().Get(u"C1").PutValue(u"Growth Rate");
    worksheet.GetCells().Get(u"B2").PutValue(100);
    worksheet.GetCells().Get(u"B3").PutValue(80);
    worksheet.GetCells().Get(u"B4").PutValue(140);
    worksheet.GetCells().Get(u"C2").PutValue(0.7);
    worksheet.GetCells().Get(u"C3").PutValue(0.8);
    worksheet.GetCells().Get(u"C4").PutValue(1.0);

    // Create a Scatter chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::Scatter, 6, 6, 15, 11);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:C4", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$4");

    // Set the Second-Axis
    chart.GetNSeries().Get(1).SetPlotOnSecondAxis(true);

    // Show the Second-Axis
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Set the second series ChartType to line
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Set the series name
    chart.GetNSeries().Get(0).SetName(u"Sales Volume");
    chart.GetNSeries().Get(1).SetName(u"Growth Rate");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the file
    workbook.Save(u"PrimaryandSecondaryAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
