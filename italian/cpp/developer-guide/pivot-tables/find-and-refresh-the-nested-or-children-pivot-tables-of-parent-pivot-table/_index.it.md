---
title: Trova e aggiorna le Pivot Table nidificate o figlie di una Pivot Table genitore con C++
linktitle: Trova e aggiorna le Pivot Table nidificate o figlie
type: docs
weight: 60
url: /it/cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Impara come trovare e aggiornare le pivot table nidificate o figlie di una pivot table padre usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

A volte, una tabella pivot utilizza un'altra tabella pivot come fonte dati, quindi è chiamata tabella pivot figlio o tabella pivot nidificata. È possibile trovare le tabelle pivot figlie di una tabella pivot principale utilizzando il metodo [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/).

## **Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot principale**

Il codice di esempio seguente carica il [file di Excel di esempio](61767747.xlsx) che contiene tre tabelle pivot. Le due tabelle pivot inferiori sono i figli della tabella pivot soprastante come mostrato in questa schermata. Il codice trova le tabelle pivot figlie utilizzando il metodo [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/) e poi le aggiorna una per volta.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Codice di Esempio**

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
