---
title: Ställ in kolumnbredd till skalbar enhet som em eller procent med C++
linktitle: Ange kolumnbredden till skalbar enhet som em eller procent
type: docs
weight: 130
url: /sv/cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Lär dig hur du ställer in kolumnbredd till skalbara enheter som em eller procent med Aspose.Cells for C++.
---

Att generera en HTML-fil från ett kalkylblad är mycket vanligt. Storleken på kolumnerna definieras i "pt" vilket fungerar i många fall. Det kan dock vara så att denna fasta storlek inte är nödvändig. Till exempel om en behållarepanel har en bredd på 600px där den här HTML-sidan visas. I detta fall kan du få en horisontell rullgardin om den genererade tabellbredden är större. Det var nödvändigt att denna fasta storlek ska ändras till en skalbar enhet som em eller procent för att få en bättre presentation. Följande provkod kan användas där [**HtmlSaveOptions.GetWidthScalable()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getwidthscalable/) är inställd på **true** för att skapa skalbar bredd.

Källfilen och utdatafiler kan laddas ned från följande länkar:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```c++
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

    // Load sample source file
    Workbook wb(srcDir + u"sampleForScalableColumns.xlsx");

    // Specify Html Save Options
    HtmlSaveOptions options;

    // Set the property for scalable width
    options.SetWidthScalable(true);

    // Specify image save format
    options.SetExportImagesAsBase64(true);

    // Save the workbook in Html format with specified Html Save Options
    wb.Save(outDir + u"outsampleForScalableColumns.html", options);

    std::cout << "Workbook saved successfully with scalable columns!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
