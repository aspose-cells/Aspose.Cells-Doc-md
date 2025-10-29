---
title: Convertir Excel en image haute résolution avec C++
linktitle: Convertir Excel en image haute résolution
type: docs
weight: 100
url: /fr/cpp/convert-excel-to-high-resolution-image/
description: Générer des images haute résolution à partir de fichiers Excel en utilisant Aspose.Cells avec C++.
---

Avec la prévalence croissante des écrans haute résolution, les images générées à 96 DPI par défaut apparaissent souvent floues et peu claires. Pour assurer la clarté sur les écrans haute résolution, il est essentiel de générer des images à une résolution plus élevée. Aspose.Cells offre la fonctionnalité de définir [**ImageOrPrintOptions.GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/) et [**ImageOrPrintOptions.GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/), permettant de créer des images de haute qualité à partir de fichiers Excel qui apparaissent nets sur des écrans haute résolution.

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
