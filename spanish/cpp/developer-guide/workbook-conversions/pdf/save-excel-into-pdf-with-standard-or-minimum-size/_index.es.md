---
title: Guardar Excel en PDF con tamaño estándar o mínimo con C++
linktitle: Guardar Excel en PDF con Tamaño Estándar o Mínimo
type: docs
weight: 340
url: /es/cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Aprende cómo guardar archivos Excel en PDF con tamaño estándar o mínimo usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Por defecto, Aspose.Cells guarda Excel en PDF con tamaño estándar. Sin embargo, también puedes guardarlo con tamaño mínimo usando la propiedad [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/). Acepta los siguientes valores:

- PdfOptimizationType::Standard
- PdfOptimizationType::MinimumSize

{{% /alert %}} 

## **Guardar Excel en PDF con Tamaño Estándar o Mínimo usando Aspose.Cells**
El siguiente código de ejemplo muestra cómo puedes guardar Excel en PDF con tamaño estándar o mínimo usando [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/) propiedad.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleBook.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"OptimizedOutput_out.pdf";

    // Load excel file into workbook object
    Workbook workbook(inputFilePath);

    // Create PDF save options
    PdfSaveOptions opts;

    // Set optimization type to minimum size
    opts.SetOptimizationType(PdfOptimizationType::MinimumSize);

    // Save the workbook to PDF with the specified options
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved to PDF with minimum size optimization!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
