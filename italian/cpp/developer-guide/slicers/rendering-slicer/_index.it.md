---
title: Rendering Slicer con C++
type: docs
weight: 40
url: /it/cpp/rendering-slicer/
description: Renderizza slicer nei file Excel usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells supporta il rendering della forma dello slicer. Se converti il tuo foglio di lavoro in un'immagine o salvi il tuo workbook in formati PDF o HTML, vedrai che gli slicers sono resi correttamente.
## **Rendering dello slicer**
Il seguente esempio di codice carica il [file Excel di esempio](67338479.xlsx) che contiene uno slicer esistente. Converte il foglio di lavoro in un'immagine impostando l'area di stampa che copre solo lo slicer. L'immagine seguente è l'[immagine di output](67338480.png) che mostra lo slicer renderizzato. Come puoi vedere, lo slicer è stato renderizzato correttamente e ha l'aspetto uguale a quello del file Excel di esempio.

![todo:image_alt_text](rendering-slicer_1)
## **Codice di Esempio**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleRenderingSlicer.xlsx");

    // Access first worksheet.
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Set the print area because we want to render slicer only.
    ws.GetPageSetup().SetPrintArea(u"B15:E25");

    // Specify image or print options, set one page per sheet and only area to true.
    ImageOrPrintOptions imgOpts;
    imgOpts.SetHorizontalResolution(200);
    imgOpts.SetVerticalResolution(200);
    imgOpts.SetImageType(ImageType::Png);
    imgOpts.SetOnePagePerSheet(true);
    imgOpts.SetOnlyArea(true);

    // Create sheet render object and render worksheet to image.
    SheetRender sr(ws, imgOpts);
    sr.ToImage(0, u"outputRenderingSlicer.png");

    Aspose::Cells::Cleanup();
}
```
