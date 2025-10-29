---
title: 使用 C++ 检测工作表是否受密码保护
linktitle: 检测工作表是否受密码保护
type: docs
weight: 360
url: /zh/cpp/detect-if-worksheet-is-password-protected/
description: 了解如何使用 Aspose.Cells for C++ 检测工作表是否受密码保护。
---

{{% alert color="primary" %}}

 可以分别保护工作簿和工作表。例如，一个电子表格可能包含一个或多个受密码保护的工作表，但整个电子表格本身可能受保护也可能不受保护。Aspose.Cells API 提供检测特定工作表是否受密码保护的方法。本文演示如何使用 Aspose.Cells for C++ API 实现此功能。

{{% /alert %}}

 Aspose.Cells for C++ 已暴露 [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) 属性，用于检测工作表是否受密码保护。布尔类型的 [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) 属性如果 [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 被密码保护，则返回 **true**，否则返回 **false**。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        std::cout << "Worksheet is password protected" << std::endl;
    }
    else
    {
        std::cout << "Worksheet is not password protected" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
