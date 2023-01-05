---
title: Deshabilite los comentarios revelados de nivel inferior al guardar en HTML
type: docs
weight: 20
url: /es/python-java/disable-downlevel-revealed-comments-while-saving-to/
---
## **Deshabilite los comentarios revelados de nivel inferior al guardar en HTML**
Cuando el archivo de Excel se convierte a HTML, Aspose.Cells agrega comentarios condicionales revelados de nivel inferior en el archivo de salida HTML. Estos comentarios condicionales son en su mayoría relevantes para las versiones antiguas de Internet Explorer y son irrelevantes en los navegadores modernos. Para obtener información adicional sobre los comentarios condicionales revelados de nivel inferior, visite el siguiente enlace

[Comentario condicional: comentario condicional revelado de nivel inferior](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Para eliminar los comentarios condicionales revelados por nivel inferior, Aspose.Cells proporciona la[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)propiedad. Configuración de la[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) propiedad a**Verdadero**eliminará los comentarios condicionales revelados por nivel inferior en el archivo de salida HTML.

La siguiente imagen muestra los comentarios condicionales revelados de nivel inferior que se eliminarán en el archivo de salida HTML

![todo:imagen_alternativa_texto](Disable-Downlevel-Revealed-Comments.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
