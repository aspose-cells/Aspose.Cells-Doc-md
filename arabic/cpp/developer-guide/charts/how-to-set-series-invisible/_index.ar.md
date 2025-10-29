---
title: كيفية جعل السلسلة غير مرئية باستخدام C++
linktitle: كيفية إخفاء سلسلة
description: في رسم بياني Excel، قد تحتاج إلى جعل السلسلة غير مرئية. يصف هذا المقال كيفية استخدام Aspose.Cells مع C++ للقيام بذلك.
keywords: رسم بياني Excel، سلسلة، غير مرئية، مُفلترة.
type: docs
weight: 74
url: /ar/cpp/how-to-set-series-invisible/
---

## كيفية إخفاء سلسلة في مخطط إكسل

في مخطط إكسل، يمكنك النقر بزر الماوس الأيمن على مخطط، ثم اختيار "تحديد البيانات"، وفي النافذة المنبثقة، يمكنك تحديد ما إذا كانت السلسلة مرئية عبر الاختيار أو إلغاء الاختيار. يمكنك تحميل [ملف النموذج](SeriesFiltered.xlsx) التالي واستخدامه في إكسل لتحقيق هذه الوظيفة، وسنشرح لاحقًا كيفية تحقيق ذلك باستخدام مكتبة Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## كيفية إخفاء سلسلة باستخدام Aspose.Cells 

نستخدم الكود التالي لإخفاء سلسلة باستخدام Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // File path for the input and output Excel files
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file
    Workbook workbook(filePath + u"SeriesFiltered.xlsx");

    // Access the charts collection of the first worksheet
    ChartCollection charts = workbook.GetWorksheets().Get(0).GetCharts();

    // Access a specific chart by name
    Chart chart = charts.Get(u"Chart 1");

    // Access filtered and non-filtered series collections
    SeriesCollection nSeriesFiltered = chart.GetFilteredNSeries();
    SeriesCollection nSeries = chart.GetNSeries();

    // Set the visibility of the first two series to be filtered
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Save the modified Excel file
    workbook.Save(filePath + u"output.xlsx");

    std::cout << "Series filtered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

يمكنك الحصول على الملف المدخل التالي [Input file](SeriesFiltered.xlsx) وملف الإخراج [output file](output.xlsx).

كما هو موضح في الشكل أدناه، السلسلتان الأوليان اللتان كانتا مرئيتين أصلاً، أصبحتا غير مرئيتين في ملف الإخراج.  
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="cpp" >}}
