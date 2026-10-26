---
title: Create Pivot Table
linktitle: Create Pivot Table
description: Create and format pivot tables with Aspose.Cells for C++.
url: /cpp/create-pivot-table/
type: docs
weight: 160
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **What is a Pivot Table?**
A pivot table is an interactive summary report: it condenses a large block of raw, row-by-row data into a compact matrix without a single formula. You decide which columns become row labels, which become column labels and which are aggregated as values — the pivot table does the grouping and the math:
- **Summarize** — total sales per product, per region or per quarter instead of long formula chains.
- **Compare** — categories on the rows and periods on the columns turn a flat list into a cross report where trends are visible at a glance.
- **Drill down** — double-click any summary value to inspect the source rows behind it.
- **Refresh** — when the source data changes, one refresh recalculates the whole report.
Typical scenarios are sales dashboards, expense breakdowns and inventory analysis — any question of the form "how do these numbers break down by category and time?". In Aspose.Cells for C++, a pivot table is created with the [PivotTableCollection.Add()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/add/) method of a worksheet. Once the pivot table is created, you can work with it using the [PivotTable](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) class.

## **Create Pivot Table**
The following sample code shows how to create a pivot table and work with it. Please check the [output Excel file](23167010.xlsx) generated with this code and the following screenshot showing the output Excel file in Microsoft Excel.
![todo:image_alt_text](create-pivot-table_1.png)

## **Sample Code**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main()
{
    Aspose::Cells::Startup();
    // Create a new workbook and get the first worksheet
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    // Write the source data: sales per sport and quarter
    cells.Get(u"A1").PutValue(u"Sport");
    cells.Get(u"B1").PutValue(u"Quarter");
    cells.Get(u"C1").PutValue(u"Sales");
    cells.Get(u"A2").PutValue(u"Golf");
    cells.Get(u"B2").PutValue(u"Qtr3");
    cells.Get(u"C2").PutValue(1500);
    cells.Get(u"A3").PutValue(u"Golf");
    cells.Get(u"B3").PutValue(u"Qtr4");
    cells.Get(u"C3").PutValue(2000);
    cells.Get(u"A4").PutValue(u"Tennis");
    cells.Get(u"B4").PutValue(u"Qtr3");
    cells.Get(u"C4").PutValue(600);
    cells.Get(u"A5").PutValue(u"Tennis");
    cells.Get(u"B5").PutValue(u"Qtr4");
    cells.Get(u"C5").PutValue(1500);
    cells.Get(u"A6").PutValue(u"Tennis");
    cells.Get(u"B6").PutValue(u"Qtr3");
    cells.Get(u"C6").PutValue(4070);
    cells.Get(u"A7").PutValue(u"Tennis");
    cells.Get(u"B7").PutValue(u"Qtr4");
    cells.Get(u"C7").PutValue(5000);
    cells.Get(u"A8").PutValue(u"Golf");
    cells.Get(u"B8").PutValue(u"Qtr3");
    cells.Get(u"C8").PutValue(6430);
    // Add a pivot table at destination cell E3, sourced from A1:C8
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"A1:C8", 2, 4);
    // Assign pivot fields: Sport to Rows, Quarter to Columns, Sales to Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Quarter");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    // Save the workbook
    workbook.Save(u"pivotTable_test_out.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}