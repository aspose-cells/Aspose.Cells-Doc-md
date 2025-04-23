---
title: Inaktivera CSS vid sparning till HTML med C++
linktitle: Inaktivera CSS vid sparning till HTML
type: docs
weight: 320
url: /sv/cpp/disable-css-while-saving-to-html/
description: Lär dig hur du inaktiverar CSS vid sparning av Excel filer till HTML med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till en HTML som en enda sida, kommer CSS-elementen vanligtvis att vara inbäddade i HTML-filen och ligga i HEAD-sektionen. Om du bifogar denna fil som innehåll/kropp i ett email, kommer CSS-elementen att tas bort av de flesta email-klienter, vilket resulterar i felaktig rendering. Version 24.12 av Aspose.Cells introducerar ett alternativ som tillåter dig att inaktivera CSS, så att stilar kan tillämpas direkt inom HTML-elementen själva. Om du vill använda HTML som innehåll/kropp i emailet, använd [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/)-egenskapen och ställ in den på **true**.

## **Inaktivera CSS vid sparning till HTML**

Följande exempel kod visar användningen av [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/)-egenskapen.

## **Exempelkod**

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

    // Load sample workbook
    Workbook wb(srcDir + u"sampleDisableCss.xlsx");

    // Disable CSS
    HtmlSaveOptions opts;
    opts.SetDisableCss(true);

    // Save the workbook in HTML
    wb.Save(outDir + u"outputDisable.html", opts);

    std::cout << "Workbook saved with CSS disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
