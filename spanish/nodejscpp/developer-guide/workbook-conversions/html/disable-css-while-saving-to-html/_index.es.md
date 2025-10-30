---
title: Desactivar CSS al guardar en HTML con Node.js mediante C++
linktitle: Desactivar CSS al guardar en HTML
type: docs
weight: 320
url: /es/nodejs-cpp/disable-css-while-saving-to-html/
description: Aprende a desactivar CSS al guardar archivos Excel en HTML usando Aspose.Cells for Node.js via C++. 
---

## **Escenarios de uso posibles**

Al guardar tu archivo Excel en HTML de una sola página, normalmente los elementos CSS se incrustan dentro del archivo HTML y estarán en la sección HEAD. Si adjuntas este archivo como contenido/cuerpo de un correo, la mayoría de los clientes de correo eliminarán los estilos CSS, resultando en una visualización incorrecta. La versión 24.12 de Aspose.Cells introduce una opción que permite desactivar opcionalmente el CSS, permitiendo que los estilos se apliquen directamente en los elementos HTML. Si quieres configurar el HTML como contenido/cuerpo del correo, usa la propiedad [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) y configúrala en **true**.

## **Desactivar CSS al guardar en HTML**

El siguiente código de ejemplo muestra el uso de la propiedad [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--). 

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableCss.xlsx"));

// Disable CSS
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableCss(true);

// Save the workbook in HTML
workbook.save(path.join(outputDir, "outputDisable.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
