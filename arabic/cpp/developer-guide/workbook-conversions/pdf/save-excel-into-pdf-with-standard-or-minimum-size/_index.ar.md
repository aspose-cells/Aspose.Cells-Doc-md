---
title: حفظ Excel كملف PDF بحجم قياسي أو أدنى باستخدام C++
linktitle: حفظ Excel إلى PDF بحجم قياسي أو حد أدنى
type: docs
weight: 340
url: /ar/cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: تعلم كيفية حفظ ملفات Excel كملف PDF بالحجم القياسي أو الأدنى باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

 بشكل افتراضي، يحفظ Aspose.Cells Excel كملف PDF بالحجم القياسي. ومع ذلك، يمكنك أيضًا حفظه بالحجم الأدنى باستخدام خاصية [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/). تقبل القيم التالية:

- PdfOptimizationType::Standard
- PdfOptimizationType::MinimumSize

{{% /alert %}} 

## **حفظ Excel إلى PDF بحجم قياسي أو حد أدنى باستخدام Aspose.Cells**
يوضح الكود النموذجي التالي كيف يمكنك حفظ Excel كملف PDF بالحجم القياسي أو الأدنى باستخدام خاصية [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/)

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
