---
title: Düz Grid Çizgisi Çizimi  C++ ile Excel den PDF ye Dönüştürme
linktitle: Düz Grid Çizgisini Render Etme
type: docs
weight: 390
url: /tr/cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Aspose.Cells kullanarak, Excel den PDF ye dönüştürürken düz grid çizgilerini nasıl render edeceğinizi öğrenin.
---

Uyumluluk için eski sürümlerle, Aspose.Cells varsayılan olarak çizgili çizgiler olarak ızgaraları render ederken, modern Excel artık ızgaraları katı çizgiler olarak gösterir.

[PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl*)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) seçeneği ile, Aspose.Cells grid çizgilerini de düz çizgi olarak render edebilir.

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
