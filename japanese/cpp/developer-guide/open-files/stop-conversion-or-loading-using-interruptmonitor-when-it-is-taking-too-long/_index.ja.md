---
title: C++でInterruptMonitorを使った変換または読み込みを停止する方法
linktitle: InterruptMonitorを使用して変換または読み込みを停止する
type: docs
weight: 100
url: /ja/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: C++でInterruptMonitorを使用した大きなExcelファイルの変換または読み込み停止方法の学習
---

## **可能な使用シナリオ**

Aspose.Cellsは、処理に時間がかかりすぎる場合に[**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/)オブジェクトを使用してWorkbookのPDF、HTML等への変換を停止することができます。変換処理はCPUとメモリの両方を消費しやすいため、リソースが限られている場合に停止するのは有用です。変換停止には[**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/)を、巨大なワークブックの読み込み停止には[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getinterruptmonitor/)を使用できます。変換停止には[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getinterruptmonitor/)、読み込み停止には[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getinterruptmonitor/)のプロパティを利用してください。

## **時間がかかりすぎる場合はInterruptMonitorを使用して変換または読み込みを停止してください**

以下のサンプルコードは、[**InterruptMonitor**](https://reference.aspose.com/cells/cpp/aspose.cells/interruptmonitor/)オブジェクトの使い方を説明しています。このコードは比較的大きなExcelファイルをPDFに変換します。処理には数秒（約30秒以上）かかる見込みです。

```cpp
// Access cell J1000000 and add some text inside it.
auto cell = ws->GetCells()->GetObjectByIndex("J1000000");
cell->PutValue("This is text.");
```

ご覧の通り、**J1000000**はXLSXファイルのかなり遠いセル位置にありますが、**WaitForWhileAndThenInterrupt()**メソッドは10秒後に変換を中断し、プログラムは終了します。以下のコードを使ってサンプル製作を実行してください。

```cpp
new StopConversionOrLoadingUsingInterruptMonitor().TestRun();
```

## **サンプルコード**

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
