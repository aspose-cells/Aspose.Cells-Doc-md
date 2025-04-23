---
title: Räkna antalet celler i arbetsbladet med C++
linktitle: Räkna antalet celler i kalkylbladet
type: docs
weight: 110
url: /sv/cpp/count-number-of-cells-in-the-worksheet/
description: I denna artikel lär du dig hur du programmässigt räknar antalet celler i Excel arbetsbladet med C++ API och Aspose.Cells.
keywords: antal celler i Excel arbetsblad C++, Excel arbetsblad celler C++
---

Du kan räkna antalet celler i kalkylbladet genom att använda [**Cells.GetCount()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcount/) eller [**Cells.GetCountLarge()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcountlarge/) egenskaper som visas i kodexemplet nedan.

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
