---
title: Contar el número de celdas en la hoja de trabajo con C++
linktitle: Contar el número de celdas en la hoja de cálculo
type: docs
weight: 110
url: /es/cpp/count-number-of-cells-in-the-worksheet/
description: En este artículo, aprenderás cómo contar de forma programática el número de celdas en la hoja de Excel usando la API de C++ con Aspose.Cells.
keywords: contar número de celdas en hoja de Excel c++, c++ para celdas de hoja de Excel
---

Puede contar el número de celdas en la hoja de cálculo utilizando las propiedades [**Cells.GetCount()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcount/) o [**Cells.GetCountLarge()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcountlarge/) como se muestra en el ejemplo de código a continuación.

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
