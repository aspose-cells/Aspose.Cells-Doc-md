---
title: 使用 C++ 验证用于保护工作表的密码
linktitle: 验证用于保护工作表的密码
type: docs
weight: 370
url: /zh/cpp/verify-password-used-to-protect-the-worksheet/
description: 了解如何使用 Aspose.Cells for C++ 验证用于保护工作表的密码。
---

{{% alert color="primary" %}}

Aspose.Cells API通过引入一些有用的属性和方法来增强[**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/)类。 其中一个方法是[**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/)，允许将密码作为*string*的实例进行指定，并验证是否已经使用相同的密码来保护[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)。

{{% /alert %}}

 如果指定的密码与用于保护工作表的密码匹配，[**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) 方法返回 **true**，否则返回 **false**。以下代码片段结合使用 [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) 方法和 [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) 属性来检测密码保护状态并验证密码。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"Sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        // Verify the password used to protect the Worksheet
        if (sheet.GetProtection().VerifyPassword(u"1234"))
        {
            std::cout << "Specified password has matched" << std::endl;
        }
        else
        {
            std::cout << "Specified password has not matched" << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
