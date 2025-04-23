---
title: C++で複数スレッドからセルの値を同時に読み取る
linktitle: 複数のスレッド
type: docs
weight: 1800
url: /ja/cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for C++ APIを通じて複合的にセル値を同時に読み取る方法を学習します。
keywords: 複数のスレッドでセル値を同時に読み取る、Aspose.Cells C++のマルチスレッド、複数スレッドでデータを読み取る
---

{{% alert color="primary" %}}

複数のスレッドで同時にセル値を読み取る必要がある場合がよくあります。この記事ではその目的で Aspose.Cells の使用方法を説明します。

{{% /alert %}}

複数のスレッドで同時にセル値を読み取るために、[**Worksheet.GetMultiThreadReading()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmultithreadreading/) を **true** に設定します。そうしないと、間違ったセル値を取得する可能性があります。

次のコード:

1. ワークブックを作成します。
1. ワークシートを追加します。
1. 文字列値でワークシートを埋めます。
1. 次に、ランダムなセルから同時に値を読み取る2つのスレッドを作成します。
   読み取った値が正しい場合、何も起こりません。読み取った値が間違っている場合は、メッセージが表示されます。

この行をコメントアウトすると、次のメッセージが表示されます:

{{< highlight cpp >}}

 testWorkbook->get_Worksheets()->Get(0)->get_Cells()->set_MultiThreadReading(true);

{{< /highlight >}}

それ以外の場合、すべてのセルから読み取った値が正しいことを意味するメッセージが表示されずにプログラムが実行されます。

{{< highlight cpp >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox::Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

それ以外の場合、セルから読み取ったすべての値が正しい場合、プログラムはメッセージを表示せずに実行されます。

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
