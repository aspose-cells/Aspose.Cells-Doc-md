---
title: Rendi linee di griglia solide durante la conversione di Excel in PDF con C++
linktitle: Rendi linee di griglia solide
type: docs
weight: 390
url: /it/cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Scopri come rendere linee di griglia solide durante la conversione di Excel in PDF con Aspose.Cells e C++.
---

Per compatibilità con versioni più vecchie, Aspose.Cells rende le linee di griglia come linee tratteggiate per impostazione predefinita durante la conversione di Excel in PDF. Tuttavia, Excel moderno rende le linee di griglia come linee solide al giorno d'oggi.

Con l'opzione [PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/), Aspose.Cells può anche rendere le linee di griglia come linee solide.

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
