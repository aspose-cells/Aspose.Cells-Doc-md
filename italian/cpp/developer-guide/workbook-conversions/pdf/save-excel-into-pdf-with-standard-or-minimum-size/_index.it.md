---
title: Salva Excel in PDF con dimensione standard o minima con C++
linktitle: Salva Excel in PDF con dimensioni standard o minime
type: docs
weight: 340
url: /it/cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Scopri come salvare file Excel in PDF con dimensione standard o minima utilizzando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Per impostazione predefinita, Aspose.Cells salva Excel in PDF con dimensione standard. Tuttavia, puoi anche salvare con dimensione minima usando la proprietà [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/). Accetta i seguenti valori:

- PdfOptimizationType::Standard
- PdfOptimizationType::MinimumSize

{{% /alert %}} 

## **Salva Excel in PDF con dimensioni standard o minime utilizzando Aspose.Cells**
Il seguente esempio di codice mostra come puoi salvare Excel in PDF con dimensione standard o minima usando [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/) proprietà.

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
