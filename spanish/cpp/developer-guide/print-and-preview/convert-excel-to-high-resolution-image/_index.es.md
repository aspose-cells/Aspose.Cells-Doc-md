---
title: Convertir Excel a Imagen de Alta Resolución con C++
linktitle: Convertir Excel en Imagen de Alta Resolución
type: docs
weight: 100
url: /es/cpp/convert-excel-to-high-resolution-image/
description: Generar imágenes de alta resolución a partir de archivos Excel usando Aspose.Cells con C++.
---

Con la creciente prevalencia de pantallas de alta resolución, las imágenes generadas a la resolución predeterminada de 96 DPI a menudo aparecen borrosas y poco claras. Para garantizar claridad en pantallas de alta resolución, es esencial generar imágenes a una DPI mayor. Aspose.Cells ofrece la funcionalidad de establecer [**ImageOrPrintOptions.GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/) y [**ImageOrPrintOptions.GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/), permitiéndote crear imágenes de alta calidad desde archivos de Excel que lucen nítidas en pantallas de alta resolución.

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
