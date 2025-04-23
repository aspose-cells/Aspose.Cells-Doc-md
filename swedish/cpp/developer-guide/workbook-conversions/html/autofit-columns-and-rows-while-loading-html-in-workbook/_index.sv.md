---
title: Automatiskt anpassa kolumner och rader vid inläsning av HTML i arbetsbok med C++
linktitle: Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken
type: docs
weight: 120
url: /sv/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Lär dig hur man autofit kolumner och rader när du laddar HTML i en arbetsbok med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Du kan autofita kolumner och rader medan du laddar in din HTML-fil i Arbetsbokobjektet. Ställ in egenskapen [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) till **true** för detta ändamål.

## **Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken**

Följande exempelkod läser först in exemplet HTML i Arbetsboken utan några laddningsalternativ och sparar den i XLSX-format. Sedan laddar den igen exemplet HTML i Arbetsboken men denna gång, laddar HTML efter att ha ställt in egenskapen [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) till **true** och sparar den i XLSX-format. Vänligen ladda ner båda de resulterande excelfilerna dvs. [Resultat Excel-fil utan AutofitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) och [Resultat Excel-fil med AutofitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Följande skärmbild visar effekten av [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) egenskapen på båda utdata-excelfilerna.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

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

    // Sample HTML string
    U16String sampleHtml(u"<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>");

    // Convert HTML string to memory stream
    std::string utf8Data = sampleHtml.ToUtf8();
    Vector<uint8_t> ms(utf8Data.size());
    std::memcpy(ms.GetData(), utf8Data.data(), utf8Data.size());

    // Load memory stream into workbook
    Workbook wb(ms);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputWithout_AutoFitColsAndRows.xlsx");

    // Specify the HTMLLoadOptions and set AutoFitColsAndRows = true
    HtmlLoadOptions opts;
    opts.SetAutoFitColsAndRows(true);

    // Load memory stream into workbook with the above HTMLLoadOptions
    Workbook wbWithOptions(ms, opts);

    // Save the workbook in xlsx format
    wbWithOptions.Save(outDir + u"outputWith_AutoFitColsAndRows.xlsx");

    std::cout << "HTML to Excel conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
