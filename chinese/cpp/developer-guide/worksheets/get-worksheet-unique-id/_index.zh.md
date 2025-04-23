---
title: 使用C++获取工作表唯一ID
linktitle: 获取工作表唯一ID
type: docs
weight: 190
url: /zh/cpp/get-worksheet-unique-id/
description: 本文介绍如何用C++库和API程序化获取Excel工作表的唯一ID。
keywords: C++获取唯一ID的工作表，C++唯一ID工作表
---

## ** 获取工作表唯一ID**

Aspose.Cells 提供通过[**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/)方法获取工作表唯一ID的功能。以下代码示例演示如何使用[**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/)方法打印工作表的唯一ID。此示例使用[样例Excel文件](105480213.xlsx)。

### 源代码

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print Unique Id
    std::cout << "Unique Id: " << worksheet.GetUniqueId().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
