---
title: C++でセルからHTML5文字列を取得
linktitle: セルからHTML5文字列を取得
type: docs
weight: 90
url: /ja/cpp/get-html5-string-from-cell/
description: Aspose.Cells for C++ APIを使用してセルからHTML5文字列を取得する方法を学びます。
keywords: セルからHTML5文字列を取得、セルからHTML5文字列を取得、セルのHTML5文字列を管理
---

## **可能な使用シナリオ**

Aspose.Cellsは、ブール値のパラメータを受け取る[**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)メソッドを使用してセルのHTML文字列を返します。**false**をパラメータとして渡すと通常のHTMLを返し、**true**を渡すとHTML5文字列を返します。

## **セルからHTML5文字列を取得**

次のサンプルコードはワークブックオブジェクトを作成し、最初のワークシートのセルA1にテキストを追加します。そして、[**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)メソッドを使用してセルA1から通常のHTMLとHTML5文字列を取得し、それらをコンソールに出力します。

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put some text inside it
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(u"This is some text.");

    // Get the Normal and Html5 strings
    U16String strNormal = cell.GetHtmlString(false);
    U16String strHtml5 = cell.GetHtmlString(true);

    // Print the Normal and Html5 strings on console
    std::cout << "Normal:\r\n" << strNormal.ToUtf8() << std::endl;
    std::cout << std::endl;
    std::cout << "Html5:\r\n" << strHtml5.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **コンソール出力**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
