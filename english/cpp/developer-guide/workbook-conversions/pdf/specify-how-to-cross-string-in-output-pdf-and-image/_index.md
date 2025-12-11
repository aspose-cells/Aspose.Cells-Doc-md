---
title: Specify how to cross strings in output PDF and image with C++
linktitle: Specify how to cross strings in output PDF and image
type: docs
weight: 120
url: /cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Learn how to control text overflow in PDF and image outputs using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When a cell contains text that is larger than the width of the cell, the string overflows if the next cell in the next column is null or empty. When you save your Excel file as PDF or image, you can control this overflow by specifying the cross type using the [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/) enumeration. It has the following values:

- **TextCrossType.Default**: Display text like MS Excel, which depends on the next cell. If the next cell is null, the string will cross; otherwise, it will be truncated.

- **TextCrossType.CrossKeep**: Display the string as MS Excel does when exporting to PDF/Image.

- **TextCrossType.CrossOverride**: Display all the text by crossing other cells and override the text of crossed cells.

- **TextCrossType.StrictInCell**: Only display the string within the width of the cell.

## **Specify how to cross strings in output PDF/Image using TextCrossType**

The following sample code loads the sample Excel file and saves it to PDF/Image format by specifying different [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/). The sample Excel file and output files can be downloaded from the following links:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Sample Code

```c++
#include <iostream>
#include <memory>
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

    // Load template Excel file
    Workbook wb(srcDir + u"sampleCrossType.xlsx");

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Save PDF file
    wb.Save(outDir + u"outputCrossType.pdf", pdfSaveOptions);

    // Initialize image or print options
    ImageOrPrintOptions imageSaveOptions;
    imageSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Initialize sheet renderer object
    SheetRender sheetRenderer(wb.GetWorksheets().Get(0), imageSaveOptions);

    // Save PNG image
    sheetRenderer.ToImage(0, outDir + u"outputCrossType.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
