---
title: Konvertera Excel till högupplöst bild med C++
linktitle: Konvertera Excel till högupplöst bild
type: docs
weight: 100
url: /sv/cpp/convert-excel-to-high-resolution-image/
description: Generera högupplösta bilder från Excelfiler med Aspose.Cells och C++.
---

Med den ökande förekomsten av högupplösta skärmar visas bilder som genereras vid standard 96 DPI ofta suddiga och otydliga. För att säkerställa klarhet på högupplösta skärmar är det viktigt att generera bilder med högre DPI. Aspose.Cells erbjuder funktionalitet för att ställa in [**ImageOrPrintOptions.GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/) och [**ImageOrPrintOptions.GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/), vilket gör att du kan skapa högkvalitativa bilder från Excel-filer som ser skarpa ut på högupplösta skärmar.

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
