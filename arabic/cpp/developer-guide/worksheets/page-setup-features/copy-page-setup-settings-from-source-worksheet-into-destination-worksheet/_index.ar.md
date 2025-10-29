---
title: نسخ إعدادات إعداد الصفحة من ورقة مصدر إلى ورقة هدف باستخدام C++
linktitle: نسخ إعدادات إعداد الصفحة
type: docs
weight: 80
url: /ar/cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: يشرح هذا المقال كيفية استخدام عينة الكود من API أو مكتبة C++ لنسخ إعدادات إعداد الصفحة من ورقة عمل المصدر إلى ورقة الهدف برمجياً.
keywords: نسخ إعدادات إعداد الصفحة بـ C++، نسخ إعدادات إعداد الصفحة إلى ورقة عمل الهدف بـ C++
---

## **سيناريوهات الاستخدام المحتملة**

عند إضافة ورقة جديدة إلى كتيب العمل، تحتوي على إعدادات إعداد الصفحة الافتراضية. قد تحتاج في بعض الأحيان إلى نقل الإعدادات ([**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)) من ورقة عمل واحدة إلى أخرى. توضح هذه الوثيقة كيفية نسخ إعدادات إعداد الصفحة من ورقة عمل واحدة إلى أخرى باستخدام واجهات برمجة التطبيقات Aspose.Cells.

## **نسخ إعدادات إعداد الصفحة من ورقة العمل المصدر إلى ورقة العمل الوجهة**

الشيفرة النموذجية التالية توضح كيفية نسخ إعدادات إعداد الصفحة من ورقة عمل واحدة إلى أخرى باستخدام طريقة [**PageSetup.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/copy/). يُرجى الاطلاع على الشيفرة النموذجية التالية وإخراجها إلى وحدة التحكم كمرجع.

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    wb.GetWorksheets().Add(u"TestSheet1");
    wb.GetWorksheets().Add(u"TestSheet2");

    Worksheet TestSheet1 = wb.GetWorksheets().Get(u"TestSheet1");
    Worksheet TestSheet2 = wb.GetWorksheets().Get(u"TestSheet2");

    TestSheet1.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3ExtraTransverse);

    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    CopyOptions copyOptions;
    TestSheet2.GetPageSetup().Copy(TestSheet1.GetPageSetup(), copyOptions);

    std::cout << "After Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "After Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
