---
title: Stop conversion or loading using InterruptMonitor when it is taking too long with C++
linktitle: Stop conversion or loading using InterruptMonitor
type: docs
weight: 100
url: /cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Learn how to stop conversion or loading of large Excel files using InterruptMonitor in Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells allows you to stop the conversion of Workbook to various formats like PDF, HTML, etc. using the [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) object when it is taking too long. The conversion process is often both CPU and Memory intensive, and it is often useful to halt it when resources are limited. You can use [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) both for stopping conversion as well as to stop loading huge workbooks. Please use [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getinterruptmonitor/) property for stopping conversion and [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getinterruptmonitor/) property for loading huge workbooks.

## **Stop conversion or loading using InterruptMonitor when it is taking too long**

The following sample code explains the usage of the [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) object. The code converts quite a large Excel file to PDF. It will take several seconds (i.e., *more than 30 seconds*) to get it converted because of these lines of code.

```cpp
// Access cell J1000000 and add some text inside it.
auto cell = ws->GetCells()->GetObjectByIndex("J1000000");
cell->PutValue("This is text.");
```

As you see, **J1000000** is quite a farther cell in the XLSX file. However, the **WaitForWhileAndThenInterrupt()** method interrupts the conversion after 10 seconds, and the program ends/terminates. Please use the following code to execute the sample code.

```cpp
new StopConversionOrLoadingUsingInterruptMonitor().TestRun();
```

## **Sample Code**

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
