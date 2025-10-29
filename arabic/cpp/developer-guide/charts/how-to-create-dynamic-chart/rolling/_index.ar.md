---
title: كيفية إنشاء رسم بياني متداول ديناميكي باستخدام C++
linktitle: كيفية إنشاء رسم بياني ديناميكي متداول
description: تعلم كيفية إنشاء رسم بياني متداول ديناميكي باستخدام Aspose.Cells for C++. دليلنا سيوضح كيفية تنفيذ انتقالات بيانات سلسة ومتوسطات متحركة في المخطط الخاص بك لعرض مستمر ومحدث.
keywords: Aspose.Cells for C++، رسم بياني متداول ديناميكي، انتقالات البيانات، متوسطات سلسة، عرض مستمر، تصور محدث.
type: docs
weight: 74
url: /ar/cpp/create-dynamic-rolling-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يشير رسم البيانات المتداول الديناميكي إلى تمثيل بياني يعرض نقاط البيانات التي تتحرك باستمرار وتحديث عبر الوقت. إنه نوع من الرسم البياني الذي يحدث نفسه باستمرار، ويعرض نافذة متداولة لأحدث نقاط البيانات بينما يتخلص من نقاط البيانات القديمة مع دخول النقاط الجديدة.

يتم استخدام رسوم بيانية متداولة ديناميكية عادةً لتصور الاتجاهات والأنماط في الوقت الفعلي أو البيانات المتدفقة. إنها مفيدة بشكل خاص في السيناريوهات التي تكون فيها الجوانب الزمنية والتغييرات عبر الوقت حرجة، مثل تحليل سوق الأسهم، مراقبة الطقس، أو تتبع الأداء الحي.

عادةً ما تستخدم هذه الرسوم البيانية آليات الرسم المتحرك أو التمرير التلقائي لضمان تقديم أحدث المعلومات دائمًا. يمكن تخصيص طول النافذة المتداولة لعرض فترة زمنية محددة، مثل الساعة الأخيرة، أو اليوم، أو الأسبوع.

في الختام، يعد رسم بياني متداول ديناميكي تمثيلًا بيانيًا محدث باستمرار يعرض أحدث نقاط البيانات مع التخلص من النقاط القديمة، مما يسمح للمستخدمين بمراقبة الاتجاهات والأنماط الفعلية.

## **استخدام Aspose Cells لإنشاء رسم بياني متداول ديناميكي**
في الفقرات التالية، سنريك كيفية إنشاء رسم بياني متداول ديناميكي باستخدام Aspose.Cells. سنريك الكود للمثال، وكذلك ملف Excel الذي تم إنشاؤه بهذا الكود.

## **الكود المثالي**
سيقوم الكود العيني التالي بتوليد [ملف رسم بياني متداول ديناميكي](DynamicRollingChart.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Your local test path
    U16String LocalPath = u"";

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A1").PutValue(u"Month");
    sheet.GetCells().Get(u"A2").PutValue(1);
    sheet.GetCells().Get(u"A3").PutValue(2);
    sheet.GetCells().Get(u"A4").PutValue(3);
    sheet.GetCells().Get(u"A5").PutValue(4);
    sheet.GetCells().Get(u"A6").PutValue(5);
    sheet.GetCells().Get(u"A7").PutValue(6);
    sheet.GetCells().Get(u"A8").PutValue(7);

    sheet.GetCells().Get(u"B1").PutValue(u"Sales");
    sheet.GetCells().Get(u"B2").PutValue(50);
    sheet.GetCells().Get(u"B3").PutValue(45);
    sheet.GetCells().Get(u"B4").PutValue(55);
    sheet.GetCells().Get(u"B5").PutValue(60);
    sheet.GetCells().Get(u"B6").PutValue(55);
    sheet.GetCells().Get(u"B7").PutValue(65);
    sheet.GetCells().Get(u"B8").PutValue(70);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 10, 3, 25, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtLabels");

    // Save the workbook as an Excel file.
    workbook.Save(LocalPath + u"DynamicRollingChart.xlsx");

    std::cout << "Dynamic rolling chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ملاحظات**
في الملف الذي تم إنشاؤه، يمكنك متابعة إضافة البيانات في الأعمدة A و B، بينما يحسب الرسم البياني ديناميكيًا أحدث 5 مجموعات من البيانات. يتم ذلك باستخدام صيغة "OFFSET" في الكود العيني:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

يمكنك محاولة تغيير الرقم "-5" إلى "-10" في الصيغة، وسوف يقوم الرسم الديناميكي بحساب أحدث 10 مجموعات من البيانات. الآن لقد قمنا بإنشاء رسم بياني متدحرج ديناميكي باستخدام Aspose.Cells بنجاح.
{{< app/cells/assistant language="cpp" >}}
