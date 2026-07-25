---  
title: Disable Pivot Table Ribbons with C++  
linktitle: Disable Pivot Table Ribbons  
type: docs  
weight: 90  
url: /cpp/disable-pivot-table-ribbons/  
description: Learn how to disable pivot table ribbons in Excel files using Aspose.Cells for C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}

Pivot table‑based reports are useful but prone to error if target users do not have detailed knowledge of Excel to configure these reports. In these circumstances, organizations will want to restrict users from being able to change a pivot table‑based report. Common pivot table features, such as adding additional filters, slicers, fields, or changing the order of certain items in the report, are generally not recommended for all users. On the other hand, these users should also be able to refresh the report and use existing filters or slicers. Aspose.Cells provides this ability to developers for restricting users from changing these reports while creating them. For this purpose, Excel offers a feature to disable the pivot table ribbon, and the same is provided by Aspose.Cells. Developers can disable the ribbon that contains controls to modify these reports.

{{% /alert %}}

## **Disable Pivot Table Ribbon using PivotTable.EnableWizard**

The following code demonstrates this feature by accessing a pivot table from a sheet and then setting **SetEnableWizard(false)**. A sample pivot table file can be downloaded from the following link.

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
    U16String inputFilePath = srcDir + u"pivot_table_test.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Access the pivot table in the first sheet
    PivotTable pt = wb.GetWorksheets().Get(0).GetPivotTables().Get(0);

    // Disable ribbon for this pivot table
    pt.SetEnableWizard(false);

    // Save output file
    wb.Save(outputFilePath);

    std::cout << "Pivot table ribbon disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
