---
title: Renderizar línea de cuadrícula sólida al convertir Excel a PDF con C++
linktitle: Renderizar línea de cuadrícula sólida
type: docs
weight: 390
url: /es/cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Aprende cómo renderizar líneas de cuadrícula sólidas al convertir Excel a PDF usando Aspose.Cells con C++.
---

Para compatibilidad con versiones anteriores, Aspose.Cells renderiza las líneas de cuadrícula como líneas punteadas por defecto al convertir Excel a PDF. Sin embargo, los Excel modernos renderizan las líneas de cuadrícula como líneas sólidas hoy en día.

Con la opción [PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/), Aspose.Cells también puede renderizar líneas de cuadrícula como líneas sólidas.

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
