---
title: Kopiera radhöjder från källdatan till destinationsdata med C++
linktitle: Kopiera radhöjderna i källområdet till destinationsområdet
type: docs
weight: 590
url: /sv/cpp/copy-row-heights-of-source-range-to-destination-range/
description: Lär dig hur du kopierar radhöjder från en källområde till ett målområde med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland behöver användare kopiera radhöjder från ett källområde till ett målområde. Aspose.Cells tillhandahåller enum [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) för detta ändamål. När du sätter egenskapen [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) med enum [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/), kommer höjderna av alla rader i källdatan att kopieras till målområdet.

{{% /alert %}}

Följande exempel förklarar hur du använder enum [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) för att kopiera radhöjder från ett källområde till ett målområde. När du öppnar den genererade Excel-filen i Microsoft Excel kommer du att se att radhöjderna i målområdet är exakt samma som i källdatan.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Source worksheet
    Worksheet srcSheet = workbook.GetWorksheets().Get(0);

    // Add destination worksheet
    Worksheet dstSheet = workbook.GetWorksheets().Add(u"Destination Sheet");

    // Set the row height of the 4th row. This row height will be copied to destination range
    srcSheet.GetCells().SetRowHeight(3, 50);

    // Create source range to be copied
    Range srcRange = srcSheet.GetCells().CreateRange(u"A1:D10");

    // Create destination range in destination worksheet
    Range dstRange = dstSheet.GetCells().CreateRange(u"A1:D10");

    // PasteOptions, we want to copy row heights of source range to destination range
    PasteOptions opts;
    opts.SetPasteType(PasteType::RowHeights);

    // Copy source range to destination range with paste options
    dstRange.Copy(srcRange, opts);

    // Write informative message in cell D4 of destination worksheet
    dstSheet.GetCells().Get(u"D4").PutValue(u"Row heights of source range copied to destination range");

    // Save the workbook in xlsx format
    workbook.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Row heights copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
