---
title: Сохранение Excel в PDF с стандартным или минимальным размером с помощью C++
linktitle: Сохранить Excel в формат PDF со стандартным или минимальным размером
type: docs
weight: 340
url: /ru/cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Узнайте, как сохранять Excel файлы в PDF с использованием стандартного или минимального размера с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

По умолчанию Aspose.Cells сохраняет Excel в PDF в стандартном размере. Однако вы также можете сохранить его с минимальным размером, используя свойство [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/). Оно принимает следующие значения:

- PdfOptimizationType::Standard
- PdfOptimizationType::MinimumSize

{{% /alert %}} 

## **Сохранение Excel в формат PDF со стандартным или минимальным размером с использованием Aspose.Cells**
Следующий пример показывает, как сохранять Excel в PDF в стандартном или минимальном размере с помощью свойства [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/).

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
