---
title: 使用C++为不同页面设置不同的页眉和页脚
linktitle: 设置不同的页眉和页脚
type: docs
weight: 35
url: /zh/cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: 本文提供示例代码，展示如何使用C++库和API以编程方式设置Excel工作表的页面设置中的各种页眉和页脚。你可以为首页、奇数页和偶数页设置页眉和页脚。
keywords: 用C++设置Excel首页页眉页脚，设置奇数页页眉页脚，设置偶数页页眉页脚
---

{{% alert color="primary" %}}

自Excel 2007起，MS Excel支持为首页、奇数页和偶数页设置不同的页眉和页脚。
Aspose.Cells支持相同的功能。

{{% /alert %}}

## **在MS Excel中设置不同的页眉和页脚**

**![设置不同的页眉和页脚](difpage.png)**

1. 点击 **页面布局 > 打印标题 > 页眉/页脚**。
1. 选中 **不同奇偶页** 或 **首页不同**。
1. 输入不同的页眉和页脚。

## **使用Aspose.Cells设置不同的页眉和页脚**

Aspose.Cells与Excel的行为相同。
1. 设置标志 [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdiffoddeven/) 和 [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdifffirst/) 
1. 输入不同的页眉和页脚。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Get the first worksheet's page setup
    PageSetup pageSetup = wb.GetWorksheets().Get(0).GetPageSetup();

    // Set different headers for odd and even pages
    pageSetup.SetIsHFDiffOddEven(true);
    pageSetup.SetHeader(1, u"I am the header of the Odd page.");
    pageSetup.SetEvenHeader(1, u"I am the header of the Even page.");

    // Set a different header for the first page
    pageSetup.SetIsHFDiffFirst(true);
    pageSetup.SetFirstPageHeader(1, u"I am the header of the First page.");

    Aspose::Cells::Cleanup();
}
```
