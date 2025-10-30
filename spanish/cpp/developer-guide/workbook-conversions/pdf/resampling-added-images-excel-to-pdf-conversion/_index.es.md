---
title: Remuestreo de imágenes añadidas  Conversión de Excel a PDF con C++
linktitle: Imágenes Agregadas con Remuestreo  Conversión de Excel a PDF
type: docs
weight: 150
url: /es/cpp/resampling-added-images-excel-to-pdf-conversion/
description: Aprende cómo remuestrear imágenes añadidas para reducir el tamaño del PDF usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Al trabajar con grandes archivos de Microsoft Excel con muchas imágenes, es posible que necesite comprimir las imágenes agregadas para reducir el tamaño del archivo PDF de salida y mejorar el rendimiento general de la conversión. Aspose.Cells admite el remuestreo de imágenes agregadas para reducir el tamaño del archivo PDF de salida y mejorar un poco el rendimiento.

{{% /alert %}}

Consulte el siguiente código de ejemplo que describe cómo realizar la tarea utilizando la API de Aspose.Cells. El ejemplo convierte un archivo de Microsoft Excel a un archivo PDF mientras comprime las imágenes en el archivo.

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

    // Initialize a new Workbook and open an Excel file
    U16String inputPath = srcDir + u"input.xlsx";
    Workbook workbook(inputPath);

    // Instantiate the PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set Image Resample properties
    pdfSaveOptions.SetImageResample(300, 70);

    // Save the PDF file
    U16String outputPath = outDir + u"OutputFile_out_pdf.pdf";
    workbook.Save(outputPath, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

El uso de la opción [**SetImageResample**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setimageresample/) minimiza el tamaño del PDF de salida, pero puede afectar ligeramente la calidad de la imagen.

{{% /alert %}} 

{{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}
