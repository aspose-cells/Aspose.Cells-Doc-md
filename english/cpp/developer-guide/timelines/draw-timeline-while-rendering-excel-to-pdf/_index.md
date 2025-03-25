---
title: Draw Timeline while rendering Excel to PDF with C++
linktitle: Draw Timeline while rendering Excel to PDF
type: docs
weight: 60
url: /cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Manage timelines of Excel files with Aspose.Cells with C++.
keywords: Rendering timeline to pdf without office 2013, office 2016, office 2019 and office 365
---

## **Draw Timeline while rendering Excel to PDF**
If you have an Excel file which has a timeline applied to it and you want to export the Excel to PDF with the timeline settings, Aspose.Cells now supports this by default. You simply export the Excel file with a timeline to PDF, and the generated PDF will show the timeline applied.

The following sample code loads the [sample Excel file](input.xlsx) that contains an existing timeline. It then saves the workbook as [output PDF file](out.pdf). The following screenshot compares the source Excel file and the generated PDF file.

<img src="out.png" width="60%">

## **Sample Code**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath(u"input.xlsx");
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Save file to pdf
    U16String outputFilePath(u"out.pdf");
    wb->Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <aspose.cells.h>

using namespace Aspose::Cells;

int main() {
    // Load the sample Excel file
    Workbook workbook(u"input.xlsx");

    // Save the workbook as a PDF file
    workbook.Save(u"output.pdf", SaveFormat::Pdf);
    return 0;
}
```

