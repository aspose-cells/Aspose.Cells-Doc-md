---
title: Stoppa konvertering eller inläsning med InterruptMonitor när det tar för lång tid i C++
linktitle: Stoppa konvertering eller inläsning med InterruptMonitor
type: docs
weight: 100
url: /sv/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Lär dig hur du stoppar konvertering eller inläsning av stora Excel filer med hjälp av InterruptMonitor i Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

Aspose.Cells tillåter dig att stoppa konverteringen av arbetsboken till olika format som PDF, HTML etc. med hjälp av [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/)-objektet när det tar för lång tid. Konverteringsprocessen är ofta både CPU- och minneskrävande, och det är ofta användbart att stoppa den när resurser är begränsade. Du kan använda [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) för att stoppa både konverteringen och inläsningen av stora arbetsböcker. Använd egenskapen [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getinterruptmonitor/) för att stoppa konverteringen och egenskapen [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getinterruptmonitor/) för att stoppa inläsningen av stora arbetsböcker.

## **Stoppa konvertering eller laddning med hjälp av InterruptMonitor när det tar för lång tid**

Följande exempel kod förklarar användningen av [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/)-objektet. Koden konverterar en ganska stor Excel-fil till PDF. Det tar flera sekunder (dvs. *mer än 30 sekunder*) att slutföra konverteringen på grund av dessa kodrader.

```cpp
// Access cell J1000000 and add some text inside it.
auto cell = ws->GetCells()->GetObjectByIndex("J1000000");
cell->PutValue("This is text.");
```

Som du ser är **J1000000** mycket avlägset cellen i XLSX-filen. Metoden **WaitForWhileAndThenInterrupt()** avbryter dock konverteringen efter 10 sekunder, och programmet avslutas/avslutas. Använd följande kod för att köra exempel-koden.

```cpp
new StopConversionOrLoadingUsingInterruptMonitor().TestRun();
```

## **Exempelkod**

```c++
#include <iostream>
#include <thread>
#include <chrono>
#include <atomic>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

class StopConversionOrLoadingUsingInterruptMonitor
{
private:
    // Output directory
    static U16String outputDir;

    // Create InterruptMonitor object
    InterruptMonitor im;

    std::atomic<bool> conversionCompleted{false};

    // This function will create workbook and convert it to Pdf format
    void CreateWorkbookAndConvertItToPdfFormat()
    {
        // Create a workbook object
        Workbook wb;

        // Assign it InterruptMonitor object
        wb.SetInterruptMonitor(im);

        // Access first worksheet
        Worksheet ws = wb.GetWorksheets().Get(0);

        // Access cell J1000000 and add some text inside it.
        Cell cell = ws.GetCells().Get(u"J1000000");
        cell.PutValue(u"This is text.");

        try
        {
            // Save the workbook to Pdf format
            wb.Save(outputDir + u"output_InterruptMonitor.pdf");

            // Show successful message
            cout << "Excel to PDF - Successful Conversion" << endl;

            conversionCompleted = true;
        }
        catch (CellsException& ex)
        {
            if (ex.GetCode() == ExceptionType::Interrupted)
            {
                cout << "Conversion process is interrupted - Message: " << ex.GetErrorMessage().ToUtf8() << endl;
            }
            else
            {
                throw;
            }
        }
    }

    // This function will interrupt the conversion process after 10s
    void WaitForWhileAndThenInterrupt()
    {
        auto start = chrono::steady_clock::now();
        while (chrono::steady_clock::now() - start < chrono::seconds(10))
        {
            if (conversionCompleted.load())
                return;
            this_thread::sleep_for(chrono::milliseconds(100));
        }
        im.Interrupt();
    }

public:
    void TestRun()
    {
        thread monitorThread(&StopConversionOrLoadingUsingInterruptMonitor::WaitForWhileAndThenInterrupt, this);
        thread conversionThread(&StopConversionOrLoadingUsingInterruptMonitor::CreateWorkbookAndConvertItToPdfFormat, this);

        monitorThread.join();
        conversionThread.join();
    }

    static void Run()
    {
        StopConversionOrLoadingUsingInterruptMonitor instance;
        instance.TestRun();

        cout << "StopConversionOrLoadingUsingInterruptMonitor executed successfully." << endl;
    }
};

U16String StopConversionOrLoadingUsingInterruptMonitor::outputDir = u"..\\Data\\02_OutputDirectory\\";

int main()
{
    Aspose::Cells::Startup();
    StopConversionOrLoadingUsingInterruptMonitor::Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```
