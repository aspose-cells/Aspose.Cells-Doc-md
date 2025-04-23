---
title: Подсчет количества ячеек в листе с помощью C++
linktitle: Посчитать количество ячеек в листе
type: docs
weight: 110
url: /ru/cpp/count-number-of-cells-in-the-worksheet/
description: В этой статье вы узнаете, как программно подсчитать количество ячеек на листе Excel с использованием API C++ с Aspose.Cells.
keywords: подсчет количества ячеек Excel листа C++, ячейки листа Excel C++
---

Вы можете подсчитать количество ячеек в листе, используя свойства [**Cells.GetCount()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcount/) или [**Cells.GetCountLarge()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcountlarge/), как показано в приведенном ниже примере кода.

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
