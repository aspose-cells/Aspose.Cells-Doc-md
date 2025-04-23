---
title: Detener la conversión o carga usando InterruptMonitor cuando toma demasiado tiempo con C++
linktitle: Detener la conversión o carga usando InterruptMonitor
type: docs
weight: 100
url: /es/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Aprenda cómo detener la conversión o carga de archivos grandes de Excel usando InterruptMonitor en Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

Aspose.Cells le permite detener la conversión de un libro de trabajo a varios formatos como PDF, HTML, etc., usando el objeto [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) cuando toma demasiado tiempo. El proceso de conversión suele ser intensivo en CPU y memoria, y a menudo es útil detenerlo cuando los recursos son limitados. Puede usar [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) tanto para detener la conversión como para detener la carga de libros de trabajo enormes. Por favor, use la propiedad [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getinterruptmonitor/) para detener la conversión y la propiedad [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getinterruptmonitor/) para detener la carga de libros de trabajo grandes.

## **Detener la conversión o carga utilizando InterruptMonitor cuando está tardando demasiado**

El siguiente código de ejemplo explica el uso del objeto [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/). El código convierte un archivo de Excel bastante grande a PDF. Tomará varios segundos (es decir, *más de 30 segundos*) en convertirlo debido a estas líneas de código.

```cpp
// Access cell J1000000 and add some text inside it.
auto cell = ws->GetCells()->GetObjectByIndex("J1000000");
cell->PutValue("This is text.");
```

Como ves, **J1000000** es una celda bastante lejana en el archivo XLSX. Sin embargo, el método **WaitForWhileAndThenInterrupt()** interrumpe la conversión después de 10 segundos, y el programa termina/detiene. Por favor, usa el siguiente código para ejecutar el código de ejemplo.

```cpp
new StopConversionOrLoadingUsingInterruptMonitor().TestRun();
```

## **Código de muestra**

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
