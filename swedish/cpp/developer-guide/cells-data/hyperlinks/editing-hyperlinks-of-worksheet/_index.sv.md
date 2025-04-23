---
title: Redigera hyperlänkar i arbetsblad med C++
linktitle: Redigera hyperlänkar i arbetsblad
type: docs
weight: 330
url: /sv/cpp/editing-hyperlinks-of-worksheet/
description: Lär dig hur du redigerar hyperlänkar i arbetsblad med API n Aspose.Cells for C++.
keywords: Redigera hyperlänkar, Redigera hyperlänkar i kalkylblad, Redigera hyperlänk i cell, Få åtkomst till alla hyperlänkar i kalkylbladet
---

{{% alert color="primary" %}}

Aspose.Cells möjliggör att du får åtkomst till alla hyperlänkar i kalkylbladet med hjälp av [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/)-samlingen. Du kan få åtkomst till varje hyperlänk från denna samling en efter en och redigera dess egenskaper.

{{% /alert %}}

 Följande exempel kod kommer åt alla hyperlänkar i arbetsbladet och ändrar deras [**GetAddress()**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getaddress/) egenskap till Aspose-webbplatsen.

```c++
#include <iostream>
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

    // Create workbook from input file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Iterate through all hyperlinks in the worksheet
    for (int32_t i = 0; i < worksheet.GetHyperlinks().GetCount(); i++)
    {
        Hyperlink hl = worksheet.GetHyperlinks().Get(i);
        hl.SetAddress(u"http://www.aspose.com");
    }

    // Save the modified workbook to the output file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Hyperlinks updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
