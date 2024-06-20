---
title: Desactivar los Comentarios Revelados de Niveles Inferiores al guardar en HTML
type: docs
weight: 20
url: /es/java/disable-downlevel-revealed-comments-while-saving-to-html/
---

## **Escenarios de uso posibles**

Cuando guarde su archivo de Excel en HTML, Aspose.Cells revelará los comentarios condicionales de versión anterior. Estos comentarios condicionales son en su mayoría relevantes para las versiones antiguas de Internet Explorer y son irrelevantes para los navegadores web modernos. Puede obtener más información sobre ellos en detalle en el siguiente enlace.

- [Comentario condicional - comentario condicional revelado de niveles inferiores](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells le permite eliminar estos comentarios revelados de versión anterior al establecer la propiedad [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) en **true**.

## **Desactivar Comentarios Revelados de Niveles Inferiores al guardar en HTML**

El siguiente código de ejemplo muestra el uso de la propiedad [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments). La captura de pantalla muestra el efecto de esta propiedad cuando no se establece como **true**. Por favor, descargue el [archivo de Excel de ejemplo](50528267.xlsx) utilizado en este código y el [HTML generado](50528266.zip) a modo de referencia.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
