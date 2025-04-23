---
title: تحديد نوع القيم X وY لنقاط سلسلة المخططات باستخدام C++
linktitle: البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني
description: تعلم كيف تحدد نوع القيم X وY في نقاط سلسلة المخططات باستخدام Aspose.Cells for C++. دليلنا سيشرح أنواع قيم البيانات المختلفة ويعرض كيفية الوصول إليها والعمل معها في مخططاتك.
keywords: Aspose.Cells for C++، رسم بياني، قيم X، قيم Y، أنواع البيانات، الوصول، العمل بها، سلسلة المخططات.
type: docs
weight: 150
url: /ar/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا، تريد معرفة نوع القيم X وY لنقاط مخطط في سلسلة. يوفر Aspose.Cells طريقتي `ChartPoint::get_XValueType` و `ChartPoint::get_YValueType` لهذا الغرض. يرجى ملاحظة أنه من الضروري استدعاء `Chart::Calculate()` قبل استخدام هذه الخصائص بشكل فعال.

## **البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني**
الكود النموذجي التالي يحمّل ملف Excel [عينة](64716905.xlsx) ويصل إلى المخطط الأول داخل ورقة العمل الأولى. ثم يستدعي `Chart::Calculate()` ويحدد نوع القيم X وY لنقطة المخطط الأولى ويطبعها على وحدة التحكم. الرجاء مراجعة مخرجات وحدة التحكم أدناه كمرجع.

## **الكود المثالي**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file containing chart
    Workbook wb(srcDir + u"sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = ws.GetCharts().Get(0);

    // Calculate chart data
    ch.Calculate();

    // Access first chart point in the first series
    ChartPoint pnt = ch.GetNSeries().Get(0).GetPoints().Get(0);

    // Print the types of X and Y values of chart point
    std::cout << "X Value Type: " << static_cast<int>(pnt.GetXValueType()) << std::endl;
    std::cout << "Y Value Type: " << static_cast<int>(pnt.GetYValueType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
