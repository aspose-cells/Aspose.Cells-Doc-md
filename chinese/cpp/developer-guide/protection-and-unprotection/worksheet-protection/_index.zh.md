---
title: 使用 C++ 保护和取消保护工作表
linktitle: 保护和取消保护工作表
type: docs
weight: 40
url: /zh/cpp/protect-and-unprotect-worksheets/
description: 使用 Aspose.Cells for C++ 保护和取消保护Excel工作表。
---

{{% alert color="primary" %}}
为防止其他用户意外或故意更改、移动或删除工作表中的数据，您可以锁定 Excel 工作表上的单元格，然后使用密码保护工作表。 
{{% /alert %}}

## ** 在 MS Excel 中保护和取消保护工作表**

**![保护和取消保护工作表](protect-and-unprotect-worksheet.png)**

1. 点击 **审阅 > 保护工作表**。
1. 在 **密码框** 中输入密码。
1. 选择 **允许** 选项。
1. 选择 **确定**，重新输入密码以确认，然后再次选择 **确定**。

## ** 使用 Aspose.Cells for C++ 保护工作表**
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

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Protect contents of the worksheet
    sheet.Protect(ProtectionType::Contents);

    // Protect worksheet with password
    sheet.GetProtection().SetPassword(u"test");

    // Save as Excel file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## ** 使用 Aspose.Cells for C++ 取消保护工作表**
使用 Aspose.Cells API 轻松取消工作表保护。如果工作表受密码保护，需要正确的密码。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet with password
    sheet.Unprotect(u"password");

    // Save the workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Worksheet unprotected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [自 Excel XP 以来的高级保护设置](/cells/zh/cpp/advanced-protection-settings-since-excel-xp/)
- [检测工作表是否受密码保护](/cells/zh/cpp/detect-if-worksheet-is-password-protected/)
- [保护工作表](/cells/zh/cpp/protecting-worksheets/)
- [取消保护工作表](/cells/zh/cpp/unprotect-a-worksheet/)
- [验证用于保护工作表的密码](/cells/zh/cpp/verify-password-used-to-protect-the-worksheet/)
{{< app/cells/assistant language="cpp" >}}
