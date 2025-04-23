---
title: Excel , OpenOffice , Json , Csv und Html Dateien mit C++ laden und verwalten
linktitle: Dateien öffnen
type: docs
weight: 20
url: /de/cpp/loading-saving-and-managing/
description: Mit Aspose.Cells for C++ ist es einfach, Excel , CSV , TSV , ODS , HTML , Numbers , Json , XML , PDF , Jpg , Tiff , Bild , Mht und XPS Dateien zu erstellen, zu öffnen und zu verwalten.
---

{{% alert color="primary" %}}

Mit Aspose.Cells for C++ ist es einfach, Excel-Dateien zu erstellen, zu öffnen und zu verwalten, z.B. um Daten abzurufen oder ein Designer-Template zu verwenden, um die Entwicklungszeit zu verkürzen.

{{% /alert %}}

## **Neue Arbeitsmappe erstellen**
Das folgende Beispiel erstellt ein neues Arbeitsbuch von Grund auf.

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

## **Datei öffnen und speichern**
Mit Aspose.Cells for C++ ist es einfach, Excel-Dateien zu öffnen, zu speichern und zu verwalten.

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

## **Fortgeschrittene Themen**
- [Verschiedene Möglichkeiten, Dateien zu öffnen](/cells/de/cpp/different-ways-to-open-files/)
- [Gefilterte definierte Namen beim Laden des Arbeitsbuchs](/cells/de/cpp/filter-defined-names-while-loading-workbook/)
- [Objekte filtern beim Laden des Arbeitsbuchs oder des Arbeitsblatts](/cells/de/cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Daten filtern beim Laden des Arbeitsbuchs aus einer Vorlage](/cells/de/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Warnungen beim Laden der Excel-Datei anzeigen](/cells/de/cpp/get-warnings-while-loading-excel-file/)
- [Quell-Excel-Datei ohne Diagramme laden](/cells/de/cpp/load-source-excel-file-without-charts/)
- [Bestimmte Arbeitsblätter in einer Arbeitsmappe laden](/cells/de/cpp/load-specific-worksheets-in-a-workbook/)
- [Arbeitsmappe mit festgelegter Druckerpapiereinstellung laden](/cells/de/cpp/load-workbook-with-specified-printer-paper-size/)
- [Öffnen von verschiedenen Microsoft Excel-Versionen Dateien](/cells/de/cpp/opening-different-microsoft-excel-versions-files/)
- [Öffnen von Dateien mit verschiedenen Formaten](/cells/de/cpp/opening-files-with-different-formats/)
- [Optimierung des Speicherverbrauchs beim Arbeiten mit großen Dateien mit umfangreichen Datensätzen](/cells/de/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Lesen von Numbers-Tabellen, entwickelt von Apple Inc., mit Aspose.Cells](/cells/de/cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Unterbrechungsüberwachung bei langandauernder Konvertierung oder beim Laden mittels InterruptMonitor stoppen](/cells/de/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Verwendung der LightCells-API](/cells/de/cpp/using-lightcells-api/)
- [Konvertieren von CSV in JSON](/cells/de/cpp/convert-csv-to-json/)
- [Excel nach JSON konvertieren](/cells/de/cpp/convert-excel-to-json/)
- [JSON in CSV konvertieren](/cells/de/cpp/convert-json-to-csv/)
- [JSON in Excel konvertieren](/cells/de/cpp/convert-json-to-excel/)
- [Excel in Html umwandeln](/cells/de/cpp/convert-excel-to-html/)
