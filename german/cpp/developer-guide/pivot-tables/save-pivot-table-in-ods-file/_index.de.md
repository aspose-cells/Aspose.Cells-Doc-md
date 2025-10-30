---
title: Pivot Tabelle im ODS Format mit C++ speichern
linktitle: Pivot Tabelle im ODS Format speichern
type: docs
weight: 150
url: /de/cpp/save-pivot-table-in-ods-file/
description: Erfahren Sie, wie Sie Pivot Tabellen mit Aspose.Cells for C++ im ODS Format speichern.
---

Aspose.Cells bietet die Möglichkeit, Pivot-Tabellen im ODS-Format zu speichern. Dafür können Sie entweder eine Arbeitsmappe mit einer bestehenden Pivot-Tabelle konvertieren oder eine neue Pivot-Tabelle erstellen und die Datei im ODS-Format speichern. Stellen Sie sicher, dass Sie [**PivotTable::CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) vor dem Speichern aufrufen, um sicherzustellen, dass die Pivot-Tabelle im Ausgabe-ODS-Datei gerendert wird. Das folgende Code-Snippet zeigt, wie eine Pivot-Tabelle in einer ODS-Datei gespeichert wird.

## Beispielcode

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get cells collection
    Cells cells = sheet.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Sport");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Quarter");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Sales");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Golf");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Golf");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Tennis");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Tennis");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Tennis");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Tennis");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Golf");

    cell = cells.Get(u"B2");
    cell.PutValue(u"Qtr3");
    cell = cells.Get(u"B3");
    cell.PutValue(u"Qtr4");
    cell = cells.Get(u"B4");
    cell.PutValue(u"Qtr3");
    cell = cells.Get(u"B5");
    cell.PutValue(u"Qtr4");
    cell = cells.Get(u"B6");
    cell.PutValue(u"Qtr3");
    cell = cells.Get(u"B7");
    cell.PutValue(u"Qtr4");
    cell = cells.Get(u"B8");
    cell.PutValue(u"Qtr3");

    cell = cells.Get(u"C2");
    cell.PutValue(1500);
    cell = cells.Get(u"C3");
    cell.PutValue(2000);
    cell = cells.Get(u"C4");
    cell.PutValue(600);
    cell = cells.Get(u"C5");
    cell.PutValue(1500);
    cell = cells.Get(u"C6");
    cell.PutValue(4070);
    cell = cells.Get(u"C7");
    cell.PutValue(5000);
    cell = cells.Get(u"C8");
    cell.PutValue(6430);

    // Get pivot tables collection
    PivotTableCollection pivotTables = sheet.GetPivotTables();

    // Add a pivot table to the worksheet
    int index = pivotTables.Add(u"=A1:C8", u"E3", u"PivotTable2");

    // Access the newly added pivot table
    PivotTable pivotTable = pivotTables.Get(index);

    // Unshow grand totals for rows
    pivotTable.SetRowGrand(false);

    // Add fields to the pivot table
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Column, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 2);

    // Calculate pivot table data
    pivotTable.CalculateData();

    // Save the workbook
    workbook.Save(outDir + u"PivotTableSaveInODS_out.ods");

    Aspose::Cells::Cleanup();
}
```

Die durch den oben genannten Code erzeugte Ausgabedatei ist zu Ihrer Referenz beigefügt.

[Ausgabedatei ODS](PivotTableSaveInODS_out.ods)
{{< app/cells/assistant language="cpp" >}}
