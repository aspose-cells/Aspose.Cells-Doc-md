---
title: Ranges aus Excel mit C++ löschen
linktitle: Bereiche löschen
type: docs
weight: 105
url: /de/cpp/delete-ranges-from-excel/
description: Erfahren Sie, wie Sie Bereiche in Excel mit Aspose.Cells und C++ löschen.
---

## **Einführung**

In Excel können Sie einen Bereich auswählen, löschen und andere Daten links oder nach oben verschieben.

**![Verschieboptionen](delete-range.png)**

## **Löschen von Bereichen mit Aspose.Cells**

Aspose.Cells bietet die [Cells.DeleteRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterange/) Methode zum Löschen eines Bereichs.

## **Bereiche löschen und Zellen nach links verschieben**

Löschen Sie einen Bereich und verschieben Sie die Zellen nach links mit den folgenden Codes in Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Gets cells.
    Cells cells = worksheet.GetCells();

    // Input some data with some formatting into a few cells in the range.
    cells.Get(u"C2").PutValue(u"C2");
    cells.Get(u"C3").PutValue(u"C3");
    CellArea ca = CellArea::CreateCellArea(u"B2", u"B3");

    // Delete the specified range of cells and shift cells to the left.
    cells.DeleteRange(ca.StartRow, ca.StartColumn, ca.EndRow, ca.EndColumn, ShiftType::Left);

    // Check if the value in B2 is equal to "C2".
    std::cout << (worksheet.GetCells().Get(u"B2").GetStringValue() == u"C2" ? "True" : "False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Bereiche löschen und Zellen nach oben verschieben**

Löschen Sie einen Bereich und verschieben Sie die Zellen nach oben mit den folgenden Codes in Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Gets cells.
    Cells cells = worksheet.GetCells();

    // Input some data with some formatting into a few cells in the range.
    cells.Get(u"B4").PutValue(u"B4");
    cells.Get(u"B5").PutValue(u"B5");

    // Creates a CellArea for the range B2:B3.
    CellArea ca = CellArea::CreateCellArea(u"B2", u"B3");

    // Deletes the specified range and shifts cells up.
    cells.DeleteRange(ca.StartRow, ca.StartColumn, ca.EndRow, ca.EndColumn, ShiftType::Up);

    // Check the value in cell B2 to verify the operation.
    std::cout << (worksheet.GetCells().Get(u"B2").GetStringValue() == u"B4" ? "Success" : "Failure") << std::endl;

    Aspose::Cells::Cleanup();
}
```
