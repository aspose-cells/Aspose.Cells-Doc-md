---
title: Add calculated field in Pivot Table with C++
linktitle: Add calculated field in Pivot Table
type: docs
weight: 130
url: /cpp/add-calculated-field-in-pivot-table/
description: How to add a calculated field in pivot table with Aspose.Cells for C++.
keywords: Adding a calculated field in pivot table.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
When you create a pivot table based on known data, you may find that the data in it is not what you want. The desired data is a combination of the original data. For example, you need to add, subtract, multiply, and divide the original data before obtaining the results you need. At that point, you need to build a calculated field and set the corresponding formula for calculation, then perform some statistics and other operations on the calculated field.  

## **Add calculated field in Pivot Table in Excel**
Insert a calculated field in a PivotTable in Excel, follow these steps:

1. Select the PivotTable that you want to add a calculated field to.  
2. Go to the **PivotTable Analyze** tab on the ribbon.  
3. Click on **Fields, Items, & Sets** and then select **Calculated Field** from the drop‑down menu.  
4. In the **Name** field, enter a name for the calculated field.  
5. In the **Formula** field, enter the formula for the calculation you want to perform using the appropriate PivotTable field names and mathematical operators.  
   <br>
   <img src="1.png" width=80% />
6. Click **OK** to create the calculated field.  
7. The new calculated field will appear in the PivotTable Field List under the **Values** section.  
8. Drag the calculated field to the **Values** section of the PivotTable to display the calculated values.  
   <br>
   <img src="2.png" width=80% />

## **Add a calculated field in Pivot Table Using C++**
Add a calculated field to an Excel file using Aspose.Cells. Please see the following sample code. After executing the example code, a pivot table with a calculated field is added to the worksheet.

1. Set the original data and create a pivot table.  
2. Create the calculated field based on the existing PivotField in the pivot table.  
3. Add the calculated field to the data area.  
4. Finally, the workbook is saved in XLSX format.  

## **Sample Code**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a Workbook object
    Workbook workbook;

    // Obtaining a reference to the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the values to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");

    cell = cells.Get("B1");
    cell.PutValue(u"Count");

    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");

    cell = cells.Get("A3");
    cell.PutValue(u"Mango");

    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");

    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);

    cell = cells.Get("B3");
    cell.PutValue(3);

    cell = cells.Get("B4");
    cell.PutValue(6);

    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);

    cell = cells.Get("C3");
    cell.PutValue(20);

    cell = cells.Get("C4");
    cell.PutValue(30);

    cell = cells.Get("C5");
    cell.PutValue(60);

    // Adding a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:C5", u"D10", u"PivotTable1");

    // Accessing the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    // Adding a calculated field to the PivotTable and dragging it to the data area
    pivotTable.AddCalculatedField(u"total", u"=Count*Price", true);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
