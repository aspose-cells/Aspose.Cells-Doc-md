---
title: 使用 C++ 保护和取消保护工作簿结构
linktitle: 保护和取消保护工作簿结构
type: docs
weight: 40
url: /zh/cpp/protect-and-unprotect-workbook-structure/
description: 使用 C++ 和 Aspose.Cells 保护或取消保护Excel文件的工作簿结构。
---

{{% alert color="primary" %}}
为防止其他用户查看隐藏工作表、添加、移动、删除或隐藏工作表，并重命名工作表，您可以使用密码保护 Excel 工作簿的结构。
{{% /alert %}}

## ** 在MS Excel中保护与取消保护工作簿结构**

**![保护和取消保护工作簿结构](protect-and-unprotect-workbook-structure.png)**

1. 点击 **审阅 > 保护工作簿**。
1. 在 **密码框** 中输入密码。
1. 选择 **确定**，重新输入密码以确认，然后再次选择 **确定**。

## ** 使用 Aspose.Cells for C++ 保护工作簿结构**
只需要以下简单代码行来实现保护 Excel 文件的工作簿结构。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Protect workbook structure with a password
    workbook.Protect(ProtectionType::Structure, u"password");

    // Save the workbook to a file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## ** 使用 Aspose.Cells for C++ 取消保护工作簿结构**
使用 Aspose.Cells API 轻松取消工作簿结构保护。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open an Excel file which workbook structure is protected.
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Unprotect workbook structure.
    workbook.Unprotect(u"password");

    // Save Excel file.
    workbook.Save(inputFilePath);

    std::cout << "Workbook structure unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}
注意：需要正确的密码。
{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
