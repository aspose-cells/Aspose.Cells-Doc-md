---
title: Остановить конвертацию или загрузку с помощью InterruptMonitor, если процесс занимает слишком много времени в C++
linktitle: Остановить конвертацию или загрузку с помощью InterruptMonitor
type: docs
weight: 100
url: /ru/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Узнайте, как останавливать конвертацию или загрузку больших файлов Excel с помощью InterruptMonitor в Aspose.Cells и C++.
---

## **Возможные сценарии использования**

Aspose.Cells позволяет останавливать конвертацию книги в различные форматы, такие как PDF, HTML и др., с помощью объекта [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/), если процесс занимает слишком много времени. Процесс конвертации часто требует значительных ресурсов CPU и памяти, поэтому его часто полезно прервать при ограниченных ресурсах. Для остановки как процесса конвертации, так и загрузки больших книг используйте свойства [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/), [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getinterruptmonitor/) и [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getinterruptmonitor/).

## **Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени**

Следующий пример показывает использование объекта [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/). Скрипт конвертирует достаточно большой Excel-файл в PDF. Процесс займет несколько секунд (то есть, более 30 секунд), из-за этого кода.

```cpp
// Access cell J1000000 and add some text inside it.
auto cell = ws->GetCells()->GetObjectByIndex("J1000000");
cell->PutValue("This is text.");
```

Как видно, **J1000000** — это очень дальняя ячейка в файле XLSX. Однако метод **WaitForWhileAndThenInterrupt()** прерывает конвертацию через 10 секунд, и программа завершает работу. Используйте следующий код для выполнения этого примера.

```cpp
new StopConversionOrLoadingUsingInterruptMonitor().TestRun();
```

## **Образец кода**

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
