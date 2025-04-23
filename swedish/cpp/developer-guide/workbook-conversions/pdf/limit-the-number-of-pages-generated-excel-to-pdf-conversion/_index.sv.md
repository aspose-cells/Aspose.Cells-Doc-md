---
title: Begränsa antalet genererade sidor  Excel till PDF konvertering med C++
linktitle: Begränsa antalet genererade sidor
type: docs
weight: 180
url: /sv/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Lär dig hur du begränsar antalet sidor som genereras när du konverterar Excel till PDF med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Ibland vill du skriva ut en serie sidor till en utdatan PDF-fil. Aspose.Cells har förmågan att begränsa antalet sidor som genereras vid konvertering av ett Excel-kalkylark till PDF-filformat.

{{% /alert %}}

## **Begränsning av antalet genererade sidor**

Följande exempel visar hur man renderar en rad sidor (3 och 4) i en Microsoft Excel-fil till PDF.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"TestBook.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Instantiate the PdfSaveOption
    PdfSaveOptions options;

    // Print only Page 3 and Page 4 in the output PDF
    // Starting page index (0-based index)
    options.SetPageIndex(3);
    // Number of pages to be printed
    options.SetPageCount(2);

    // Path of output PDF file
    U16String outputFilePath = srcDir + u"outPDF1.out.pdf";

    // Save the PDF file
    wb.Save(outputFilePath, options);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Om kalkylbladet innehåller formler är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) precis innan du renderar det till PDF. Det säkerställer att formelberoende värden beräknas om och de korrekta värdena renderas i den utdatafil som genereras.

{{% /alert %}}
