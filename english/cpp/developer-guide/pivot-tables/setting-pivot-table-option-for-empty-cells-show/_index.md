---
title: Setting Pivot Table Option - For Empty Cells Show with C++
linktitle: Setting Pivot Table Option - For Empty Cells Show
type: docs
weight: 40
url: /cpp/setting-pivot-table-option-for-empty-cells-show/
description: Learn how to set the "For empty cells show" option in pivot tables using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can set different pivot table options using Aspose.Cells. One such option is **“For empty cells show.”** By setting this option, all empty cells in a pivot table are displayed as a specified string.

{{% /alert %}}

## **Setting Pivot Table Option in Microsoft Excel**

To find and set this option in Microsoft Excel:

1. Select a pivot table and right‑click.  
2. Select **PivotTable Options**.  
3. Select the **Layout & Format** tab.  
4. Select the **For empty cells show** option and specify a string.

## **Setting Pivot Table Option Using Aspose.Cells**

Aspose.Cells provides the [**PivotTable.GetDisplayNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getdisplaynullstring/) and [**PivotTable.GetNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getnullstring/) methods for setting the **“For empty cells show”** pivot table option.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Get the first pivot table
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    PivotTable pt = pivotTables.Get(0);

    // Indicate whether to display the empty cell value
    pt.SetDisplayNullString(true);

    // Set the null string
    pt.SetNullString(u"null");

    // Calculate pivot table data
    pt.CalculateData();

    // Set RefreshDataOnOpeningFile to false
    pt.SetRefreshDataOnOpeningFile(false);

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Related Articles

- [Formatting Pivot Table](/cells/cpp/formatting-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
