---
title: Ocultar contenido superpuesto con CrossHideRight mientras se guarda en HTML
type: docs
weight: 100
url: /es/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---
## **Posibles escenarios de uso**

Cuando guarda su archivo de Excel en HTML, puede especificar diferentes tipos de cruces para las cadenas de celdas. De forma predeterminada, Aspose.Cells genera HTML según Microsoft Excel, pero cuando cambia el[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)a[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)luego oculta todas las cadenas en el lado derecho de la celda que están superpuestas o superpuestas con la cadena de celdas.

## **Ocultar contenido superpuesto con CrossHideRight mientras se guarda en HTML**

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](64716916.xlsx)y lo guarda en[salida HTML](64716915.zip)después de configurar el[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)como[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). La captura de pantalla explica cómo[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)afecta la salida HTML de la salida predeterminada.

![todo:imagen_alternativa_texto](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
