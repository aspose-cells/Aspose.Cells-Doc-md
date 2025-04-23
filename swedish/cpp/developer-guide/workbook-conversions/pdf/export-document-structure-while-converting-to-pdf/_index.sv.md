---  
title: Exportera dokumentstruktur vid konvertering till PDF med C++  
linktitle: Exportera dokumentstruktur vid konvertering till PDF  
type: docs  
weight: 360  
url: /sv/cpp/export-document-structure-while-converting-to-pdf/  
description: Lär dig hur man exporterar dokumentstrukturen vid konvertering till PDF med Aspose.Cells i C++.  
---  

Möjligheterna för PDF-logisk struktur ger ett sätt att inkludera information om dokumentets innehållsstruktur i en PDF-fil. Aspose.Cells behåller information om strukturen från ett Microsoft Excel-dokument, såsom celler, rader, tabeller, arbetsblad, bilder, former, sidhuvud/sidfot etc.  

Med alternativet [PdfSaveOptions.GetExportDocumentStructure()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getexportdocumentstructure/) kan du spara till en märkt PDF med dokumentstrukturen exporterad.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the Excel file with image, shape, chart, etc.
    Workbook workbook(u"document-structure-example.xlsx");

    // Set to export document structure.
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetExportDocumentStructure(true);

    // Save the PDF file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file saved successfully with document structure!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  


