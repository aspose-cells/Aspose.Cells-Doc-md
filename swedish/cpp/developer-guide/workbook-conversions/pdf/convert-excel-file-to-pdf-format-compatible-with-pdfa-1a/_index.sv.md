---
title: Konvertera Excel fil till PDF format kompatibelt med PDFA 1a med C++
linktitle: Konvertera Excelfil till PDF format kompatibelt med PDFA 1a
type: docs
weight: 130
url: /sv/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Lär dig hur du konverterar Excel filer till PDF/A 1a kompatibla PDF format med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

PDF/A är en unik variant av PDF designad för långsiktigt bevarande av dokument. PDF/A är en ISO-standardiserad version av det bärbara dokumentformatsformatet (PDF) som är ett arkivformat för PDF som inbäddar alla typsnitt som används i dokumentet inom PDF-filen. PDF/A skiljer sig från PDF genom att förbjuder funktioner som typsnittlänkning (i stället för typsnittsinbäddning) och kryptering. Aspose.Cells gör det möjligt att spara Excel-filer till PDF/A-kompatibla PDF-filer (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab och PDF/A-3u stöds). Denna guide beskriver hur man sparar arbetsboken i PDF/A-kompatibelt PDF-format.

## **Konvertera Excel-fil till PDF-format kompatibelt med PDF/A-1a**

Utvecklare kan använda klassen [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) för att ställa in olika attribut för konverteringen. Att ställa in olika egenskaper för klassen [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) ger dig kontroll över utskrift, typsnitt, säkerhet och kompressionsinställningar för den valda PDF-filen. Den viktigaste egenskapen är [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/), som gör att du kan spara Excel-filer till PDF/A-kompatibla PDF-filer.

Följande provkod förklarar hur man konverterar Excel-fil till PDF-format kompatibelt med PDF/A-1a. Se [utmatnings-PDF](outputCompliancePdfA1a.pdf) samt skärmbilden för referens.

## **Skärmdump**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and add some message inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This PDF format is compatible with PDFA-1a.");

    // Create pdf save options and set its compliance to PDFA-1a
    PdfSaveOptions opts;
    opts.SetCompliance(PdfCompliance::PdfA1a);

    // Save the output pdf
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputCompliancePdfA1a.pdf", opts);

    std::cout << "PDF created successfully with PDFA-1a compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
