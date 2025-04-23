---
title: Nested oder Kinder Pivot Tabellen der Eltern Pivot Tabelle mit C++ finden und aktualisieren
linktitle: Nested oder Kinder Pivot Tabellen finden und aktualisieren
type: docs
weight: 60
url: /de/cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Lernen Sie, wie Sie verschachtelte oder Kinder Pivot Tabellen eines Eltern Pivot Tabellen mit Aspose.Cells for C++ finden und aktualisieren.
---

## **Mögliche Verwendungsszenarien**

Manchmal verwendet eine Pivot-Tabelle eine andere Pivot-Tabelle als Datenquelle, daher wird sie als untergeordnete Pivot-Tabelle oder verschachtelte Pivot-Tabelle bezeichnet. Sie können die untergeordneten Pivot-Tabellen einer übergeordneten Pivot-Tabelle unter Verwendung der [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/)-Methode finden.

## **Finden und Aktualisieren der untergeordneten oder Kind-Pivot-Tabellen der übergeordneten Pivot-Tabelle**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767747.xlsx), die drei Pivot-Tabellen enthält. Die unteren zwei Pivot-Tabellen sind die Kinder der obigen Pivot-Tabelle, wie in diesem Screenshot gezeigt. Der Code findet die untergeordneten Pivot-Tabellen unter Verwendung der [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/)-Methode und aktualisiert sie dann nacheinander.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Beispielcode**

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
