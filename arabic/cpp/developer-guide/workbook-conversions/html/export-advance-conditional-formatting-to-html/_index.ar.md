---
title: تصدير تنسيق الشرط DataBar و ColorScale و IconSet أثناء تحويل Excel إلى HTML باستخدام C++
linktitle: تصدير التنسيق الشرطي إلى HTML
type: docs
weight: 30
url: /ar/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
description: تعلم كيفية تصدير تنسيق الشرطي DataBar و ColorScale و IconSet أثناء تحويل ملفات Excel إلى HTML باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

 يمكنك تصدير تنسيق الشرطي DataBar و ColorScale و IconSet عند تحويل ملف Excel الخاص بك إلى HTML. تدعم Microsoft Excel جزئياً هذه الميزة لكن Aspose.Cells for C++ يدعمها بالكامل.

{{% /alert %}} 

## **تصدير تنسيق الشرطي DataBar و ColorScale و IconSet أثناء تحويل Excel إلى HTML**
يُظهر الصورة أدناه [ملف Excel العيني](5115558.xlsx) مع تنسيق الشرطي DataBar و ColorScale و IconSet. يمكنك تحميل [ملف Excel العيني](5115558.xlsx) من الرابط المقدم.

![todo:image_alt_text](conversion_1.png)

تُظهر الصورة أدناه ملف HTML الناتج من Aspose.Cells مع تنسيق الشرطي DataBar و ColorScale و IconSet. كما ترى، يبدو مطابقًا تمامًا لـ [ملف Excel العيني](5115558.xlsx).

![todo:image_alt_text](conversion_2.png)

### **الكود المثالي**
الكود النموذجي التالي يحول ملف Excel العيني إلى HTML، وهو مجرد تحويل عادي [إكسل إلى HTML](/cells/ar/cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).

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

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Load your sample excel file in a workbook object
    Workbook wb(filePath);

    // Save it in HTML format
    wb.Save(outDir + u"ConvertingToHTMLFiles_out.html", SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
