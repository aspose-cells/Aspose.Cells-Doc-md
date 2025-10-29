---
title: إيقاف التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً مع C++
linktitle: إيقاف التحويل أو التحميل باستخدام InterruptMonitor
type: docs
weight: 100
url: /ar/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: تعلم كيفية إيقاف تحويل أو تحميل ملفات Excel الكبيرة باستخدام InterruptMonitor في Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

 يتيح لك Aspose.Cells إيقاف تحويل دفتر العمل إلى تنسيقات متنوعة مثل PDF و HTML، باستخدام الكائن [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) عندما يستغرق وقتًا طويلاً. غالبًا ما يكون عملية التحويل مكثفة من حيث وحدة المعالجة المركزية والذاكرة، وغالبًا ما يكون من المفيد إيقافها عندما تكون الموارد محدودة. يمكنك استخدام [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) لإيقاف التحويل وكذلك لإيقاف تحميل دفاتر العمل الضخمة. يرجى استخدام الخاصية [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getinterruptmonitor/) لإيقاف التحويل والخ property [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getinterruptmonitor/) لإيقاف تحميل دفاتر العمل الضخمة.

## **توقّف عن التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً**

 يوضح الكود التالي استخدام [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/). يحول الكود ملف Excel كبير جدًا إلى PDF. سيستغرق الأمر عدة ثوانٍ (أي أكثر من 30 ثانية) لإتمام التحويل بسبب هذا السطر من الكود.

```cpp
// Access cell J1000000 and add some text inside it.
auto cell = ws->GetCells()->GetObjectByIndex("J1000000");
cell->PutValue("This is text.");
```

 كما ترى، فإن **J1000000** هو خلية بعيدة جدًا في ملف XLSX. ومع ذلك، تقوم طريقة **WaitForWhileAndThenInterrupt()** بمقاطعة التحويل بعد 10 ثوانٍ، وتنتهي / تُنهى البرنامج. يرجى استخدام الكود التالي لتنفيذ الكود النموذجي.

```cpp
new StopConversionOrLoadingUsingInterruptMonitor().TestRun();
```

## **الكود المثالي**

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
