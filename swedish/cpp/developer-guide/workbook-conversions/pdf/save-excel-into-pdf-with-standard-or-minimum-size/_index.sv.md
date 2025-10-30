---
title: Spara Excel till PDF med standard eller minsta storlek med C++
linktitle: Spara Excel som PDF med standard eller minsta storlek
type: docs
weight: 340
url: /sv/cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Lär dig hur du sparar Excel filer till PDF med standard eller minsta storlek med Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Som standard sparar Aspose.Cells Excel till PDF med standardstorlek. Du kan också spara det med minsta storlek med egenskapen [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/). Den accepterar följande värden:

- PdfOptimizationType::Standard
- PdfOptimizationType::MinimumSize

{{% /alert %}} 

## **Spara Excel som PDF med standard- eller minsta storlek med Aspose.Cells**
Följande exempel visar hur du kan spara Excel till PDF med standard eller minsta storlek med hjälp av [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/) egenskapen.

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
