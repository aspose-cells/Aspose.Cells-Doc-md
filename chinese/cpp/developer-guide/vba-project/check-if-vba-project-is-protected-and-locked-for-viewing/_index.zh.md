---
title: 用C++检测VBA项目是否受保护且锁定以供查看
linktitle: 检查VBA项目是否受保护并已锁定以供查看
type: docs
weight: 30
url: /zh/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: 学习如何用Aspose.Cells for C++检测Excel中VBA项目是否已受保护且锁定查看。
---

## 用C++检测VBA项目是否受保护且锁定查看

Aspose.Cells允许你检测Excel文件的VBA（Visual Basic for Applications）项目是否已受保护且锁定查看。API提供[**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/)属性，如果被锁定查看，则返回[**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/)为**true**。

## **示例代码**

以下示例代码加载[示例Excel文件](43352065.xlsm)，并检测其VBA（Visual Basic for Applications）项目是否已受保护且锁定查看。请查看其控制台输出作为参考。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCheckifVBAProjectisProtected.xlsm";

    // Load your source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Check if "Lock project for viewing" is true or not
    std::cout << "Is VBA Project Locked for Viewing: " << vbaProject.GetIslockedForViewing() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **控制台输出**

这是上述示例代码在使用提供的[示例Excel文件](43352065.xlsm)时执行时的控制台输出。

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
