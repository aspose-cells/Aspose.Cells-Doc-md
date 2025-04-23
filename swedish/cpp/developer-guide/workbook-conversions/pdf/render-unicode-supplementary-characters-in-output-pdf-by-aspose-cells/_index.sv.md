---
title: Render Unicode tilläggstecken i utdata PDF med C++ av Aspose.Cells
linktitle: Render Unicode tilläggstecken
type: docs
weight: 350
url: /sv/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Lär dig hur man renderar Unicode tilläggstecken i utdata PDF med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Normala Unicode-tecken är 2 byte långa medan Unicode Supplementary-tecken är 4 byte långa. Aspose.Cells stöder nu rendering av dessa 4-byte Unicode-tecken.

I den Unicode-tekniska standarden är Supplementary-tecken de tecken som tilldelats kodpunkter från U+10000 till U+10FFFF. Med andra ord är dessa Unicode-tecken större än U+FFFF.

- I UTF-8 är dessa tecken var och en 4 byte långa.
- I UTF-16 kräver dessa tecken 2 surrogat (16-bitars enheter).

{{% /alert %}}

## Rendera Unicode Supplementära tecken i utdata-PDF med Aspose.Cells

Följande skärmbild visar hur Aspose.Cells renderade [käll-Excel-filen](5115563.xlsx) till [utdata-PDF](5115564.pdf). Som du kan se har alla tre Unicode Supplementära-tecken renderats exakt som gjorts av Microsoft Excel.

![todo:image_alt_text](output.png)

## Exempelkod

Du kan använda följande exempelkod för att konvertera [källa excel-filen](5115563.xlsx) till [utdata PDF](5115564.pdf).

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"unicode-supplementary-characters.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"RenderUnicodeInOutput_out.pdf";

    // Load the source excel file containing Unicode Supplementary characters
    Workbook wb(inputFilePath);

    // Save the workbook as PDF
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully with Unicode Supplementary characters!" << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```
