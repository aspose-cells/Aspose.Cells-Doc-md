---
title: تعطيل تصدير برامج الإطار وخصائص المستند مع C++
type: docs
weight: 310
url: /ar/cpp/disable-exporting-frame-scripts-and-document-properties/
description: تعطيل تصدير برامج الإطار وخصائص المستند باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يقوم Aspose.Cells بتصدير برامج الإطار وخصائص المستند أثناء تحويل دفتر العمل إلى HTML. الإصدار 8.6.0 من Aspose.Cells for C++ يوفر خيارًا يتيح لك تعطيل تصدير برامج الإطار وخصائص المستند بشكل اختياري. يرجى استخدام الخاصية HtmlSaveOptions.ExportFrameScriptsAndProperties لتعطيل التصدير.

{{% /alert %}}

## **تعطيل تصدير الإطارات النصية وخصائص المستند**

الشيفرة النموذجية التالية تتيح لك تعطيل تصدير الإطارات النصية وخصائص المستند. بمجرد تحويل دفتر العمل إلى HTML، لن يحتوي الملف الناتج على أي إطارات نصية أو خصائص مستند.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the required workbook to convert
    U16String inputFilePath = srcDir + u"Sample1.xlsx";
    Workbook workbook(inputFilePath);

    // Disable exporting frame scripts and document properties
    HtmlSaveOptions options;
    options.SetExportFrameScriptsAndProperties(false);

    // Save workbook as HTML
    workbook.Save(outDir + u"output.out.html", options);

    std::cout << "Workbook saved successfully as HTML!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
