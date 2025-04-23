---
title: 使用 C++ 为渲染自动调整行高
linktitle: 在渲染时自动调整列的行高
type: docs
weight: 130
url: /zh/cpp/autofit-rows-for-rendering/
description: 了解如何使用 Aspose.Cells 与 C++ 自动适应 Excel 文件中的行以进行渲染。
---

通常，当您想要在单元格中显示所有文本时，您可以在 Microsoft Excel 的普通视图中进行行高自动调整，放大到 100%。这样可以在普通视图中完全显示文本，甚至在打印或将文件保存为 PDF 时，文本也能正确显示。

但在一些情况下，自动调整行在普通视图中效果良好，但当切换到打印视图或将文件保存为 PDF 时，文本会被截断。请查看源文件 [Book1.xlsx](Book1.xlsx) 和屏幕截图。

![打印视图中文本被截断](text_clipped_in_printview.png)

 如果想防止保存的 PDF 文件中文本被剪裁，可以使用 [AutoFitterOptions.GetForRendering()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getforrendering/) 选项自动调整行高。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize workbook instance
    Workbook workbook(u"Book1.xlsx");

    // Set autofit options for rendering
    AutoFitterOptions autoFitterOptions;
    autoFitterOptions.SetForRendering(true);

    // Autofit rows with options
    workbook.GetWorksheets().Get(0).AutoFitRows(autoFitterOptions);

    // Save to PDF
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    Aspose::Cells::Cleanup();
}
```

现在，在输出的 PDF 文件中文本不再被截断。

![保存的 PDF 文件中文本未被截断](text_not_clipped_in_saved_pdf.png)
