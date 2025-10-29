---
title: تحديد أي محور موجود في الرسم البياني باستخدام C++
description: تعلم كيفية تحديد أي محور موجود في رسم بياني تم إنشاؤه باستخدام Aspose.Cells for C++. سيساعدك دليلنا على فهم كيفية التعرف على والوصول إلى المحاور المختلفة في الرسم، بما في ذلك الفئة، القيمة، والمحاور الثانوية.
keywords: Aspose.Cells for C++، رسم بياني، محور، الوجود، الفئة، القيمة، الثانوي.
type: docs
weight: 140
url: /ar/cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

أحيانًا، يحتاج المستخدم إلى معرفة ما إذا كان محور معين موجود في المخطط أم لا. على سبيل المثال، يريد معرفة ما إذا كان محور القيم الثانوي موجود داخل المخطط أم لا. بعض المخططات مثل الكعكة، الكعكة المنفوخة، البيتزا، البيتزا المكدسة، الثلاثي الكعكة، الثلاثي المنفوخ، الدونات، الدونات المنفوخة، إلخ، لا تحتوي على محور.

توفر Aspose.Cells [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/) لتحديد ما إذا كان لدى المخطط محور معين أم لا.

{{% /alert %}}

 يوضح الكود التالي استخدام [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/) لتحديد ما إذا كان الرسم البياني التجريبي يحتوي على محور فئة وقيمة أساسي وثانوي.

## كود C++ لتحديد أي محور موجود في الرسم البياني

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart
    Chart chart = worksheet.GetCharts().Get(0);

    // Determine which axis exists in the chart
    bool ret = chart.HasAxis(AxisType::Category, true);
    std::wcout << u"Has Primary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Category, false);
    std::wcout << u"Has Secondary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, true);
    std::wcout << u"Has Primary Value Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, false);
    std::wcout << u"Has Secondary Value Axis: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

## الناتج على واجهة الأوامر الناتجة عن الكود المثال

تم عرض إخراج وحدة التحكم للشفرة أدناه التي تعرض القيمة الصحيحة للفئة الأساسية ومحور القيمة والقيمة الخاطئة للفئة الثانوية ومحور القيمة.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
