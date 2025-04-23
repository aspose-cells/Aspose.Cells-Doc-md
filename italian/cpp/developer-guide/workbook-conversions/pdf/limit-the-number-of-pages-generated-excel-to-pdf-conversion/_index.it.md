---
title: Limitare il Numero di Pagine Generate  Conversione Excel in PDF con C++
linktitle: Limitare il Numero di Pagine Generate
type: docs
weight: 180
url: /it/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Impara come limitare il numero di pagine generate durante la conversione di Excel in PDF usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte si desidera stampare un intervallo di pagine in un file PDF di output. Aspose.Cells ha la capacità di impostare un limite su quante pagine vengono generate durante la conversione di un foglio di calcolo di Excel nel formato di file PDF.

{{% /alert %}}

## **Limitazione del numero di pagine generate**

L'esempio seguente mostra come rendere un intervallo di pagine (3 e 4) in un file Microsoft Excel in PDF.

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

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) appena prima di renderlo in PDF. Questo assicura che i valori dipendenti dalle formule vengano ricalcolati e che i valori corretti vengano resi nel file di output.

{{% /alert %}}
