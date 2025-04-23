---
title: Disegna Slicer durante la conversione di Excel in PDF con C++
linktitle: Disegnare un filtro durante il rendering di Excel in PDF
type: docs
weight: 60
url: /it/cpp/draw-slicer-while-rendering-excel-to-pdf/
description: Esporta Excel in PDF con impostazioni di slicer utilizzando Aspose.Cells con C++.
---

## **Disegna lo slicer durante il rendering di Excel in PDF**
Se hai un file Excel con uno slicer applicato e vuoi esportarlo in PDF con le impostazioni dello slicer, Aspose.Cells supporta questa funzionalità di default. Basta esportare il file Excel con lo slicer in PDF e il PDF generato mostrerà lo slicer applicato.

Il seguente codice di esempio carica il [file Excel di esempio](94044165.xlsx) che contiene un slicer esistente. Quindi salva il libro di lavoro come [file PDF di output](94044166.pdf). La seguente schermata confronta il file Excel di origine e il file PDF generato.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **Codice di Esempio**
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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleSlicerChart.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"SampleSlicerChart.pdf";

    // Create workbook from the excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PDF file
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved as PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
