---
title: Create Pivot Tables and Pivot Charts with C++
linktitle: Create Pivot Tables and Pivot Charts
type: docs
weight: 20
url: /cpp/create-pivot-tables-and-pivot-charts/
description: Learn how to create pivot tables and pivot charts in Excel files using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

A pivot table is an interactive summary of records. For example, you may have hundreds of invoice entries in a list in a worksheet. A pivot table can total the invoices by customer, product, or date. With Microsoft Excel, it is possible to quickly rearrange the information in the pivot table by dragging buttons to a new position.

A pivot chart is an interactive graphical representation of the data in a pivot table. Pivot charts were introduced in Excel 2000. Using a pivot chart makes it even easier to understand the data since the pivot table creates subtotals and totals automatically.

Aspose.Cells supports [pivot tables](/cells/cpp/create-pivot-tables-and-pivot-charts/) and [pivot charts](/cells/cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Adding Pivot Tables and Charts**

Aspose.Cells provides a special set of classes used to create pivot tables. These classes are used to create and set PivotTable objects, which act as a PivotTable object's basic building blocks:

- **PivotField**, a field in a pivot table report.
- **PivotFields**, a collection of all the PivotField objects in a pivot table.
- **PivotTable**, a PivotTable report on a worksheet.
- **PivotTables**, a collection of all the PivotTable objects on the worksheet.

### **Preparing to use Aspose.Cells**

1. Download and install Aspose.Cells:
   1. [Download Aspose.Cells](https://downloads.aspose.com/cells/cpp).
   1. Install it on your development computer.
      All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents. To work with the component in its full capacity, you do need to have a valid license.
1. Create a project:
   1. Start your C++ IDE (e.g., Visual Studio).
   1. Create a new console application.
1. Add references:
   Add reference to the Aspose.Cells component into your project, for example, `...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`.

### **Adding a Pivot Table**

To create a pivot table using Aspose.Cells:

1. Add some data to a worksheet cells using a `Cell` object's `PutValue` method. You can also use a template file already filled with data. The data will be used as the pivot table's data source.
1. Add a pivot table to the worksheet by calling the `PivotTables` collection's `Add` method (encapsulated in the `Worksheet` object).
1. Access the new `PivotTable` object from the `PivotTables` collection by passing its index. Use any of the pivot table objects encapsulated in the `PivotTable` object to manage the table.

Code examples are given below.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Name the sheet
    sheet.SetName(u"Data");

    // Get the cells collection
    Cells cells = sheet.GetCells();

    // Set values to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Employee");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Quarter");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Product");
    cell = cells.Get(u"D1");
    cell.PutValue(u"Continent");
    cell = cells.Get(u"E1");
    cell.PutValue(u"Country");
    cell = cells.Get(u"F1");
    cell.PutValue(u"Sale");

    // Fill employee names
    cell = cells.Get(u"A2");
    cell.PutValue(u"David");
    cell = cells.Get(u"A3");
    cell.PutValue(u"David");
    cell = cells.Get(u"A4");
    cell.PutValue(u"David");
    cell = cells.Get(u"A5");
    cell.PutValue(u"David");
    cell = cells.Get(u"A6");
    cell.PutValue(u"James");
    cell = cells.Get(u"A7");
    cell.PutValue(u"James");
    cell = cells.Get(u"A8");
    cell.PutValue(u"James");
    cell = cells.Get(u"A9");
    cell.PutValue(u"James");
    cell = cells.Get(u"A10");
    cell.PutValue(u"James");
    cell = cells.Get(u"A11");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A12");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A13");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A14");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A15");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A16");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A17");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A18");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A19");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A20");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A21");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A22");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A23");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A24");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A25");
    cell.PutValue(u"Jean");
    cell = cells.Get(u"A26");
    cell.PutValue(u"Jean");
    cell = cells.Get(u"A27");
    cell.PutValue(u"Jean");
    cell = cells.Get(u"A28");
    cell.PutValue(u"Ada");
    cell = cells.Get(u"A29");
    cell.PutValue(u"Ada");
    cell = cells.Get(u"A30");
    cell.PutValue(u"Ada");

    // Fill quarters
    cell = cells.Get(u"B2");
    cell.PutValue(1);
    cell = cells.Get(u"B3");
    cell.PutValue(2);
    cell = cells.Get(u"B4");
    cell.PutValue(3);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(1);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(3);
    cell = cells.Get(u"B9");
    cell.PutValue(4);
    cell = cells.Get(u"B10");
    cell.PutValue(4);
    cell = cells.Get(u"B11");
    cell.PutValue(1);
    cell = cells.Get(u"B12");
    cell.PutValue(1);
    cell = cells.Get(u"B13");
    cell.PutValue(2);
    cell = cells.Get(u"B14");
    cell.PutValue(2);
    cell = cells.Get(u"B15");
    cell.PutValue(3);
    cell = cells.Get(u"B16");
    cell.PutValue(4);
    cell = cells.Get(u"B17");
    cell.PutValue(4);
    cell = cells.Get(u"B18");
    cell.PutValue(1);
    cell = cells.Get(u"B19");
    cell.PutValue(1);
    cell = cells.Get(u"B20");
    cell.PutValue(2);
    cell = cells.Get(u"B21");
    cell.PutValue(3);
    cell = cells.Get(u"B22");
    cell.PutValue(3);
    cell = cells.Get(u"B23");
    cell.PutValue(4);
    cell = cells.Get(u"B24");
    cell.PutValue(4);
    cell = cells.Get(u"B25");
    cell.PutValue(1);
    cell = cells.Get(u"B26");
    cell.PutValue(2);
    cell = cells.Get(u"B27");
    cell.PutValue(3);
    cell = cells.Get(u"B28");
    cell.PutValue(1);
    cell = cells.Get(u"B29");
    cell.PutValue(2);
    cell = cells.Get(u"B30");
    cell.PutValue(3);

    // Fill products
    cell = cells.Get(u"C2");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C3");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C4");
    cell.PutValue(u"Chai");
    cell = cells.Get(u"C5");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C6");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C7");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C8");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C9");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C10");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C11");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C12");
    cell.PutValue(u"Chai");
    cell = cells.Get(u"C13");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C14");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C15");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C16");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C17");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C18");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C19");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C20");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C21");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C22");
    cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C23");
    cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C24");
    cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C25");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C26");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C27");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C28");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C29");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C30");
    cell.PutValue(u"Chocolade");

    // Fill continents
    cell = cells.Get(u"D2");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D3");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D4");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D5");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D6");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D7");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D8");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D9");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D10");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D11");
    cell.PutValue(u"America");
    cell = cells.Get(u"D12");
    cell.PutValue(u"America");
    cell = cells.Get(u"D13");
    cell.PutValue(u"America");
    cell = cells.Get(u"D14");
    cell.PutValue(u"America");
    cell = cells.Get(u"D15");
    cell.PutValue(u"America");
    cell = cells.Get(u"D16");
    cell.PutValue(u"America");
    cell = cells.Get(u"D17");
    cell.PutValue(u"America");
    cell = cells.Get(u"D18");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D19");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D20");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D21");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D22");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D23");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D24");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D25");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D26");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D27");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D28");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D29");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D30");
    cell.PutValue(u"Africa");

    // Fill countries
    cell = cells.Get(u"E2");
    cell.PutValue(u"China");
    cell = cells.Get(u"E3");
    cell.PutValue(u"India");
    cell = cells.Get(u"E4");
    cell.PutValue(u"Korea");
    cell = cells.Get(u"E5");
    cell.PutValue(u"India");
    cell = cells.Get(u"E6");
    cell.PutValue(u"France");
    cell = cells.Get(u"E7");
    cell.PutValue(u"France");
    cell = cells.Get(u"E8");
    cell.PutValue(u"Germany");
    cell = cells.Get(u"E9");
    cell.PutValue(u"Italy");
    cell = cells.Get(u"E10");
    cell.PutValue(u"France");
    cell = cells.Get(u"E11");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E12");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E13");
    cell.PutValue(u"Brazil");
    cell = cells.Get(u"E14");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E15");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E16");
    cell.PutValue(u"Canada");
    cell = cells.Get(u"E17");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E18");
    cell.PutValue(u"Italy");
    cell = cells.Get(u"E19");
    cell.PutValue(u"France");
    cell = cells.Get(u"E20");
    cell.PutValue(u"Italy");
    cell = cells.Get(u"E21");
    cell.PutValue(u"New Zealand");
    cell = cells.Get(u"E22");
    cell.PutValue(u"Australia");
    cell = cells.Get(u"E23");
    cell.PutValue(u"Australia");
    cell = cells.Get(u"E24");
    cell.PutValue(u"New Zealand");
    cell = cells.Get(u"E25");
    cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E26");
    cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E27");
    cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E28");
    cell.PutValue(u"Egypt");
    cell = cells.Get(u"E29");
    cell.PutValue(u"Egypt");
    cell = cells.Get(u"E30");
    cell.PutValue(u"Egypt");

    // Fill sales
    cell = cells.Get(u"F2");
    cell.PutValue(2000);
    cell = cells.Get(u"F3");
    cell.PutValue(500);
    cell = cells.Get(u"F4");
    cell.PutValue(1200);
    cell = cells.Get(u"F5");
    cell.PutValue(1500);
    cell = cells.Get(u"F6");
    cell.PutValue(500);
    cell = cells.Get(u"F7");
    cell.PutValue(1500);
    cell = cells.Get(u"F8");
    cell.PutValue(800);
    cell = cells.Get(u"F9");
    cell.PutValue(900);
    cell = cells.Get(u"F10");
    cell.PutValue(500);
    cell = cells.Get(u"F11");
    cell.PutValue(1600);
    cell = cells.Get(u"F12");
    cell.PutValue(600);
    cell = cells.Get(u"F13");
    cell.PutValue(2000);
    cell = cells.Get(u"F14");
    cell.PutValue(500);
    cell = cells.Get(u"F15");
    cell.PutValue(900);
    cell = cells.Get(u"F16");
    cell.PutValue(700);
    cell = cells.Get(u"F17");
    cell.PutValue(1400);
    cell = cells.Get(u"F18");
    cell.PutValue(1350);
    cell = cells.Get(u"F19");
    cell.PutValue(300);
    cell = cells.Get(u"F20");
    cell.PutValue(500);
    cell = cells.Get(u"F21");
    cell.PutValue(1000);
    cell = cells.Get(u"F22");
    cell.PutValue(1500);
    cell = cells.Get(u"F23");
    cell.PutValue(1500);
    cell = cells.Get(u"F24");
    cell.PutValue(1600);
    cell = cells.Get(u"F25");
    cell.PutValue(1000);
    cell = cells.Get(u"F26");
    cell.PutValue(1200);
    cell = cells.Get(u"F27");
    cell.PutValue(1300);
    cell = cells.Get(u"F28");
    cell.PutValue(1500);
    cell = cells.Get(u"F29");
    cell.PutValue(1400);
    cell = cells.Get(u"F30");
    cell.PutValue(1000);

    // Add a new sheet
    Worksheet sheet2 = workbook.GetWorksheets().Get(workbook.GetWorksheets().Add());
    sheet2.SetName(u"PivotTable");

    // Get the pivot tables collection
    PivotTableCollection pivotTables = sheet2.GetPivotTables();

    // Add a pivot table
    int index = pivotTables.Add(u"=Data!A1:F30", u"B3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);

    // Show grand totals
    pivotTable.SetShowRowGrandTotals(true);
    pivotTable.SetShowColumnGrandTotals(true);

    // Set auto format
    pivotTable.SetIsAutoFormat(true);
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report6);

    // Add fields to row area
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 1);

    // Add fields to column area
    pivotTable.AddFieldToArea(PivotFieldType::Column, 3);

    // Add fields to data area
    pivotTable.AddFieldToArea(PivotFieldType::Data, 5);

    // Set number format for the first data field
    pivotTable.GetDataFields().Get(0).SetNumberFormat(u"$#,##0.00");

    // Save the workbook
    workbook.Save(outDir + u"pivotTable_test.out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Adding a Pivot Chart**

To create a PivotChart using Aspose.Cells:

1. Add a chart.
1. Set the `PivotSource` of the chart to refer to an existing pivot table in the spreadsheet.
1. Set other attributes.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"pivotTable_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"pivotChart_test_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Adding a new sheet
    Worksheet sheet3 = workbook.GetWorksheets().Get(workbook.GetWorksheets().Add(SheetType::Chart));

    // Naming the sheet
    sheet3.SetName(u"PivotChart");

    // Adding a column chart
    int index = sheet3.GetCharts().Add(ChartType::Column, 0, 5, 28, 16);

    // Setting the pivot chart data source
    sheet3.GetCharts().Get(index).SetPivotSource(u"PivotTable!PivotTable1");
    sheet3.GetCharts().Get(index).SetHidePivotFieldButtons(false);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
