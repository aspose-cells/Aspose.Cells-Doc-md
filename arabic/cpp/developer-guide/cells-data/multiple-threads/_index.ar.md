---
title: قراءة قيم الخلايا في عدة موضوعات في وقت واحد باستخدام ++C
linktitle: الخيوط المتعددة
type: docs
weight: 1800
url: /ar/cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: تعلم كيفية قراءة قيم الخلايا في عدة موضوعات في وقت واحد من خلال API Aspose.Cells for C++.
keywords: قراءة قيم الخلايا في عدة موضوعات في وقت واحد، Aspose.Cells C++ متعدد الموضوعات، قراءة البيانات في مواضيع متعددة
---

{{% alert color="primary" %}}

من الضروري قراءة قيم الخلية في خيوط متعددة بشكل متزامن ، وهو متطلب شائع. يشرح هذا المقال كيفية استخدام Aspose.Cells لهذا الغرض.

{{% /alert %}}

لقراءة قيم الخلية في أكثر من خيط بشكل متزامن، ضبط [**Worksheet.GetMultiThreadReading()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmultithreadreading/) إلى **true**. إذا لم تفعل ذلك ، قد تحصل على قيم الخلية الخاطئة.

الكود التالي:

1. ينشئ دفتر عمل.
1. إضافة ورقة عمل.
1. ملء ورقة العمل بقيم السلسلة.
1. ثم ينشئ خيطين يقرأان قيمًا بشكل متزامن من الخلايا العشوائية.
   إذا كانت القيم المقروءة صحيحة، لا يحدث شيء. إذا كانت القيم المقروءة غير صحيحة، يتم عرض رسالة.

إذا قمت بتعليق هذا السطر:

{{< highlight cpp >}}

 testWorkbook->get_Worksheets()->Get(0)->get_Cells()->set_MultiThreadReading(true);

{{< /highlight >}}

سيتم عرض الرسالة التالية:

{{< highlight cpp >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox::Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

وإلا، يعمل البرنامج بدون عرض أي رسالة مما يعني أن جميع القيم المقروءة من الخلايا صحيحة.

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
