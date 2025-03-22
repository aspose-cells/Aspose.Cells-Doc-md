---
title: Ignore Hidden Columns while Exporting Worksheet Data to Data Table with C++
linktitle: Ignore Hidden Columns while Exporting Worksheet Data to Data Table
type: docs
weight: 330
url: /cpp/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/
description: Learn how to Ignore Hidden Columns while Exporting Worksheet Data to Data Table through the Aspose.Cells for C++ API.
keywords: Export Visible Columns Data to DataTable, Export unhidden Columns Data to DataTable, Export Columns Data to DataTable and Exclude hidden Columns, Ignore Hidden Columns while Exporting Worksheet Data to Data Table
---

{{% alert color="primary" %}}

Sometimes, you want to ignore hidden columns while exporting worksheet data to a data table. You can achieve it using Aspose.Cells by setting the [**ExportTableOptions.PlotVisibleColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/exporttableoptions/plotvisiblecolumns/) to **true**. By default, its value is **false**, so you need to set it **true** to ignore the hidden columns.

{{% /alert %}}

The following sample code explains the usage of [**ExportTableOptions.PlotVisibleColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/exporttableoptions/plotvisiblecolumns/) property in ignoring the hidden columns while exporting the worksheet entire data to the data table.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"Sample.xlsx";

    // Create workbook
    Workbook workbook(inputPath);

    // Get first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create export table options
    ExportTableOptions opts;
    opts.SetPlotVisibleColumns(true);

    // Get total rows and columns
    int totalRows = worksheet.GetCells().GetMaxRow() + 1;
    int totalColumns = worksheet.GetCells().GetMaxColumn() + 1;

    // Export data to DataTable
    DataTable dt = worksheet.GetCells().ExportDataTable(0, 0, totalRows, totalColumns, opts);

    Aspose::Cells::Cleanup();
}
```