---
title: Excel mit Standard oder Minimale Größe in PDF mit C++ speichern
linktitle: Excel in PDF mit Standard oder Minimalgröße speichern
type: docs
weight: 340
url: /de/cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Lernen Sie, wie Sie Excel Dateien mit Standard oder Minimale Größe mit Aspose.Cells for C++ in PDF speichern.
---

{{% alert color="primary" %}} 

Standardmäßig speichert Aspose.Cells Excel im Standardformat in PDF. Sie können es jedoch auch mit minimaler Größe unter Verwendung der [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/) Eigenschaft speichern. Es akzeptiert folgende Werte:

- PdfOptimizationType::Standard
- PdfOptimizationType::MinimumSize

{{% /alert %}} 

## **Speichern Sie Excel in PDF mit Standard- oder Minimalgröße mithilfe von Aspose.Cells**
Das folgende Beispiel zeigt, wie Sie Excel mit Standard- oder Minimalsize mithilfe der [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/) Eigenschaft in PDF speichern können.

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
