---
title: كيفية إنشاء رسم بياني للتصفح التلقائي باستخدام C++
linktitle: إنشاء رسم بياني للتصفح التلقائي
description: تعلم كيفية إنشاء رسم بياني للتصفح التلقائي باستخدام Aspose.Cells for C++. دليل خطوة بخطوة سيظهر كيفية تنفيذ انتقالات بيانات سلسة والتصفح التلقائي في المخطط الخاص بك لعرض مستمر ومحدث.
keywords: Aspose.Cells for C++، رسم بياني للتصفح التلقائي، انتقالات البيانات، التصفح السلس، عرض مستمر، تحديث التصور.
type: docs
weight: 75
url: /ar/cpp/create-dynamic-scrolling-chart/
---

## **سيناريوهات الاستخدام المحتملة**
رسم بياني متدحرج ديناميكي هو نوع من التمثيل البياني المستخدم لعرض البيانات التي تتغير مع مرور الوقت. تم تصميمه لتوفير رؤية في الوقت الحقيقي للبيانات، مما يتيح للمستخدمين تتبع التحديثات المستمرة والاتجاهات. يقوم الرسم البياني بالتحديث بشكل مستمر كلما تمت إضافة بيانات جديدة، ويمرر تلقائيًا لعرض أحدث المعلومات.

يتم استخدام رسوم بيانية متدحرجة ديناميكية عادة في مختلف الصناعات، مثل التمويل، وتحليل سوق الأسهم، وتتبع الطقس، وتحليل وسائل التواصل الاجتماعي. إنها تمكن المستخدمين من تصور وتحليل أنماط البيانات واتخاذ قرارات مستنيرة استنادًا إلى المعلومات في الوقت الحقيقي.

عموما، تعتبر هذه الرسوم بيانية متدحرجة ديناميكية أدوات قيمة لمراقبة وتحليل البيانات الزمنية، وتسهيل اتخاذ القرارات في الوقت الحقيقي وتعزيز القدرات على تصور البيانات.

استخدام Aspose Cells لإنشاء رسم بياني ديناميكي متدحرج

## **استخدام Aspose Cells لإنشاء رسم بياني للتصفح التلقائي**
 في الفقرات التالية، سنوضح لك كيفية إنشاء رسم بياني للتصفح التلقائي باستخدام Aspose.Cells. سنعرض لك الكود للمثال، بالإضافة إلى الملف إكسل الذي تم إنشاؤه باستخدام هذا الكود.

## **الكود المثالي**
سينشئ الكود العينة التالي [ملف الرسم البياني الديناميكي المتدحرج](DynamicScrollingChart.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String localPath(u"");

    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Day");
    sheet.GetCells().Get(u"B1").PutValue(u"Sales");

    int allDays = 30;
    int showDays = 10;
    int currentDay = 1;

    Cells cells = sheet.GetCells();
    for (int i = 0; i < allDays; i++)
    {
        int row = i + 1;
        cells.Get(row, 0).PutValue(i + 1);
        cells.Get(row, 1).PutValue(50 * (i % 2) + 20 * (i % 3) + 10 * (i / 3));
    }

    sheet.GetCells().Get(u"G19").PutValue(u"Start Day");
    sheet.GetCells().Get(u"G20").PutValue(currentDay);
    sheet.GetCells().Get(u"H19").PutValue(u"Show Days");
    sheet.GetCells().Get(u"H20").PutValue(showDays);

    int index = sheets.GetNames().Add(u"Sheet1!ChtScrollData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    index = sheets.GetNames().Add(u"Sheet1!ChtScrollLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    ScrollBar bar = sheet.GetShapes().AddScrollBar(2, 0, 3, 0, 200, 30);
    bar.SetMin(0);
    bar.SetMax(allDays - showDays);
    bar.SetCurrentValue(currentDay);
    bar.SetLinkedCell(u"$G$20");

    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 2, 4, 15, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtScrollData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtScrollLabels");

    workbook.Save(localPath + u"DynamicScrollingChart.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **ملاحظات**
في الملف الذي تم إنشاؤه، يمكنك التشغيل على شريط التمرير، في حين يقوم الرسم البياني بحساب البيانات العشر مجموعات الأحدث تلقائيًا. يتم ذلك باستخدام صيغة "OFFSET" في الكود العينة:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

يمكنك محاولة تغيير الرقم "10" إلى "15" في خلية "Sheet1!$H$20"، وسيقوم الرسم الديناميكي بحساب أحدث 15 مجموعة من البيانات. الآن لدينا رسم بياني متدحرج ديناميكي باستخدام Aspose.Cells بنجاح.
