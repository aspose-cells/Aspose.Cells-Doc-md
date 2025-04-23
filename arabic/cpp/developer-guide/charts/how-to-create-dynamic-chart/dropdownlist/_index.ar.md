---
title: كيفية إنشاء رسم بياني ديناميكي مع قائمة منسدلة باستخدام C++
linktitle: إنشاء رسم بياني ديناميكي مع القائمة المنسدلة
description: تعلم كيفية إنشاء رسم بياني ديناميكي يتحدث استنادًا إلى اختيار قائمة منسدلة باستخدام Aspose.Cells for C++. دليلنا خطوة بخطوة سيعرض كيفية دمج قائمة منسدلة في المخطط الخاص بك لتصور البيانات بشكل مرن.
keywords: Aspose.Cells for C++، رسم بياني ديناميكي، قائمة منسدلة، تصور البيانات، التكامل، تصور مرن.
type: docs
weight: 76
url: /ar/cpp/create-dynamic-chart-with-dropdownlist/
---

## **سيناريوهات الاستخدام المحتملة**
رسم بياني ديناميكي مع قائمة منسدلة في إكسل هو أداة قوية تتيح للمستخدمين إنشاء رسوم بيانية تفاعلية يمكن تحديثها بناءً على البيانات المحددة. تكون هذه الميزة مفيدة بشكل خاص في الحالات التي تحتاج فيها إلى تحليل مجموعات بيانات متعددة أو مقارنة سيناريوات مختلفة.

تطبيق شائع آخر لرسم بياني ديناميكي بقائمة منسدلة في التحليل المالي. على سبيل المثال ، قد تحتوي شركة على مجموعات متعددة من البيانات المالية لسنوات أو أقسام مختلفة. من خلال استخدام قائمة منسدلة ، يمكن للمستخدمين تحديد مجموعة البيانات المحددة التي يرغبون في تحليلها ، وسيتم تحديث الرسم البياني تلقائيًا لعرض المعلومات المقابلة. يُسمح بذلك بسهولة المقارنة والتعرف على الاتجاهات أو الأنماط.

تطبيق آخر هو في المبيعات والتسويق. قد تحتوي شركة على بيانات مبيعات لمنتجات أو مناطق مختلفة. باستخدام رسم بياني ديناميكي مع قائمة منسدلة ، يمكن للمستخدمين اختيار منتج محدد أو منطقة من القائمة المنسدلة ، وسيتم تحديث الرسم البياني بشكل ديناميكي لعرض أداء المبيعات للاختيار المحدد. يساعد ذلك في تحديد المناطق أو المنتجات الأكثر أداءً واتخاذ قرارات تستند إلى البيانات.

باختصار ، يوفر رسم بياني ديناميكي مع قائمة منسدلة في إكسل وسيلة مرنة وتفاعلية لتصور وتحليل البيانات. إنه قيم في الحالات التي تحتاج فيها إلى مقارنة مجموعات بيانات متعددة أو استكشاف سيناريوات مختلفة ، مما يجعله أداة متعددة الاستخدامات للتحليل المالي والمبيعات والتسويق والعديد من التطبيقات الأخرى.

## ** استخدام Aspose Cells لإنشاء رسم بياني ديناميكي مع القائمة المنسدلة**
 في الفقرات التالية، سنوضح لك كيفية إنشاء رسم بياني ديناميكي باستخدام Aspose.Cells. سنعرض لك الكود للمثال، بالإضافة إلى ملف إكسل الذي تم إنشاؤه باستخدام هذا الكود.

## **الكود المثالي**
سيقوم الكود العيني التالي بتوليد [ملف رسم بياني ديناميكي مع قائمة منسدلة](DynamicChartWithDropdownlist.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A3").PutValue(u"Tea");
    sheet.GetCells().Get(u"A4").PutValue(u"Coffee");
    sheet.GetCells().Get(u"A5").PutValue(u"Sugar");

    // In this example, we will add 12 months of data
    sheet.GetCells().Get(u"B2").PutValue(u"Jan");
    sheet.GetCells().Get(u"C2").PutValue(u"Feb");
    sheet.GetCells().Get(u"D2").PutValue(u"Mar");
    sheet.GetCells().Get(u"E2").PutValue(u"Apr");
    sheet.GetCells().Get(u"F2").PutValue(u"May");
    sheet.GetCells().Get(u"G2").PutValue(u"Jun");
    sheet.GetCells().Get(u"H2").PutValue(u"Jul");
    sheet.GetCells().Get(u"I2").PutValue(u"Aug");
    sheet.GetCells().Get(u"J2").PutValue(u"Sep");
    sheet.GetCells().Get(u"K2").PutValue(u"Oct");
    sheet.GetCells().Get(u"L2").PutValue(u"Nov");
    sheet.GetCells().Get(u"M2").PutValue(u"Dec");

    int allMonths = 12;
    int iCount = 3;
    for (int i = 0; i < iCount; i++)
    {
        for (int j = 0; j < allMonths; j++)
        {
            int _row = i + 2;
            int _column = j + 1;
            sheet.GetCells().Get(_row, _column).PutValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
        }
    }

    // This is the Dropdownlist for Dynamic Data
    CellArea ca = CellArea::CreateCellArea(9, 0, 9, 0);
    int _index = sheet.GetValidations().Add(ca);
    Validation _va = sheet.GetValidations().Get(_index);
    _va.SetType(ValidationType::List);
    _va.SetInCellDropDown(true);
    _va.SetFormula1(u"=$B$2:$M$2");

    sheet.GetCells().Get(u"A9").PutValue(u"Current Month");
    sheet.GetCells().Get(u"A10").PutValue(u"Jan");

    Style _style = sheet.GetCells().Get(u"A10").GetStyle();
    _style.GetFont().SetIsBold(true);
    _style.SetPattern(BackgroundType::Solid);
    _style.SetForegroundColor(Color::Yellow());
    sheet.GetCells().Get(u"A10").SetStyle(_style);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtMonthData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtXLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=Sheet1!$A$3:$A$5");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 8, 2, 20, 8);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"month", true);
    chart.GetNSeries().Get(0).SetName(u"=Sheet1!$A$10");
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtMonthData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtXLabels");

    // Save the workbook as an Excel file.
    workbook.Save(u"DynamicChartWithDropdownlist.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **ملاحظات**
في الملف الذي تم إنشاؤه، سيقوم الرسم البياني بحساب البيانات ديناميكيًا بالنسبة للشهر المحدد. يتم ذلك باستخدام صيغة "OFFSET" في الكود العيني:

```cpp
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

يمكنك محاولة تغيير قيمة القائمة المنسدلة في الخلية "Sheet1!$A$10"، وسوف ترى التغيير الديناميكي في الرسم البياني. الآن لقد قمنا بإنشاء رسم بياني ديناميكي مع قائمة منسدلة باستخدام Aspose.Cells بنجاح.
