---
title: Desactivar exportación de Scripts de Marco y Propiedades de Documento con C++
type: docs
weight: 310
url: /es/cpp/disable-exporting-frame-scripts-and-document-properties/
description: Desactivar exportación de scripts de marco y propiedades de documento usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells exporta scripts de marco y propiedades de documento al convertir un libro de trabajo a HTML. La versión 8.6.0 de Aspose.Cells for C++ introduce una opción que permite desactivar opcionalmente la exportación de scripts de marco y propiedades de documento. Usa la propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties para desactivar la exportación.

{{% /alert %}}

## **Desactivar la exportación de scripts de marco y propiedades del documento**

El siguiente código de muestra te permite desactivar la exportación de scripts de marco y propiedades del documento. Una vez que conviertas un libro de trabajo a HTML, el archivo de salida no contendrá ningún script de marco ni propiedades del documento.

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

    // Open the required workbook to convert
    U16String inputFilePath = srcDir + u"Sample1.xlsx";
    Workbook workbook(inputFilePath);

    // Disable exporting frame scripts and document properties
    HtmlSaveOptions options;
    options.SetExportFrameScriptsAndProperties(false);

    // Save workbook as HTML
    workbook.Save(outDir + u"output.out.html", options);

    std::cout << "Workbook saved successfully as HTML!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
