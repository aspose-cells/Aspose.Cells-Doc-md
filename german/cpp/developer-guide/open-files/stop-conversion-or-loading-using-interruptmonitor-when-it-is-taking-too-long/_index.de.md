---
title: Die Umwandlung oder das Laden mit InterruptMonitor bei zu langer Dauer stoppen, mit C++
linktitle: Conversion oder Laden mit InterruptMonitor stoppen
type: docs
weight: 100
url: /de/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Erfahren Sie, wie Sie die Umwandlung oder das Laden großer Excel Dateien mit InterruptMonitor in Aspose.Cells und C++ stoppen können.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es, die Umwandlung des Arbeitsbuchs in verschiedene Formate wie PDF, HTML usw. mit dem [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/)-Objekt zu stoppen, wenn diese zu lange dauert. Der Konvertierungsprozess ist oft CPU- und speicherintensiv, weshalb es nützlich sein kann, ihn bei begrenzten Ressourcen zu unterbrechen. Sie können [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) sowohl zum Stoppen der Konvertierung als auch zum Stoppen des Ladens riesiger Arbeitsmappen verwenden. Bitte verwenden Sie für das Stoppen der Konvertierung die Eigenschaft [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getinterruptmonitor/), für das Laden riesiger Arbeitsmappen die Eigenschaft [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getinterruptmonitor/).

## ** Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert**

Der folgende Beispielcode zeigt die Verwendung des [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/)-Objekts. Der Code wandelt eine recht große Excel-Datei in PDF um. Es wird mehrere Sekunden (d.h. *mehr als 30 Sekunden*) dauern, bis die Umwandlung abgeschlossen ist, aufgrund dieser Zeilen Code.

```cpp
// Access cell J1000000 and add some text inside it.
auto cell = ws->GetCells()->GetObjectByIndex("J1000000");
cell->PutValue("This is text.");
```

Wie Sie sehen, ist **J1000000** eine ziemlich entfernte Zelle in der XLSX-Datei. Die Methode **WaitForWhileAndThenInterrupt()** unterbricht die Umwandlung nach 10 Sekunden, und das Programm beendet/stoppt. Bitte verwenden Sie den folgenden Code, um das Beispiel auszuführen.

```cpp
new StopConversionOrLoadingUsingInterruptMonitor().TestRun();
```

## **Beispielcode**

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
