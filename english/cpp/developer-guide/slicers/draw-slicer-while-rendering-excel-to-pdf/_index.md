---
title: Draw Slicer while rendering Excel to PDF with C++
linktitle: Draw Slicer while rendering Excel to PDF
type: docs
weight: 60
url: /cpp/draw-slicer-while-rendering-excel-to-pdf/
description: Export Excel to PDF with slicer settings using Aspose.Cells with C++.
---

## **Draw Slicer while rendering Excel to PDF**
If you have an Excel file which has a slicer applied to it and you want to export the Excel to PDF with the slicer settings, Aspose.Cells now supports this by default. You simply export the Excel file with a slicer to PDF, and the generated PDF will show the slicer applied.

The following sample code loads the [sample Excel file](94044165.xlsx) that contains an existing slicer. It then saves the workbook as [output PDF file](94044166.pdf). The following screenshot compares the source Excel file and the generated PDF file.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **Sample Code**
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