---
title: 如何用C++设置工作簿的自动恢复属性
linktitle: 如何设置工作簿的AutoRecover属性
type: docs
weight: 220
url: /zh/cpp/how-to-set-autorecover-property-of-workbook/
description: 学习如何用Aspose.Cells for C++启用或禁用工作簿的自动恢复属性。
---

{{% alert color="primary" %}}

你可以使用Aspose.Cells设置工作簿的自动恢复属性。该属性的默认值为 **true**。当你将其设置为 **false** 时，Microsoft Excel会禁用该Excel文件的自动恢复（自动保存）。

Aspose.Cells提供了 [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) 属性，用以启用或禁用这个选项。

{{% /alert %}}

以下代码说明了如何使用工作簿的 [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) 属性。代码首先读取此属性的默认值（为 **true**），然后将其设置为 **false**，并保存工作簿。之后再次读取，显示此属性的值（此时为 **false**）。

## 使用C++设置工作簿的自动恢复属性

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook.GetSettings().GetAutoRecover() << std::endl;

    // Set AutoRecover property to false
    workbook.GetSettings().SetAutoRecover(false);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    // Read the saved workbook again
    Workbook workbook2(outDir + u"output_out.xlsx");

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook2.GetSettings().GetAutoRecover() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **输出**

这是上面示例代码的控制台输出。

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
