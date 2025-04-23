---
title: Rita tidslinje medan Excel konverteras till PDF med C++
linktitle: Rita tidslinje vid rendering av Excel till PDF
type: docs
weight: 60
url: /sv/cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Hantera tidslinjer för Excel filer med Aspose.Cells och C++.
keywords: Rendering tidslinje till pdf utan office 2013, office 2016, office 2019 och office 365
---

## **Rita tidslinje vid rendering av Excel till PDF**
Om du har en Excel-fil med tillämpad tidslinje och vill exportera den till PDF med tidslinjeinställningar, stöder Aspose.Cells detta nu som standard. Exportera helt enkelt Excel-filen med tidslinje till PDF, och den genererade PDF-filen visar tillämpad tidslinje.

Följande exempelkod laddar in den [exempel-Excel-filen](input.xlsx) som innehåller en befintlig tidslinje. Sedan sparar den arbetsboken som [utmatnings-PDF-filen](out.pdf). Följande skärmbild jämför käll-Excel-filen och den genererade PDF-filen.

<img src="out.png" width="60%">

## **Exempelkod**
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
    Aspose::Cells::Startup();
    // Load the sample Excel file
    Workbook workbook(u"input.xlsx");

    // Save the workbook as a PDF file
    workbook.Save(u"output.pdf", SaveFormat::Pdf);
    Aspose::Cells::Cleanup();
    return 0;

}
```

