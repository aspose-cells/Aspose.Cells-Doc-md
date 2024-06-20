---
title: Desactivar los Comentarios Revelados de Niveles Inferiores al guardar en HTML
type: docs
weight: 20
url: /es/net/disable-downlevel-revealed-comments-while-saving-to/
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel en HTML, entonces Aspose.Cells revela Comentarios Condicionales de Niveles Inferiores. Estos comentarios condicionales son mayormente relevantes para versiones antiguas de Internet Explorer y son irrelevantes para navegadores web modernos. Puedes leer más sobre ellos en detalle en el siguiente enlace.

- [Comentario condicional - comentario condicional revelado de niveles inferiores](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells te permite eliminar estos Comentarios Revelados de Niveles Inferiores estableciendo la propiedad [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) a **true**.

## **Desactivar Comentarios Revelados de Niveles Inferiores al guardar en HTML**

El siguiente código de muestra muestra el uso de la propiedad [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments). La captura de pantalla muestra el efecto de esta propiedad cuando no está establecida en true. Por favor descarga el [archivo de Excel de muestra](50528257.xlsx) usado en este código y el [HTML de salida](50528258.zip) generado por él para una referencia.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
