---
title: Renderizza sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions con C++
linktitle: Renderizza sequenza di pagine
type: docs
weight: 110
url: /it/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
description: Renderizza una sequenza di pagine da un file Excel in immagini usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

È possibile rendere una sequenza di pagine del file Excel in immagini utilizzando Aspose.Cells con le proprietà [**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/) e [**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/). Queste proprietà sono utili quando ci sono ad esempio migliaia di pagine nel foglio di lavoro ma si desidera renderne solo alcune. Questo non solo risparmierà tempo di elaborazione ma risparmierà anche l'utilizzo della memoria del processo di rendering.

## **Rendere la sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions**

Il seguente codice di esempio carica il [file Excel di esempio](55541781.xlsx) e rende solo le pagine 4, 5, 6 e 7 utilizzando le proprietà [**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/) e [**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/). Ecco le pagine renderizzate generate dal codice.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **Codice di Esempio**

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sampleImageOrPrintOptions_PageIndexPageCount.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetPageIndex(3);
    opts.SetPageCount(4);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(ws, opts);

    for (int i = opts.GetPageIndex(); i < sr.GetPageCount(); i++)
    {
        std::wstring pageNum = std::to_wstring(i + 1);
        U16String filePath = outDir + U16String(u"outputImage-") + 
            U16String(reinterpret_cast<const char16_t*>(pageNum.c_str())) + 
            U16String(u".png");
        sr.ToImage(i, filePath);
    }

    std::cout << "Images generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
