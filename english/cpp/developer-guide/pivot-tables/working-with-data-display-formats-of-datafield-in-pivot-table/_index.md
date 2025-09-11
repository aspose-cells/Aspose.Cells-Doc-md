---
title: Working with Data Display Formats of DataField in Pivot Table with C++
linktitle: Working with Data Display Formats of DataField in Pivot Table
type: docs
weight: 140
url: /cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Learn how to work with data display formats of DataField in Pivot Table using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells supports all the data display formats of DataField.

{{% /alert %}}

## **"Rank Smallest to Largest" and "Rank Largest to Smallest" Display Format Option**

Aspose.Cells provides the ability to set the display format option for pivot fields. For this, the API provides the [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) property. To rank largest to smallest, you may set the [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) property to [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). The following code snippet demonstrates setting the display format options.

Sample source and output files can be downloaded from here for testing the sample code:

[Source Excel File](101089332.xlsx)

[Output Excel File](101089333.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"PivotTableSample.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotIndex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Accessing the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Accessing the first data field in the data fields
    PivotField pivotField = pivotFields.Get(0);

    // Setting data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::RankLargestToSmallest);

    // Calculate data
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outDir + u"PivotTableDataDisplayFormatRanking_out.xlsx");

    std::cout << "PivotTable data display format ranking applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}