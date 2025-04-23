---
title: Rendera kalkylblad till grafiskt sammanhang med C++
linktitle: Rendera arbetsblad till grafiskt sammanhang
type: docs
weight: 300
url: /sv/cpp/render-worksheet-to-graphic-context/
description: Lär dig hur du renderar ett kalkylblad till ett grafiskt sammanhang med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells kan nu rendera ett kalkylblad till ett grafiskt sammanhang. Det grafiska sammanhanget kan vara vilken som helst som en bildfil, skärm eller skrivare etc. Använd en av följande två metoder för att rendera ett kalkylblad till ett grafiskt sammanhang.

- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)
- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)

{{% /alert %}}

Följande kod visar hur man använder Aspose.Cells för att rendera ett kalkylblad till ett grafiskt sammanhang. När du kör koden skrivs hela kalkylbladet ut och det återstående tomma utrymmet fylls med blå färg i det grafiska sammanhanget, och bilden sparas som filen **OutputImage_out_.png**. Du kan använda vilken Excel-fil som helst som källa för att prova detta kodexempel. Läs även kommentarerna i koden för bättre förståelse.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleBook.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outDir + u"OutputImage_out.png");

    Aspose::Cells::Cleanup();
}
```
