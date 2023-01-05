---
title: Ocultar contenido superpuesto al convertir Excel a HTML
type: docs
weight: 40
url: /es/python-java/hide-overlaid-content-while-converting-excel-to/
---
## **Ocultar contenido superpuesto al convertir Excel a HTML**
Cuando guarda su archivo de Excel en HTML, puede especificar diferentes tipos de cruces para las cadenas de celdas. De forma predeterminada, Aspose.Cells genera HTML según Microsoft Excel, pero cuando cambia el[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)a[CRUZ_OCULTAR_CORRECTO](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)luego oculta todas las cadenas en el lado derecho de la celda que están superpuestas o superpuestas con la cadena de celdas.

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](sampleHidingOverlaidContentWithCrossHideRight.xlsx)y lo guarda en[salida HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)después de configurar el[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)como[CRUZ_OCULTAR_CORRECTO](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). La captura de pantalla explica cómo[CRUZ_OCULTAR_CORRECTO](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)afecta la salida HTML de la salida predeterminada.

![todo:imagen_alternativa_texto](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
