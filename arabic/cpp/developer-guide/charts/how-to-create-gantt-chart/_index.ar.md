---
title: كيفية إنشاء رسم بياني جانت باستخدام C++
linktitle: كيفية إنشاء مخطط جانت
type: docs
weight: 72
url: /ar/cpp/how-to-create-gantt-chart/
description: تعلم كيفية إنشاء رسم جانت باستخدام واجهة برمجة تطبيقات Aspose.Cells for C++.
keywords: إنشاء رسم جانت باستخدام C++، إضافة رسم جانت، إدراج رسم جانت
---

## **ما هو مخطط جانت**

مخطط جانت هو نوع من مخططات الأعمدة يوضح جدول مشروع. يُظهر تواريخ بدء وانتهاء عناصر المشروع المختلفة. يمثل كل مهمة أو نشاط بواسطة عمود، وطوله يتوافق مع مدته. تشير مخططات جانت أيضًا إلى الاعتماديات بين المهام، مما يسمح لمديري المشاريع برؤية التسلسل الذي يجب إكمال المهام فيه. تستخدم على نطاق واسع في إدارة المشاريع لتخطيط، جدولة، وتتبع المشاريع بشكل فعال.

## **كيفية إنشاء مخطط جانت في إكسل**

يمكنك إنشاء مخطط جانت في إكسل باتباع هذه الخطوات:
1. إضافة بعض البيانات لمخطط جانت. 
<br>
<img src="00.png" width=50% />
1. اختر البيانات واذهب إلى إدراج --> مخططات --> إدراج مخطط عمود أو مخطط أعمدة --> مخطط الأعمدة المجمعة. في مثالنا، هو B1:B7، ثم إدراج مخطط **مخطط أعمدة مجمعة**.
<br>
<img src="1.png" width=50% />

1. اختر الرسم البياني، **اختيار البيانات**->**إضافة**، عيّن **اسم السلسلة** و**قيم السلسلة** كما يلي.
<br>
<img src="2.png" width=50% />

1. اختر المخطط، عدل **محور البيانات الأفقي (الفئة)**.
<br>
<img src="3.png" width=50% />

1. **تنسيق المحور** للمحور الصادي، حدد **الفئات بترتيب عكسي**.
1. حدد **السلسلة الزرقاء** وعيّن **الملء->لا تعبئة**.
1. **تشكيل المحور** محور X، عيّن **القيمة الدنيا والقصوى** (1/5/2019:43470، 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **إضافة تسميات البيانات** للمخطط، الآن ستحصل على مخطط جانت.
<br>
<img src="0.png" width=50% />


## **كيفية إضافة مخطط جانت في Aspose.Cells**
يرجى مراجعة رمز العينة التالي. يقوم بتحميل ملف إكسل عينة ([sample.xlsx](sample.xlsx)) الذي يحتوي على بعض البيانات النموذجية. ثم ينشئ مخطط الأعمدة المجمعة استنادًا إلى البيانات الأولية ويحدد الخصائص ذات الصلة. في النهاية، يحفظ ملف العمل بصيغة XLSX الناتجة ([result.xlsx](result.xlsx)). تُظهر لقطة الشاشة التالية مخطط جانت الذي أنشأته Aspose.Cells في ملف الإكسل الناتج.
<br>
<img src="5.png" width=60% />

### **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create BarStacked Chart
    int32_t chartIndex = worksheet.GetCharts().Add(ChartType::BarStacked, 5, 6, 20, 15);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Set the chart title name
    chart.GetTitle().SetText(u"Gantt Chart");

    // Set the chart title visibility
    chart.GetTitle().SetIsVisible(true);

    // Set data range
    chart.SetChartDataRange(u"B1:B6", true);

    // Add series data range
    chart.GetNSeries().Add(u"C2:C6", true);

    // No fill for one series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set the Horizontal(Category) Axis
    chart.GetNSeries().SetCategoryData(u"A2:A6");

    // Reverse the Horizontal(Category) Axis
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set the value axis's MinValue and MaxValue
    chart.GetValueAxis().SetMinValue(worksheet.GetCells().Get(u"B2").GetValue());
    chart.GetValueAxis().SetMaxValue(worksheet.GetCells().Get(u"D6").GetValue());

    // Set the PlotArea with no fill
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Show the DataLabels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowValue(true);

    // Disable the Legend
    chart.SetShowLegend(false);

    // Save the result
    workbook.Save(u"result.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
