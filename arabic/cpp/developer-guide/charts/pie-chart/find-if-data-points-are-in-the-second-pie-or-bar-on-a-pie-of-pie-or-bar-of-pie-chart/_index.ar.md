---
title: اكتشف إذا كانت نقاط البيانات في الفطيرة الثانية أو العمود على رسم بياني من نوع فطيرة من فطيرة أو رسم بياني من نوع عمود في فطيرة باستخدام C++
linktitle: العثور على ما إذا كانت نقاط البيانات في الرسم البياني الدائري الثاني أو الرسم البياني الشريطي الثاني
description: تعلم كيفية استخدام Aspose.Cells for C++ للعثور على ما إذا كانت نقاط البيانات في الفطيرة الثانية أو العمود على رسم بياني من نوع فطيرة من فطيرة أو رسم بياني من نوع عمود في فطيرة. سيُظهر دليلنا كيفية التعرف على والوصول إلى الفطيرة أو العامود الثانوي على رسم بياني مركب، مما يتيح لك تحليل البيانات ومعالجتها بفعالية.
keywords: Aspose.Cells for C++، رسم بياني من نوع فطيرة من فطيرة، رسم بياني من نوع عمود من فطيرة، فطيرة ثانوية، عمود ثانوي، تحليل البيانات، معالجة البيانات.
type: docs
weight: 180
url: /ar/cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **سيناريوهات الاستخدام المحتملة**
 يمكنك معرفة ما إذا كانت نقاط بيانات السلسلة في الفطيرة الثانية على رسم بياني *فطيرة من فطيرة* أو في العمود على رسم بياني *عمود من فطيرة* باستخدام Aspose.Cells. يرجى استخدام الخاصية [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) لتحديد ذلك.

يرجى تنزيل [ملف إكسل نموذجي](5115193.xlsx) المستخدم في رمز العينة أدناه ورؤية الإخراج من وحدة التحكم الخاصة به. إذا فتحت [ملف إكسل العيني](5115193.xlsx)، ستجد، أن جميع نقاط البيانات التي تقل عن 10 داخل الشريط *شريطي* على رسم بياني من الدائرة الدائرية كما يظهر أيضًا في إخراج وحدة التحكم.

## **العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'**
يوضح الكود المثالي التالي كيفية العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"PieBars.xlsx";
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Chart chart = worksheet.GetCharts().Get(0);
    chart.Calculate();

    Series series = chart.GetNSeries().Get(0);

    int pointCount = series.GetPoints().GetCount();
    for (int i = 0; i < pointCount; ++i)
    {
        ChartPoint chartPoint = series.GetPoints().Get(i);

        if (chartPoint.Get_YValue().IsNull())
            continue;

        std::cout << "Value: " << chartPoint.Get_YValue().ToDouble() << std::endl;
        std::cout << "IsInSecondaryPlot: " << (chartPoint.IsInSecondaryPlot() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**
يرجى الاطلاع على مخرجات وحدة التحكم التالية التي تم إنشاؤها بعد تنفيذ رمز العينة أعلاه مع ملف Excel التجريبي ([ملفExcel عينة](5115193.xlsx)). إذا كانت [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) **غير صحيحة**، فإن نقطة البيانات تقع داخل الفطيرة أو إذا كانت **صحيحة**، فإن نقطة البيانات تقع داخل العمود.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
