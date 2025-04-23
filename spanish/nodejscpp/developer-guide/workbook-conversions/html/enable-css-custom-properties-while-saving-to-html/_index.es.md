---
title: Habilitar propiedades personalizadas de CSS al guardar en HTML con Node.js mediante C++
linktitle: Habilitar Propiedades Personalizadas de CSS al guardar en HTML
type: docs
weight: 320
url: /es/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/
description: Aprende cómo habilitar propiedades CSS personalizadas al guardar archivos de Excel en HTML usando Aspose.Cells for Node.js via C++. 
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel en HTML, para el escenario en que hay múltiples ocurrencias de una misma imagen en base64, con la propiedad personalizada, los datos de la imagen solo necesitan guardarse una vez, mejorando así el rendimiento del HTML resultante. Usa [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--) y configúralo a **true** al guardar en HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Habilitar Propiedades Personalizadas de CSS al guardar en HTML**

El siguiente código de ejemplo muestra el uso de la propiedad [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--). La captura de pantalla muestra el efecto cuando no está configurada en **true**. Descarga el [archivo de Excel de ejemplo](50528260.xlsx) utilizado en este código y el [HTML generado](50528261.zip) para referencia.



## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleEnableCssCustomProperties.xlsx"));

const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportImagesAsBase64(true);

// Enable EnableCssCustomProperties
opts.setEnableCssCustomProperties(true);

// Save the workbook in HTML
workbook.save(path.join(dataDir, "outputEnableCssCustomProperties.html"), opts);
```
