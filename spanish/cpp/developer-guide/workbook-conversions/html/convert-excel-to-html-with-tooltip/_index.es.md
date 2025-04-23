---
title: Convertir Excel a HTML con tooltip usando C++
linktitle: Convertir Excel a HTML con tooltip
type: docs
weight: 200
url: /es/cpp/convert-excel-to-html-with-tooltip/
description: Convertir Excel a HTML añadiendo tooltips con Aspose.Cells usando C++.
---

## **Convertir Excel a HTML con tooltip**

Podría haber casos en los que el texto se corte en el HTML generado y desees mostrar el texto completo como tooltip al pasar el cursor. Aspose.Cells soporta esto proporcionando la propiedad [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/). Establecer la propiedad [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/) en **true** añadirá el texto completo como tooltip en el HTML generado.

La siguiente imagen muestra el tooltip en el archivo HTML generado.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

El siguiente ejemplo carga el [archivo fuente de Excel](98107416.xlsx) y genera el [archivo HTML de salida](98107417.zip) con el tooltip.

Código de muestra

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook workbook(sourceDir + u"AddTooltipToHtmlSample.xlsx");

    // Setup HTML save options
    HtmlSaveOptions options;
    options.SetAddTooltipText(true);  // Enable tooltip text in output

    // Save as HTML
    workbook.Save(outputDir + u"AddTooltipToHtmlSample_out.html", options);

    std::cout << "Workbook saved with tooltip text added!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
