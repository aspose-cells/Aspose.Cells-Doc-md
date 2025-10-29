---
title: إكسل إلى HTML  استخدم خيار تفضيل العرض لتحسين التصميم مع C++
linktitle: Excel to HTML  استخدام خيار PresentationPreference لتحسين التخطيط
type: docs
weight: 220
url: /ar/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
description: تعلم كيف render تصميم أفضل عند حفظ ملفات Excel في HTML باستخدام C++.
---

{{% alert color="primary" %}} 

 توفر Aspose.Cells خاصية HtmlSaveOptions.PresentationPreference المفيدة للمطورين الذين يحتاجون إلى عرض تخطيط أفضل عند حفظ ملف Microsoft Excel إلى تنسيق HTML أو MHT. القيمة الافتراضية للخاصية هي false. نوصي بتعيين هذه الخاصية إلى true للحصول على عرض مقبول أكثر للتقارير من Excel.

{{% /alert %}} 

يرجى الرجوع إلى الشيفرة النموذجية أدناه التي توضح كيفية عرض ملف HTML من تقرير Excel بتفضيل العرض.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Instantiate the Workbook and load an Excel file
    Workbook workbook(inputFilePath);

    // Create HtmlSaveOptions object
    HtmlSaveOptions options;

    // Set the Presentation preference option
    options.SetPresentationPreference(true);

    // Save the Excel file to HTML with specified option
    U16String outputFilePath = srcDir + u"outPresentationlayout1.out.html";
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file saved as HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
