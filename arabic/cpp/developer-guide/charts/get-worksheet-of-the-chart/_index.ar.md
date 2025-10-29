---
title: الحصول على ورقة العمل للمخطط باستخدام ++C
linktitle: الحصول على ورقة البيانات للشارت
description: تعلم كيفية استرجاع ورقة العمل المرتبطة بمخطط Excel باستخدام Aspose.Cells for C++. سيُظهر لك دليلنا كيفية الوصول إلى ورقة العمل وتنفيذ العمليات عليها للتلاعب بالبيانات الأساسية للمخطط.
keywords: Aspose.Cells for C++، مخططات Excel، أوراق العمل، ت Manipulation البيانات، البيانات الأساسية، العمليات.
type: docs
weight: 1000
url: /ar/cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

 أحيانًا، تريد الوصول إلى ورقة عمل من مرجع مخطط. توفر Aspose.Cells الطريقة [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) التي ترجع مرجع ورقة العمل التي تحتوي على المخطط.

{{% /alert %}}

 يُوضح المثال التالي كيفية استخدام طريقة [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/). يطبع الكود أولًا اسم ورقة العمل، ثم يصل إلى أول مخطط على ورقة العمل. ثم يطبع اسم ورقة العمل مرة أخرى، باستخدام الطريقة [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/).

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

    // Create workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print worksheet name
    cout << "Sheet Name: " << worksheet.GetName().ToUtf8() << endl;

    // Access the first chart inside this worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the chart's sheet and display its name again
    cout << "Chart's Sheet Name: " << chart.GetWorksheet().GetName().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

أدناه نتيجة الإخراج على الشاشة التي يؤدي إليها الكود المثالي. كما يمكنك رؤية، فإنه يطبع اسم الورقة نفسه بكلتا المرتين.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
