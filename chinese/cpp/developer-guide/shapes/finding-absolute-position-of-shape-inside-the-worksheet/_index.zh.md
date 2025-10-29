---
title: 在工作表中查找形状的绝对位置（C++）
linktitle: 查找工作表内形状的绝对位置
type: docs
weight: 8000
url: /zh/cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: 使用Aspose.Cells和C++确定形状在工作表中的绝对位置。
---

{{% alert color="primary" %}}

有时，您需要知道工作表中形状的绝对位置。Aspose.Cells提供了 [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlefttocorner/) 和 [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) 属性来实现这一目的。这些属性返回形状在工作表中的绝对位置（以像素为单位）。

{{% /alert %}}

以下示例代码显示了工作表中第一个形状的绝对位置（以像素为单位）。示例代码显示了以下控制台输出：

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

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

    // Load the sample Excel file inside the workbook object
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first shape inside the worksheet
    Shape shape = worksheet.GetShapes().Get(0);

    // Displays the absolute position of the shape
    std::wcout << L"Absolute Position of this Shape is (" << shape.GetLeftToCorner() << L" , " << shape.GetTopToCorner() << L")" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
