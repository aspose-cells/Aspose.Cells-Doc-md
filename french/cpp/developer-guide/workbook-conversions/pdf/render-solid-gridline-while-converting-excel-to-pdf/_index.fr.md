---
title: Rendre une grille solide lors de la conversion d Excel en PDF avec C++
linktitle: Rendre une grille solide
type: docs
weight: 390
url: /fr/cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Apprenez comment rendre les lignes de grille solides lors de la conversion d Excel en PDF avec Aspose.Cells en C++.
---

Pour la compatibilité avec les versions plus anciennes, Aspose.Cells rend par défaut les lignes de grille en pointillés lors de la conversion d'Excel en PDF. Cependant, Excel moderne rend maintenant les lignes de grille en lignes solides.

Avec l'option [PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/), Aspose.Cells peut également rendre les lignes de grille en lignes solides.

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
