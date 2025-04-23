---
title: Convertire file XLS con immagini o grafici in PDF con C++
linktitle: Converti il file XLS con immagini o grafici nel formato PDF
type: docs
weight: 50
url: /it/cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Convertire file XLS contenenti immagini o grafici in documenti PDF utilizzando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

Aspose.Cells supporta la conversione di file XLS contenenti immagini e grafici in documenti PDF. Aspose.Cells for C++ può funzionare indipendentemente per convertire un foglio di calcolo in PDF: non è necessario Aspose.PDF per C++ per la conversione. Il processo può essere eseguito in memoria poiché non dipende da file XML temporanei o intermedi. Ciò significa che grandi file Excel, ad esempio quelli che contengono immagini, grafici e altri oggetti di disegno, possono essere convertiti rapidamente ed efficacemente.

{{% /alert %}} 
## **Codice di Esempio**

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String designerFile = srcDir + u"SampleInput.xls";

    // Path of output pdf file
    U16String pdfFile = outDir + u"Output.out.pdf";

    try
    {
        // Open the template excel file
        std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(designerFile);

        // Save the pdf file
        wb->Save(pdfFile, SaveFormat::Pdf);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}} 

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [Calculate(CalculationData data)](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/) subito prima di convertirlo in PDF. In questo modo si garantisce che i valori dipendenti dalle formule siano ricalcolati e i valori corretti siano visualizzati nel PDF.

{{% /alert %}}
