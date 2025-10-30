---
title: Desactivar CSS al guardar en HTML con C++
linktitle: Desactivar CSS al guardar en HTML
type: docs
weight: 320
url: /es/cpp/disable-css-while-saving-to-html/
description: Aprende cómo desactivar CSS al guardar archivos de Excel en HTML usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel como HTML de una sola página, generalmente los elementos CSS se insertan dentro del archivo HTML y se ubican en la sección HEAD. Si adjuntas este archivo como contenido/cuerpo de un email, la mayoría de los clientes de correo eliminarán los elementos CSS, resultando en una presentación incorrecta. La versión 24.12 de Aspose.Cells introduce una opción que permite desactivar CSS opcionalmente, permitiendo que los estilos se apliquen directamente en los elementos HTML. Si deseas establecer el HTML como contenido/cuerpo del correo, usa la propiedad [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/) y configúrala en **true**.

## **Desactivar CSS al guardar en HTML**

El siguiente código muestra cómo usar la propiedad [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/).

## **Código de muestra**

```cpp
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

    // Load sample workbook
    Workbook wb(srcDir + u"sampleDisableCss.xlsx");

    // Disable CSS
    HtmlSaveOptions opts;
    opts.SetDisableCss(true);

    // Save the workbook in HTML
    wb.Save(outDir + u"outputDisable.html", opts);

    std::cout << "Workbook saved with CSS disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
