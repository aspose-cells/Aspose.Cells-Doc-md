---
title: الحصول على مجموعات الرموز، أشرطة البيانات أو كائنات مقياس الألوان المستخدمة في التنسيق الشرطي باستخدام C++
linktitle: حصل على مجموعات الأيقونات أو أشرطة البيانات أو كائنات مقاييس الألوان
description: Aspose.Cells for C++ مكتبة للعمل مع ملفات جداول البيانات. تدعم استخدام مجموعات الأيقونات، وأشرطة البيانات، والكائنات ذات مقياس الألوان في التنسيق الشرطي لعرض البيانات من جداول البيانات. يوضح هذا المقال كيفية استخدام مكتبة Aspose.Cells لاسترجاع البيانات لهذه الكائنات.
keywords: Aspose.Cells، التنسيق الشرطي، مجموعات الرموز، شريط بيانات، مقياس اللون، جدول بيانات
type: docs
weight: 10
url: /ar/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}} 

أحيانًا، تحتاج إلى استرجاع مجموعات الأيقونات المستخدمة في التنسيق الشرطي لخلية أو مجموعة خلايا وترغب في إنشاء ملف صورة بناءً عليها. قد يتطلب الأمر قراءة أشرطة البيانات أو مقاييس الألوان المستخدمة في التنسيق الشرطي. يدعم Aspose.Cells for C++ هذه الميزة.

{{% /alert %}} 

يظهر نموذج الشفرة التالي كيفية قراءة مجموعات الأيقونات المستخدمة للتنسيق الشرطي. بواسطة واجهة برمجة التطبيقات البسيطة لـ Aspose.Cells، يتم حفظ بيانات صورة مجموعة الأيقونات كصورة.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell cell = sheet.GetCells().Get(u"A1");

    // Get the conditional formatting result object
    ConditionalFormattingResult cfr = cell.GetConditionalFormattingResult();

    // Get the icon set
    ConditionalFormattingIcon icon = cfr.GetConditionalFormattingIcon();

    // Get the image data from the icon
    Vector<uint8_t> imageData = icon.GetImageData();

    // Create the image file based on the icon's image data
    ofstream outputFile((outDir + u"imgIcon.out.jpg").ToUtf8(), ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Icon image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
