---
title: Convertire Excel in immagine ad alta risoluzione con C++
linktitle: Convertire Excel in immagine ad alta risoluzione
type: docs
weight: 100
url: /it/cpp/convert-excel-to-high-resolution-image/
description: Genera immagini ad alta risoluzione dai file Excel utilizzando Aspose.Cells con C++.
---

Con la crescente diffusione di schermi ad alta risoluzione, le immagini generate a 96 DPI di default appaiono spesso sfocate e poco chiare. Per garantire la chiarezza su schermi ad alta risoluzione, è essenziale generare immagini a DPI più elevati. Aspose.Cells offre la funzionalità di impostare [**ImageOrPrintOptions.GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/) e [**ImageOrPrintOptions.GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/), permettendoti di creare immagini di alta qualità da file Excel che risultano nitide su display ad alta risoluzione.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the Excel file
    Workbook workbook(u"input.xlsx");

    // Create an instance of ImageOrPrintOptions
    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300); // Set horizontal resolution to 300 DPI
    options.SetVerticalResolution(300);   // Set vertical resolution to 300 DPI
    options.SetImageType(ImageType::Png); // Set the image type

    // Get the worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Create a SheetRender instance
    SheetRender render(sheet, options);

    // Generate and save the image
    render.ToImage(0, u"output.png");

    std::cout << "Image generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
