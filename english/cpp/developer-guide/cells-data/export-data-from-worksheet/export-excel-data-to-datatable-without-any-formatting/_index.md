---
title: Export Excel Data to DataTable without any Formatting with C++
linktitle: Export Excel Data to DataTable without Formatting
type: docs
weight: 280
url: /cpp/export-excel-data-to-datatable-without-any-formatting/
description: Learn how to Export Excel Data to DataTable without any Formatting through the Aspose.Cells for C++ API.
keywords: Export Excel Data to DataTable without any Formatting, Specify Cell Value Format Strategy, Add Format Strategy When Exporting Data to DataTable.
---

{{% alert color="primary" %}}

Sometimes users want to export Excel data into a data table without any formatting. For example, if some cell has a value 0.012345 and it is formatted to display two decimal places, then when the user exports Excel data to a data table, it will be exported as 0.01 and not as 0.012345. To deal with this problem, Aspose.Cells has provided the [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/exporttableoptions/formatstrategy/) property, which can take one of these three values:

- **CellValueFormatStrategy::CellStyle**
- **CellValueFormatStrategy::DisplayStyle**
- **CellValueFormatStrategy::None**

If you set it to [**CellValueFormatStrategy::None**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/), then it will export the data without any formatting.

{{% /alert %}}

## Sample Code

The following sample explains the use of the [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/exporttableoptions/formatstrategy/) property to export Excel data with and without any formatting.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Put value inside the cell
    cell.PutValue(0.012345);

    // Format the cell that it should display 0.01 instead of 0.012345
    Style style = cell.GetStyle();
    style.SetNumber(2);
    cell.SetStyle(style);

    // Display the cell values as it displays in excel
    std::cout << "Cell String Value: " << cell.GetStringValue().ToUtf8() << std::endl;

    // Display the cell value without any format
    std::cout << "Cell String Value without Format: " << cell.GetStringValue(CellValueFormatStrategy::None).ToUtf8() << std::endl;

    // Export Data Table Options with FormatStrategy as CellStyle
    ExportTableOptions opts;
    opts.SetExportAsString(true);
    opts.SetFormatStrategy(CellValueFormatStrategy::CellStyle);

    // Export Data Table
    DataTable dt = worksheet.GetCells().ExportDataTable(0, 0, 1, 1, opts);

    // Display the value of very first cell
    std::cout << "Export Data Table with Format Strategy as Cell Style: " << dt.GetRows().Get(0).Get(0).ToString().ToUtf8() << std::endl;

    // Export Data Table Options with FormatStrategy as None
    opts.SetFormatStrategy(CellValueFormatStrategy::None);
    dt = worksheet.GetCells().ExportDataTable(0, 0, 1, 1, opts);

    // Display the value of very first cell
    std::cout << "Export Data Table with Format Strategy as None: " << dt.GetRows().Get(0).Get(0).ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Console Output**

Below is the console debug output of the above sample code:

{{< highlight java >}}
Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345
{{< /highlight >}}