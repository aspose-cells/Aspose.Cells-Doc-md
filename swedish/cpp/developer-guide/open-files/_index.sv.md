---
title: Ladda och hantera Excel , OpenOffice , Json , Csv och Html filer med C++
linktitle: Öppna filer
type: docs
weight: 20
url: /sv/cpp/loading-saving-and-managing/
description: Med Aspose.Cells for C++ är det enkelt att skapa, öppna och hantera Excel , CSV , TSV , ODS , HTML , Numbers , Json , XML , Pdf , Jpg , Tiff , Bild , Mht och XPS filer.
---

{{% alert color="primary" %}}

 Med Aspose.Cells for C++ är det enkelt att skapa, öppna och hantera Excel-filer, till exempel för att hämta data eller använda en designer-mall för att snabba på utvecklingsprocessen.

{{% /alert %}}

## **Skapa en ny arbetsbok**
Följande exempel skapar en ny arbetsbok från grunden.

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

    // Instantiate a Workbook object that represents Excel file.
    Workbook wb;

    // When you create a new workbook, a default "Sheet1" is added to the workbook.
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access the "A1" cell in the sheet.
    Cell cell = sheet.GetCells().Get(u"A1");

    // Input the "Hello World!" text into the "A1" cell
    cell.PutValue(u"Hello World!");

    // Save the Excel file.
    wb.Save(srcDir + u"MyBook_out.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## ** Öppna och spara en fil**
 Med Aspose.Cells for C++ är det enkelt att öppna, spara och hantera Excel-filer.

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

    // Setting Date Time
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

## **Avancerade ämnen**
- [Olika sätt att öppna filer](/cells/sv/cpp/different-ways-to-open-files/)
- [Filtrera definierade namn vid laddning av arbetsbok](/cells/sv/cpp/filter-defined-names-while-loading-workbook/)
- [Filtrera objekt vid laddning av arbetsbok eller kalkylblad](/cells/sv/cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtrera vilken typ av data som laddas från mallfilen](/cells/sv/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Få varningar vid laddning av Excel-fil](/cells/sv/cpp/get-warnings-while-loading-excel-file/)
- [Ladda käll-Excel-fil utan diagram](/cells/sv/cpp/load-source-excel-file-without-charts/)
- [Ladda specifika arbetsblad i en arbetsbok](/cells/sv/cpp/load-specific-worksheets-in-a-workbook/)
- [Ladda arbetsbok med specificerad pappersstorlek](/cells/sv/cpp/load-workbook-with-specified-printer-paper-size/)
- [Öppna filer från olika Microsoft Excel-versioner](/cells/sv/cpp/opening-different-microsoft-excel-versions-files/)
- [Öppna filer med olika format](/cells/sv/cpp/opening-files-with-different-formats/)
- [Optimerar minnesanvändning vid arbete med stora filer med stora dataset](/cells/sv/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Läs Numbers-ark utvecklat av Apple Inc. med Aspose.Cells](/cells/sv/cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Avsluta konvertering eller laddning med InterruptMonitor när det tar för lång tid](/cells/sv/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Använda LightCells API](/cells/sv/cpp/using-lightcells-api/)
- [Konvertera CSV till JSON](/cells/sv/cpp/convert-csv-to-json/)
- [Konvertera Excel till JSON](/cells/sv/cpp/convert-excel-to-json/)
- [Konvertera JSON till CSV](/cells/sv/cpp/convert-json-to-csv/)
- [Konvertera JSON till Excel](/cells/sv/cpp/convert-json-to-excel/)
- [Konvertera Excel till Html](/cells/sv/cpp/convert-excel-to-html/)
