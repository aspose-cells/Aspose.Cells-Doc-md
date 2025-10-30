---
title: Renderizar hoja de cálculo en contexto gráfico con Node.js vía C++
linktitle: Renderizar hoja de cálculo en contexto gráfico
type: docs
weight: 300
url: /es/nodejs-cpp/render-worksheet-to-graphic-context/
description: Aprende cómo renderizar una hoja de cálculo a un contexto gráfico usando Aspose.Cells for Node.js via C++. Esto incluye renderizar a archivos de imagen, pantallas y impresoras.
---

{{% alert color="primary" %}}

Ahora Aspose.Cells puede renderizar hojas de cálculo a un contexto gráfico. El contexto gráfico puede ser cualquier cosa como un archivo de imagen, pantalla o impresora, etc. Usa uno de los siguientes dos métodos para renderizar una hoja de cálculo a un contexto gráfico.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

El siguiente código ilustra cómo usar Aspose.Cells para renderizar una hoja de cálculo en un contexto gráfico. Una vez que ejecutes el código, imprimirá toda la hoja y llenará el espacio vacío restante con color azul en el contexto gráfico y guardará la imagen como archivo **OutputImage_out_.png**. Puedes usar cualquier archivo de Excel para probar este código. También lee los comentarios dentro del código para mejor comprensión.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook object from source file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create empty image buffer
const bmpOptions = new AsposeCells.ImageOrPrintOptions();
bmpOptions.setOnePagePerSheet(true);

// Render worksheet to image
const sheetRender = new AsposeCells.SheetRender(worksheet, bmpOptions);
sheetRender.toImage(0, dataDir + "/OutputImage_out.png");

// Save the image in Png format
```
{{< app/cells/assistant language="nodejs-cpp" >}}
