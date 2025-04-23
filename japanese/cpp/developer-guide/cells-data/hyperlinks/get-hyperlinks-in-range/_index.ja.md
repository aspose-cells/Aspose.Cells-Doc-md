---
title: C++で範囲内のハイパーリンクを取得
linktitle: 範囲内のハイパーリンクを取得
type: docs
weight: 100
url: /ja/cpp/get-hyperlinks-in-range/
description: Aspose.Cells for C++ APIを使用して範囲内のハイパーリンクを取得する方法を学びます。
keywords: 範囲内のハイパーリンクを取得、選択した範囲内のすべてのハイパーリンクを取得、範囲内のハイパーリンクの削除、選択した範囲内のハイパーリンクを削除
---

## **範囲内のハイパーリンクを取得**

[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)クラスは、選択した範囲のすべてのハイパーリンクを返す[**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/gethyperlinks/)プロパティを提供します。また、[**Hyperlink.Delete**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/delete/)メソッドを呼び出すことでハイパーリンクを削除することもできます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"HyperlinksSample.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Range range = worksheet.GetCells().CreateRange(u"A2", u"B3");
    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();

    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink& link = hyperlinks[i];
        std::cout << link.GetArea().ToString().ToUtf8() << " : " << link.GetAddress().ToUtf8() << std::endl;
        link.Delete();
    }

    workbook.Save(outDir + u"HyperlinksSample_out.xlsx");
    std::cout << "Hyperlinks processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
