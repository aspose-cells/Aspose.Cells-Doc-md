---
title: Ocultar Contenido Superpuesto al Convertir Excel a HTML
type: docs
weight: 40
url: /es/python-java/hide-overlaid-content-while-converting-excel-to/
---

## **Ocultar Contenido Superpuesto al Convertir Excel a HTML**
Cuando guarda su archivo de Excel a HTML, puede especificar diferentes tipos de cruce para las cadenas de celdas. Por defecto, Aspose.Cells genera HTML según Microsoft Excel, pero cuando cambia [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) a [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT), oculta todas las cadenas en el lado derecho de la celda que están superpuestas o se superponen con la cadena de la celda.

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](sampleHidingOverlaidContentWithCrossHideRight.xlsx) y lo guarda en [HTML de salida](HTML-outputHidingOverlaidContentWithCrossHideRight.zip) después de establecer el [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) como [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). La captura de pantalla explica cómo [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) afecta el HTML de salida desde la salida predeterminada.

![todo:image_alt_text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
