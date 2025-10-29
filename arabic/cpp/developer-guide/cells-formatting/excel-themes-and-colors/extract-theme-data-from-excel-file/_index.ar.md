---
title: استخراج بيانات السمة من ملف إكسل باستخدام C++
linktitle: استخراج بيانات النسق من ملف Excel
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جداول البيانات. تدعم استخراج بيانات السمة من ملفات Excel، مما يتيح للمستخدمين الحصول على معلومات النمط والتنسيق للمستندات. يقدم هذا المقال مقدمة لكيفية استخراج بيانات السمة من ملفات Excel باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells، ملف Excel، بيانات الموضوع، نمط، تنسيق
type: docs
weight: 120
url: /ar/cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

يسمح Aspose.Cells للمستخدمين باستخراج البيانات المتعلقة بالسمة من ملف Excel. على سبيل المثال، يمكنك استخراج اسم السمة المطبقة على دفتر العمل ولون السمة المطبقة على خلية أو حدود الخلية، إلخ.

يمكنك تطبيق سمة على دفتر العمل الخاص بك باستخدام Microsoft Excel عبر أمر تخطيط الصفحة > السمات.

{{% /alert %}}

## كود C++ لاستخراج بيانات السمة من ملف Excel

يستخرج نموذج الشفرة التالي اسم السمة المطبق على دفتر العمل المصدر ثم يستخرج لون السمة المطبقة على الخلية A1 ولون السمة المطبقة على الحد السفلي للخلية.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Extract theme name applied to this workbook
    std::cout << "Theme: " << workbook.GetTheme().ToUtf8() << std::endl;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Get the style object
    Style style = cell.GetStyle();

    // Check if theme has foreground color defined
    if (style.GetForegroundThemeColor().IsNull())
    {
        std::cout << "Theme has not foreground color defined." << std::endl;
    }
    else
    {
        // Extract theme color applied to this cell
        std::cout << "Foreground Theme Color Type: " << static_cast<int>(style.GetForegroundThemeColor().GetColorType()) << std::endl;
    }

    // Extract theme color applied to the bottom border of the cell
    Border bot = style.GetBorders().Get(BorderType::BottomBorder);
    if (bot.GetThemeColor().IsNull())
    {
        std::cout << "Theme has not Border color defined." << std::endl;
    }
    else
    {
        std::cout << "Border Theme Color Type: " << static_cast<int>(bot.GetThemeColor().GetColorType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
