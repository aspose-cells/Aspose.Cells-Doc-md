---
title: Compter le nombre de cellules dans la feuille de calcul avec C++
linktitle: Compter le nombre de cellules dans la feuille de calcul
type: docs
weight: 110
url: /fr/cpp/count-number-of-cells-in-the-worksheet/
description: Dans cet article, vous apprendrez comment compter de manière programmatique le nombre de cellules dans la feuille de calcul Excel en utilisant l API C++ avec Aspose.Cells.
keywords: compter le nombre de cellules de la feuille Excel c++, cellule de feuille Excel c++
---

Vous pouvez compter le nombre de cellules dans la feuille de calcul en utilisant les propriétés [**Cells.GetCount()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcount/) ou [**Cells.GetCountLarge()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcountlarge/) comme indiqué dans l'exemple de code ci-dessous.

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
