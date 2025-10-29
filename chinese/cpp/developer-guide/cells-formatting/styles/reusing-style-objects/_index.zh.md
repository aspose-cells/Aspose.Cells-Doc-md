---
title: 使用C++重用样式对象
linktitle: 重用样式对象
description: 在Aspose.Cells for C++中，通过创建和使用可重用的样式对象，可以简化样式管理并提高代码效率。我们的指南将帮助您利用可重用样式对象的优势，并将其实现于您的应用程序中。
keywords: Aspose.Cells for C++，重用样式对象，样式管理，代码效率，可重用样式，应用程序开发，API参考，示例代码，下载，支持。
type: docs
weight: 3000
url: /zh/cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

重用样式对象可以节省内存并加快程序运行速度。

{{% /alert %}}

若要对工作表中的大范围单元格应用一些格式设置：

1. 创建一个样式对象。
1. 指定属性。
1. 将样式应用于范围中的单元格。

```cpp
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

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style styleObject = workbook.CreateStyle();
    styleObject.GetFont().SetColor(Color::Red());
    styleObject.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(styleObject);
    cell2.SetStyle(styleObject);

    // Put the values inside the cell
    cell1.PutValue(u"Hello World!");
    cell2.PutValue(u"Hello World!!");

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

由于 [**Cell.GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) 方法占用的内存明显较少，并且效率更高，旧的 Cell.Style 属性在 Aspose.Cells 7.1.0 版本中已被移除，因为它消耗了大量不必要的内存。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
