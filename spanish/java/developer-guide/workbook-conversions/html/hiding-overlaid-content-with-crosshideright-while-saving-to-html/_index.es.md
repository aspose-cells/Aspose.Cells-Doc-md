---
title: Ocultar contenido superpuesto con CrossHideRight al guardar en HTML
type: docs
weight: 100
url: /es/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---

## **Escenarios de uso posibles**

Cuando guarda su archivo de Excel a HTML, puede especificar diferentes tipos de cruces para las cadenas de celdas. De forma predeterminada, Aspose.Cells genera HTML según Microsoft Excel, pero cuando cambia el [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) por el [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT), se ocultan todas las cadenas en el lado derecho de la celda que están superpuestas con la cadena de la celda.

## **Ocultar Contenido Superpuesto con CrossHideRight al guardar en HTML**

El siguiente código de muestra carga el [archivo de Excel de muestra](64716916.xlsx) y lo guarda en [HTML de salida](64716915.zip) después de establecer el [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) como [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT). La captura de pantalla explica cómo [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT) afecta al HTML de salida desde la salida predeterminada.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
{{< app/cells/assistant language="java" >}}
