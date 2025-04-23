---
title: Återanvändning av stilobjekt med C++
linktitle: Återanvända stilobjekt
description: I Aspose.Cells for C++ kan du förenkla stilhantering och förbättra kodens effektivitet genom att skapa och använda återanvändbara stilobjekt. Vår guide hjälper dig att dra nytta av fördelarna med återanvändbara stilobjekt och implementera dem i din applikation.
keywords: Aspose.Cells for C++, Återanvändning av stilobjekt, Stilhantering, Kod effektivitet, Återanvändbara stilar, Applikationsutveckling, API dokumentation, Exempel på kod, Ladda ner, Support.
type: docs
weight: 3000
url: /sv/cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

Att återanvända stilobjekt kan spara minne och göra ett program snabbare.

{{% /alert %}}

För att tillämpa viss formatering på en stor omfattning av celler i en arbetsbok:

1. Skapa en stilobjekt.
1. Ange attributen.
1. Tillämpa stilen på cellerna i området.

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

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style styleObject = workbook.CreateStyle();
    styleObject.GetFont().SetColor(Color::Red());
    styleObject.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(styleObject);
    cell2.SetStyle(styleObject);

    // Put the values inside the cell
    cell1.PutValue(u"Hello World!");
    cell2.PutValue(u"Hello World!!");

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Eftersom tillvägagångssättet [**Cell.GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) använder mycket mindre minne och är effektivt, togs den äldre Cell.Style-egenskapen bort med versionen Aspose.Cells 7.1.0, vilken använde mycket onödigt minne.

{{% /alert %}}
