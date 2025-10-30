---
title: セルのHTML文字列を管理するC++
linktitle: セルのHTML文字列を管理する
type: docs
weight: 600
url: /ja/cpp/manage-cells-html-string/
description: Aspose.Cells for C++ APIを通じてセルのHTML文字列管理方法を学びます。
keywords: セル内にHTML文字列を追加する、セル内にHTML文字列を設定する、HTML文字列を追加する、セルのHTML文字列を取得する、セルのHTML文字列を管理する
---

## **可能な使用シナリオ**
特定のセルにスタイルを設定してデータを表示したい場合、HTML文字列をセルに割り当てることができます。もちろん、セルのHTML文字列を取得も可能です。Aspose.Cellsはこの機能を提供します。目標を達成するためのプロパティやメソッドを備えています。
- [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)
- [**Cell::SetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/sethtmlstring/)

## **Aspose.Cellsを使用してHTML文字列を取得および設定する**
この例では、次のことができます:

1. ワークブックを作成し、いくつかのデータを追加します。
1. 最初のワークシートで特定のセルを取得します。
1. セルにHTML文字列を設定します。
1. セルのHTML文字列を取得します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");

    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");

    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");

    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");

    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    Cell c3 = cells.Get(u"C3");
    // Set HTML string for C3 cell
    c3.SetHtmlString(u"<b>test bold</b>");

    Cell c4 = cells.Get(u"C4");
    // Set HTML string for C4 cell
    c4.SetHtmlString(u"<i>test italic</i>");

    // Get the HTML string of specific cell
    std::cout << c3.GetHtmlString().ToUtf8() << std::endl;
    std::cout << c4.GetHtmlString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## サンプルコードによって生成された出力

上記のサンプルコードの出力を以下のスクリーンショットで示します。

![todo:image_alt_text](htmlstring.png)
{{< app/cells/assistant language="cpp" >}}
