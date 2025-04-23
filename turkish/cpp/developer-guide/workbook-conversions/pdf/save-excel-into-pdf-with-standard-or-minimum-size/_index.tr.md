---
title: Excel i Standart veya Minimal Boyutta PDF olarak kaydet  C++ ile
linktitle: Excel i Standart veya Minimum Boyutlu PDF ye Kaydetme
type: docs
weight: 340
url: /tr/cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını standart veya minimum boyutta PDF ye nasıl kaydedeceğinizi öğrenin.
---

{{% alert color="primary" %}} 

 Varsayılan olarak, Aspose.Cells Excel'i Standart boyut ile PDF'ye kaydeder. Ancak, [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/) özelliği kullanılarak Minimum boyutla da kaydedilebilir. Aşağıdaki değerleri kabul eder:

- PdfOptimizationType::Standard
- PdfOptimizationType::MinimumSize

{{% /alert %}} 

## **Aspose.Cells ile Excel'i Standart veya Minimum Boyutlu PDF'ye Kaydetme**
Aşağıdaki örnek kod, [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/) özelliği kullanarak Excel'i Standart veya Minimum boyut ile PDF'ye nasıl kaydedeceğinizi gösterir.

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
