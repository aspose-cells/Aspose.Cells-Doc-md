---
title: Trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants d’un tableau croisé dynamique parent avec C++
linktitle: Trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants
type: docs
weight: 60
url: /fr/cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Apprenez comment trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants d’un tableau croisé dynamique parent en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Parfois, un tableau croisé dynamique utilise un autre tableau croisé dynamique en tant que source de données, on l'appelle un tableau croisé dynamique enfant ou un tableau croisé dynamique imbriqué. Vous pouvez trouver les tableaux croisés dynamiques enfants d'un tableau croisé dynamique parent en utilisant la méthode [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/).

## **Trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent**

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767747.xlsx) qui contient trois tableaux croisés dynamiques. Les deux tableaux croisés dynamiques inférieurs sont les enfants du tableau croisé dynamique ci-dessus comme indiqué dans cette capture d'écran. Le code trouve les tableaux croisés dynamiques enfants en utilisant la méthode [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/) et les actualise un par un.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Code d'exemple**

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
{{< app/cells/assistant language="cpp" >}}
