---
title: Konvertera Excel till HTML med verktygstips med C++
linktitle: Konvertera Excel till HTML med verktygstips
type: docs
weight: 200
url: /sv/cpp/convert-excel-to-html-with-tooltip/
description: Konvertera Excel till HTML samtidigt som du lägger till verktygstips med Aspose.Cells med C++.
---

## **Konvertera Excel till HTML med verktygstips**

Det kan finnas fall där texten klipps av i den genererade HTML och du vill visa hela texten som ett verktygstips vid hover-händelsen. Aspose.Cells stöder detta genom att tillhandahålla [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/)-egenskapen. Att sätta [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/) till **true** kommer att lägga till hela texten som ett verktygstips i den genererade HTML.

Följande bild visar tooltipen i den genererade HTML-filen.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Följande kodexempel laddar [käll-Excel-filen](98107416.xlsx) och genererar [utdata-HTML-filen](98107417.zip) med verktygstips.

Exempelkod

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook workbook(sourceDir + u"AddTooltipToHtmlSample.xlsx");

    // Setup HTML save options
    HtmlSaveOptions options;
    options.SetAddTooltipText(true);  // Enable tooltip text in output

    // Save as HTML
    workbook.Save(outputDir + u"AddTooltipToHtmlSample_out.html", options);

    std::cout << "Workbook saved with tooltip text added!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
