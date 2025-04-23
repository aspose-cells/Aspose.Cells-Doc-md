---
title: Desactivar Comentarios Revelados en nivel inferior al guardar en HTML con Node.js mediante C++
linktitle: Desactivar los Comentarios Revelados de Niveles Inferiores al guardar en HTML
type: docs
weight: 20
url: /es/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Aprende cómo desactivar los comentarios revelados en nivel inferior al guardar un archivo Excel en HTML usando Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**

Al guardar tu archivo Excel en HTML, Aspose.Cells revela los Comentarios Condicionales en nivel inferior. Estos comentarios condicionales son relevantes principalmente para versiones antiguas de Internet Explorer y no para navegadores modernos. Puedes leer más detalles en el siguiente enlace.

- [Comentario condicional - comentario condicional revelado de niveles inferiores](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Node.js via C++ te permite eliminar estos Comentarios Revelados en nivel inferior configurando la propiedad [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--) en **true**.

## **Desactivar Comentarios Revelados de Niveles Inferiores al guardar en HTML**

El siguiente ejemplo muestra cómo usar la propiedad [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--). La captura de pantalla muestra el efecto de esta propiedad cuando no está configurada en true. Descarga el [archivo de ejemplo Excel](50528257.xlsx) usado en este código y el [HTML de salida](50528258.zip) generado por él para referencia.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Código de muestra**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableDownlevelRevealedComments.xlsx"));

// Disable DisableDownlevelRevealedComments
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableDownlevelRevealedComments(true);

// Save the workbook in html
workbook.save(path.join(outputDir, "outputDisableDownlevelRevealedComments_true.html"), opts);
```
