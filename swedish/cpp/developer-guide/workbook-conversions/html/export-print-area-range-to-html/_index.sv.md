---
title: Exportera utskriftsområdesintervall till HTML med C++
linktitle: Exportera utskriftsområdet till HTML
type: docs
weight: 60
url: /sv/cpp/export-print-area-range-to/
description: Lär dig hur du exporterar utskriftsområdet till HTML med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Detta är ett vanligt scenario där vi behöver exportera endast utskriftsområdet, dvs. ett valt cellintervall, istället för hela bladet till HTML. Denna funktion är redan tillgänglig för PDF-rendering; nu kan du även göra detta för HTML. Först, ställ in utskriftsområdet i arbetsbladets siduppsättningsobjekt. Därefter, använd [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportprintareaonly/)-flaggan för att exportera endast det valda området.

## **Exempelkod**

Följande exempel kod hjälper dig att ladda en arbetsbok och sedan exportera utskriftsområdet till HTML. Testfilen för denna funktion kan laddas ner via länken:

[sampleInlineCharts.xlsx](79527946.xlsx)

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleInlineCharts.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputInlineCharts.html";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area
    worksheet.GetPageSetup().SetPrintArea(u"D2:M20");

    // Initialize HtmlSaveOptions
    HtmlSaveOptions options;

    // Set flag to export print area only
    options.SetExportPrintAreaOnly(true);

    // Save to HTML format
    workbook.Save(outputFilePath, options);

    std::cout << "HTML file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
