---
title: Formatting Pivot Table with C++
linktitle: Formatting Pivot Table
type: docs
weight: 10
url: /cpp/formatting-pivot-table/
description: Learn how to customize the appearance of pivot tables using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Pivot Table Appearance**

How to Create a Pivot Table explains how to create a simple pivot table. This article describes how to customize a pivot table's appearance by setting various properties:

- Pivot table format options
- Pivot fields format options
- Data field format options

### **Setting Pivot Table Format Options**

The [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) class controls the overall pivot table and can be formatted in a number of ways.

#### **Setting the AutoFormat Type**

Microsoft Excel offers a number of different pre‑set report formats. Aspose.Cells supports these formatting options too. To access them:

1. Set [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isautoformat/) to **true**.  
2. Assign a formatting option from the [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottableautoformattype/) enumeration.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    int pivotindex = 0;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Set the PivotTable report to be automatically formatted
    pivotTable.SetIsAutoFormat(true);

    // Set the PivotTable autoformat type
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "PivotTable formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Setting Format Options**

The code sample below shows how to format the pivot table to show grand totals for rows and columns, how to set the report's field order, and how to set a custom string for null values.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Set the PivotTable report to show grand totals for rows
    pivotTable.SetShowRowGrandTotals(true);

    // Set the PivotTable report to show grand totals for columns
    pivotTable.SetShowColumnGrandTotals(true);

    // Set the PivotTable report to display a custom string in cells that contain null values
    pivotTable.SetDisplayNullString(true);
    pivotTable.SetNullString(u"null");

    // Set the PivotTable report's layout
    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "PivotTable settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Formatting Look and Feel Manually**

To format how the pivot table report looks manually, instead of using pre‑set report formats, use the [**PivotTable.Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) and [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) methods. Create a style object for your desired formatting, for example:

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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    auto pivot = worksheet.GetPivotTables().Get(0);

    // Set pivot table style
    pivot.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);

    // Create a new style
    Style style = workbook.CreateStyle();
    style.GetFont().SetName(u"Arial Black");
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    // Apply style to pivot table
    pivot.FormatAll(style);

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table style applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Setting Pivot Field Format Options**

The [**PivotField**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/) class represents a field in a pivot table and can be formatted in a number of ways. The code sample below shows how to:

- Access row fields.
- Set subtotals.
- Set autosort.
- Set autoshow.

#### **Setting Row/Column/Page Fields Format**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"Book1.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Set the PivotTable report to show grand totals for rows
    pivotTable.SetShowRowGrandTotals(true);

    // Access the row fields
    PivotFieldCollection pivotFields = pivotTable.GetRowFields();

    // Access the first row field in the row fields
    PivotField pivotField = pivotFields.Get(0);

    // Set subtotals
    pivotField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    pivotField.SetSubtotals(PivotFieldSubtotalType::Count, true);

    // Set autosort options
    // Enable auto sort for the field
    pivotField.SetIsAutoSort(true);

    // Set the field to sort in ascending order
    pivotField.SetIsAscendSort(true);

    // Use the field itself for auto sort
    pivotField.SetAutoSortField(-5);

    // Set autoShow options
    // Enable auto show for the field
    pivotField.SetIsAutoShow(true);

    // Set the field to show in descending order
    pivotField.SetIsAscendShow(false);

    // Use a data field for auto show
    pivotField.SetAutoShowField(0);

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "PivotTable settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Setting Data Fields Format**

The code sample below shows how to set display formats and number formats for data fields.

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

    // Load a template file
    U16String inputFilePath = srcDir + u"Book1.xls";
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Access the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Access the first data field
    PivotField pivotField = pivotFields.Get(0);

    // Set data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::PercentageOf);

    // Set the base field
    pivotField.GetShowValuesSetting().SetBaseFieldIndex(1);

    // Set the base item
    pivotField.GetShowValuesSetting().SetBaseItemPositionType(PivotItemPositionType::Next);

    // Set number format
    pivotField.SetNumber(10);

    // Save the Excel file
    U16String outputFilePath = outDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Clearing Pivot Fields**

The [**PivotFieldCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfieldcollection/) has a method named [**Clear()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfieldcollection/clear/) that allows you to clear pivot fields. Use it when you want to clear all the pivot fields in the areas, for example, page, column, row, or data. The code sample below shows how to clear all the pivot fields in a data area.

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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the pivot tables in the sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();

    // Get the first PivotTable
    PivotTable pivotTable = pivotTables.Get(0);

    // Clear all the data fields
    pivotTable.GetDataFields().Clear();

    // Add a new data field
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Betrag Netto FW");

    // Set the refresh data flag off
    pivotTable.SetRefreshDataFlag(false);

    // Refresh and calculate the pivot table data
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
