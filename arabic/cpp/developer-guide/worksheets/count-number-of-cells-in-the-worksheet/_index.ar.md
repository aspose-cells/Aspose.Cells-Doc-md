---
title: حساب عدد الخلايا في ورقة العمل باستخدام C++
linktitle: عدد خلايا ورقة العمل
type: docs
weight: 110
url: /ar/cpp/count-number-of-cells-in-the-worksheet/
description: في هذا المقال، ستتعلم كيفية عد عدد الخلايا في ورقة عمل Excel برمجيًا باستخدام واجهة برمجة تطبيقات C++ مع Aspose.Cells.
keywords: حساب عدد خلايا ورقة العمل في Excel باستخدام C++، خلايا ورقة عمل Excel C++
---

يمكنك إحصاء عدد الخلايا في الورقة باستخدام الخصائص [**Cells.GetCount()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcount/) أو [**Cells.GetCountLarge()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcountlarge/) كما هو موضح في مثال الكود أدناه.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    Workbook workbook(sourceDir + u"BookWithSomeData.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print number of cells in the Worksheet
    std::cout << "Number of Cells: " << worksheet.GetCells().GetCount() << std::endl;

    // In case the number of cells is greater than 2147483647, use CountLarge
    std::cout << "Number of Cells (CountLarge): " << worksheet.GetCells().GetCountLarge() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
