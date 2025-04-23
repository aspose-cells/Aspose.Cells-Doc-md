---
title: C++を使用してExcelをPDFに変換する際に、格子線をソリッドにレンダリングします。
linktitle: 格子線をソリッドにレンダリング
type: docs
weight: 390
url: /ja/cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Aspose.Cellsを使用してExcelをPDFに変換する際に、ソリッド格子線をレンダリングする方法を学びます。
---

古いバージョンとの互換性のため、Aspose.Cellsはデフォルトでは点線のラインとしてグリッドラインをレンダリングします。ただし、現代のExcelではグリッドラインは実線としてレンダリングされます。

[PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)]（https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/）のオプションを使用すると、Aspose.Cellsは格子線をソリッド線としてレンダリングできます。

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
