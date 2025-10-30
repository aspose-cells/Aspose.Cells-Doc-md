---
title: C++ kullanarak Çalışma Sayfasındaki hücrelerin sayısını sayma
linktitle: Çalışma Sayfasındaki Hücrelerin Sayısını Say
type: docs
weight: 110
url: /tr/cpp/count-number-of-cells-in-the-worksheet/
description: Bu makalede, Aspose.Cells API si ile C++ kullanarak Excel çalışma sayfasındaki hücrelerin sayısını programlı olarak nasıl sayacağınızı öğreneceksiniz.
keywords: Excel çalışma sayfası hücrelerini saymak C++ ile
---

Aşağıdaki örnekte verilen kod örneğinde gösterildiği gibi, çalışma sayfasındaki hücre sayısını [**Cells.GetCount()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcount/) veya [**Cells.GetCountLarge()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcountlarge/) özelliklerini kullanarak sayabilirsiniz.

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
