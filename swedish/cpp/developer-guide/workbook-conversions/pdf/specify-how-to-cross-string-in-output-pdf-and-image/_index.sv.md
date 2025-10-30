---
title: Ange hur man korsar strängar i utdata PDF och bild med C++
linktitle: Ange hur du ska korsa strängen i utdata PDF och bild
type: docs
weight: 120
url: /sv/cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Lär dig hur man kontrollerar textöverflöd i PDF och bildutgångar med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

 När en cell innehåller text eller sträng som är större än cellens bredd, överflödar strängen om nästa cell i nästa kolumn är null eller tom. När du sparar ditt Excel-fil till PDF eller Bild kan du kontrollera detta överflöde genom att specificera korsningstypen med hjälp av [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/)-uppräkningen. Den har följande värden:

- **TextCrossType.Default**: Visa text som MS Excel, vilket beror på nästa cell. Om nästa cell är null, kommer strängen att överkorsas eller skäras av.

- **TextCrossType.CrossKeep**: Visa strängen som MS Excel-exporterar till PDF/Bild.

- **TextCrossType.CrossOverride**: Visa all text genom att korsar andra celler och åsidosätter texten i korsade celler.

- **TextCrossType.StrictInCell**: Visar endast strängen inom cellens bredd.

## **Ange hur du ska korsa strängen i utdata PDF/Bild med hjälp av TextCrossType**

Följande kod laddar standadexempel fil och sparar den i PDF/Bild-format genom att specificera olika [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/). Standadexempel fil och utdatafiler kan laddas ner från följande länkar:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Exempelkod

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load template Excel file
    Workbook wb(srcDir + u"sampleCrosssType.xlsx");

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Save PDF file
    wb.Save(outDir + u"outputCrosssType.pdf", pdfSaveOptions);

    // Initialize image or print options
    ImageOrPrintOptions imageSaveOptions;
    imageSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Initialize sheet renderer object
    SheetRender sheetRenderer(wb.GetWorksheets().Get(0), imageSaveOptions);

    // Save PNG image
    sheetRenderer.ToImage(0, outDir + u"outputCrosssType.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
