---
title: Conta il numero di celle nel foglio di lavoro con C++
linktitle: Contare il numero di celle nel foglio di lavoro
type: docs
weight: 110
url: /it/cpp/count-number-of-cells-in-the-worksheet/
description: In questo articolo imparerai come contare programmaticamente il numero di celle nel foglio di lavoro Excel usando l API C++ con Aspose.Cells.
keywords: conta numero di celle nel foglio di lavoro Excel c++, celle nel foglio di lavoro Excel c++
---

Puoi contare il numero di celle nel foglio di lavoro utilizzando le proprietà [**Cells.GetCount()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcount/) o [**Cells.GetCountLarge()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcountlarge/) come mostrato nell'esempio di codice riportato di seguito.

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
