---
title: 使用C++从单元格获取HTML5字符串
linktitle: 从单元格获取HTML5字符串
type: docs
weight: 90
url: /zh/cpp/get-html5-string-from-cell/
description: 通过Aspose.Cells for C++ API学习如何从单元格获取HTML5字符串。
keywords: 从单元格获取 HTML5 字符串，从单元格获取 HTML5 字符串，管理单元的 HTML5 字符串
---

## **可能的使用场景**

 Aspose.Cells使用接受布尔参数的[**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)方法返回单元格的HTML字符串。传入**false**作为参数，将返回普通HTML；传入**true**，将返回HTML5字符串。

## ** 从单元格获取HTML5字符串**

以下示例代码创建一个工作簿对象，并在第一个工作表的A1单元格中添加一些文本。然后使用[**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)方法从A1单元格获取普通的HTML和HTML5字符串，并将它们打印在控制台上。

## **示例代码**

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

## **控制台输出**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
