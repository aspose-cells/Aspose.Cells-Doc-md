---
title: Renderizar una página PDF por cada hoja de Excel  Conversión de Excel a PDF con C++
type: docs
weight: 100
url: /es/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Convierte hojas de Excel en formato PDF con una página por cada hoja usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

Al trabajar con archivos grandes de Microsoft Excel (por ejemplo, un libro que tiene muchas hojas, cada una con 50 columnas y 300 o más filas de datos), puede que desees que la salida en PDF muestre una página por cada hoja, independientemente del tamaño de la hoja. Esto implicará que cada página tenga un tamaño de página muy diferente. Esto se puede lograr usando Aspose.Cells for C++.

{{% /alert %}} 

Consulte el siguiente código de ejemplo que convierte un archivo de Excel con varias hojas de cálculo a PDF.

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

    // Initialize a new Workbook and open an Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Implement one page per worksheet option
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetOnePagePerSheet(true);

    // Save the PDF file
    U16String outputFile = srcDir + u"OutputFile.out.pdf";
    workbook.Save(outputFile, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Si la opción [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)]](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) está configurada en **true**, todo el contenido de la hoja se renderizará en una sola página PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Si tu hoja de cálculo contiene fórmulas, es recomendable llamar a [Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) justo antes de renderizar la hoja a PDF. Esto asegura que los valores dependientes de fórmula se recalcule y que los valores correctos se muestren en el PDF.

{{% /alert %}}
