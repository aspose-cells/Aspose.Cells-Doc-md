---
title: Lettura dei valori delle celle in più thread contemporaneamente con C++
linktitle: Thread multipli
type: docs
weight: 1800
url: /it/cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Impara come leggere i valori delle celle in più thread contemporaneamente tramite l API Aspose.Cells for C++.
keywords: Leggi i valori delle celle in più thread contemporaneamente, Aspose.Cells C++ più thread, leggere dati in più thread
---

{{% alert color="primary" %}}

La necessità di leggere i valori delle celle in thread multipli contemporaneamente è una richiesta comune. Questo articolo spiega come utilizzare Aspose.Cells per questo scopo.

{{% /alert %}}

Per leggere i valori delle celle in più di un thread contemporaneamente, impostare [**Worksheet.GetMultiThreadReading()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmultithreadreading/) su **true**. In caso contrario, si potrebbero ottenere valori di celle errati.

Il seguente codice:

1. Crea un workbook.
1. Aggiunge un foglio di lavoro.
1. Popola il foglio di lavoro con valori di stringa.
1. Quindi crea due thread che leggono contemporaneamente valori da celle casuali.
   Se i valori letti sono corretti, non succede nulla. Se i valori letti non sono corretti, viene visualizzato un messaggio.

Se si commenta questa riga:

{{< highlight cpp >}}

 testWorkbook->get_Worksheets()->Get(0)->get_Cells()->set_MultiThreadReading(true);

{{< /highlight >}}

allora viene visualizzato il seguente messaggio:

{{< highlight cpp >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox::Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

In caso contrario, il programma viene eseguito senza mostrare alcun messaggio, il che significa che tutti i valori letti dalle celle sono corretti.

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
