---
title: Desactivar los Comentarios Downlevel Revealed al guardar en HTML con C++
linktitle: Desactivar Comentarios Revelados en Niveles Inferiores
type: docs
weight: 20
url: /es/cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Eliminar Comentarios Revelados en Niveles Inferiores al guardar archivos de Excel en HTML usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel en HTML, Aspose.Cells revela Comentarios Condicionales en Niveles Inferiores. Estos comentarios condicionales son principalmente relevantes para versiones antiguas de Internet Explorer y son irrelevantes para navegadores Web modernos. Puedes leer sobre ellos en detalle en el siguiente enlace.

- [Comentario condicional - comentario condicional revelado de niveles inferiores](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells te permite eliminar estos Comentarios Revelados en Niveles Inferiores configurando la propiedad [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/) a **true**.

## **Desactivar Comentarios Revelados de Niveles Inferiores al guardar en HTML**

El siguiente código de ejemplo muestra el uso de la propiedad [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/). La captura de pantalla muestra el efecto de esta propiedad cuando no está configurada a true. Por favor, descarga el [archivo de Excel de ejemplo](50528257.xlsx) utilizado en este código y el [HTML de salida](50528258.zip) generado para referencia.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample workbook
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(sourceDir + u"sampleDisableDownlevelRevealedComments.xlsx");

    // Disable DisableDownlevelRevealedComments
    HtmlSaveOptions opts;
    opts.SetDisableDownlevelRevealedComments(true);

    // Save the workbook in html
    wb.Save(outputDir + u"outputDisableDownlevelRevealedComments_true.html", opts);

    std::cout << "Workbook saved successfully with DisableDownlevelRevealedComments enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
