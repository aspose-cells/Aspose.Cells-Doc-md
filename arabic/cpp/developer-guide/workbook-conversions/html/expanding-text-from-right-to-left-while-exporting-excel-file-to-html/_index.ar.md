---
title: توسيع النص من اليمين إلى اليسار أثناء تصدير ملف Excel إلى HTML باستخدام C++
linktitle: توسيع النص من اليمين إلى اليسار أثناء تصدير ملف Excel إلى HTML
type: docs
weight: 60
url: /ar/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
description: تعلم كيف تقوم بتوسيع النص من اليمين إلى اليسار أثناء تصدير ملفات Excel إلى HTML باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

 يدعم Aspose.Cells for C++ الآن توسيع النص من اليمين إلى اليسار أثناء تصدير ملفات Excel إلى HTML. تم تنفيذ هذه الميزة منذ الإصدار v8.9.0.0. إذا كان ملف Excel المصدر الخاص بك يحتوي على أي نص يتوسع من اليمين إلى اليسار، فستقوم Aspose.Cells بتصديره إلى HTML بشكل صحيح.

{{% /alert %}} 

## **توسيع النص من اليمين إلى اليسار أثناء تصدير ملف Excel إلى HTML**

 الكود النموذجي التالي يحول ملف Excel العيني إلى HTML. يُظهر هذا الصورة كيف يبدو ملف Excel في Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

 تُظهر هذه الصورة كيف تبدو [HTML الناتج المولد مع الإصدار الأقدم](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

 تُظهر هذه الصورة كيف يبدو [HTML الناتج المولد مع الإصدار الأحدث](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

كما يتضح في الصور، يقوم الإصدار الأحدث بتوسيع النص المسند إلى اليمين إلى اليسار بشكل صحيح، تمامًا مثل Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source excel file inside the workbook object
    Workbook wb(srcDir + u"sample.xlsx");

    // Save workbook in html format
    U16String outputPath = srcDir + u"ExpandTextFromRightToLeft_out_" + CellsHelper::GetVersion() + u".html";
    wb.Save(outputPath, SaveFormat::Html);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
