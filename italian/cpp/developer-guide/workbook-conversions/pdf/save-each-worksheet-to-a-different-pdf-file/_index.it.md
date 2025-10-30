---
title: Salva ogni foglio di lavoro in un file PDF diverso con C++
linktitle: Salva ciascun foglio di calcolo in un file PDF separato
type: docs
weight: 130
url: /it/cpp/save-each-worksheet-to-a-different-pdf-file/
description: Scopri come salvare ogni foglio di lavoro di un file Excel in un file PDF separato usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Aspose.Cells supporta la conversione di file XLS (che contengono immagini, grafici, ecc.) in documenti PDF. Aspose.Cells for C++ può funzionare indipendentemente per convertire un foglio di calcolo in PDF e non è necessario usare Aspose.PDF per C++ per la conversione. La conversione non richiede che il software crei o usi file temporanei poiché l'intero processo può essere eseguito in memoria.

{{% /alert %}} 

## **Salva ciascun foglio di calcolo in un file PDF separato**
Se hai bisogno di salvare ogni foglio del tuo file Excel modello per generare diversi file PDF, puoi farlo facilmente. Puoi provare a impostare un indice di foglio a [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) alla volta per renderlo in PDF.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Get the Excel file path
    U16String filePath = srcDir + u"input.xlsx";

    // Instantiate a new workbook and open the Excel file from its location
    Workbook workbook(filePath);

    // Get the count of the worksheets in the workbook
    int sheetCount = workbook.GetWorksheets().GetCount();

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Take PDFs of each sheet
    for (int j = 0; j < sheetCount; j++)
    {
        Worksheet ws = workbook.GetWorksheets().Get(j);

        // Set worksheet to output
        SheetSet sheetSet(Vector<int32_t>{ ws.GetIndex() });
        pdfSaveOptions.SetSheetSet(sheetSet);

        // Save the workbook with the current worksheet as PDF
        workbook.Save(srcDir + u"worksheet-" + ws.GetName() + u".out.pdf", pdfSaveOptions);
    }

    std::cout << "PDFs generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Se il tuo foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) subito prima di renderizzarlo in formato PDF. Questo assicura che i valori dipendenti dalle formule siano ricalcolati, e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
