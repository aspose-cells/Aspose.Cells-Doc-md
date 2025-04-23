---
title: Отрисовка сплошной сетки при преобразовании Excel в PDF с помощью C++
linktitle: Отрисовка сплошной сетки
type: docs
weight: 390
url: /ru/cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Узнайте, как отображать сплошные линии сетки при преобразовании Excel в PDF с помощью Aspose.Cells и C++.
---

Для совместимости со старыми версиями Aspose.Cells по умолчанию отображает линии сетки пунктирными при преобразовании Excel в PDF. Однако современные версии Excel отображают линии сетки как сплошные линии.

С помощью опции [PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/), Aspose.Cells также может отображать линии сетки как сплошные линии.

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
