---
title: Limitar el número de páginas generadas  Conversión de Excel a PDF con C++
linktitle: Limitar el número de páginas generadas
type: docs
weight: 180
url: /es/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Aprende cómo limitar el número de páginas generadas al convertir Excel a PDF usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A veces, deseas imprimir un rango de páginas en un archivo PDF de salida. Aspose.Cells tiene la capacidad de establecer un límite en cuántas páginas se generan al convertir una hoja de cálculo de Excel al formato de archivo PDF.

{{% /alert %}}

## **Limitar el número de páginas generadas**

El siguiente ejemplo muestra cómo renderizar un rango de páginas (3 y 4) en un archivo de Microsoft Excel a PDF.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"TestBook.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Instantiate the PdfSaveOption
    PdfSaveOptions options;

    // Print only Page 3 and Page 4 in the output PDF
    // Starting page index (0-based index)
    options.SetPageIndex(3);
    // Number of pages to be printed
    options.SetPageCount(2);

    // Path of output PDF file
    U16String outputFilePath = srcDir + u"outPDF1.out.pdf";

    // Save the PDF file
    wb.Save(outputFilePath, options);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) justo antes de renderizarla a PDF. Haciendo esto asegura que se recalculen los valores dependientes de la fórmula y que se rendericen correctamente en el archivo de salida.

{{% /alert %}}
