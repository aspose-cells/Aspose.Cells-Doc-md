---
title: Parsing Pivot Cached Records while loading Excel file with C++
linktitle: Parsing Pivot Cached Records
type: docs
weight: 70
url: /cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: Learn how to parse pivot cached records while loading Excel files using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

When you create a Pivot Table, Microsoft Excel takes a copy of the source data and stores it in the Pivot Cache. The Pivot Cache is held inside the memory of Microsoft Excel. You cannot see it but that is the data the Pivot Table references when you build your Pivot Table or change a Slicer selection or move rows/columns around. This enables Microsoft Excel to be very responsive to changes in the Pivot Table but it can also double the size of your file. After all, the Pivot Cache is just a duplicate of your source data so it makes sense that your file size will be potentially double.

When you load your Excel file inside the Workbook object, you can decide whether you also want to load the records of Pivot Cache or not, using the [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/) property. The default value of this property is **false**. If Pivot Cache is quite big, it can increase the performance. But if you also want to load the records of Pivot Cache, you should set this property as **true**.

## **Parsing Pivot Cached Records while loading Excel file**

The following sample code explains the usage of [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/) property. It loads the [sample Excel file](61767773.xlsx) while parsing the pivot cached records. Then it refreshes the pivot table and saves it as the [output Excel file](61767774.xlsx).

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

    // Create load options
    LoadOptions options;

    // Set ParsingPivotCachedRecords true, default value is false
    options.SetParsingPivotCachedRecords(true);

    // Load the sample Excel file containing pivot table cached records
    U16String inputFilePath = srcDir + u"sampleParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    Workbook wb(inputFilePath, options);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Set refresh data flag true
    pt.SetRefreshDataFlag(true);

    // Refresh and calculate pivot table
    pt.RefreshData();
    pt.CalculateData();

    // Set refresh data flag false
    pt.SetRefreshDataFlag(false);

    // Save the output Excel file
    U16String outputFilePath = outDir + u"outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot table cached records parsed and refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}