---
title: Enregistrer Excel en PDF avec taille standard ou minimale avec C++
linktitle: Enregistrer Excel en PDF avec une taille standard ou minimale
type: docs
weight: 340
url: /fr/cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Apprenez comment enregistrer des fichiers Excel en PDF avec une taille standard ou minimale en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Par défaut, Aspose.Cells enregistre Excel en PDF avec une taille standard. Cependant, vous pouvez également l'enregistrer avec une taille minimale en utilisant la propriété [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/). Elle accepte les valeurs suivantes :

- PdfOptimizationType::Standard
- PdfOptimizationType::TailleMinimale

{{% /alert %}} 

## **Enregistrer Excel en PDF avec une taille standard ou minimale en utilisant Aspose.Cells**
Le code d'exemple suivant montre comment vous pouvez enregistrer Excel en PDF avec une taille Standard ou Minimale en utilisant la propriété [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/).

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
{{< app/cells/assistant language="cpp" >}}
