---
title: Exportar hoja de cálculo o gráfico a imagen con ancho y alto deseados con C++
linktitle: Exportar hoja de cálculo o gráfico a imagen con ancho y alto deseados
type: docs
weight: 290
url: /es/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/
description: Usa Aspose.Cells para exportar hoja de cálculo o gráfico a imagen con el ancho y el alto deseados en C++.
---

{{% alert color="primary" %}}

Puede utilizar Aspose.Cells para exportar su hoja de cálculo o gráfico a una imagen con el ancho y alto deseados. Proporciona el método [**ImageOrPrintOptions.SetDesiredSize()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/setdesiredsize/) para establecer el ancho y alto deseados de la imagen exportada. El ancho y alto se especifican en unidades de píxeles.

{{% /alert %}}

El siguiente código exporta la hoja de cálculo a una imagen con tamaño de 400x400.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook object from source file
    Workbook workbook(sourceDir + u"sampleWorksheetToImageDesiredSize.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetDesiredSize(400, 400, false);

    // Render sheet into image
    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outputDir + u"outputWorksheetToImageDesiredSize.png");

    std::cout << "Worksheet rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
