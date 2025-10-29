---
title: Чтение значений ячеек в нескольких потоках одновременно с помощью C++
linktitle: Несколько потоков
type: docs
weight: 1800
url: /ru/cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Узнайте, как читать значения ячеек в нескольких потоках одновременно через API Aspose.Cells for C++.
keywords: Читать значения ячеек в нескольких потоках одновременно, Aspose.Cells C++ Много потоков, чтение данных в нескольких потоках
---

{{% alert color="primary" %}}

Необходимость чтения значений ячеек в нескольких потоках одновременно - это распространенная потребность. В этой статье объясняется, как использовать Aspose.Cells для этой цели.

{{% /alert %}}

Для чтения значений ячеек в более чем одном потоке одновременно установите [**Worksheet.GetMultiThreadReading()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmultithreadreading/) в **true**. В противном случае вы можете получить неправильные значения ячеек.

Следующий код:

1. Создает рабочую книгу.
1. Добавляет лист.
1. Заполняет лист строковыми значениями.
1. Затем создает два потока, которые одновременно читают значения из случайных ячеек.
   Если прочитанные значения правильные, ничего не происходит. Если прочитанные значения неправильные, то отображается сообщение.

Если вы закомментируете эту строку:

{{< highlight cpp >}}

 testWorkbook->get_Worksheets()->Get(0)->get_Cells()->set_MultiThreadReading(true);

{{< /highlight >}}

тогда отображается следующее сообщение:

{{< highlight cpp >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox::Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

В противном случае программа работает без отображения любого сообщения, что означает, что все значения, считываемые из ячеек, являются правильными.

```cpp
#include <iostream>
#include <thread>
#include <random>
#include <chrono>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

static Workbook testWorkbook;

U16String IntToU16String(int value) {
    wstring ws = to_wstring(value);
    return U16String(reinterpret_cast<const char16_t*>(ws.c_str()));
}

void ThreadLoop()
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> rowDist(0, 9999);
    uniform_int_distribution<> colDist(0, 99);

    while (true)
    {
        try
        {
            int row = rowDist(gen);
            int col = colDist(gen);
            U16String s = testWorkbook.GetWorksheets().Get(0).GetCells().Get(row, col).GetStringValue();
            U16String expected = U16String(u"R") + IntToU16String(row) + U16String(u"C") + IntToU16String(col);
            if (s != expected)
            {
                cout << "This message will show up when cells read values are incorrect." << endl;
            }
        }
        catch (...) {}
    }
}

void TestMultiThreadingRead()
{
    testWorkbook = Workbook();
    testWorkbook.GetWorksheets().Clear();
    testWorkbook.GetWorksheets().Add(u"Sheet1");

    for (int row = 0; row < 10000; row++)
    {
        for (int col = 0; col < 100; col++)
        {
            U16String value = U16String(u"R") + IntToU16String(row) + U16String(u"C") + IntToU16String(col);
            testWorkbook.GetWorksheets().Get(0).GetCells().Get(row, col).SetValue(value);
        }
    }

    // Commenting this line will show a pop-up message
    // testWorkbook.GetWorksheets().Get(0).GetCells().SetMultiThreadReading(true);

    thread myThread1(ThreadLoop);
    thread myThread2(ThreadLoop);

    this_thread::sleep_for(chrono::seconds(5));

    myThread1.detach();
    myThread2.detach();
}

int main()
{
    Aspose::Cells::Startup();
    TestMultiThreadingRead();
    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
