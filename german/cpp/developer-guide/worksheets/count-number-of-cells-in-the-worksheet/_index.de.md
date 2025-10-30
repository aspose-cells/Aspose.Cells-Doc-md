---
title: Anzahl der Zellen im Arbeitsblatt mit C++ zählen
linktitle: Anzahl der Zellen im Arbeitsblatt zählen
type: docs
weight: 110
url: /de/cpp/count-number-of-cells-in-the-worksheet/
description: In diesem Artikel lernen Sie, wie man programmatisch die Anzahl der Zellen im Excel Arbeitsblatt mit C++ API und Aspose.Cells zählt.
keywords: Zellenanzahl in Excel Arbeitsblatt C++, Excel Arbeitsblattzellen C++
---

Sie können die Anzahl der Zellen im Arbeitsblatt mithilfe der [**Cells.GetCount()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcount/) oder [**Cells.GetCountLarge()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcountlarge/) Eigenschaften wie im folgenden Codebeispiel gezeigt zählen.

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
