---
title: قراءة عنوان فرعي للرسم البياني من ملف ODS باستخدام C++
linktitle: قراءة عنوان المخطط من ملف ODS
description: تعلم كيف تستخدم Aspose.Cells for C++ لقراءة العنوان الفرعي للرسم البياني من ملف جدول بيانات OpenDocument (ODS). سيُظهر دليلنا كيف تستخرج وتصل إلى العنوان الفرعي للرسم البياني لمزيد من التحليل أو العرض.
keywords: Aspose.Cells for C++، قراءة عنوان فرعي للرسم البياني، جدول بيانات OpenDocument، ملف ODS، استخراج الرسم البياني، تحليل البيانات.
type: docs
weight: 160
url: /ar/cpp/read-chart-subtitle-from-ods-file/
---

## **قراءة عنوان الرسم البياني من ملف ODS**

توفر Aspose.Cells لك القدرة على قراءة عناوين الرسوم البيانية في ملفات ODS باستخدام خاصية [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/). يقوم الكود العيني التالي بتحميل [ملف ODS نموذجي](89620481.ods) وقراءة عنوان الرسم البياني باستخدام خاصية [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/) وطباعته في نافذة الكونسول. يرجى الرجوع إلى مخرجات الكونسول المعروضة أدناه للإشارة.

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load excel file containing charts
    Workbook workbook(srcDir + u"SampleChart.ods");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Print chart subtitle
    cout << "Chart Subtitle: " << chart.GetSubTitle().GetText().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
