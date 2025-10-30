---
title: Rendera solida rutlinjer när du konverterar Excel till PDF med C++
linktitle: Rendera solida rutlinjer
type: docs
weight: 390
url: /sv/cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Lär dig hur du renderar solida rutlinjer när du konverterar Excel till PDF med Aspose.Cells och C++.
---

För kompatibilitet med äldre versioner, konverterar Aspose.Cells rutnätslinjer som prickade linjer som standard när du konverterar Excel till PDF. Moderna Excel-versioner visar dock rutnätslinjer som solida linjer numera.

Med alternativet [PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl*)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) kan Aspose.Cells också rendera rutlinjer som solida linjer.

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
{{< app/cells/assistant language="cpp" >}}
