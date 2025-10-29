---
title: اكتشاف نوع الرابط التشعبي باستخدام C++
linktitle: اكتشاف نوع الرابط الفائق
type: docs
weight: 160
url: /ar/cpp/detect-hyperlink-type/
description: تعلم كيفية اكتشاف نوع الرابط التشعبي من خلال API Aspose.Cells for C++.
keywords: اكتشاف نوع الروابط التشعبية, كشف نوع الروابط التشعبية, الحصول على نوع الروابط التشعبية
---

## **كشف نوع الروابط التشعبية**

يمكن أن يحتوي ملف إكسل على أنواع مختلفة من الرابط الشعبي مثل الرابط الخارجي، مرجع الخلية، مسار الملف، الخ. Aspose.Cells تدعم ميزة كشف نوع الرابط. تتمثل أنواع الروابط التشعبية في تقديم فئة  [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) زمرة التعداد. تحتوي فئة التعداد  [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) على الأعضاء التالية.

- الخارجي: رابط خارجي
- مسار الشكل: مسار ملف\مجلد محلي بالكامل.
- البريد الإلكتروني: بريد إلكتروني
- مرجع الخلية: ربط الخلية أو النطاق المسمى.

للتحقق من نوع الرابط التشعبي، توفر فئة  [**Hyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/) خاصية  [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) بنوع العود. الشيفة النصية التالية توضح استخدام خاصية  [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) عن طريق استخدام هذا الملف  [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) مثلاً.

### كود المصدر

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"LinkTypes.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    if (!worksheet)
    {
        std::cerr << "Worksheet not found!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Range range = worksheet.GetCells().CreateRange(u"A1", u"A7");
    if (!range)
    {
        std::cerr << "Range creation failed!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();


    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink link = hyperlinks[i];
        if (link)
        {
            std::cout << link.GetTextToDisplay().ToUtf8() << ": "
                << static_cast<int>(link.GetLinkType()) << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

الناتج التالي الذي تم إنشاؤه بواسطة مقتطف الكود أعلاه.

### إخراج الكونسول
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
{{< app/cells/assistant language="cpp" >}}
