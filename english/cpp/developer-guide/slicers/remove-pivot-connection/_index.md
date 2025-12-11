---  
title: Remove Pivot Connection with C++  
linktitle: Remove Pivot Connection  
type: docs  
weight: 30  
url: /cpp/remove-pivot-connection/  
description: Learn how to remove a pivot connection with the Aspose.Cells library using C++.  
keywords: Remove pivot connection without Office 2013, Office 2016, Office 2019, and Office 365.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

If you want to disassociate a slicer from a pivot table in Excel, you need to right‑click the slicer and select **Report Connections…**. In the options list, you can modify the check box. Similarly, if you want to disassociate a slicer from a pivot table programmatically using the Aspose.Cells API, please use the [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/removepivotconnection/) method. It will disassociate the slicer from the pivot table.  

## **Disassociate slicer and pivot table**  

The following sample code loads the [sample Excel file](remove-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicer and then disassociates the slicer from the pivot table. Finally, it saves the workbook as [output Excel file](remove-pivot-connection-out.xlsx).  

## **Sample Code**  

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing a slicer
    U16String inputFilePath = u"remove-pivot-connection.xlsx";
    Workbook wb(inputFilePath);

    // Access the first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTable pivottable = ws.GetPivotTables().Get(0);

    // Access the first slicer inside the slicer collection
    Slicer slicer = ws.GetSlicers().Get(0);

    // Remove PivotTable connection
    slicer.RemovePivotConnection(pivottable);

    // Save the workbook in the output XLSX format
    U16String outputFilePath = u"remove-pivot-connection-out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot connection removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
