---
title: محور التاريخ باستخدام C++
linktitle: محور التاريخ
description: تعلم كيفية إدارة محور التاريخ في Aspose.Cells for C++. سيساعدك دليلنا على فهم كيفية العمل مع تنسيقات التاريخ المختلفة، مقاييس الوقت، وتواتر تسميات العلامات.
keywords: Aspose.Cells for C++، محور التاريخ، إدارة، تنسيقات التاريخ، مقاييس الوقت، تواتر تسميات العلامات.
type: docs
weight: 200
url: /ar/cpp/date-axis/
---

## **سيناريوهات الاستخدام المحتملة**
عند إنشاء رسم بياني من بيانات ورقة العمل التي تستخدم التواريخ، ويتم رسم التواريخ على المحور الأفقي (فئة) في الرسم، يتغير Aspose.Cells تلقائيًا إلى محور تاريخ (مقياس زمني).
يعرض محور التاريخ التواريخ وفقًا للترتيب الزمني بفواصل زمنية محددة أو وحدات قاعدية، مثل عدد الأيام، أو الأشهر، أو السنوات، حتى إذا كانت التواريخ على ورقة العمل ليست بترتيب تسلسلي أو بنفس الوحدات القاعدية.
 بشكل افتراضي، يحدد Aspose.Cells الوحدات الأساسية لمحور التاريخ بناءً على أصغر فرق بين أي تاريخين في بيانات ورقة العمل. على سبيل المثال، إذا كانت البيانات لأسعار الأسهم حيث أصغر فرق بين التواريخ هو سبعة أيام، يضبط Aspose.Cells الوحدة الأساسية إلى الأيام، ولكن يمكنك تغيير الوحدة الأساسية إلى الأشهر أو السنوات إذا كنت تريد رؤية أداء السهم على مدى فترة أطول.

## **معاملة محور التاريخ مثل Microsoft Excel**
 يرجى مراجعة رمز العينة التالي الذي ينشئ ملف إكسل جديد ويضع قيم الرسم البياني في ورقة العمل الأولى. 
ثم نضيف رسم بياني ونعين نوع الـ [**Axis**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) 
إلى [**TimeScale**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/categorytype/) ومن ثم نضبط الوحدات الأساسية على الأيام.

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add the sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Date");

    // 14 means datetime format
    Style style = worksheet.GetCells().GetStyle();
    style.SetNumber(14);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A2").SetStyle(style);
    worksheet.GetCells().Get(u"A2").PutValue(Date{2022, 6, 26, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A3").SetStyle(style);
    worksheet.GetCells().Get(u"A3").PutValue(Date{2022, 5, 22, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A4").SetStyle(style);
    worksheet.GetCells().Get(u"A4").PutValue(Date{2022, 8, 3, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"B1").PutValue(u"Price");
    worksheet.GetCells().Get(u"B2").PutValue(40);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(60);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 9, 6, 21, 13);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Set the Axis type to Date time
    chart.GetCategoryAxis().SetCategoryType(CategoryType::TimeScale);

    // Set the base unit for CategoryAxis to days
    chart.GetCategoryAxis().SetBaseUnitScale(TimeUnit::Days);

    // Set the direction for the axis text to be vertical
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Vertical);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set max value of Y axis
    chart.GetValueAxis().SetMaxValue(70);

    // Set major unit
    chart.GetValueAxis().SetMajorUnit(10);

    // Save the file
    workbook.Save(u"DateAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
