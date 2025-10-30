---
title: Ignorar errores al convertir Excel a PDF con C++
linktitle: Ignorar Errores al Renderizar Excel a PDF
type: docs
weight: 80
url: /es/cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Aprende cómo ignorar errores durante la conversión de Excel a PDF usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

A veces, al convertir tu archivo de Excel a PDF, ocurren errores o excepciones y el proceso de conversión termina. Puedes ignorar estos errores durante la conversión usando la propiedad [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/). De esta manera, el proceso de conversión finalizará sin lanzar errores o excepciones, aunque puede ocurrir pérdida de datos. Utiliza esta propiedad solo si la pérdida de datos no es crítica para ti.

## **Ignorar errores al renderizar Excel a PDF**

El siguiente código carga el [archivo de Excel de muestra](55541778.xlsx), pero este archivo de Excel presenta errores y genera un error durante la [conversión a PDF](55541779.pdf) en 17.11. Sin embargo, dado que estamos usando la propiedad [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/), no genera error. Sin embargo, una *forma con flecha roja redondeada* como la que se muestra en esta captura de pantalla se pierde.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Código de muestra**

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
{{< app/cells/assistant language="cpp" >}}
