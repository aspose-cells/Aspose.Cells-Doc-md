---
title: Dölja överlagrat innehåll med CrossHideRight vid sparande till HTML med C++
linktitle: Dölja överlagt innehåll med CrossHideRight medan du sparar till HTML
type: docs
weight: 100
url: /sv/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Använd CrossHideRight med Aspose.Cells i C++ för att dölja överlagrat innehåll vid sparande till HTML.
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML kan du specificera olika kors-typer för cellsträngar. Som standard genererar Aspose.Cells HTML enligt Microsoft Excel, men när du ändrar kors-typen till [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) döljs alla strängar till höger om cellen som är överlagrade eller overlapping med cellsträngen.

## **Dölja överlagt innehåll med CrossHideRight vid sparning till Html**

Följande exempel kod laddar [exempel-Excelfilen](64716894.xlsx) och sparar den till [utdata-HTML](64716893.zip) efter att ha ställt in [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gethtmlcrossstringtype/) som [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). Skärmbilden förklarar hur [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) påverkar utdata HTML från standardutgången.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");

    // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::CrossHideRight);

    // Save to HTML with HtmlSaveOptions
    wb.Save(outputDir + u"outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html", opts);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
