---
title: Anpassad sortering i PivotTabell med C++
linktitle: Anpassad sortering i Pivot tabell
type: docs
weight: 130
url: /sv/cpp/custom-sorting-in-pivot-table/
description: Lär dig hur man sorterar PivotTabeller på fältvärden med Aspose.Cells och C++.
---

## **Anpassad sortering i Pivot-tabell**
Genom att använda Aspose.Cells API kan du sortera PivotTabeller på fältvärden. Följande kodsnutt laddar den exempel-Excel filen och lägger till tre pivot-tabeller. Den första pivot-tabellen är utan anpassad sortering, den andra är sorterad på "SeaFood"-radfältvärden, och den tredje är sorterad på "28/07/2000"-kolumnfältvärden.

Provfil och utdatafiler kan laddas ner här för att testa provkoden:

[Källa Excelfil](98107428.xlsx)

[Utmatnings-excelfil](98107429.xlsx)

[Utmatnings-PD-fil](98107430.pdf)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook wb(srcDir + u"SamplePivotSort.xlsx");

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Get the pivot tables collection
    PivotTableCollection pivotTables = sheet.GetPivotTables();

    // Source PivotTable
    // Add a PivotTable to the worksheet
    int index = pivotTables.Add(u"=Sheet1!A1:C10", u"E3", u"PivotTable2");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = pivotTables.Get(index);

    // Unshow grand totals for rows and columns
    pivotTable.SetShowRowGrandTotals(false);
    pivotTable.SetShowColumnGrandTotals(false);

    // Drag the first field to the row area
    pivotTable.AddFieldToArea(PivotFieldType::Row, 1);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    rowField.SetIsAutoSort(true);
    rowField.SetIsAscendSort(true);

    // Drag the second field to the column area
    pivotTable.AddFieldToArea(PivotFieldType::Column, 0);
    PivotField colField = pivotTable.GetColumnFields().Get(0);
    colField.SetNumberFormat(u"dd/mm/yyyy");
    colField.SetIsAutoSort(true);
    colField.SetIsAscendSort(true);

    // Drag the third field to the data area
    pivotTable.AddFieldToArea(PivotFieldType::Data, 2);

    pivotTable.RefreshData();
    pivotTable.CalculateData();
    // End of source PivotTable

    // Sort the PivotTable on "SeaFood" row field values
    // Add a PivotTable to the worksheet
    index = pivotTables.Add(u"=Sheet1!A1:C10", u"E10", u"PivotTable2");

    // Access the instance of the newly added PivotTable
    pivotTable = pivotTables.Get(index);

    // Unshow grand totals for rows and columns
    pivotTable.SetShowRowGrandTotals(false);
    pivotTable.SetShowColumnGrandTotals(false);

    // Drag the first field to the row area
    pivotTable.AddFieldToArea(PivotFieldType::Row, 1);
    rowField = pivotTable.GetRowFields().Get(0);
    rowField.SetIsAutoSort(true);
    rowField.SetIsAscendSort(true);

    // Drag the second field to the column area
    pivotTable.AddFieldToArea(PivotFieldType::Column, 0);
    colField = pivotTable.GetColumnFields().Get(0);
    colField.SetNumberFormat(u"dd/mm/yyyy");
    colField.SetIsAutoSort(true);
    colField.SetIsAscendSort(true);
    colField.SetAutoSortField(0);

    // Drag the third field to the data area
    pivotTable.AddFieldToArea(PivotFieldType::Data, 2);

    pivotTable.RefreshData();
    pivotTable.CalculateData();
    // End of sort the PivotTable on "SeaFood" row field values

    // Sort the PivotTable on "28/07/2000" column field values
    // Add a PivotTable to the worksheet
    index = pivotTables.Add(u"=Sheet1!A1:C10", u"E18", u"PivotTable2");

    // Access the instance of the newly added PivotTable
    pivotTable = pivotTables.Get(index);

    // Unshow grand totals for rows and columns
    pivotTable.SetShowRowGrandTotals(false);
    pivotTable.SetShowColumnGrandTotals(false);

    // Drag the first field to the row area
    pivotTable.AddFieldToArea(PivotFieldType::Row, 1);
    rowField = pivotTable.GetRowFields().Get(0);
    rowField.SetIsAutoSort(true);
    rowField.SetIsAscendSort(true);
    rowField.SetAutoSortField(0);

    // Drag the second field to the column area
    pivotTable.AddFieldToArea(PivotFieldType::Column, 0);
    colField = pivotTable.GetColumnFields().Get(0);
    colField.SetNumberFormat(u"dd/mm/yyyy");
    colField.SetIsAutoSort(true);
    colField.SetIsAscendSort(true);

    // Drag the third field to the data area
    pivotTable.AddFieldToArea(PivotFieldType::Data, 2);

    pivotTable.RefreshData();
    pivotTable.CalculateData();
    // End of sort the PivotTable on "28/07/2000" column field values

    // Save the Excel file
    wb.Save(outDir + u"out_java.xlsx");

    // Save as PDF
    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);
    wb.Save(outDir + u"out_java.pdf", options);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
