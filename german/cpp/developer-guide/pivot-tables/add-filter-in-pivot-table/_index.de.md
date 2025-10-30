---
title: Pivot Filter mit C++
linktitle: Pivot Filter
type: docs
weight: 130
url: /de/cpp/add-or-clear-pivot-filter/
description: Erfahren Sie, wie Sie in Pivot Tabellen mit Aspose.Cells und C++ einen Filter hinzufügen.
keywords: Hinzufügen eines Filters in einer Pivot Tabelle ohne Office 2013, Office 2016, Office 2019 und Office 365.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie eine Pivot-Tabelle mit bekannten Daten erstellen und filtern möchten, lernen und verwenden Sie den Filter. Er kann Ihnen helfen, die gewünschten Daten effizient herauszufiltern. Mit der API von Aspose.Cells können Sie Filter auf Felder in Pivot-Tabellen hinzufügen und löschen. 

## **Filter in Pivot-Tabelle in Excel hinzufügen**
Filter in Pivot-Tabelle in Excel hinzufügen, folgen Sie diesen Schritten:

1. Wählen Sie die Pivot-Tabelle aus, aus der Sie den Filter löschen möchten. 
2. Klicken Sie auf den Dropdown-Pfeil für den Filter, den Sie in der Pivot-Tabelle hinzufügen möchten.
3. Wählen Sie "Top 10" aus dem Dropdown-Menü.
<br>
<img src="3.png" width=80% />
4. Legen Sie den Anzeigemodus und die Filteranzahl fest.
<br>
<img src="4.png" width=80% />

## **Filter in Pivot-Tabelle hinzufügen**
Bitte sehen Sie sich den folgenden Beispielcode an. Es legt die Daten fest und erstellt darauf basierend eine Pivot-Tabelle. Fügen Sie dann einen Filter im Zeilenfeld der Pivot-Tabelle hinzu. Schließlich speichert es die Arbeitsmappe im Format [output XLSX](filterout.xlsx). Nach Ausführung des Beispielcodes wird eine Pivot-Tabelle mit einem Top-10-Filter zum Arbeitsblatt hinzugefügt.

### **Beispielcode**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the workbook
    workbook.Save(u"filterout.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filter in Pivot-Tabelle in Excel löschen**
Filter in Pivot-Tabelle in Excel löschen, befolgen Sie diese Schritte:

1. Wählen Sie die Pivot-Tabelle aus, aus der Sie den Filter löschen möchten. 
2. Klicken Sie auf den Dropdown-Pfeil für den Filter, den Sie in der Pivot-Tabelle löschen möchten.
3. Wählen Sie "Filter löschen" aus dem Dropdown-Menü aus.
<br>
<img src="1.png" width=80% />
4. Wenn Sie alle Filter aus der Pivot-Tabelle löschen möchten, können Sie auch auf die Schaltfläche "Filter löschen" im PivotTable-Analyse-Tab im Menüband in Excel klicken.
<br>
<img src="2.png" width=80% />

## **Filter in Pivot-Tabelle löschen**
Filter in Pivot-Tabelle löschen mit Aspose.Cells. Bitte beachten Sie den folgenden Beispielcode. 
1. Daten setzen und eine Pivot-Tabelle basierend darauf erstellen. 
2. Einen Filter auf das Zeilenfeld der Pivot-Tabelle hinzufügen. 
3. Die Arbeitsmappe im Format [output XLSX](out_add.xlsx) speichern. Nach Ausführung des Beispielcodes wird eine Pivot-Tabelle mit einem Top10-Filter zum Arbeitsblatt hinzugefügt. 
4. Den Filter auf einem bestimmten Pivot-Feld löschen. Nach Ausführung des Codes zum Löschen des Filters wird der Filter auf dem spezifischen Pivot-Feld gelöscht. Bitte prüfen Sie das [output XLSX](out_delete.xlsx).

### **Beispielcode**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_add.xlsx");

    // Clear PivotFilter from the specific PivotField
    pivotTable.GetPivotFilters().ClearFilter(field.GetBaseIndex());
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_delete.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
