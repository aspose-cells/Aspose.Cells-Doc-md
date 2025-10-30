---
title: Rendera en PDF sida per Excel listblad  Excel till PDF konvertering med C++
type: docs
weight: 100
url: /sv/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Konvertera Excel listblad till PDF format med en sida för varje blad med Aspose.Cells och C++.
---

{{% alert color="primary" %}} 

När du arbetar med stora Microsoft Excel-filer (t.ex. en arbetsbok med många blad, varje med 50 kolumner och 300 eller fler rader med data) kanske du vill att PDF-utgången ska visa en sida per kalkylblad, oavsett storleken på bladet. Detta innebär att varje sida sannolikt kommer att ha en radikalt annorlunda sidstorlek. Detta kan uppnås med hjälp av Aspose.Cells for C++.

{{% /alert %}} 

Se följande exempel på kod som konverterar en Excel-fil med flera kalkylblad till PDF.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Initialize a new Workbook and open an Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Implement one page per worksheet option
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetOnePagePerSheet(true);

    // Save the PDF file
    U16String outputFile = srcDir + u"OutputFile.out.pdf";
    workbook.Save(outputFile, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Om [PaginatedSaveOptions(PaginatedSaveOptions_Impl*)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) är inställt på **true**, kommer allt bladinnehåll att renderas till en enda PDF-sida.

{{% /alert %}} {{% alert color="primary" %}} 

Om ditt kalkylblad innehåller formler är det bäst att anropa [Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) precis innan du renderar kalkylbladet till PDF. Detta säkerställer att de formelberoende värdena omräknas och att de rätta värdena visas i PDF:en.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
