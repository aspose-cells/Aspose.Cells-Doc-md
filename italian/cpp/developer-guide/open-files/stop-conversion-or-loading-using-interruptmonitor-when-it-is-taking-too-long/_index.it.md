---
title: Interrompi la conversione o il caricamento usando InterruptMonitor quando richiede troppo tempo con C++
linktitle: Interrompi la conversione o il caricamento usando InterruptMonitor
type: docs
weight: 100
url: /it/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Impara come interrompere la conversione o il caricamento di grandi file Excel usando InterruptMonitor in Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells ti permette di interrompere la conversione di un workbook in vari formati come PDF, HTML, ecc., usando l'oggetto [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) quando richiede troppo tempo. Il processo di conversione è spesso intensivo in CPU e memoria ed è spesso utile arrestarlo quando le risorse sono limitate. Puoi usare [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) sia per interrompere la conversione sia per interrompere il caricamento di grandi workbooks. Si prega di usare la proprietà [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getinterruptmonitor/) per interrompere la conversione e la proprietà [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getinterruptmonitor/) per interrompere il caricamento di grandi workbooks.

## **Interrompere la conversione o il caricamento utilizzando InterruptMonitor quando sta impiegando troppo tempo**

Il codice di esempio seguente spiega l'uso dell'oggetto [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/). Il codice converte un file Excel abbastanza grande in PDF. Ci vorranno diversi secondi (cioè, *più di 30 secondi*) per completare la conversione a causa di queste righe di codice.

```cpp
// Access cell J1000000 and add some text inside it.
auto cell = ws->GetCells()->GetObjectByIndex("J1000000");
cell->PutValue("This is text.");
```

Come puoi vedere, **J1000000** è una cella abbastanza lontana nel file XLSX. Tuttavia, il metodo **WaitForWhileAndThenInterrupt()** interrompe la conversione dopo 10 secondi, e il programma termina/interrompe. Usa il seguente codice per eseguire l'esempio.

```cpp
new StopConversionOrLoadingUsingInterruptMonitor().TestRun();
```

## **Codice di Esempio**

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
