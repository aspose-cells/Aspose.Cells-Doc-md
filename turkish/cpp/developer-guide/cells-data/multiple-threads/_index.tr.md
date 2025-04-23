---
title: C++ ile Aynı Anda Çoklu Diziyle Hücre Değerlerini Okuma
linktitle: Çoklu İş Parçacıkları
type: docs
weight: 1800
url: /tr/cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for C++ API kullanarak Çoklu İş Parçacığında Hücre Değerleri Okuma yı nasıl yapacağınızı öğrenin.
keywords: Çoklu İş Parçacığında Hücre Değerlerini Oku, Aspose.Cells C++ Çoklu İş Parçacığı, Çoklu İş Parçacığında Veri Okuma
---

{{% alert color="primary" %}}

Aynı Anda Birden Fazla İş Parçacığında hücre değerlerini okuma ihtiyacı yaygın bir gereksinimdir. Bu makale bu amaçla Aspose.Cells'in nasıl kullanılacağını açıklar.

{{% /alert %}}

Daha fazla bir iş parçacığında hücre değerlerini okumak için [**Worksheet.GetMultiThreadReading()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmultithreadreading/) değerini **true** olarak ayarlayın. Aksi takdirde yanlış hücre değerlerini alabilirsiniz.

Aşağıdaki kod:

1. Bir çalışma kitabı oluşturur.
1. Bir çalışma sayfası ekler.
1. Çalışma sayfasını dize değerleriyle doldurur.
1. Sonra rastgele hücrelerden aynı anda değer okuyan iki iş parçacığı oluşturur.
   Okunan değerler doğru ise hiçbir şey olmaz. Okunan değerler yanlışsa bir mesaj görüntülenir.

Eğer bu satırı yorumlarsanız:

{{< highlight cpp >}}

 testWorkbook->get_Worksheets()->Get(0)->get_Cells()->set_MultiThreadReading(true);

{{< /highlight >}}

o zaman aşağıdaki mesaj görüntülenir:

{{< highlight cpp >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox::Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Aksi takdirde, program herhangi bir mesaj göstermeden çalışır, bu da demek olur ki tüm hücrelerden okunan değerler doğrudur.

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
