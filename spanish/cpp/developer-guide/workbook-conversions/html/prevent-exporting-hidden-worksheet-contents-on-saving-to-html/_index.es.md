---
title: Prevenir la exportación de contenido oculto en la hoja de trabajo al guardar en HTML con C++
linktitle: Prevenir la exportación de contenido oculto de la hoja de trabajo
type: docs
weight: 210
url: /es/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Aprende cómo prevenir la exportación de contenido oculto de la hoja de trabajo al guardar libros de trabajo de Excel en HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puede guardar libros de Excel en HTML. Sin embargo, si el libro contiene hojas de cálculo ocultas, por defecto Aspose.Cells exporta los contenidos ocultos de la hoja de cálculo al directorio de salida HTML (_files) que contiene archivos como hojas de cálculo, imágenes, tabstrip.htm, stylesheet.css, etc. A veces, exportar el contenido de las hojas de cálculo ocultas de esta manera no es apropiado. Por ejemplo, si la hoja de cálculo oculta contiene imágenes que no deben ser exportadas al directorio _files.

{{% /alert %}}

Aspose.Cells proporciona la propiedad [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexporthiddenworksheet/). De forma predeterminada, está configurada en **true** y se exportan las hojas de cálculo ocultas a HTML. Si la establece en **false**, Aspose.Cells no exportará los contenidos de la hoja de cálculo oculta.

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
    U16String inputFilePath = srcDir + u"WorkbookWithHiddenContent.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"HtmlWithoutHiddenContent_out.html";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Create HTML save options
    HtmlSaveOptions options;

    // Do not export hidden worksheet contents
    options.SetExportHiddenWorksheet(false);

    // Save the workbook
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully without hidden content!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
