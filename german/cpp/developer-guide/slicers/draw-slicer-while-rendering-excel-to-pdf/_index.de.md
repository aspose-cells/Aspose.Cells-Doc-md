---
title: Zeichnen Sie Slicer beim Rendern von Excel in PDF mit C++
linktitle: Slicer zeichnen beim Rendern von Excel zu PDF
type: docs
weight: 60
url: /de/cpp/draw-slicer-while-rendering-excel-to-pdf/
description: Excel mit Slicer Einstellungen nach PDF exportieren mit Aspose.Cells in C++.
---

## **Slicer zeichnen beim Rendern von Excel zu PDF**
Wenn Sie eine Excel-Datei mit einem Slicer haben und diese mit Slicer-Einstellungen in PDF exportieren möchten, unterstützt Aspose.Cells dies jetzt standardmäßig. Sie exportieren einfach die Excel-Datei mit Slicer nach PDF, und das generierte PDF zeigt den Slicer in der angewendeten Version.

Der folgende Beispielcode lädt die [Beispieldatei](94044165.xlsx), die bereits einen Slicer enthält. Dann speichert er die Arbeitsmappe als [Ausgabe-PDF-Datei](94044166.pdf). Der folgende Screenshot vergleicht die Quell-Excel-Datei und die generierte PDF-Datei.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **Beispielcode**
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
