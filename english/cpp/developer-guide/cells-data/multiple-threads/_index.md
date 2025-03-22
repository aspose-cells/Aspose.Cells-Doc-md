---
title: Reading Cell Values in Multiple Threads Simultaneously with C++
linktitle: Multiple Threads
type: docs
weight: 1800
url: /cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Learn how to read Cell Values in Multiple Threads Simultaneously through the Aspose.Cells for C++ API.
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells C++ Multiple Threads, Read data in Multiple Threads
---

{{% alert color="primary" %}}

Needing to read cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.

{{% /alert %}}

To read cell values in more than one thread simultaneously, set [**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/multithreadreading/) to **true**. If you do not, you might get the wrong cell values.

The following code:

1. Creates a workbook.
1. Adds a worksheet.
1. Populates the worksheet with string values.
1. It then creates two threads that simultaneously read values from random cells.
   If the values read are correct, nothing happens. If the values read are incorrect, then a message is displayed.

If you comment this line:

{{< highlight cpp >}}

 testWorkbook->get_Worksheets()->Get(0)->get_Cells()->set_MultiThreadReading(true);

{{< /highlight >}}

then the following message is displayed:

{{< highlight cpp >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox::Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Otherwise, the program runs without showing any message which means all values read from cells are correct.

```c++
#include <iostream>
#include <thread>
#include <random>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

static Workbook testWorkbook;

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
            U16String expected = U16String(u"R") + U16String::FromInt(row) + U16String(u"C") + U16String::FromInt(col);
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
            U16String value = U16String(u"R") + U16String::FromInt(row) + U16String(u"C") + U16String::FromInt(col);
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