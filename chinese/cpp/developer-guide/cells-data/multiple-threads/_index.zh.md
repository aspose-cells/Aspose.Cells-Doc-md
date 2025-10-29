---
title: 用C++实现多线程同时读取单元格数值
linktitle: 多线程
type: docs
weight: 1800
url: /zh/cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: 学习如何通过Aspose.Cells for C++ API同时在多个线程中读取单元格值。
keywords: 在C++中实现多线程同时读取单元格值，使用Aspose.Cells
---

{{% alert color="primary" %}}

需要同时在多个线程中读取单元格值是一个常见的需求。本文解释了如何使用Aspose.Cells来实现这一目的。

{{% /alert %}}

要同时在多个线程中读取单元格值，请将 [**Worksheet.GetMultiThreadReading()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmultithreadreading/) 设置为 **true**。如果不这样做，您可能会获取错误的单元格值。

以下代码：

1. 创建一个工作簿。
1. 添加一个工作表。
1. 用字符串值填充工作表。
1. 然后创建两个同时从随机单元格中读取值的线程。
   如果读取的值是正确的，则不会发生任何事情。如果读取的值不正确，则会显示一条消息。

如果您注释掉这一行：

{{< highlight cpp >}}

 testWorkbook->get_Worksheets()->Get(0)->get_Cells()->set_MultiThreadReading(true);

{{< /highlight >}}

那么将显示以下消息：

{{< highlight cpp >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox::Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

否则，程序将在不显示任何消息的情况下运行，这意味着从单元格中读取的所有值都是正确的。

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
