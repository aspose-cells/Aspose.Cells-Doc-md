---
title: Deshabilite los comentarios revelados de nivel inferior al guardar en HTML
type: docs
weight: 20
url: /es/net/disable-downlevel-revealed-comments-while-saving-to/
---
## **Posibles escenarios de uso**

Cuando guarda su archivo de Excel en HTML, Aspose.Cells revela comentarios condicionales de nivel inferior. Estos comentarios condicionales son principalmente relevantes para versiones anteriores de Internet Explorer y son irrelevantes para los navegadores web modernos. Puedes leer sobre ellos en detalle en el siguiente enlace.

- [Comentario condicional: comentario condicional revelado de nivel inferior](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells le permite eliminar estos comentarios revelados de nivel inferior configurando el[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) propiedad a**verdadero**.

## **Deshabilite los comentarios revelados de nivel inferior al guardar en HTML**

El siguiente código de ejemplo muestra el uso de[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) propiedad. La captura de pantalla muestra el efecto de esta propiedad cuando no se establece en verdadero. Por favor descarga el[ejemplo de archivo de Excel](50528257.xlsx) utilizado en este código y el[HTML de salida](50528258.zip) generado por él para una referencia.

![todo:imagen_alternativa_texto](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
