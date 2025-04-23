---
title: 在将Excel转换为PDF时渲染实线网格线 with C++
linktitle: 渲染实线网格线
type: docs
weight: 390
url: /zh/cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: 了解如何在将Excel转换为PDF时渲染实线网格线，使用Aspose.Cells与C++。
---

为了兼容旧版本，Aspose.Cells在将Excel转换为PDF时默认渲染网格线为点线。然而，现代Excel现在将网格线渲染为实线。

通过[PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)，Aspose.Cells也可以将网格线渲染为实线。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Create an empty Workbook
    Workbook wb;

    // Prepare data
    wb.GetWorksheets().Get(0).GetCells().Get(u"D9").PutValue(u"gridline");

    // Enable to print gridline
    wb.GetWorksheets().Get(0).GetPageSetup().SetPrintGridlines(true);

    // Set to render gridline as solid line
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetGridlineType(GridlineType::Hair);

    // Save the pdf file with PdfSaveOptions
    wb.Save(u"..\\Data\\02_OutputDirectory\\test_Cpp.pdf", pdfSaveOptions);

    std::cout << "PDF file saved successfully with gridlines!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

![solid-gridline.png](solid-gridline.png)
