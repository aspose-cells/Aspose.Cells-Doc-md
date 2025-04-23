---
title: 使用C++管理单元格HTML字符串
linktitle: 管理单元格HTML字符串
type: docs
weight: 600
url: /zh/cpp/manage-cells-html-string/
description: 通过Aspose.Cells for C++ API学习如何管理单元格HTML字符串。
keywords: 在单元格中添加 HTML 字符串，设置单元格中的 HTML 字符串，添加 HTML 字符串，获取单元格的 HTML 字符串，管理单元格的 HTML 字符串
---

## **可能的使用场景**
 当您需要为特定单元格设置样式化数据时，可以将HTML字符串分配给单元格。 当然，您也可以获取单元格的HTML字符串。Aspose.Cells提供了此功能。Aspose.Cells提供以下属性和方法以帮助您实现目标。
- [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)
- [**Cell::SetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/sethtmlstring/)

## **使用 Aspose.Cells 获取和设置 HTML 字符串**
此示例演示如何：

1. 创建一个工作簿并添加一些数据。
1. 获取第一个工作表中的特定单元格。
1. 将HTML字符串设置给单元格。
1. 获取单元格的HTML字符串。

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

## 示例代码生成的输出

以下截图显示了上述示例代码的输出。

![todo:image_alt_text](htmlstring.png)
