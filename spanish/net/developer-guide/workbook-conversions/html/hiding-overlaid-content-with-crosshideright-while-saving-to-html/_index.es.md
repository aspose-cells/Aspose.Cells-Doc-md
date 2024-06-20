---
title: Ocultar contenido superpuesto con CrossHideRight al guardar en HTML
type: docs
weight: 100
url: /es/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel a HTML, puedes especificar diferentes tipos de cruces para las cadenas de celdas. De forma predeterminada, Aspose.Cells genera HTML según Microsoft Excel, pero cuando cambias el tipo de cruce a [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype), entonces oculta todas las cadenas en el lado derecho de la celda que se superponen o están superpuestas con la cadena de la celda.

## **Ocultar contenido superpuesto con CrossHideRight al guardar en Html**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716894.xlsx) y lo guarda en [HTML de salida](64716893.zip) después de configurar [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype) como [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). La captura de pantalla explica cómo [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) afecta el HTML de salida desde la salida predeterminada.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
