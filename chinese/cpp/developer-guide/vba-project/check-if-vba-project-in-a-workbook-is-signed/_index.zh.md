---
title: 用C++检查工作簿中的VBA项目是否已签名
linktitle: 检查工作簿中的VBA项目是否已签名
type: docs
weight: 70
url: /zh/cpp/check-if-vba-project-in-a-workbook-is-signed/
description: 用Aspose.Cells在C++中检测工作簿中的VBA项目是否已签名
---

{{% alert color="primary" %}}

你可以通过**工具 > 数字签名...**菜单命令在Microsoft Excel中检测你的VBA项目是否已签名。也可以用Aspose.Cells的[**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned)属性进行程序检测。

{{% /alert %}}

## **用C++检测工作簿中的VBA项目是否已签名**

以下代码加载工作簿，并使用[**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned)属性检测其VBA项目是否已签名。若已签名，返回**true**；否则返回**false**。

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
    U16String sampleFilePath = srcDir + u"Sample1.xlsx";

    // Create workbook
    Workbook workbook(sampleFilePath);

    // Check if the VBA project is signed
    bool isSigned = workbook.GetVbaProject().IsSigned();
    std::wcout << u"VBA Project is Signed: " << (isSigned ? u"true" : u"false") << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
