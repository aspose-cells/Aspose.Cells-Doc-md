---
title: Show Report Filter Pages Option with C++
linktitle: Show Report Filter Pages Option
type: docs
weight: 110
url: /cpp/show-report-filter-pages-option/
description: Learn how to enable the "Show Report Filter Pages" option in pivot tables using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Show Report Filter Pages Option**
Excel supports creating pivot tables, adding report filters, and enabling the "Show Report Filter Pages" option. Aspose.Cells also supports this feature, enabling the "Show Report Filter Pages" option on the created pivot table. Below is a screenshot showing the "Show Report Filter Pages" option in Excel.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

Sample source file and output files can be downloaded from here for testing the sample code:

[Source Excel File](81920786.xlsx)  

[Output Excel File](81920787.xlsx)

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

    // Load template file
    Workbook wb(srcDir + u"samplePivotTable.xlsx");

    // Get first pivot table in the worksheet
    PivotTable pt = wb.GetWorksheets().Get(1).GetPivotTables().Get(0);

    // Set pivot field
    pt.ShowReportFilterPage(pt.GetPageFields().Get(0));

    // Set position index for showing report filter pages
    pt.ShowReportFilterPageByIndex(pt.GetPageFields().Get(0).GetPosition());

    // Set the page field name
    pt.ShowReportFilterPageByName(pt.GetPageFields().Get(0).GetName());

    // Save the output file
    wb.Save(outDir + u"outputSamplePivotTable.xlsx");

    std::cout << "Pivot table report filter pages set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
