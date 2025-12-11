---
title: Loading and Managing Excel, OpenOffice, JSON, CSV, and HTML Files with C++
linktitle: Open Files
type: docs
weight: 20
url: /cpp/loading-saving-and-managing/
description: With Aspose.Cells for C++, it is simple to create, open, and manage Excel, CSV, TSV, ODS, HTML, Numbers, JSON, XML, PDF, JPG, TIFF, Image, MHT, and XPS files.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

With Aspose.Cells for C++, it is simple to create, open, and manage Excel files, for example, to retrieve data or use a designer template to speed up the development process.

{{% /alert %}}

## **Creating a New Workbook**
The following example creates a new workbook from scratch.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    try
    {
        // Create a License object
        License license;

        // Set the license of Aspose.Cells to avoid the evaluation limitations
        license.SetLicense(srcDir + u"Aspose.Cells.lic");
    }
    catch (const std::exception& ex)
    {
        std::cerr << ex.what() << std::endl;
    }

    // Instantiate a Workbook object that represents an Excel file.
    Workbook wb;

    // When you create a new workbook, a default "Sheet1" is added to the workbook.
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access the "A1" cell in the sheet.
    Cell cell = sheet.GetCells().Get(u"A1");

    // Insert the "Hello World!" text into the "A1" cell
    cell.PutValue(u"Hello World!");

    // Save the Excel file.
    wb.Save(srcDir + u"MyBook_out.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Opening and Saving a File**
With Aspose.Cells for C++, it is simple to open, save, and manage Excel files.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"dest.xlsx";

    // Create a Workbook object and open an Excel file using its file path
    Workbook workbook1(inputFilePath);

    // Adding new sheet
    WorksheetCollection sheets = workbook1.GetWorksheets();
    Worksheet sheet = sheets.Add(u"MySheet");

    // Setting active sheet
    sheets.SetActiveSheetIndex(1);

    // Setting values
    Cells cells = sheet.GetCells();

    // Setting text
    cells.Get(u"A1").PutValue(u"Hello!");

    // Setting number
    cells.Get(u"A2").PutValue(1000);

    // Setting date and time
    Cell cell = cells.Get(u"A3");
    Date currentDate;
    currentDate.year = 2023; // Replace with actual current year
    currentDate.month = 10;  // Replace with actual current month
    currentDate.day = 5;     // Replace with actual current day
    currentDate.hour = 12;   // Replace with actual current hour
    currentDate.minute = 30; // Replace with actual current minute
    currentDate.second = 0;  // Replace with actual current second
    cell.PutValue(currentDate);

    // Setting style for date
    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    // Setting formula
    cells.Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Saving the workbook to disk
    workbook1.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advanced Topics**
- [Different Ways to Open Files](/cells/cpp/different-ways-to-open-files/)
- [Filter Defined Names While Loading Workbook](/cells/cpp/filter-defined-names-while-loading-workbook/)
- [Filter Objects While Loading Workbook or Worksheet](/cells/cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtering the Kind of Data While Loading the Workbook from Template File](/cells/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Get Warnings While Loading Excel File](/cells/cpp/get-warnings-while-loading-excel-file/)
- [Load Source Excel File Without Charts](/cells/cpp/load-source-excel-file-without-charts/)
- [Load Specific Worksheets in a Workbook](/cells/cpp/load-specific-worksheets-in-a-workbook/)
- [Load Workbook with Specified Printer Paper Size](/cells/cpp/load-workbook-with-specified-printer-paper-size/)
- [Opening Different Microsoft Excel Versions Files](/cells/cpp/opening-different-microsoft-excel-versions-files/)
- [Opening Files with Different Formats](/cells/cpp/opening-files-with-different-formats/)
- [Optimizing Memory Usage While Working with Big Files Having Large Datasets](/cells/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Read Numbers Spreadsheet Developed by Apple Inc. Using Aspose.Cells](/cells/cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Stop Conversion or Loading Using InterruptMonitor When It Is Taking Too Long](/cells/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Using LightCells API](/cells/cpp/using-lightcells-api/)
- [Convert CSV to JSON](/cells/cpp/convert-csv-to-json/)
- [Convert Excel to JSON](/cells/cpp/convert-excel-to-json/)
- [Convert JSON to CSV](/cells/cpp/convert-json-to-csv/)
- [Convert JSON to Excel](/cells/cpp/convert-json-to-excel/)
- [Convert Excel to HTML](/cells/cpp/convert-excel-to-html/)
{{< app/cells/assistant language="cpp" >}}
