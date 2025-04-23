---
title: Dibuja un segmentador al renderizar Excel a PDF con C++
linktitle: Dibujar un rebanador mientras se renderiza Excel a PDF
type: docs
weight: 60
url: /es/cpp/draw-slicer-while-rendering-excel-to-pdf/
description: Exporta Excel a PDF con configuraciones de segmentador usando Aspose.Cells con C++.
---

## **Dibujar un rebanador al renderizar Excel a PDF**
Si tienes un archivo de Excel al que se le aplicó un segmentador y deseas exportar el Excel a PDF con la configuración del segmentador, Aspose.Cells ahora soporta esto por defecto. Solo exporta el archivo de Excel con segmentador a PDF, y el PDF generado mostrará el segmentador aplicado.

El siguiente código de ejemplo carga el [archivo Excel de muestra](94044165.xlsx) que contiene un filtro existente. Luego guarda el libro como [archivo PDF de salida](94044166.pdf). La siguiente captura de pantalla compara el archivo Excel de origen y el archivo PDF generado.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **Código de muestra**
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
