---
title: Renderizza foglio di lavoro su contesto grafico con C++
linktitle: Rappresentare il foglio di calcolo nel contesto grafico
type: docs
weight: 300
url: /it/cpp/render-worksheet-to-graphic-context/
description: Scopri come renderizzare un foglio di lavoro su un contesto grafico utilizzando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells ora può rendere un foglio di lavoro su un contesto grafico. Il contesto grafico può essere qualsiasi cosa come un file immagine, schermo, stampante, ecc. Si prega di utilizzare uno dei seguenti due metodi per rendere un foglio di lavoro su un contesto grafico.

- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)
- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)

{{% /alert %}}

Il seguente codice illustra come utilizzare Aspose.Cells per rendere un foglio di lavoro su un contesto grafico. Una volta eseguito il codice, stamperà l'intero foglio di lavoro e riempirà lo spazio vuoto residuo con colore blu nel contesto grafico e salverà l'immagine come file **OutputImage_out_.png**. Puoi utilizzare qualsiasi file Excel di origine per testare questo codice. Si prega anche di leggere i commenti all'interno del codice per una migliore comprensione.

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
