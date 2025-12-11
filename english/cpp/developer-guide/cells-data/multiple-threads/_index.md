---  
title: Reading Cell Values in Multiple Threads Simultaneously with C++  
linktitle: Multiple Threads  
type: docs  
weight: 1800  
url: /cpp/reading-cell-values-in-multiple-threads-simultaneously/  
description: Learn how to read cell values in multiple threads simultaneously through the Aspose.Cells for C++ API.  
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells C++ Multiple Threads, Read data in Multiple Threads  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

Reading cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.  

{{% /alert %}}  

To read cell values in more than one thread simultaneously, set [**Worksheet.GetMultiThreadReading()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmultithreadreading/) to **true**. If you do not, you might get incorrect cell values.  

The following code:  

1. Creates a workbook.  
2. Adds a worksheet.  
3. Populates the worksheet with string values.  
4. Creates two threads that simultaneously read values from random cells. If the values read are correct, nothing happens. If the values read are incorrect, a message is displayed.  

If you comment this line:  

{{< highlight cpp >}}  
testWorkbook.get_Worksheets().Get(0).get_Cells().set_MultiThreadReading(true);  
{{< /highlight >}}  

then the following message is displayed:  

{{< highlight cpp >}}  
if (s != "R" + row + "C" + col)  
{  
    MessageBox::Show("This message box will show up when the cell values read are incorrect.");  
}  
{{< /highlight >}}  

Otherwise, the program runs without showing any message, which means all values read from cells are correct.  

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

    // Commenting out this line will show a pop-up message
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
