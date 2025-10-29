---
title: 通过 C++ 保护或取消保护共享工作簿
linktitle: 密码保护或取消保护共享工作簿
type: docs
weight: 10
url: /zh/cpp/password-protect-or-unprotect-the-shared-workbook/
description: 学习如何用 Aspose.Cells for C++ 对共享工作簿进行密码保护或取消保护。
---

## **可能的使用场景**

您可以像以下截图中的 Microsoft Excel 一样使用 Aspose.Cells 保护或取消保护共享工作簿。Aspose.Cells 还支持使用 [**Workbook::ProtectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/protectsharedworkbook/) 和 [**Workbook::UnprotectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/unprotectsharedworkbook/) 方法进行此操作。

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **密码保护或取消保护共享工作簿**

以下示例代码创建一个工作簿并保护它，同时启用共享，然后将其另存为 [输出 Excel 文件](55541777.xlsx)。截图显示当您尝试取消保护时，Microsoft Excel 会提示您输入密码以取消保护。

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty Excel file
    Workbook wb;

    // Protect the Shared Workbook with Password
    wb.ProtectSharedWorkbook(u"1234");

    // Uncomment this line to Unprotect the Shared Workbook
    // wb.UnprotectSharedWorkbook(u"1234");

    // Save the output Excel file
    wb.Save(u"outputProtectSharedWorkbook.xlsx");

    std::cout << "Shared workbook protection applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
