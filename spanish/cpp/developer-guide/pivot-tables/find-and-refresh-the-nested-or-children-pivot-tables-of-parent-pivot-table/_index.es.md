---
title: Encontrar y actualizar las tablas dinámicas anidadas o hijas de la tabla dinámica principal con C++
linktitle: Encontrar y actualizar tablas dinámicas anidadas o hijas
type: docs
weight: 60
url: /es/cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Aprende cómo encontrar y actualizar tablas dinámicas anidadas o hijas de una tabla dinámica principal usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

A veces, una tabla dinámica utiliza otra tabla dinámica como origen de datos, por lo que se le llama tabla dinámica secundaria o tabla dinámica anidada. Puede encontrar las tablas dinámicas secundarias de una tabla dinámica principal utilizando el método [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/).

## **Encontrar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal**

El siguiente código de muestra carga el [archivo Excel de muestra](61767747.xlsx) que contiene tres tablas dinámicas. Las dos tablas dinámicas inferiores son las hijas de la tabla dinámica anterior, como se muestra en esta captura de pantalla. El código encuentra las tablas dinámicas secundarias utilizando el método [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/) y luego las actualiza una por una.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath = u"sampleFindAndRefreshNestedOrChildrenPivotTables.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access third pivot table
    PivotTable ptParent = ws.GetPivotTables().Get(2);

    // Access the children of the parent pivot table
    Vector<PivotTable> ptChildren = ptParent.GetChildren();

    // Refresh all the children pivot table
    int count = ptChildren.GetLength();
    for (int idx = 0; idx < count; idx++)
    {
        // Access the child pivot table
        PivotTable ptChild = ptChildren[idx];

        // Refresh the child pivot table
        ptChild.RefreshData();
        ptChild.CalculateData();
    }

    std::cout << "Children pivot tables refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
