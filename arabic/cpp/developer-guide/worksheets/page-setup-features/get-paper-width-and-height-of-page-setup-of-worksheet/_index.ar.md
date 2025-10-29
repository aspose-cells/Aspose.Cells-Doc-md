---
title: الحصول على عرض وارتفاع الورق لإعداد الصفحة في ورقة العمل باستخدام C++
linktitle: الحصول على عرض وارتفاع الورق لإعداد الصفحة
type: docs
weight: 50
url: /ar/cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: تعلم كيف تحصل على عرض وارتفاع الورق في إعداد صفحة ورقة العمل باستخدام كود C++ برمجيًا بواسطة API Aspose.Cells for C++.
keywords: عرض الورق في إعداد الصفحة في Excel باستخدام C++، ارتفاع الورق في إعداد الصفحة في Excel باستخدام C++
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا، تحتاج إلى معرفة عرض وارتفاع حجم الورق كما تم تعيينه في إعداد الصفحة للورقة العمل. يرجى استخدام طريقتي [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) و [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/) لهذا الغرض.

## **الحصول على عرض وارتفاع الورق لإعداد الصفحة لورقة العمل**

يوضح الكود النموذجي التالي استخدام طريقتي [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) و [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/). يغير أولاً حجم الورق إلى *A2* ثم يحدد عرض وارتفاع الورق، ثم يغيره إلى *A3*، *A4*، *Letter* ويحدد عرض وارتفاع الورق على التوالي.

### **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook class
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set paper size to A2 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA2);
    cout << "PaperA2: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A3 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3);
    cout << "PaperA3: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A4 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);
    cout << "PaperA4: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to Letter and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperLetter);
    cout << "PaperLetter: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **مخرجات الوحدة**

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
