---
title: Rita slicer under rendering av Excel till PDF med C++
linktitle: Rita Slicer vid rendering av Excel till PDF
type: docs
weight: 60
url: /sv/cpp/draw-slicer-while-rendering-excel-to-pdf/
description: Exportera Excel till PDF med slicerinställningar med Aspose.Cells och C++.
---

## **Rita Slicer vid rendering av Excel till PDF**
Om du har en Excel-fil som har en slicer applicerad på sig och du vill exportera Excel till PDF med slicerinställningarna, stöder Aspose.Cells detta nu som standard. Du exporterar enkelt Excel-filen med slicer till PDF, och den genererade PDF:en visar den tillämpade slicern.

Följande exempelkod laddar in [exempel Excel-filen](94044165.xlsx) som innehåller en befintlig slicer. Den sparar sedan arbetsboken som [utmatnings PDF-filen](94044166.pdf). Följande skärmdump jämför käll-Excel-filen och den genererade PDF-filen.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **Exempelkod**
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
