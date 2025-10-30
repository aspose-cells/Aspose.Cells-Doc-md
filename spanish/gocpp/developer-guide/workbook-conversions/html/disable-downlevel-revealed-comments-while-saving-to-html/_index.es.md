---
title: Desactivar comentarios revelados en nivel inferior al guardar en HTML con Golang vía C++
linktitle: Desactivar Comentarios Revelados en Niveles Inferiores
type: docs
weight: 20
url: /es/go-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Eliminar comentarios revelados en nivel inferior al guardar archivos de Excel en HTML usando Aspose.Cells con Golang vía C++.
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel en HTML, Aspose.Cells revela Comentarios Condicionales en Niveles Inferiores. Estos comentarios condicionales son principalmente relevantes para versiones antiguas de Internet Explorer y son irrelevantes para navegadores Web modernos. Puedes leer sobre ellos en detalle en el siguiente enlace.

- [Comentario condicional - comentario condicional revelado de niveles inferiores](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells te permite eliminar estos Comentarios Revelados en Niveles Inferiores configurando la propiedad [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/) a **true**.

## **Desactivar Comentarios Revelados de Niveles Inferiores al guardar en HTML**

El siguiente código de ejemplo muestra el uso de la propiedad [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/). La captura de pantalla muestra el efecto de esta propiedad cuando no está configurada a true. Por favor, descarga el [archivo de Excel de ejemplo](50528257.xlsx) utilizado en este código y el [HTML de salida](50528258.zip) generado para referencia.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableDownlevelRevealedCommentsWhileSavingToHtml.go" >}}
