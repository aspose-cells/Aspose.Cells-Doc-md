---
title: Convert XLS File with Images or Charts to PDF with C++
linktitle: Convert XLS File with Images or Charts to PDF
type: docs
weight: 50
url: /cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Convert XLS files containing images or charts to PDF documents using Aspose.Cells with C++.
---

{{% alert color="primary" %}} 

Aspose.Cells supports converting XLS files that contain images and charts to PDF documents. Aspose.Cells for C++ can work independently to convert a spreadsheet to PDF: Aspose.PDF for C++ is not required for the conversion. The process can be done in memory as the process does not depend on temporary or intermediary XML files. This means that large Excel files, for example, ones containing images, charts, and other drawing objects, can be converted quickly and efficiently.

{{% /alert %}} 
## **Sample Code**

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String designerFile = srcDir + u"SampleInput.xls";

    // Path of output pdf file
    U16String pdfFile = outDir + u"Output.out.pdf";

    try
    {
        // Open the template excel file
        std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(designerFile);

        // Save the pdf file
        wb->Save(pdfFile, SaveFormat::Pdf);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}} 

If the spreadsheet contains formulas, it is best to call the [Calculate(CalculationData data)](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/) method just before rendering to PDF. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}