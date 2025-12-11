---
title: Add Pivot Connection with C++
linktitle: Add Pivot Connection
type: docs
weight: 30
url: /cpp/add-pivot-connection/
description: Learn how to add a pivot connection with the Aspose.Cells library using C++.
keywords: Add pivot connection for Office 2013, Office 2016, Office 2019, and Office 365.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If you want to associate a slicer and a pivot table in Excel, you need to right‑click the slicer and select the **Report Connections...** item. In the options list, you can toggle the check box. Similarly, if you want to associate a slicer and a pivot table programmatically using the Aspose.Cells API, please use the [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/addpivotconnection/) method. It will associate the slicer with the pivot table.

## **Associate Slicer and PivotTable**

The following sample code loads the [sample Excel file](add-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicer and then associates the slicer with the pivot table. Finally, it saves the workbook as [output Excel file](add-pivot-connection-out.xlsx).

## **Sample Code**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"add-pivot-connection.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"add-pivot-connection-out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    PivotTable pivotTable = pivotTables.Get(0);

    // Access the first slicer inside the slicer collection
    SlicerCollection slicers = worksheet.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Add PivotTable connection
    slicer.AddPivotConnection(pivotTable);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "PivotTable connection added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
