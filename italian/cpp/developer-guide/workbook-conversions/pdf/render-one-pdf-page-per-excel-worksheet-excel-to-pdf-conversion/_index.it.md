---
title: Rendi una pagina PDF per ogni foglio di lavoro di Excel  Conversione Excel in PDF con C++
type: docs
weight: 100
url: /it/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Converti i fogli di lavoro di Excel in formato PDF con una pagina per ogni foglio utilizzando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

Quando si lavora con file Microsoft Excel di grandi dimensioni (ad esempio una cartella di lavoro con molti fogli, ciascuno con 50 colonne e 300 o più righe di dati), potresti voler che l'output PDF mostri una pagina per ogni foglio, indipendentemente dalle dimensioni del foglio. Ciò significa che ogni pagina avrà probabilmente una dimensione molto diversa. Questo può essere ottenuto usando Aspose.Cells for C++.

{{% /alert %}} 

Si prega di vedere il seguente codice di esempio che converte un file di Excel con più fogli di lavoro in PDF.

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

Se l'opzione [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) è impostata su **true**, tutto il contenuto del foglio verrà renderizzato in una singola pagina PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Se il tuo foglio di calcolo contiene formule, è meglio chiamare [Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) prima di rendere il foglio di calcolo in PDF. Questo assicura che i valori dipendenti dalle formule siano ricalcolati e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}
