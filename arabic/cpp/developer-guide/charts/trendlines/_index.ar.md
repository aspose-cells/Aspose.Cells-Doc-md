---
title: الحصول على نص المعادلة لاتجاه خط الاتجاه في الرسم البياني باستخدام C++
linktitle: خطوط الاتجاه
description: تعلم كيفية استخدام Aspose.Cells for C++ لاسترجاع نص المعادلة لخط الاتجاه في رسم بياني تم إنشاؤه في Microsoft Excel. ستوضح أدلتنا كيفية الوصول إلى واستخراج معادلة خط الاتجاه لمزيد من التحليل أو العرض.
keywords: Aspose.Cells for C++، خط اتجاه الرسم البياني، نص المعادلة، Microsoft Excel، تحليل البيانات، العرض.
type: docs
weight: 110
url: /ar/cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

يمكنك استرجاع نص المعادلة لخط اتجاه الرسم البياني باستخدام Aspose.Cells. توفر Aspose.Cells الواجهة البرمجية للتطبيقات [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) التي تُرجع نص المعادلة لخط اتجاه الرسم البياني. لاستخدام هذه الواجهة البرمجية، سيلزمك أولاً استدعاء الطريقة [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/).

{{% /alert %}}

يعرض لقطة الشاشة التالية المخطط مع خط اتجاه والنص المعادلة الخاص به مرئي باللون الأحمر. سنسترجع هذا النص باستخدام الخاصية [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) في الكود التالي.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## كود C++ للحصول على نص معادلة خط الاتجاه في الرسم البياني

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

    // Create workbook object from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Calculate the Chart first to get the Equation Text of Trendline
    chart.Calculate();

    // Access the Trendline
    Trendline trendLine = chart.GetNSeries().Get(0).GetTrendLines().Get(0);

    // Read the Equation Text of Trendline
    std::cout << "Equation Text: " << trendLine.GetDataLabels().GetText().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## الإخراج الذي تم توليده بواسطة رمز العينة

هذا هو إنتاج الكونسول للكود العيني أعلاه.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
