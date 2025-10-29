---
title: تحميل ملف Excel المصدر بدون رسومات بيانية باستخدام C++
linktitle: تحميل ملف Excel المصدر بدون رسوم بيانية
type: docs
weight: 420
url: /ar/cpp/load-source-excel-file-without-charts/
description: تعلم كيفية تحميل ملف Excel بدون رسومات بيانية باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يسمح Aspose.Cells لك بتحميل ملف Excel الخاص بك بدون مخططات. يرجى استخدام الخاصية [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) لهذا الغرض.

{{% /alert %}}

## **تحميل جدول بيانات بدون رسوم بيانية**

يقوم الكود النموذجي التالي بتحميل ملف Excel النموذجي بدون مخططات وحفظه بتنسيق PDF الناتج.

```c++
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

    // Specify the load options and filter the data
    LoadOptions options;

    // Include everything except charts
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xlsx";

    // Load the workbook with specified load options
    Workbook workbook(inputFilePath, options);

    // Path of output PDF file
    U16String outputFilePath = outDir + u"ResultWithoutChart.pdf";

    // Save the workbook in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully without charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
