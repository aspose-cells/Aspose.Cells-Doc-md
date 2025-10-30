---
title: Uzun süren işlemler sırasında kesintiye uğratmak veya yüklemeyi durdurmak için InterruptMonitor kullanımı (C++)
linktitle: InterruptMonitor Kullanarak İşlemi Durdurma veya Yüklemeyi Kesme
type: docs
weight: 100
url: /tr/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Aspose.Cells te büyük Excel dosyalarının yüklenmesini veya dönüştürülmesini InterruptMonitor ile durdurmayı nasıl öğrenebilirsiniz.
---

## **Olası Kullanım Senaryoları**

 Aspose.Cells, [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) nesnesini kullanarak, çok uzun süren dönüştürme işlemlerinde PDF, HTML gibi biçimlere dönüşüm veya yüklemeyi durdurmanıza olanak tanır. Dönüştürme işlemi genellikle CPU ve Bellek yoğun olduğu için, kaynaklar sınırlıyken durdurmak faydalı olabilir. Hem dönüştürmeyi durdurmak hem de büyük çalışma kitaplarını yüklemeyi durdurmak için [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) ve [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getinterruptmonitor/) özelliklerini kullanabilirsiniz. Ayrıca, [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getinterruptmonitor/) özelliği ile büyük çalışma kitaplarının yüklenmesini durdurabilirsiniz.

## **Çok uzun sürüyorsa, Duraklatma İzleyiciyi kullanarak dönüşümü veya yüklemeyi durdurun**

 Aşağıdaki örnek kod, [**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/) nesnesinin kullanımını açıklar. Kod, oldukça büyük bir Excel dosyasını PDF'ye dönüştürür. Bu işlem, birkaç saniye (yani, *30 saniyeden fazla*) sürebilir, çünkü bu satır kodlar nedeniyle.

```cpp
// Access cell J1000000 and add some text inside it.
auto cell = ws->GetCells()->GetObjectByIndex("J1000000");
cell->PutValue("This is text.");
```

 Gördüğünüz gibi, **J1000000** hücresi oldukça uzak bir konumdadır. Ancak, **WaitForWhileAndThenInterrupt()** yöntemi dönüştürmeyi 10 saniye sonra durdurur ve program sona erer/kapanır. Lütfen aşağıdaki kodu kullanarak örnek kodu çalıştırın.

```cpp
new StopConversionOrLoadingUsingInterruptMonitor().TestRun();
```

## **Örnek Kod**

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
