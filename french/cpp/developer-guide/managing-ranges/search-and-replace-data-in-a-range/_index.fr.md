---
title: Rechercher et remplacer des données dans une plage avec C++
linktitle: Rechercher et remplacer des données dans une plage
type: docs
weight: 170
url: /fr/cpp/search-and-replace-data-in-a-range/
description: Cet article montre comment rechercher et remplacer des données dans une plage dans Excel en utilisant du code C++.
keywords: recherche et remplacement de données en C++ dans Excel, recherche de données en C++ dans Excel, recherche et remplacement de données dans une plage en C++, recherche de données dans une plage en C++, recherche de données dans une plage en C++, recherche de données dans Excel en C++, recherche de données dans une plage, recherche de données dans Excel avec C++, recherche et remplacement de données dans une plage avec C++
---

{{% alert color="primary" %}}

Parfois, vous devez rechercher et remplacer des données spécifiques dans une plage, en ignorant toute valeur de cellule en dehors de la plage souhaitée. Aspose.Cells vous permet de limiter la recherche à une plage spécifique. Cet article explique comment.

{{% /alert %}}

Aspose.Cells fournit la méthode [**FindOptions::SetRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/setrange/) pour spécifier une plage lors de la recherche de données. L'exemple de code ci-dessous montre comment rechercher et remplacer des données dans une plage.

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
