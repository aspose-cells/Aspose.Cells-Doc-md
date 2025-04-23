---
title: Ocultar contenido superpuesto con CrossHideRight al guardar en HTML
type: docs
weight: 100
url: /es/python-net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Escenarios de uso posibles**

Al guardar tu archivo Excel en HTML, puedes especificar diferentes tipos de cruce para cadenas de celdas. Por defecto, Aspose.Cells para Python via .NET genera HTML según Microsoft Excel, pero al cambiar el tipo de cruce a [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/), oculta todas las cadenas en el lado derecho de la celda que estén superpuestas o se crucen con la cadena de la celda.

## **Ocultar contenido superpuesto con CrossHideRight al guardar en Html**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716894.xlsx) y lo guarda en [HTML de salida](64716893.zip) después de configurar [**HtmlSaveOptions.html_cross_string_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/html_cross_string_type) como [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/). La captura de pantalla explica cómo [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) afecta el HTML de salida desde la salida predeterminada.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
