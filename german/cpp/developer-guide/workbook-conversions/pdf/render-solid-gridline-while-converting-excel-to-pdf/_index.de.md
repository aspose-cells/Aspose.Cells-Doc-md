---
title: Gerade Linien bei der Konvertierung von Excel nach PDF rendern
linktitle: Gerade Linien rendern
type: docs
weight: 390
url: /de/cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Erfahren Sie, wie Sie beim Konvertieren von Excel nach PDF mit Aspose.Cells für C++ gerade Linien rendern.
---

Aus Kompatibilitätsgründen rendern Aspose.Cells standardmäßig Gitterlinien als gepunktete Linien beim Konvertieren von Excel in PDF. Moderne Versionen von Excel rendern Gitterlinien jedoch als durchgezogene Linien.

Mit der Option [PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) kann Aspose.Cells Gitterlinien auch als durchgezogene Linien rendern.

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
