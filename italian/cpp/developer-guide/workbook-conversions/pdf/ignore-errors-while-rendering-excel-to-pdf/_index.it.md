---
title: Ignora gli Errori durante il Rendering di Excel in PDF con C++
linktitle: Ignora gli errori durante la conversione di Excel in PDF
type: docs
weight: 80
url: /it/cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Impara come ignorare gli errori durante la conversione di Excel in PDF utilizzando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

A volte, quando converti il tuo file Excel in PDF, si verificano errori o eccezioni e il processo di conversione termina. Puoi ignorare tutti questi errori durante il processo di conversione utilizzando la proprietà [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/). In questo modo, il processo di conversione verrà completato senza errori o eccezioni, ma potrebbe verificarsi perdita di dati. Pertanto, utilizza questa proprietà solo se la perdita di dati non è critica per te.

## **Ignora gli errori durante la conversione di Excel in PDF**

Il seguente codice carica il [file Excel di esempio](55541778.xlsx), ma il file Excel di esempio è errato e genera un errore durante la [conversione in PDF](55541779.pdf) in 17.11, ma poiché stiamo usando la proprietà [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/), non genera errori. Tuttavia, una *forma a freccia rossa arrotondata* come mostrato in questo screenshot viene persa.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Codice di Esempio**

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleErrorExcel2Pdf.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"outputErrorExcel2Pdf.pdf";

    // Load the Sample Workbook that throws Error on Excel2Pdf conversion
    Workbook wb(inputFilePath);

    // Specify Pdf Save Options - Ignore Error
    PdfSaveOptions opts;
    opts.SetIgnoreError(true);

    // Save the Workbook in Pdf with Pdf Save Options
    wb.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully with error ignored!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
