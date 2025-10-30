---
title: Generar miniatura de la hoja de cálculo con C++
linktitle: Generar miniatura de la hoja de cálculo
type: docs
weight: 110
url: /es/cpp/generate-thumbnail-of-the-worksheet/
description: Generar miniaturas de hojas de cálculo como imágenes usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Puede ser útil generar miniaturas de hojas de cálculo. Una miniatura es una imagen pequeña que se puede pegar en un documento de Word o en una presentación de PowerPoint para dar una vista previa de lo que hay en la hoja de cálculo. Se puede agregar a una página web con un enlace para descargar el documento original y tiene una serie de otros usos.

{{% /alert %}} 

Aspose.Cells for C++ te permite exportar hojas de cálculo a archivos de imagen, haciendo que la generación de miniaturas sea sencilla. El siguiente código de ejemplo demuestra cómo exportar hojas de cálculo a archivos de imagen usando C++.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source workbook
    Workbook book(srcDir + u"sampleGenerateThumbnailOfWorksheet.xlsx");

    // Configure image rendering options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Bmp);
    imgOptions.SetVerticalResolution(200);
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetDesiredSize(600, 600, true); // Set thumbnail dimensions

    // Access first worksheet
    WorksheetCollection worksheets = book.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Render worksheet to image
    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputGenerateThumbnailOfWorksheet.bmp");

    std::cout << "Worksheet thumbnail generated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
