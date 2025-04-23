---
title: Ocultar contenido superpuesto con CrossHideRight al guardarlo en HTML con C++
linktitle: Ocultar contenido superpuesto con CrossHideRight al guardar en HTML
type: docs
weight: 100
url: /es/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Usa CrossHideRight con Aspose.Cells en C++ para ocultar contenido superpuesto al guardar en HTML.
---

## **Escenarios de uso posibles**

Al guardar tu archivo de Excel en HTML, puedes especificar diferentes tipos de cruce para las cadenas de celdas. Por defecto, Aspose.Cells genera HTML según Microsoft Excel, pero cuando cambias el tipo de cruce a [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype), oculta todas las cadenas en el lado derecho de la celda que están superpuestas o solapadas con la cadena de la celda.

## **Ocultar contenido superpuesto con CrossHideRight al guardar en Html**

El siguiente código de ejemplo carga el [archivo Excel de ejemplo](64716894.xlsx) y lo guarda en [HTML de salida](64716893.zip) después de configurar [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gethtmlcrossstringtype/) como [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). La captura de pantalla explica cómo [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) afecta el HTML de salida respecto al predeterminado.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");

    // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::CrossHideRight);

    // Save to HTML with HtmlSaveOptions
    wb.Save(outputDir + u"outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html", opts);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
