---
title: Calculate Page Setup Scaling Factor with C++
linktitle: Calculate Page Setup Scaling Factor
type: docs
weight: 300
url: /cpp/calculate-page-setup-scaling-factor/
description: This article provides sample code explaining how to use the C++ API or library to calculate Page Setup scaling factor using Fit to n page(s) wide by m tall option of Excel worksheet programmatically.
keywords: Fit to n page wide by m tall excel c++, calculate page setup scaling factor c++
---

{{% alert color="primary" %}}

When you set Page Setup Scaling using **Fit to n page(s) wide by m tall** option, Microsoft Excel calculates the Page Setup Scaling Factor. You can calculate the same thing using [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/) property. This property returns a double value which can be converted to percentage value. For example, if it returns 0.5 then it means scaling factor is 50%.

{{% /alert %}}

The following sample code illustrates how to calculate page setup scaling factor using [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/) property.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some data in these cells
    worksheet.GetCells().Get(u"A4").PutValue(u"Test");
    worksheet.GetCells().Get(u"S4").PutValue(u"Test");

    // Set paper size
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Set fit to pages wide as 1
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Calculate page scale via sheet render
    ImageOrPrintOptions options;
    SheetRender sr(worksheet, options);

    // Convert page scale double value to percentage
    double pageScale = sr.GetPageScale();
    std::wstring strPageScale = std::to_wstring(pageScale * 100) + L"%";

    // Write the page scale value
    std::wcout << strPageScale << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```