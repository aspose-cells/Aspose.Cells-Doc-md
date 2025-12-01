---
title: Refresh and Calculate Pivot Table having Calculated Items with C++
linktitle: Refresh and Calculate Pivot Table having Calculated Items
type: docs
weight: 40
url: /cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Refresh and calculate pivot table with calculated items using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells now supports refreshing and calculating pivot table having calculated items. Please use the [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) and [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) as usual to perform this function.

{{% /alert %}}

## **Refresh and Calculate Pivot Table having Calculated Items**

The following sample code loads the [source excel file](5115238.xlsx) which contains a pivot table having three calculated items such as "add", "div", "div2". We first change the value of cell D2 to 20 and then refresh and calculate the pivot table using Aspose.Cells APIs and save the workbook in PDF format. The results in the [output PDF](5115229.pdf) show that Aspose.Cells refreshed and calculated the pivot table having calculated items successfully. You can verify it using Microsoft Excel by manually putting the value 20 in cell D2 and then refreshing the pivot table via Alt+F5 shortcut key or clicking the pivot table Refresh button.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    
    // Load source Excel file containing a pivot table having calculated items
    U16String sampleFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(sampleFilePath);

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell D2
    sheet.GetCells().Get(u"D2").PutValue(20);

    // Refresh and calculate all the pivot tables inside this sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    for (int32_t i = 0; i < pivotTables.GetCount(); ++i)
    {
        PivotTable pt = pivotTables.Get(i);
        pt.RefreshData();
        pt.CalculateData();
    }

    // Save the workbook in output PDF
    U16String outputFilePath = srcDir + u"RefreshAndCalculateItems_out.pdf";
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
