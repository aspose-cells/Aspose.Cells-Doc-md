---
title: Få textbredden av cellvärdet med C++
linktitle: Få textbredd av cellvärde
type: docs
weight: 50
url: /sv/cpp/get-text-width-of-cell-value/
description: Lär dig hur du får textbredden av cellvärdet via API n Aspose.Cells for C++.
keywords: Få textbredd av cellvärde, Få textbredd av cellvärde
---

## **Få textens bredd av cellvärdet**

 Ibland kan utvecklare behöva beräkna bredden på cellens värde för att organisera data i ett layout. Aspose.Cells tillhandahåller [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/)-metoden som låter utvecklare få textbredden för cellens värde. Följande exempel visar hur du använder [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) för att komma åt textbredden för cellens värde.

Källfilen som används i den följande kodsnutten bifogas för din referens.

[Källfil](96928090.xlsx)

## Exempelkod

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory path for source files
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from the specified Excel file
    Workbook workbook(sourceDir + u"GetTextWidthSample.xlsx");

    // Calculate the text width for the string value of cell A1
    double textWidth = CellsHelper::GetTextWidth(workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue(), workbook.GetDefaultStyle().GetFont(), 1);

    // Output the text width
    std::wcout << u"Text width: " << textWidth << std::endl;

    Aspose::Cells::Cleanup();
}
```
