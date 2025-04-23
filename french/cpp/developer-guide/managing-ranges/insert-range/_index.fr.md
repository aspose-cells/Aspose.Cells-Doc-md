---  
title: Insérer des plages dans Excel avec C++  
linktitle: Insérer des plages  
type: docs  
weight: 105  
url: /fr/cpp/insert-ranges-to-excel/  
description: Apprenez comment insérer des plages dans des fichiers Excel en utilisant Aspose.Cells avec C++.   
---  

## **Introduction**

Dans Excel, vous pouvez sélectionner une plage, puis insérer une plage et déplacer d'autres données vers la droite ou vers le bas.

**![Options de décalage](InsertRange.png)**

## **Insérer des plages en utilisant Aspose.Cells**

Aspose.Cells fournit la méthode [Cells.InsertRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrange/) pour insérer une plage.

## **Insérer des plages et déplacer les cellules vers la droite**

Insérer une plage et décaler les cellules vers la droite avec Aspose.Cells :

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

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into a few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    CellArea ca = CellArea::CreateCellArea(u"A1", u"A2");
    worksheet.GetCells().InsertRange(ca, ShiftType::Right);

    std::cout << (worksheet.GetCells().Get(u"B1").GetStringValue() == u"Test" ? "True" : "False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Insérer des plages et décaler les cellules vers le bas**

Insérer une plage et décaler les cellules vers le bas avec Aspose.Cells :

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

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formatting into
    // a few cells in the range.
    sourceRange.Get(0, 0).SetValue(u"Test");
    sourceRange.Get(1, 0).SetValue(u"123");
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A2");
    worksheet.GetCells().InsertRange(ca, ShiftType::Down);

    std::cout << (worksheet.GetCells().Get(u"A3").GetStringValue() == u"Test" ? "True" : "False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

