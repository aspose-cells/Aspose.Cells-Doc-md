---
title: إيجاد الموقع المطلق للشكل داخل ورقة العمل باستخدام ++C
linktitle: العثور على الموقع المطلق للشكل داخل ورقة العمل
type: docs
weight: 8000
url: /ar/cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: تحديد الموقع المطلق للشكل في ورقة العمل باستخدام Aspose.Cells مع ++C.
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى معرفة الموضع المطلق لشكل في ورقة العمل. توفر Aspose.Cells الخصائص [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlefttocorner/) و [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) لهذا الغرض. تُعيد هذه الخصائص الموضع المطلق للشكل داخل ورقة العمل بالبكسل.

{{% /alert %}}

يعرض الكود العيني التالي الموضع المطلق لأول شكل في ورقة العمل بالبكسل. يعرض الكود العيني الإخراج التالي على وحدة التحكم:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the sample Excel file inside the workbook object
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first shape inside the worksheet
    Shape shape = worksheet.GetShapes().Get(0);

    // Displays the absolute position of the shape
    std::wcout << L"Absolute Position of this Shape is (" << shape.GetLeftToCorner() << L" , " << shape.GetTopToCorner() << L")" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
