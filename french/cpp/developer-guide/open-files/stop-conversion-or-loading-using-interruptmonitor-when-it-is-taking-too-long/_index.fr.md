---
title: Arrêter la conversion ou le chargement en utilisant InterruptMonitor lorsque cela prend trop de temps avec C++
linktitle: Arrêter la conversion ou le chargement en utilisant InterruptMonitor
type: docs
weight: 100
url: /fr/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Apprenez comment arrêter la conversion ou le chargement de gros fichiers Excel en utilisant InterruptMonitor dans Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet d’arrêter la conversion du classeur vers divers formats tels que PDF, HTML, etc., en utilisant l’objet [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) lorsque cela prend trop de temps. Le processus de conversion est souvent intensif en CPU et en mémoire, et il peut être utile de l’interrompre lorsque les ressources sont limitées. Vous pouvez utiliser [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) pour arrêter à la fois la conversion et le chargement de gros classeurs. Veuillez utiliser la propriété [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getinterruptmonitor/) pour arrêter la conversion et la propriété [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getinterruptmonitor/) pour arrêter le chargement de gros classeurs.

## **Arrêter la conversion ou le chargement à l'aide de InterruptMonitor lorsqu'il prend trop de temps**

Le code d’exemple suivant explique l’utilisation de l’objet [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/). Le code convertit un fichier Excel assez volumineux en PDF. La conversion prendra plusieurs secondes (plus de 30 secondes) en raison de ces lignes de code.

```cpp
// Access cell J1000000 and add some text inside it.
auto cell = ws->GetCells()->GetObjectByIndex("J1000000");
cell->PutValue("This is text.");
```

Comme vous le voyez, **J1000000** est une cellule très éloignée dans le fichier XLSX. Cependant, la méthode **WaitForWhileAndThenInterrupt()** interrompt la conversion après 10 secondes, et le programme se termine/interrupt. Veuillez utiliser le code suivant pour exécuter l’exemple.

```cpp
new StopConversionOrLoadingUsingInterruptMonitor().TestRun();
```

## **Code d'exemple**

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
{{< app/cells/assistant language="cpp" >}}
