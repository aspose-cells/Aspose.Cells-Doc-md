---
title: Läsa cellvärden i flera trådar samtidigt med C++
linktitle: Flera trådar
type: docs
weight: 1800
url: /sv/cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Lär dig hur du läser cellvärden i flera trådar samtidigt via API et Aspose.Cells for C++.
keywords: Läs cellvärden i flera trådar samtidigt, Aspose.Cells C++ Flervägstråd, läs data i flera trådar
---

{{% alert color="primary" %}}

Att behöva läsa cellvärden i flera trådar samtidigt är ett vanligt krav. Den här artikeln förklarar hur man använder Aspose.Cells för detta ändamål.

{{% /alert %}}

För att läsa cellvärden i mer än en tråd samtidigt, ange [**Worksheet.GetMultiThreadReading()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmultithreadreading/) till **true**. Om du inte gör det kan du få felaktiga cellvärden.

Följande kod:

1. Skapar en arbetsbok.
1. Lägger till en arbetsblad.
1. Fyller arbetsbladet med strängvärden.
1. Skapar sedan två trådar som samtidigt läser värden från slumpmässiga celler.
   Om de lästa värdena är korrekta händer ingenting. Om de lästa värdena är inkorrekta visas ett meddelande.

Om du kommenterar denna rad:

{{< highlight cpp >}}

 testWorkbook->get_Worksheets()->Get(0)->get_Cells()->set_MultiThreadReading(true);

{{< /highlight >}}

visas sedan följande meddelande:

{{< highlight cpp >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox::Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

I annat fall körs programmet utan att visa något meddelande, vilket betyder att alla värden som läses från cellerna är korrekta.

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
