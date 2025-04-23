---
title: Sök och ersätt data i ett område med C++
linktitle: Sök och ersätt data i ett intervall
type: docs
weight: 170
url: /sv/cpp/search-and-replace-data-in-a-range/
description: Denna artikel visar hur man söker och ersätter data i ett område i Excel med C++ kod.
keywords: c++ sök och ersätt data i Excel, c++ sök data i Excel, c++ sök och ersätt data i ett område, c++ sök data i ett område, c++ sök data i ett område, c++ sök data i ett område, c++ sök data i Excel, c++ sök data i område, sök och ersätt data i Excel med c++, sök och ersätt data i ett område med c++, sök och ersätt data i område med c++
---

{{% alert color="primary" %}}

Ibland behöver du söka efter och ersätta specifik data i ett område, och ignorera cellvärden utanför detta område. Aspose.Cells tillåter att begränsa sökningen till ett specifikt område. Denna artikel förklarar hur.

{{% /alert %}}

Aspose.Cells tillhandahåller metoden [**FindOptions::SetRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/setrange/) för att specificera ett område vid sökning av data. Följande kodexempel visar hur man söker och ersätter data i ett område.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"input.xlsx";

    // Create workbook
    Workbook workbook(filePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Specify the range where you want to search
    // Here the range is E9:H15
    CellArea area = CellArea::CreateCellArea(u"E9", u"H15");

    // Specify Find options
    FindOptions opts;
    opts.SetLookInType(LookInType::Values);
    opts.SetLookAtType(LookAtType::EntireContent);
    opts.SetRange(area);

    Cell cell;
    do
    {
        // Search the cell with value search within range
        cell = worksheet.GetCells().Find(u"search", cell, opts);

        // If no such cell found, then break the loop
        if (!cell)
            break;

        // Replace the cell with value replace
        cell.PutValue(u"replace");

    } while (true);

    // Save the workbook
    U16String outputPath = srcDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
