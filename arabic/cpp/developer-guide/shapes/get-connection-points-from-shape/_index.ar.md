---
title: الحصول على نقاط الاتصال من الشكل باستخدام ++C
linktitle: الحصول على نقاط الاتصال من الشكل
type: docs
weight: 3500
url: /ar/cpp/get-connection-points-from-shape/
description: تعلم كيفية استرداد نقاط اتصال الشكل باستخدام Aspose.Cells for C++.
---

توفر Aspose.Cells ميزات غنية لإدارة الأشكال في جداول البيانات. أحيانًا هناك حاجة للحصول على نقاط الاتصال لشكل للمحاذاة أو التمركز. يمكن استخدام الكود التالي للحصول على قائمة بنقاط الاتصال لشكل باستخدام طريقة [Shape.GetConnectionPoints()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getconnectionpoints/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"sampleGetFonts.xlsx");

    Vector<Font> fonts = workbook.GetFonts();

    for (int i = 0; i < fonts.GetLength(); ++i)
    {
        std::cout << fonts[i].ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

.
{{< app/cells/assistant language="cpp" >}}
