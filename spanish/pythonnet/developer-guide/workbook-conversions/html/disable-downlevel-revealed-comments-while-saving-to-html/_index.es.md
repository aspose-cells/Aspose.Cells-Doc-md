---
title: Desactivar los Comentarios Revelados de Niveles Inferiores al guardar en HTML
type: docs
weight: 20
url: /es/python-net/disable-downlevel-revealed-comments-while-saving-to/
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo Excel en HTML, Aspose.Cells para Python via .NET revela Comentarios Condicionales en niveles inferiores. Estos comentarios condicionales son relevantes principalmente para versiones antiguas de Internet Explorer y no son relevantes para navegadores modernos. Puedes leer más sobre ellos en el siguiente enlace.

- [Comentario condicional - comentario condicional revelado de niveles inferiores](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells para Python via .NET te permite eliminar estos Comentarios Revelados en niveles inferiores configurando la propiedad [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments) en **true**.

## **Desactivar Comentarios Revelados de Niveles Inferiores al guardar en HTML**

El siguiente código de muestra muestra el uso de la propiedad [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments). La captura de pantalla muestra el efecto de esta propiedad cuando no está establecida en true. Por favor descarga el [archivo de Excel de muestra](50528257.xlsx) usado en este código y el [HTML de salida](50528258.zip) generado por él para una referencia.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
{{< app/cells/assistant language="python-net" >}}
