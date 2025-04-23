---
title: احصل على النطاق مع روابط خارجية باستخدام C++
linktitle: الحصول على المدى مع الروابط الخارجية
type: docs
weight: 120
url: /ar/cpp/get-range-with-external-links/
description: تعلم كيفية استرداد النطاقات ذات الروابط الخارجية في ملفات Excel باستخدام Aspose.Cells مع C++.
---

## **الحصول على نطاق مع روابط خارجية**

كثيرًا ما تصل ملفات Excel إلى البيانات من ملفات أخرى باستخدام روابط خارجية. توفر Aspose.Cells خيار استرداد هذه الروابط الخارجية باستخدام طريقة [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/). ترجع طريقة [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) مصفوفة من النوع [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/). يوفر فئة [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) خاصية [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) التي تعيد اسم الملف الخارجي. تكشف فئة [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) عن الأعضاء التالية.

- [**GetEndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendcolumn/): عمود النهاية للمنطقة
- [**GetEndRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendrow/): الصف النهائي للمنطقة
- [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/): الحصول على اسم الملف الخارجي إذا كان هذا مرجع خارجي
- [**IsArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isarea/): يشير إلى ما إذا كان هذا منطقة
- [**IsExternalLink**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isexternallink/): يشير إلى ما إذا كان هذا ارتباط خارجي
- [**GetSheetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getsheetname/): يشير إلى الورقة التي يقع فيها هذا المرجع
- [**GetStartColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartcolumn/): العمود الابتدائي للمنطقة
- [**GetStartRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartrow/): صف البداية للمنطقة

يوضح رمز النموذج المقدم أدناه استخدام طريقة [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) للحصول على النطاقات ذات الروابط الخارجية.

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook workbook(srcDir + u"SampleExternalReferences.xlsx");

    WorksheetCollection sheets = workbook.GetWorksheets();
    NameCollection namedRanges = sheets.GetNames();

    for (int i = 0; i < namedRanges.GetCount(); ++i)
    {
        Name namedRange = namedRanges.Get(i);
        Vector<ReferredArea> referredAreas = namedRange.GetReferredAreas(true);

        if (!referredAreas.IsNull())
        {
            for (int j = 0; j < referredAreas.GetLength(); ++j)
            {
                ReferredArea referredArea = referredAreas[j];
                std::cout << "IsExternalLink: " << referredArea.IsExternalLink() << std::endl;
                std::cout << "IsArea: " << referredArea.IsArea() << std::endl;
                std::cout << "SheetName: " << referredArea.GetSheetName().ToUtf8() << std::endl;
                std::cout << "ExternalFileName: " << referredArea.GetExternalFileName().ToUtf8() << std::endl;
                std::cout << "StartColumn: " << referredArea.GetStartColumn() << std::endl;
                std::cout << "StartRow: " << referredArea.GetStartRow() << std::endl;
                std::cout << "EndColumn: " << referredArea.GetEndColumn() << std::endl;
                std::cout << "EndRow: " << referredArea.GetEndRow() << std::endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
