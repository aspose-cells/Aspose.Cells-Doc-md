---
title: Buscar y Reemplazar datos en un rango con C++
linktitle: Buscar y Reemplazar Datos en un Rango
type: docs
weight: 170
url: /es/cpp/search-and-replace-data-in-a-range/
description: Este artículo muestra cómo buscar y reemplazar datos en un rango en Excel usando código en C++.
keywords: Buscar y reemplazar datos en Excel con C++, buscar datos en Excel, buscar y reemplazar datos en un rango, buscar datos en un rango, buscar datos en rango, buscar datos en Excel, buscar datos en rango en C++, buscar datos en rango en C++, buscar y reemplazar datos en Excel con C++, buscar y reemplazar datos en rango con C++, buscar y reemplazar datos en rango con C++
---

{{% alert color="primary" %}}

A veces necesitas buscar y reemplazar datos específicos en un rango, ignorando cualquier valor de celda fuera del rango deseado. Aspose.Cells permite limitar una búsqueda a un rango específico. Este artículo explica cómo.

{{% /alert %}}

Aspose.Cells proporciona el método [**FindOptions::SetRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/setrange/) para especificar un rango al buscar datos. El siguiente ejemplo de código demuestra cómo buscar y reemplazar datos en un rango.

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
