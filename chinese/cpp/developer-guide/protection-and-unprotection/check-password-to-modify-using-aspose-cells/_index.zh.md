---
title: 使用 Aspose.Cells 和 C++ 检查密码修改权限
linktitle: 检查密码修改权限
type: docs
weight: 2400
url: /zh/cpp/check-password-to-modify-using-aspose-cells/
description: 使用 Aspose.Cells 和 C++ 检查提供的密码是否匹配“密码修改”
---

{{% alert color="primary" %}}

 有时你需要以编程方式检查提供的密码是否与“密码修改”匹配。Aspose.Cells 提供 WorkbookSettings.WriteProtection.ValidatePassword() 方法，可以用来检查密码是否正确。

{{% /alert %}}

## **在Microsoft Excel中检查修改密码**

您可以在创建Microsoft Excel工作簿时指定**打开密码**和**修改密码**。请参阅此截图，显示Microsoft Excel提供的界面以指定这些密码。

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **使用Aspose.Cells检查修改密码**

以下示例代码加载了[源 Excel](5112232.xlsx) 文件。它具有打开密码为1234和修改密码为5678。该代码首先检查是否567为正确的修改密码，并返回false，然后检查是否5678为修改密码，并返回true。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleBook.xlsx";

    // Specify password to open inside the load options
    LoadOptions opts;
    opts.SetPassword(u"1234");

    // Open the source Excel file with load options
    Workbook workbook(inputFilePath, opts);

    // Check if "567" is the password to modify
    bool ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"567");
    std::wcout << L"Is 567 correct Password to modify: " << ret << std::endl;

    // Check if "5678" is the password to modify
    ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"5678");
    std::wcout << L"Is 5678 correct Password to modify: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **控制台输出**

这是加载了[源 Excel](5112232.xlsx) 文件后的上述示例代码的控制台输出。

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
