---
title: تعطيل الالتفاف النصي لملصقات البيانات في المخطط باستخدام C++
linktitle: تعطيل الالتفاف النصي لملصقات البيانات
description: تعلم كيفية تعطيل التفاف النص لعناوين البيانات في الرسوم البيانية باستخدام Aspose.Cells for C++. سيرشدك دليلنا إلى كيفية منع تداخل العناوين الطويلة وتوفير عروض بيانية أكثر قابلية للقراءة والوضوح.
keywords: Aspose.Cells for C++، الرسوم البيانية، عناوين البيانات، التفاف النص، التداخل، قابلية القراءة، العروض.
type: docs
weight: 70
url: /ar/cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

يسمح Microsoft Excel 2013 للمستخدمين بتضمين أو عدم تضمين النص داخل تسميات البيانات في الرسم البياني. بشكل افتراضي، يكون النص داخل تسميات البيانات في الرسم البياني في حالة التضمين.

يوفر Aspose.Cells [**DataLabels.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/istextwrapped/) خاصية يمكنك تعيين True أو False لتمكين أو تعطيل تضمين النص بتسميات البيانات على التوالي.

{{% /alert %}}

يظهر النموذج العيني التالي كيفية تعطيل تضمين النص لتسميات البيانات في الرسم البياني.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Load the sample Excel file inside the workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Disable the Text Wrapping of Data Labels in all Series
    chart.GetNSeries().Get(0).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(1).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(2).GetDataLabels().SetIsTextWrapped(false);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Text wrapping disabled successfully in data labels!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
