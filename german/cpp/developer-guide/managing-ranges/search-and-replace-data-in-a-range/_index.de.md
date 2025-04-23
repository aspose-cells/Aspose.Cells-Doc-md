---
title: Daten in einem Bereich suchen und ersetzen mit C++
linktitle: Daten in einem Bereich suchen und ersetzen
type: docs
weight: 170
url: /de/cpp/search-and-replace-data-in-a-range/
description: Dieser Artikel zeigt, wie man Daten in einem Bereich in Excel mit C++ Code sucht und ersetzt.
keywords: C++ Suche und Ersetzen von Daten in Excel, C++ Suche nach Daten in Excel, C++ Suche und Ersetzen von Daten in einem Bereich, C++ Suche nach Daten in einem Bereich, C++ Suche nach Daten in einem Bereich, C++ Suche nach Daten in Range, C++ Suche nach Daten in Excel, C++ Suche nach Daten in Range, Suche und Ersetzen von Daten in Excel mit C++, Suche und Ersetzen von Daten in einem Bereich mit C++, Suche und Ersetzen von Daten in Range mit C++
---

{{% alert color="primary" %}}

Manchmal müssen Sie nach bestimmten Daten in einem Bereich suchen und diese ersetzen, wobei Werte außerhalb des gewünschten Bereichs ignoriert werden. Aspose.Cells ermöglicht es, eine Suche auf einen bestimmten Bereich zu beschränken. Dieser Artikel erklärt, wie.

{{% /alert %}}

Aspose.Cells bietet die [**FindOptions::SetRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/setrange/)-Methode zum Festlegen eines Bereichs bei der Datensuche. Das untenstehende Code-Beispiel zeigt, wie man Daten in einem Bereich sucht und ersetzt.

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
