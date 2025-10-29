---
title: Supprimer des plages d Excel avec C++
linktitle: Supprimer des plages
type: docs
weight: 105
url: /fr/cpp/delete-ranges-from-excel/
description: Apprenez comment supprimer des plages dans Excel en utilisant Aspose.Cells avec C++.
---

## **Introduction**

Dans Excel, vous pouvez sélectionner une plage, puis la supprimer et décaler d'autres données vers la gauche ou vers le haut.

**![Options de décalage](delete-range.png)**

## **Supprimer des plages en utilisant Aspose.Cells**

Aspose.Cells fournit la méthode [Cells.DeleteRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterange/) pour supprimer une plage.

## **Supprimer des plages et décaler les cellules à gauche**

Supprimer une plage et décaler les cellules vers la gauche comme dans les codes suivants avec Aspose.Cells :

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

## **Supprimer des plages et décaler les cellules vers le haut**

Supprimer une plage et décaler les cellules vers le haut comme dans les codes suivants avec Aspose.Cells :

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
{{< app/cells/assistant language="cpp" >}}
