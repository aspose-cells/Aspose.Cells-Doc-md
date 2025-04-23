---
title: 使用C++获取范围内的超链接
linktitle: 获取范围内的超链接
type: docs
weight: 100
url: /zh/cpp/get-hyperlinks-in-range/
description: 通过Aspose.Cells for C++ API学习如何获取范围内的超链接。
keywords: 获取范围内的超链接，获取所选范围内的所有超链接，删除范围内的超链接，删除所选范围内的超链接
---

## **获取范围内的超链接**

[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) 类提供一个 [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/gethyperlinks/) 属性，返回选择范围内的所有超链接。您还可以通过调用 [**Hyperlink.Delete**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/delete/) 方法删除超链接。

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
