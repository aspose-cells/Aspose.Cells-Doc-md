---
title: Caricare e gestire file Excel, OpenOffice, Json, Csv e Html con C++
linktitle: Aprire i file
type: docs
weight: 20
url: /it/cpp/loading-saving-and-managing/
description: Con Aspose.Cells for C++, è semplice creare, aprire e gestire file Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Immagini, Mht e XPS.
---

{{% alert color="primary" %}}

Con Aspose.Cells for C++, è semplice creare, aprire e gestire file Excel, ad esempio per recuperare dati o utilizzare un modello di progettazione per accelerare il processo di sviluppo.

{{% /alert %}}

## **Creazione di un nuovo foglio di lavoro**
Il seguente esempio crea un nuovo workbook da zero.

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

## **Aprire e salvare un file**
Con Aspose.Cells for C++, è semplice aprire, salvare e gestire i file Excel.

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

## **Argomenti Avanzati**
- [Diversi modi per aprire i file](/cells/it/cpp/different-ways-to-open-files/)
- [Filtrare i nomi definiti durante il caricamento del workbook](/cells/it/cpp/filter-defined-names-while-loading-workbook/)
- [Filtrare oggetti durante il caricamento del workbook o del foglio di lavoro](/cells/it/cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtrare il tipo di dati durante il caricamento del workbook da un file modello](/cells/it/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Ottieni avvisi durante il caricamento del file Excel](/cells/it/cpp/get-warnings-while-loading-excel-file/)
- [Carica il file Excel di origine senza grafici](/cells/it/cpp/load-source-excel-file-without-charts/)
- [Carica fogli di lavoro specifici in un libro di lavoro](/cells/it/cpp/load-specific-worksheets-in-a-workbook/)
- [Carica workbook con dimensione della carta della stampante specificata](/cells/it/cpp/load-workbook-with-specified-printer-paper-size/)
- [Apertura di file di diverse versioni di Microsoft Excel](/cells/it/cpp/opening-different-microsoft-excel-versions-files/)
- [Apertura di file con formati diversi](/cells/it/cpp/opening-files-with-different-formats/)
- [Ottimizzazione dell'uso della memoria durante la gestione di file di grandi dimensioni con grandi set di dati](/cells/it/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Leggi Foglio di calcolo numerico sviluppato da Apple Inc. usando Aspose.Cells](/cells/it/cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Interrompi la conversione o il caricamento usando InterruptMonitor quando richiede troppo tempo](/cells/it/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Utilizzo di API LightCells](/cells/it/cpp/using-lightcells-api/)
- [Convertire CSV in JSON](/cells/it/cpp/convert-csv-to-json/)
- [Converti Excel in JSON](/cells/it/cpp/convert-excel-to-json/)
- [Convertire JSON in CSV](/cells/it/cpp/convert-json-to-csv/)
- [Converti JSON in Excel](/cells/it/cpp/convert-json-to-excel/)
- [Converti Excel in Html](/cells/it/cpp/convert-excel-to-html/)
