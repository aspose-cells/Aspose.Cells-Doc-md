---
title: Autofit Rader för Rendering med C++
linktitle: Autoanpassa rader för rendering
type: docs
weight: 130
url: /sv/cpp/autofit-rows-for-rendering/
description: Lär dig hur du autofitar rader för rendering i Excel filer med Aspose.Cells och C++.
---

I allmänhet, när du vill visa all text i en cell kan du använda autofit för rad i Normalt läge med 100% zoom i Microsoft Excel. Detta gör att texten blir helt synlig i Normalt läge, och även när du skriver ut eller sparar filen som en PDF kommer texten att visas korrekt.

I vissa fall fungerar dock autofit-raden bra i Normalt läge, men när du växlar till utskriftsvy eller sparar filen som en PDF klipps texten. Var god kontrollera källfilen [Book1.xlsx](Book1.xlsx) och skärmklippen.

![text klipps i utskriftsvyn](text_klipps_i_utskriftsvyn.png)

Om du vill förhindra att text klipps i den sparade PDF-filen kan du autofitta raden med alternativet [AutoFitterOptions.GetForRendering()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getforrendering/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize workbook instance
    Workbook workbook(u"Book1.xlsx");

    // Set autofit options for rendering
    AutoFitterOptions autoFitterOptions;
    autoFitterOptions.SetForRendering(true);

    // Autofit rows with options
    workbook.GetWorksheets().Get(0).AutoFitRows(autoFitterOptions);

    // Save to PDF
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    Aspose::Cells::Cleanup();
}
```

Nu är texten inte klippt i den här PDF-filen.

![text klipps inte i sparad pdf](text_klipps_inte_i_sparad_pdf.png)
