---
title: عرض نطاق الخلايا كتسميات البيانات باستخدام ++C
linktitle: عرض نطاق الخلية كعلامات البيانات
description: تعلم كيفية عرض نطاق من الخلايا كتسميات البيانات في المخططات باستخدام Aspose.Cells for C++. ستوضح دليلتنا كيفية ربط التسميات بمصدر البيانات الخاص بك وتنسيقها لتوفير معلومات دقيقة وذات معنى في رسومك البيانية.
keywords: Aspose.Cells for C++، التخطيط، تسميات البيانات، نطاق الخلايا، مصدر البيانات، التنسيق، الدقة، المعلومات ذات المعنى.
type: docs
weight: 130
url: /ar/cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

في Microsoft Excel 2013، يمكنك عرض نطاق الخلية لتسميات البيانات. يدعم Aspose.Cells هذه الميزة.

{{% /alert %}}

## **علامة اختيار لعرض نطاق الخلايا كتسميات بيانات**

لعرض نطاق الخلايا كتسميات بيانات في Microsoft Excel:

1. حدد تسميات بيانات السلسلة وانقر بزر الماوس الأيمن لفتح القائمة المنسدلة.
1. حدد **تنسيق تسميات البيانات**. تعرض خيارات التسميات.
1. حدد أو قم بمسح الخيار **تحتوي التسمية على - قيمة من الخلايا**.

الشفرة التالية تصل إلى بيانات تسميات سلسلة الرسم البياني وتحدد الخاصية [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/getshowcellrange/) إلى **true** لتحديد الخيار **التسمية تحتوي - القيمة من الخلايا**.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook from the source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Check the "Label Contains - Value From Cells"
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();
    dataLabels.SetShowCellRange(true);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
