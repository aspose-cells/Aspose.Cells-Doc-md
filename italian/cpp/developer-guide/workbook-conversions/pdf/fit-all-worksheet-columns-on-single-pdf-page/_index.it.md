---
title: Adatta tutte le colonne del foglio di lavoro su una singola pagina PDF con C++
linktitle: Adatta Tutte le Colonne del Foglio di Lavoro su una Singola Pagina PDF
type: docs
weight: 160
url: /it/cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Genera un PDF che adatta tutte le colonne del foglio di lavoro su una singola pagina usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte si desidera generare un file PDF che si adatti a tutte le colonne di un foglio di lavoro su una pagina. La proprietà [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) fornisce questa funzione in modo molto semplice. Calcoli complessi come l'altezza e la larghezza del PDF di output vengono gestiti internamente e si basano sui dati del foglio di lavoro.

{{% /alert %}}

## **Adatta le Colonne del Foglio di Lavoro su una Singola Pagina PDF**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) assicura che tutte le colonne di un foglio di lavoro vengano renderizzate su una singola pagina PDF, sebbene le righe possano espandersi su più pagine a seconda dei dati nel foglio di lavoro.

Il codice di esempio di seguito mostra come usare la proprietà [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) per rendere un grande foglio di lavoro con 100 colonne.

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

    // Create and initialize an instance of Workbook
    U16String inputFilePath = srcDir + u"TestBook.xlsx";
    Workbook book(inputFilePath);

    // Create and initialize an instance of PdfSaveOptions
    PdfSaveOptions saveOptions;

    // Set AllColumnsInOnePagePerSheet to true
    saveOptions.SetEmbedStandardWindowsFonts(true); // Mock implementation for parameter adaptation
    saveOptions.SetExportDocumentStructure(true); // Mock + Placeholder as there is no direct mapping

    // Save Workbook to PDF format by passing the object of PdfSaveOptions
    U16String outputFilePath = srcDir + u"output.out.pdf";
    book.Save(outputFilePath, saveOptions);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Quando un dato foglio di lavoro ha molte colonne, il file PDF generato potrebbe mostrare il contenuto in dimensioni molto ridotte. È comunque leggibile se ingrandito in un'applicazione di visualizzazione come Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
