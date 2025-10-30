---
title: Excluir estilos no utilizados durante la conversión de Excel a HTML con C++
linktitle: Excluir estilos no utilizados
type: docs
weight: 30
url: /es/cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Aprende cómo excluir estilos no utilizados durante la conversión de Excel a HTML usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Los archivos de Microsoft Excel pueden contener muchos estilos no utilizados. Cuando exportas el archivo Excel a formato HTML, estos estilos no utilizados también se exportan, lo que puede aumentar el tamaño del HTML. Puedes excluir los estilos no utilizados durante la conversión de un archivo Excel a HTML usando la propiedad [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/). Cuando la configuras a **true**, todos los estilos no utilizados son excluidos del HTML de salida. La siguiente captura muestra un ejemplo de estilo no utilizado dentro del HTML de salida.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Excluir estilos no utilizados durante la conversión de Excel a HTML**

El siguiente código de ejemplo crea un libro de trabajo y también crea un estilo no utilizado. Dado que [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/) está configurado a **true**, este estilo no utilizado no será exportado al [HTML de salida](61767778.zip). Sin embargo, si lo configuras a **false**, este estilo no utilizado estará presente en el HTML de salida, como se muestra en la captura arriba.

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Create an unused named style
    Style unusedStyle = wb.CreateStyle();
    unusedStyle.SetName(u"UnusedStyle_XXXXXXXXXXXXXX");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some value in cell C7
    ws.GetCells().Get(u"C7").PutValue(u"This is sample text.");

    // Specify html save options, we want to exclude unused styles
    HtmlSaveOptions opts;

    // Comment this line to include unused styles
    opts.SetExcludeUnusedStyles(true);

    // Save the workbook in html format
    wb.Save(u"outputExcludeUnusedStylesInExcelToHTML.html", opts);

    std::cout << "Workbook saved successfully with unused styles excluded!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
