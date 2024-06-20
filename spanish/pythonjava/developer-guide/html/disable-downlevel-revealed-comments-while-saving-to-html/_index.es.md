---
title: Desactivar los Comentarios Revelados de Niveles Inferiores al guardar en HTML
type: docs
weight: 20
url: /es/python-java/disable-downlevel-revealed-comments-while-saving-to/
---

## **Desactivar Comentarios Revelados de Niveles Inferiores al guardar en HTML**
Cuando se convierte un archivo de Excel a HTML, Aspose.Cells agrega comentarios condicionales revelados en versiones anteriores en el archivo HTML de salida. Estos comentarios condicionales son principalmente relevantes para versiones antiguas de Internet Explorer y no tienen relevancia en los navegadores modernos. Para obtener información adicional sobre los comentarios condicionales revelados, visite el siguiente enlace

[Comentario condicional - Comentario condicional revelado de versiones anteriores](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Para eliminar los comentarios condicionales revelados de versiones anteriores, Aspose.Cells proporciona la propiedad [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments). Configurar la propiedad [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) a **Verdadero** eliminará los comentarios condicionales revelados de versiones anteriores en el archivo HTML de salida.

La siguiente imagen muestra los comentarios condicionales revelados de versiones anteriores que se eliminarán en el archivo HTML de salida

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
