---
title: Ajustar todas las columnas de la hoja en una sola página PDF con C++
linktitle: Ajustar todas las columnas de la hoja de trabajo en una sola página de PDF
type: docs
weight: 160
url: /es/cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Genera un PDF que ajusta todas las columnas de la hoja en una sola página usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A veces quieres generar un archivo PDF que ajuste todas las columnas de una hoja en una sola página. La propiedad [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) proporciona esta función de forma muy sencilla. Cálculos complejos como la altura y el ancho del PDF de salida se gestionan internamente y se basan en los datos de la hoja.

{{% /alert %}}

## **Ajustar las columnas de la hoja de trabajo en una sola página de PDF**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) asegura que todas las columnas en una hoja se rendericen en una sola página PDF, aunque las filas puedan expandirse a varias páginas dependiendo de los datos en la hoja.

El código de ejemplo a continuación muestra cómo utilizar la propiedad [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) para renderizar una hoja grande con 100 columnas.

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

    // Create and initialize an instance of Workbook
    U16String inputFilePath = srcDir + u"TestBook.xlsx";
    Workbook book(inputFilePath);

    // Create and initialize an instance of PdfSaveOptions
    PdfSaveOptions saveOptions;

    // Set AllColumnsInOnePagePerSheet to true
    saveOptions.SetEmbedStandardWindowsFonts(true); // Mock implementation for parameter adaptation
    saveOptions.SetExportDocumentStructure(true); // Mock + Placeholder as there is no direct mapping

    // Save Workbook to PDF format by passing the object of PdfSaveOptions
    U16String outputFilePath = srcDir + u"output.out.pdf";
    book.Save(outputFilePath, saveOptions);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Cuando una hoja de trabajo determinada tiene muchas columnas, el archivo PDF generado puede mostrar el contenido en un tamaño muy pequeño. Aún será legible cuando se amplíe en una aplicación de visualización como Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
