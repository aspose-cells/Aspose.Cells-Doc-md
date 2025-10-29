---
title: 在工作表中删除重复行（使用C++）
linktitle: 在工作表中删除重复行
type: docs
weight: 370
url: /zh/cpp/remove-duplicate-rows-in-a-worksheet/
description: 学习如何使用Aspose.Cells for C++ API删除工作表中的重复行。
---

{{% alert color="primary" %}}

删除重复行是Microsoft Excel的许多实用功能之一。它允许用户删除工作表中的重复行，并可选择检查哪些列中的重复信息。

Aspose.Cells提供了 `Cells::RemoveDuplicates()` 方法用于此操作。也可以设置 `startRow`、`startColumn`、`endRow` 和 `endColumn` 来选择列。

以下是可以下载以进行此功能测试的样本文件：

[removeduplicates.xlsx](removeduplicates.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook book(u"removeduplicates.xlsx");

    // Remove duplicates from the first worksheet
    book.GetWorksheets().Get(0).GetCells().RemoveDuplicates(0, 0, 5, 3);

    // Save the result
    book.Save(u"removeduplicates-result.xlsx");

    std::cout << "Duplicates removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
