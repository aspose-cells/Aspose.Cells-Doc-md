---
title: Habilitar Propiedades Personalizadas de CSS al guardar en HTML con C++
linktitle: Habilitar Propiedades Personalizadas de CSS al guardar en HTML
type: docs
weight: 320
url: /es/cpp/enable-css-custom-properties-while-saving-to-html/
description: Aprende cómo habilitar las propiedades personalizadas de CSS al guardar archivos de Excel en HTML usando Aspose.Cells for C++. Mejora el rendimiento reduciendo datos de imagen redundantes.
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel en HTML, en el escenario que haya múltiples ocurrencias para una misma imagen en base64, con propiedad personalizada, solo es necesario guardar los datos de la imagen una vez, mejorando así el rendimiento del HTML resultante. Usa la propiedad [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/) y configúrala a **true** al guardar en HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Habilitar Propiedades Personalizadas de CSS al guardar en HTML**

El siguiente código de ejemplo muestra el uso de la propiedad [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/). La captura de pantalla muestra el efecto de esta propiedad cuando no está configurada a **true**. Por favor, descarga el [archivo de Excel de ejemplo](50528260.xlsx) utilizado en este código y el [HTML de salida](50528261.zip) generado para referencia.

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
    Workbook wb(srcDir + u"sampleEnableCssCustomProperties.xlsx");

    // Create HtmlSaveOptions object
    HtmlSaveOptions opts;

    // Set ExportImagesAsBase64 to true
    opts.SetExportImagesAsBase64(true);

    // Enable EnableCssCustomProperties
    opts.SetEnableCssCustomProperties(true);

    // Save the workbook in HTML format
    wb.Save(outDir + u"outputEnableCssCustomProperties.html", opts);

    std::cout << "Workbook saved successfully with CSS custom properties enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
