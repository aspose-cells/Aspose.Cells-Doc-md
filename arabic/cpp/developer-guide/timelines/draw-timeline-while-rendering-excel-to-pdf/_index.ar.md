---
title: رسم جدول زمني أثناء تصدير Excel إلى PDF باستخدام C++
linktitle: رسم الجدول الزمني أثناء تحويل إكسيل إلى PDF
type: docs
weight: 60
url: /ar/cpp/draw-timeline-while-rendering-excel-to-pdf/
description: إدارة الجداول الزمنية لملفات Excel باستخدام Aspose.Cells مع C++.
keywords: تحويل الجدول الزمني إلى PDF بدون Office 2013، Office 2016، Office 2019 وOffice 365
---

## **رسم الجدول الزمني أثناء تحويل Excel إلى PDF**
إذا كان لديك ملف Excel يحتوي على جدول زمني مطبق وتريد تصديره إلى PDF مع إعدادات الجدول الزمني، يدعم Aspose.Cells الآن ذلك بشكل افتراضي. ببساطة، صدر ملف Excel مع جدول زمني إلى PDF، وسيعرض PDF الناتج الجدول الزمني المطبق.

الكود النموذجي التالي يحمل [ملف Excel عيني](input.xlsx) الذي يحتوي على جدول زمني موجود. ثم يحفظ المصنف كـ [ملف PDF الناتج](out.pdf). اللقطة الشاشية التالية تقارن ملف Excel المصدر بالملف PDF المعدل.

<img src="out.png" width="60%">

## **الكود المثالي**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath(u"input.xlsx");
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Save file to pdf
    U16String outputFilePath(u"out.pdf");
    wb->Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <aspose.cells.h>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();
    // Load the sample Excel file
    Workbook workbook(u"input.xlsx");

    // Save the workbook as a PDF file
    workbook.Save(u"output.pdf", SaveFormat::Pdf);
    Aspose::Cells::Cleanup();
    return 0;

}
```

{{< app/cells/assistant language="cpp" >}}
